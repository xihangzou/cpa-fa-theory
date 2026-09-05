#!/usr/bin/env python3
"""Prepare and validate source-image Markdown projects; no integration or Anki operations."""

import argparse
import collections
import hashlib
import json
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
PASS = "pass"
VALID_REVIEW_CHECKS = {"pass", "not_applicable"}
UNRESOLVED = re.compile(r"\[要(?:画像|原本)確認|\[UNRESOLVED")
SIMPLE_ID = re.compile(r"[A-Za-z0-9_-]+")
SECTION_ID = re.compile(r"[A-Za-z0-9_.-]+")
COMMIT = re.compile(r"[0-9a-f]{40}")


def require(ok, message):
    if not ok:
        raise ValueError(message)


def read(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write(path, obj):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def safe(root, relative):
    require(isinstance(relative, str) and relative, "Project path must be a non-empty string")
    root = root.resolve()
    path = (root / relative).resolve()
    require(path.is_relative_to(root), "Path escapes project: " + relative)
    return path


def text(path):
    # newline="" preserves CRLF/LF bytes after UTF-8 decoding. Batch assembly must
    # preserve all chunk-body bytes except the explicitly removed headings.
    with Path(path).open("r", encoding="utf-8", newline="") as stream:
        return stream.read()


def identifiers(values, where, allow_empty=False):
    require(isinstance(values, list), where + ": expected a list")
    require(allow_empty or values, where + ": empty list")
    require(all(isinstance(value, str) and value for value in values), where + ": invalid ID")
    require(len(values) == len(set(values)), where + ": duplicate ID")
    return values


def ordered_subset(values, reference, where):
    positions = {value: index for index, value in enumerate(reference)}
    require(set(values) <= positions.keys(), where + ": value outside allowed scope")
    indexes = [positions[value] for value in values]
    require(indexes == sorted(indexes), where + ": values are out of source order")


def passed(value, where):
    require(value == PASS, where + ": status must be pass")


def no_unresolved_record(value, where):
    serialized = json.dumps(value, ensure_ascii=False)
    require(not UNRESOLVED.search(serialized), where + ": unresolved marker")


def ingest(project, source, source_id, dpi):
    from PIL import Image

    require(SIMPLE_ID.fullmatch(source_id), "Use a simple unique source ID.")
    manifest = read(project / "sources.json")
    require(
        source_id not in {entry["id"] for entry in manifest},
        "Source ID already exists; preserve existing edition.",
    )
    require(dpi >= 150, "Use at least 150 DPI; default 300.")
    destination = project / "pages" / source_id
    require(not destination.exists(), "Page directory already exists.")
    records = []
    with tempfile.TemporaryDirectory() as temp:
        stage = Path(temp)
        if source.is_file() and source.suffix.lower() == ".pdf":
            require(
                shutil.which("pdftoppm") and shutil.which("pdfinfo"),
                "Install Poppler: pdftoppm and pdfinfo.",
            )
            info = subprocess.run(
                ["pdfinfo", str(source)], check=True, capture_output=True, text=True
            ).stdout
            count = int(re.search(r"^Pages:\s+(\d+)", info, re.M)[1])
            subprocess.run(
                [
                    "pdftoppm",
                    "-jpeg",
                    "-r",
                    str(dpi),
                    "-jpegopt",
                    "quality=95",
                    str(source),
                    str(stage / "page"),
                ],
                check=True,
                capture_output=True,
            )
            files = sorted(
                stage.glob("page-*.jpg"), key=lambda path: int(path.stem.split("-")[-1])
            )
            require(len(files) == count, "Rendered page count differs from PDF count.")
            original = "sources/" + source_id + ".pdf"
            require(not (project / original).exists(), "Original destination already exists.")
            (project / "sources").mkdir(exist_ok=True)
            shutil.copy2(source, project / original)
            source_record = {
                "id": source_id,
                "kind": "pdf",
                "original": original,
                "sha256": sha(project / original),
                "dpi": dpi,
            }
        else:
            require(
                source.is_dir(),
                "Input must be a PDF or a directory of page-NNN.jpg images. Export slides to PDF first.",
            )
            files = list(source.iterdir())
            require(
                files
                and all(
                    path.is_file() and re.fullmatch(r"page-[0-9]+\.jpg", path.name)
                    for path in files
                ),
                "Image directory must contain only page-NNN.jpg files.",
            )
            files.sort(key=lambda path: int(path.stem.split("-")[-1]))
            numbers = [int(path.stem.split("-")[-1]) for path in files]
            require(
                len(numbers) == len(set(numbers)) and min(numbers) > 0,
                "Duplicate or invalid page numbers.",
            )
            source_record = {
                "id": source_id,
                "kind": "images",
                "original": "Provided page images; copied byte-for-byte",
                "sha256": None,
                "dpi": None,
            }
        destination.mkdir(parents=True)
        for file in files:
            number = int(file.stem.split("-")[-1])
            target = destination / f"page-{number:03}.jpg"
            shutil.copy2(file, target)
            with Image.open(target) as image:
                image.verify()
            with Image.open(target) as image:
                width, height = image.size
            records.append(
                {
                    "id": f"{source_id}:{number:03}",
                    "pdf_page": number,
                    "printed_page": None,
                    "image": str(target.relative_to(project)),
                    "sha256": sha(target),
                    "width": width,
                    "height": height,
                    "disposition": "include",
                    "reason": "",
                }
            )
    source_record.update(edition="FILL IN title and edition", pages=records)
    manifest.append(source_record)
    write(project / "sources.json", manifest)
    print(
        f"Ingested {len(records)} pages. Verify orientation, legibility, edition, printed-page mapping, and exclusions."
    )


def validate_sources(project):
    sources = read(project / "sources.json")
    require(isinstance(sources, list) and sources, "Sources must be populated.")
    pages = {}
    page_sources = {}
    source_ids = set()
    for source in sources:
        require(isinstance(source, dict), "Invalid source record")
        source_id = source.get("id")
        require(
            isinstance(source_id, str) and source_id and source_id not in source_ids,
            "Duplicate or invalid source ID",
        )
        source_ids.add(source_id)
        require(
            source.get("edition") and "FILL IN" not in str(source["edition"]),
            source_id + ": record the source title and edition.",
        )
        require(source.get("kind") in {"pdf", "images"}, source_id + ": invalid source kind")
        if source["kind"] == "pdf":
            original = safe(project, source.get("original"))
            require(original.is_file(), source_id + ": missing original PDF")
            require(sha(original) == source.get("sha256"), source_id + ": original PDF changed.")
        source_pages = source.get("pages")
        require(isinstance(source_pages, list) and source_pages, source_id + ": pages missing")
        physical_numbers = set()
        image_paths = set()
        for page in source_pages:
            require(isinstance(page, dict), source_id + ": invalid page record")
            page_id = page.get("id")
            require(
                isinstance(page_id, str) and page_id and page_id not in pages,
                "Duplicate or invalid page ID: " + str(page_id),
            )
            image = safe(project, page.get("image"))
            physical = page.get("pdf_page")
            require(
                isinstance(physical, int) and physical > 0 and physical not in physical_numbers,
                source_id + ": duplicate or invalid physical page number",
            )
            physical_numbers.add(physical)
            require(image not in image_paths, source_id + ": duplicate page image path")
            image_paths.add(image)
            require(image.is_file(), "Missing page image: " + page_id)
            require(sha(image) == page.get("sha256"), "Page changed: " + page_id)
            require(
                page.get("disposition") in {"include", "exclude"},
                "Invalid page disposition: " + page_id,
            )
            require(
                page["disposition"] != "exclude" or page.get("reason"),
                "Excluded page needs reason: " + page_id,
            )
            pages[page_id] = page
            page_sources[page_id] = source_id
        require(
            [page["pdf_page"] for page in source_pages]
            == sorted(page["pdf_page"] for page in source_pages),
            source_id + ": physical pages are out of order",
        )
        no_unresolved_record(source, source_id + ": source manifest")
    return sources, pages, page_sources


def validate_chunk_text(task_id, raw):
    require(not UNRESOLVED.search(raw), task_id + ": unresolved source content")
    require("**" not in raw, task_id + ": remove bold formatting from structured source Markdown")


def split_chunk(task_id, raw):
    match = re.match(r"\A---\r?\n(.*?)\r?\n---\r?\n", raw, re.S)
    require(match is not None, task_id + ": missing YAML metadata")
    metadata = yaml.safe_load(match[1])
    require(isinstance(metadata, dict), task_id + ": YAML metadata must be a mapping")
    return metadata, raw[match.end() :]


def legacy_source_check(project):
    _, pages, _ = validate_sources(project)
    tasks = read(project / "tasks.json")
    require(isinstance(tasks, list) and tasks, "Tasks must be populated.")
    used = collections.Counter()
    task_ids = set()
    for task in tasks:
        require(isinstance(task, dict), "Invalid task record")
        task_id = task.get("id")
        require(
            isinstance(task_id, str) and task_id and task_id not in task_ids,
            "Duplicate or invalid task ID",
        )
        task_ids.add(task_id)
        expected = identifiers(task.get("expected_pages"), task_id + ": expected_pages")
        processing = identifiers(
            task.get("processing_pages", expected), task_id + ": processing_pages"
        )
        require(set(expected) <= pages.keys(), task_id + ": invalid page scope")
        require(set(processing) <= set(expected), task_id + ": invalid page scope")
        require(
            all(pages[page]["disposition"] == "include" for page in processing),
            task_id + ": processes excluded page",
        )
        passed(task.get("status"), task_id)
        chunk = safe(project, task.get("output"))
        require(chunk.is_file(), task_id + ": missing chunk")
        validate_chunk_text(task_id, text(chunk))
        used.update(processing)
    require(
        all(used[page] == 1 for page, value in pages.items() if value["disposition"] == "include"),
        "Included pages must belong to exactly one processing task (context-only pages may repeat in expected_pages).",
    )
    return pages, tasks


def batch_manifest_check(project):
    _, pages, page_sources = validate_sources(project)
    require((project / "source-map.json").is_file(), "Missing source-map.json")
    require(isinstance(read(project / "source-map.json"), (dict, list)), "Invalid source-map.json")
    inventory_path = project / "inventory-review.json"
    require(inventory_path.is_file(), "Missing inventory-review.json")
    inventory = read(inventory_path)
    require(isinstance(inventory, dict), "Invalid inventory-review.json")
    passed(inventory.get("status"), "inventory-review.json")
    require(inventory.get("unresolved_count") == 0, "Inventory review has unresolved items")
    no_unresolved_record(inventory, "inventory-review.json")

    batches = read(project / "batches.json")
    require(isinstance(batches, list) and batches, "Batches must be populated.")
    no_unresolved_record(batches, "batches.json")
    batch_ids = set()
    expected_owners = collections.Counter()
    processing_owners = collections.Counter()
    batch_map = collections.OrderedDict()
    source_page_order = collections.defaultdict(list)
    for page in pages:
        source_page_order[page_sources[page]].append(page)
    last_batch_position = collections.defaultdict(lambda: -1)
    for batch in batches:
        require(isinstance(batch, dict), "Invalid batch record")
        batch_id = batch.get("id")
        require(
            isinstance(batch_id, str) and batch_id and batch_id not in batch_ids,
            "Duplicate or invalid batch ID",
        )
        batch_ids.add(batch_id)
        expected = identifiers(batch.get("expected_pages"), batch_id + ": expected_pages")
        processing = identifiers(batch.get("processing_pages"), batch_id + ": processing_pages")
        require(set(expected) <= pages.keys(), batch_id + ": unknown expected page")
        require(set(processing) <= set(expected), batch_id + ": processing page outside expected range")
        expected_included = [
            page for page in expected if pages[page]["disposition"] == "include"
        ]
        require(
            processing == expected_included,
            batch_id + ": processing_pages must exactly equal included expected_pages in source order",
        )
        require(
            len({page_sources[page] for page in expected}) == 1,
            batch_id + ": a batch may reference only one source",
        )
        source_id = page_sources[expected[0]]
        ordered_subset(expected, source_page_order[source_id], batch_id + ": expected_pages")
        first_position = source_page_order[source_id].index(expected[0])
        require(
            first_position > last_batch_position[source_id],
            batch_id + ": batches are out of physical source order",
        )
        last_batch_position[source_id] = source_page_order[source_id].index(expected[-1])
        chapter_keys = identifiers(batch.get("chapter_keys"), batch_id + ": chapter_keys")
        require(all(SIMPLE_ID.fullmatch(key) for key in chapter_keys), batch_id + ": invalid chapter key")
        passed(batch.get("inventory_status"), batch_id + ": inventory_status")
        safe(project, batch.get("fragment"))
        expected_owners.update(expected)
        processing_owners.update(processing)
        batch_map[batch_id] = batch

    require(
        all(count <= 1 for count in expected_owners.values()),
        "A physical page appears in more than one batch expected range",
    )
    included = {page for page, record in pages.items() if record["disposition"] == "include"}
    require(
        set(processing_owners) == included
        and all(processing_owners[page] == 1 for page in included),
        "Each included physical page must have exactly one batch owner",
    )
    return pages, page_sources, batches, batch_map


def chunk_record(project, task, batch, pages, page_sources, source_id):
    task_id = task.get("id")
    require(isinstance(task_id, str) and task_id, "Invalid section task ID")
    require(task.get("batch_id") == batch["id"], task_id + ": batch_id mismatch")
    for key in ("chapter", "section", "title"):
        require(str(task.get(key, "")).strip(), task_id + ": missing " + key)
    chapter = str(task["chapter"])
    section = str(task["section"])
    require(SIMPLE_ID.fullmatch(chapter), task_id + ": invalid chapter ID")
    require(SECTION_ID.fullmatch(section), task_id + ": invalid section ID")
    require(chapter in batch["chapter_keys"], task_id + ": chapter outside batch contract")
    expected = identifiers(task.get("expected_pages"), task_id + ": expected_pages")
    processing = identifiers(task.get("processing_pages"), task_id + ": processing_pages")
    require(set(expected) <= set(batch["expected_pages"]), task_id + ": expected page outside batch")
    require(set(processing) <= set(expected), task_id + ": processing page outside task expectation")
    require(set(processing) <= set(batch["processing_pages"]), task_id + ": processing page outside batch")
    ordered_subset(expected, batch["expected_pages"], task_id + ": expected_pages")
    ordered_subset(processing, batch["processing_pages"], task_id + ": processing_pages")
    require(
        all(page_sources[page] == source_id for page in expected),
        task_id + ": page belongs to another source",
    )
    require(
        all(pages[page]["disposition"] == "include" for page in processing),
        task_id + ": processes excluded page",
    )
    passed(task.get("status"), task_id)

    chunk = safe(project, task.get("output"))
    require(chunk.is_file(), task_id + ": missing chunk")
    raw = text(chunk)
    validate_chunk_text(task_id, raw)
    metadata, body = split_chunk(task_id, raw)
    for key in ("id", "pdf_pages", "pages", "chapter", "section", "title", "batch_id"):
        require(key in metadata, task_id + ": missing YAML field " + key)
    require(metadata["id"] == task_id, task_id + ": chunk ID mismatch")
    require(metadata["batch_id"] == batch["id"], task_id + ": chunk batch mismatch")
    require(str(metadata["chapter"]) == chapter, task_id + ": chunk chapter mismatch")
    require(str(metadata["section"]) == section, task_id + ": chunk section mismatch")
    require(str(metadata["title"]) == str(task["title"]), task_id + ": chunk title mismatch")
    require(str(metadata["pdf_pages"]).strip(), task_id + ": empty pdf_pages")
    require(str(metadata["pages"]).strip(), task_id + ": empty printed pages")
    current_hash = sha(chunk)
    require(task.get("chunk_sha256") == current_hash, task_id + ": chunk hash changed")

    lines = body.splitlines()
    h1 = [line for line in lines if line.startswith("# ")]
    h2 = [line for line in lines if line.startswith("## ")]
    require(h1 and len(set(h1)) == 1, task_id + ": missing or contradictory chapter heading")
    require(h2 and len(set(h2)) == 1, task_id + ": missing or contradictory section heading")
    require(h2[0][3:] == str(task["title"]), task_id + ": section heading/title mismatch")
    nonblank = [line for line in lines if line.strip()]
    require(
        len(nonblank) >= 2 and nonblank[0] == h1[0] and nonblank[1] == h2[0],
        task_id + ": chunk body must begin with its chapter and section headings",
    )

    locators = task.get("locators")
    require(isinstance(locators, list) and locators, task_id + ": locators missing")
    located = set()
    locator_order = []
    for locator in locators:
        require(isinstance(locator, dict), task_id + ": invalid locator")
        page = locator.get("page")
        require(page in processing, task_id + ": out-of-batch chunk locator: " + str(page))
        require(
            locator.get("printed_page") == pages[page].get("printed_page"),
            task_id + ": locator printed-page mismatch: " + page,
        )
        require(
            isinstance(locator.get("source_region"), str) and locator["source_region"].strip(),
            task_id + ": locator source_region missing",
        )
        heading = locator.get("destination_heading")
        require(
            isinstance(heading, str) and heading in lines and heading.startswith("## "),
            task_id + ": locator destination_heading missing from chunk",
        )
        if page not in located:
            locator_order.append(page)
        located.add(page)
    require(located == set(processing), task_id + ": locator coverage differs from processing_pages")
    require(locator_order == processing, task_id + ": locators are out of source order")
    return {
        "task": task,
        "chapter": chapter,
        "section": section,
        "chapter_heading": h1[0],
        "section_heading": h2[0],
        "raw": raw,
        "body": body,
        "chunk_sha256": current_hash,
    }


def validate_task_order(records, where):
    seen_chapters = set()
    seen_sections = collections.defaultdict(set)
    chapter_headings = {}
    section_headings = {}
    previous_chapter = None
    previous_section = None
    for record in records:
        task_id = record["task"]["id"]
        chapter = record["chapter"]
        section = record["section"]
        if chapter != previous_chapter:
            require(chapter not in seen_chapters, where + ": chapter returns out of order: " + chapter)
            seen_chapters.add(chapter)
            previous_chapter = chapter
            previous_section = None
        require(
            chapter_headings.setdefault(chapter, record["chapter_heading"])
            == record["chapter_heading"],
            task_id + ": contradictory repeated chapter heading",
        )
        key = (chapter, section)
        if section != previous_section:
            require(
                section not in seen_sections[chapter],
                task_id + ": out-of-order continuation returns to section " + section,
            )
            seen_sections[chapter].add(section)
            previous_section = section
        require(
            section_headings.setdefault(key, record["section_heading"])
            == record["section_heading"],
            task_id + ": contradictory repeated section heading",
        )


def check_review(project, batch, fragment, records, pages):
    review_path = safe(project, fragment.get("review"))
    require(review_path.is_file(), batch["id"] + ": missing batch review")
    review = read(review_path)
    require(isinstance(review, dict), batch["id"] + ": invalid batch review")
    no_unresolved_record(review, batch["id"] + ": review")
    require(review.get("batch_id") == batch["id"], batch["id"] + ": review batch mismatch")
    require(review.get("source_id") == fragment["source_id"], batch["id"] + ": review source mismatch")
    passed(review.get("status"), batch["id"] + ": review")
    require(review.get("unresolved_count") == 0, batch["id"] + ": review has unresolved items")

    images = review.get("source_images")
    require(isinstance(images, list), batch["id"] + ": review source_images missing")
    image_map = {}
    for item in images:
        require(isinstance(item, dict), batch["id"] + ": invalid source image evidence")
        page = item.get("page")
        require(page not in image_map, batch["id"] + ": duplicate source image evidence")
        image_map[page] = item.get("sha256")
    require(
        list(image_map) == batch["processing_pages"],
        batch["id"] + ": review source image order/coverage mismatch",
    )
    require(
        all(image_map[page] == pages[page]["sha256"] for page in image_map),
        batch["id"] + ": review source image hash mismatch",
    )

    outputs = review.get("section_outputs")
    require(isinstance(outputs, list), batch["id"] + ": review section_outputs missing")
    output_pairs = []
    for item in outputs:
        require(isinstance(item, dict), batch["id"] + ": invalid section output evidence")
        output_pairs.append((item.get("task"), item.get("chunk_sha256")))
    require(
        output_pairs
        == [(record["task"]["id"], record["chunk_sha256"]) for record in records],
        batch["id"] + ": review section output hash/order mismatch",
    )

    coverage = review.get("coverage")
    require(isinstance(coverage, list), batch["id"] + ": review coverage missing")
    coverage_pages = []
    for item in coverage:
        require(isinstance(item, dict), batch["id"] + ": invalid coverage row")
        page = item.get("page")
        require(page not in coverage_pages, batch["id"] + ": duplicate coverage page")
        coverage_pages.append(page)
        passed(item.get("status"), batch["id"] + ": page coverage " + str(page))
        require(
            isinstance(item.get("regions"), list)
            and item["regions"]
            and all(isinstance(region, str) and region.strip() for region in item["regions"]),
            batch["id"] + ": coverage regions missing for " + str(page),
        )
    require(coverage_pages == batch["processing_pages"], batch["id"] + ": review page coverage mismatch")

    for key in ("findings", "corrections"):
        require(isinstance(review.get(key), list), batch["id"] + ": review " + key + " missing")
    checks = review.get("checks")
    require(isinstance(checks, dict), batch["id"] + ": review checks missing")
    for key in ("numerical", "diagram", "false_proposition"):
        require(
            checks.get(key) in VALID_REVIEW_CHECKS,
            batch["id"] + ": invalid review check " + key,
        )
    require(
        isinstance(review.get("reviewer_model"), str) and review["reviewer_model"].strip(),
        batch["id"] + ": reviewer_model missing",
    )
    commits = review.get("dependency_commits")
    require(
        isinstance(commits, list)
        and commits
        and all(isinstance(commit, str) and COMMIT.fullmatch(commit) for commit in commits),
        batch["id"] + ": dependency_commits must contain full commit SHAs",
    )
    return review


def batch_check(project, batch_id, manifest=None):
    if manifest is None:
        manifest = batch_manifest_check(project)
    pages, page_sources, _, batch_map = manifest
    require(batch_id in batch_map, "Unknown batch: " + batch_id)
    batch = batch_map[batch_id]
    fragment_path = safe(project, batch["fragment"])
    require(fragment_path.is_file(), batch_id + ": missing fragment")
    fragment = read(fragment_path)
    require(isinstance(fragment, dict), batch_id + ": invalid fragment")
    no_unresolved_record(fragment, batch_id + ": fragment")
    require(fragment.get("batch_id") == batch_id, batch_id + ": fragment batch mismatch")
    expected_source = page_sources[batch["expected_pages"][0]]
    require(fragment.get("source_id") == expected_source, batch_id + ": fragment source mismatch")
    passed(fragment.get("status"), batch_id + ": fragment")
    tasks = fragment.get("tasks")
    require(isinstance(tasks, list) and tasks, batch_id + ": section tasks missing")
    task_ids = set()
    records = []
    cited = set()
    for task in tasks:
        require(isinstance(task, dict), batch_id + ": invalid section task")
        task_id = task.get("id")
        require(task_id not in task_ids, batch_id + ": duplicate section task ID")
        task_ids.add(task_id)
        record = chunk_record(project, task, batch, pages, page_sources, expected_source)
        records.append(record)
        cited.update(task["processing_pages"])
    require(cited == set(batch["processing_pages"]), batch_id + ": section citations do not cover the batch")
    task_chapters = list(dict.fromkeys(record["chapter"] for record in records))
    require(
        task_chapters == batch["chapter_keys"],
        batch_id + ": section tasks do not cover declared chapter keys in order",
    )
    validate_task_order(records, batch_id)
    check_review(project, batch, fragment, records, pages)
    return records


def batch_project_check(project):
    manifest = batch_manifest_check(project)
    _, _, batches, _ = manifest
    records = []
    task_ids = set()
    for batch in batches:
        current = batch_check(project, batch["id"], manifest)
        for record in current:
            task_id = record["task"]["id"]
            require(task_id not in task_ids, "Duplicate section task ID across batches: " + task_id)
            task_ids.add(task_id)
        records.extend(current)
    validate_task_order(records, "canonical task order")

    tasks = read(project / "tasks.json")
    require(isinstance(tasks, list) and tasks, "Canonical tasks.json must be populated")
    no_unresolved_record(tasks, "Canonical tasks.json")
    require(tasks == [record["task"] for record in records], "Canonical tasks.json differs from ordered fragments")

    by_chapter = collections.OrderedDict()
    for record in records:
        by_chapter.setdefault(record["chapter"], []).append(record)
    for chapter, chapter_records in by_chapter.items():
        require(SIMPLE_ID.fullmatch(chapter), "Invalid chapter ID: " + chapter)
        gate_path = safe(project, "qa/chapters/" + chapter + ".json")
        require(gate_path.is_file(), "Missing chapter review gate: " + chapter)
        gate = read(gate_path)
        require(isinstance(gate, dict), "Invalid chapter review gate: " + chapter)
        no_unresolved_record(gate, "Chapter review gate " + chapter)
        require(str(gate.get("chapter")) == chapter, "Chapter review gate ID mismatch: " + chapter)
        passed(gate.get("status"), "Chapter review gate " + chapter)
        require(gate.get("unresolved_count") == 0, "Chapter review gate has unresolved items: " + chapter)
        expected_chunks = [
            {"task": record["task"]["id"], "chunk_sha256": record["chunk_sha256"]}
            for record in chapter_records
        ]
        require(gate.get("chunks") == expected_chunks, "Chapter review hashes/order mismatch: " + chapter)
    return records


def source_check(project):
    if (project / "batches.json").exists():
        return batch_project_check(project)
    return legacy_source_check(project)


def legacy_assembled(project):
    _, tasks = legacy_source_check(project)
    chapters = collections.OrderedDict()
    sections = {}
    chapter_titles = {}
    evidence = []
    previous_chapter = None
    for task in tasks:  # Explicit order, never lexicographic filename order.
        chunk = safe(project, task["output"])
        raw = text(chunk)
        metadata, body = split_chunk(task["id"], raw)
        require(metadata["id"] == task["id"], "Chunk ID does not match task")
        require(str(metadata["chapter"]) == str(task["chapter"]), "Chunk chapter does not match task")
        chapter = str(task["chapter"])
        require(
            chapter == previous_chapter or chapter not in chapters,
            "Tasks must be grouped in chapter reading order",
        )
        previous_chapter = chapter
        output = chapters.setdefault(chapter, [])
        section = str(task["section"])
        seen = sections.setdefault(chapter, {})
        for line in body.splitlines(keepends=True):
            if line.startswith("# "):
                title = line.strip()
                if chapter in chapter_titles:
                    require(chapter_titles[chapter] == title, "Conflicting chapter titles")
                    continue
                chapter_titles[chapter] = title
            elif line.startswith("## "):
                title = line.strip()
                if section in seen:
                    require(seen[section] == title, "Conflicting section headings; split tasks per section")
                    continue
                seen[section] = title
            output.append(line)
        output.append("\n")
        evidence.append(
            {
                "task": task["id"],
                "chunk_sha256": sha(chunk),
                "processing_pages": task.get("processing_pages", task["expected_pages"]),
            }
        )
    require(set(chapters) == set(chapter_titles), "Each chapter must have a chapter heading")
    chapter_text = {key: "".join(value).strip() + "\n" for key, value in chapters.items()}
    return chapter_text, "\n".join(chapter_text.values()), evidence


def boundary_heading_indexes(task_id, body):
    lines = body.splitlines(keepends=True)
    nonblank = [index for index, line in enumerate(lines) if line.strip()]
    require(len(nonblank) >= 2, task_id + ": chunk body must begin with chapter and section headings")
    first, second = nonblank[0], nonblank[1]
    require(lines[first].startswith("# "), task_id + ": first boundary heading must be chapter level")
    require(lines[second].startswith("## "), task_id + ": second boundary heading must be section level")
    return lines, first, second


def batch_assembled(project):
    records = batch_project_check(project)
    chapters = collections.OrderedDict()
    evidence = []
    previous_chapter = None
    previous_section = None
    for record in records:
        task = record["task"]
        chapter = record["chapter"]
        section = record["section"]
        lines, chapter_heading, section_heading = boundary_heading_indexes(task["id"], record["body"])
        remove = set()
        if chapter == previous_chapter:
            remove.add(chapter_heading)
            if section == previous_section:
                remove.add(section_heading)
        transformed = "".join(line for index, line in enumerate(lines) if index not in remove)
        chapters.setdefault(chapter, []).append(transformed)
        evidence.append(
            {
                "task": task["id"],
                "batch": task["batch_id"],
                "chapter": chapter,
                "section": section,
                "chunk_sha256": record["chunk_sha256"],
                "processing_pages": task["processing_pages"],
                "removed_boundary_headings": [lines[index].rstrip("\r\n") for index in sorted(remove)],
            }
        )
        previous_chapter = chapter
        previous_section = section
    chapter_text = collections.OrderedDict(
        (chapter, "".join(parts)) for chapter, parts in chapters.items()
    )
    return chapter_text, "".join(chapter_text.values()), evidence


def assembled(project):
    if (project / "batches.json").exists():
        return batch_assembled(project)
    return legacy_assembled(project)


def assemble(project):
    batch_mode = (project / "batches.json").exists()
    chapters, body, evidence = assembled(project)
    merged = project / "merged"
    merged.mkdir(exist_ok=True)
    for stale in merged.glob("chapter-*.md"):
        stale.unlink()
    chapter_rows = []
    for index, (chapter, content) in enumerate(chapters.items()):
        relative = f"merged/chapter-{index:03}.md"
        (project / relative).write_text(content, encoding="utf-8", newline="")
        chapter_rows.append({"id": chapter, "output": relative, "sha256": sha(project / relative)})
    (merged / "textbook.md").write_text(body, encoding="utf-8", newline="")
    if batch_mode:
        payload = {
            "chapters": chapter_rows,
            "chunks": [
                dict(item, output=next(row["output"] for row in chapter_rows if row["id"] == item["chapter"]))
                for item in evidence
            ],
            "sha256": sha(merged / "textbook.md"),
        }
    else:
        payload = {
            "chapters": list(chapters),
            "chunks": evidence,
            "sha256": sha(merged / "textbook.md"),
        }
    write(merged / "assembly.json", payload)
    print("Merged without rewriting body text. Source revision: sha256:" + sha(merged / "textbook.md"))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    subcommands = parser.add_subparsers(dest="command", required=True)
    for name, help_text in (
        ("init", "create an empty legacy source project"),
        ("check-manifest", "validate batch/source inventory records and image hashes"),
        ("check", "validate a complete legacy or batch-mode project"),
        ("assemble", "validate and assemble reviewed chunks"),
    ):
        command = subcommands.add_parser(name, help=help_text)
        command.add_argument("project", type=Path)
    ingest_parser = subcommands.add_parser("ingest", help="copy page JPGs or render a PDF")
    ingest_parser.add_argument("project", type=Path)
    ingest_parser.add_argument("source", type=Path)
    ingest_parser.add_argument("--source-id", required=True)
    ingest_parser.add_argument("--dpi", type=int, default=300)
    batch_parser = subcommands.add_parser(
        "check-batch", help="validate one batch shard, its chunks, and review evidence"
    )
    batch_parser.add_argument("project", type=Path)
    batch_parser.add_argument("--batch", required=True)
    arguments = parser.parse_args()
    project = arguments.project.resolve()
    try:
        if arguments.command == "init":
            require(not project.exists(), "Choose a new project directory")
            shutil.copytree(ROOT / "assets/project-template", project)
            for directory in ("sources", "pages", "chunks", "merged"):
                (project / directory).mkdir()
        elif arguments.command == "ingest":
            ingest(project, arguments.source.resolve(), arguments.source_id, arguments.dpi)
        elif arguments.command == "check-manifest":
            batch_manifest_check(project)
            print(
                "Source/batch manifest checks pass; inventory evidence is recorded, but automatic checks do not prove semantic coverage."
            )
        elif arguments.command == "check-batch":
            batch_check(project, arguments.batch)
            print(
                "Selected batch checks pass; semantic coverage depends on the recorded image review and is not proven automatically."
            )
        elif arguments.command == "check":
            source_check(project)
            print(
                "Source/task structural checks pass; image-to-text meaning requires human source review."
            )
        else:
            assemble(project)
    except (
        ValueError,
        KeyError,
        TypeError,
        FileNotFoundError,
        json.JSONDecodeError,
        yaml.YAMLError,
    ) as error:
        parser.exit(1, str(error) + "\n")


if __name__ == "__main__":
    main()
