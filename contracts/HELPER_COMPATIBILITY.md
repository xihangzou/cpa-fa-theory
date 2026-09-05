# Helper compatibility contract

Issue `JPG-000` adds batch-aware validation without replacing the legacy `sources.json` plus `tasks.json` workflow. The implementation baseline was remote `main` commit `040f12a6d01d1fd90864037c464b8d5defbfcfe3`.

## Why the additive model is compatible

A batch is the sole processing owner of physical page images. A section task is a provenance citation inside that owner. Two section tasks may therefore cite distinct regions of the same included page without creating a second page owner. A task still represents exactly one section or an adjacent bounded continuation of the same section ID.

The designated layout inspection confirmed the two required shapes without transcribing production content: CS physical 008 contains two numbered sections on one image, and CS physical 208/209 is a question/answer pair. The first requires shared section-level citation within one page batch; the second requires a batch to retain adjacent pages as one review unit. Neither case requires relaxing the one-owner rule or flattening source sections.

All six cataloged source PDFs matched their planned SHA-256 values and physical page counts during this compatibility review. All 1,758 supplied JPGs for T1, T2, T3, W1, and W2 also matched their cataloged byte hashes; CS has no planned JPG baseline before its inventory issue. These identity checks are not production ingestion or semantic source review.

## Commands

```text
python3 workflow/scripts/source_md.py check-manifest PROJECT
python3 workflow/scripts/source_md.py check-batch PROJECT --batch ISSUE-ID
python3 workflow/scripts/source_md.py check PROJECT
python3 workflow/scripts/source_md.py assemble PROJECT
```

- `check-manifest` validates `sources.json`, `source-map.json`, `inventory-review.json`, and `batches.json`, including live source-image hashes and unique included-page ownership. It does not require future fragments or chunks.
- `check-batch` first validates the complete manifest, then only the named fragment, its chunks, and its review. Unfinished sibling batches are allowed.
- `check` retains legacy behavior when `batches.json` is absent. In batch mode it validates every batch, requires canonical `tasks.json` to equal the ordered fragment tasks, and requires current PASS chapter gates.
- `assemble` always runs the applicable complete check first. Batch-mode assembly cannot run from fragment evidence alone or while a source, batch, task, review, or chapter gate is unpassed.

Success messages deliberately state that structural/hash checks do not prove semantic source coverage. A human image review remains authoritative.

## Batch-mode record schema

Existing `sources.json` fields retain their legacy meaning. Batch mode additionally requires valid JSON `source-map.json` and this minimal acceptance state in `inventory-review.json`:

```json
{"status":"pass","unresolved_count":0}
```

`batches.json` is an ordered array. Every accepted batch uses:

```json
{
  "id": "BATCH-ID",
  "expected_pages": ["SRC:001"],
  "processing_pages": ["SRC:001"],
  "fragment": "fragments/BATCH-ID.json",
  "chapter_keys": ["C01"],
  "inventory_status": "pass"
}
```

The helper requires ordered, unique, known physical IDs. `processing_pages` must exactly equal the included pages in `expected_pages`. Expected ranges cannot overlap or return to an earlier physical position, and every included manifest page has exactly one batch owner. A batch is single-source. Excluded pages require manifest reasons and never appear in `processing_pages`.

Each `fragments/BATCH-ID.json` uses:

```json
{
  "batch_id": "BATCH-ID",
  "source_id": "SRC",
  "status": "pass",
  "tasks": [],
  "review": "reviews/BATCH-ID.json"
}
```

Each ordered task has these fields:

```json
{
  "id": "BATCH-ID-S01",
  "batch_id": "BATCH-ID",
  "chapter": "C01",
  "section": "C01.1",
  "title": "Synthetic section title",
  "expected_pages": ["SRC:001"],
  "processing_pages": ["SRC:001"],
  "output": "chunks/BATCH-ID/section.md",
  "status": "pass",
  "locators": [
    {
      "page": "SRC:001",
      "printed_page": "1",
      "source_region": "upper region",
      "destination_heading": "## Synthetic section title"
    }
  ],
  "chunk_sha256": "CURRENT_64_HEX_DIGEST"
}
```

Task pages and locator first appearances remain in source order. Task pages stay inside the owning batch; locator pages stay inside the task processing set and reproduce the manifest's actual `printed_page` value. The locator union must cover every task processing page, while the task citation union must cover every included batch page. Sharing a page between tasks is valid only inside that page's one owning batch. Every declared `chapter_keys` value must have a section task.

The chunk YAML requires `id`, `pdf_pages`, `pages`, `chapter`, `section`, `title`, and `batch_id`. Chapter IDs use letters, digits, underscores, and hyphens; section IDs additionally allow dots such as `01.1`. Its first two nonblank body lines are the matching `#` chapter and `##` section headings. Other `##` headings cannot introduce a second section. Repeated adjacent tasks may reuse one section ID as continuations; after another section starts, returning to the earlier section ID is rejected.

Each batch review uses the following checked fields:

```json
{
  "batch_id": "BATCH-ID",
  "source_id": "SRC",
  "status": "pass",
  "source_images": [{"page":"SRC:001","sha256":"CURRENT_64_HEX_DIGEST"}],
  "section_outputs": [{"task":"BATCH-ID-S01","chunk_sha256":"CURRENT_64_HEX_DIGEST"}],
  "coverage": [{"page":"SRC:001","regions":["upper region"],"status":"pass"}],
  "findings": [],
  "corrections": [],
  "checks": {
    "numerical": "not_applicable",
    "diagram": "not_applicable",
    "false_proposition": "not_applicable"
  },
  "unresolved_count": 0,
  "reviewer_model": "recorded reviewer",
  "dependency_commits": ["FULL_40_HEX_COMMIT"]
}
```

Review source images and section outputs must exactly match current ordered hashes. Coverage has one PASS row per processing page with nonempty reviewed-region descriptions. Each specialized check is `pass` or `not_applicable`; all other statuses are rejected.

Canonical `tasks.json` is the exact ordered concatenation of fragment task arrays. For each current chapter `KEY`, `qa/chapters/KEY.json` requires:

```json
{
  "chapter": "KEY",
  "status": "pass",
  "unresolved_count": 0,
  "chunks": [{"task":"BATCH-ID-S01","chunk_sha256":"CURRENT_64_HEX_DIGEST"}]
}
```

The `chunks` array exactly lists that chapter's canonical tasks and current hashes in source order.

## Rejection and path rules

The helper rejects missing or duplicate IDs/pages, missing one-owner coverage, overlapping/out-of-order batches, changed source or chunk hashes, project-relative paths that resolve outside the project, excluded-page processing, batch/source/chapter mismatches, out-of-batch locators, incomplete locator/page coverage, stale review or chapter hashes, unresolved markers, bold source Markdown, non-PASS gates, contradictory repeated headings, and out-of-order continuations.

Project-controlled paths (`original` PDF, page image, batch fragment, batch review, and task output) are resolved beneath the project, including symlink resolution. Local authority paths stored as inventory provenance in `source-map.json` are records rather than helper-controlled output paths and are not opened by these commands.

## Byte-preserving assembly

Legacy assembly retains its existing output behavior. Batch-mode assembly:

1. removes each chunk's YAML envelope;
2. keeps the first chapter and section boundary headings;
3. removes only an adjacent chunk's duplicated initial chapter heading, plus its duplicated initial section heading when the section ID is a continuation;
4. concatenates every other UTF-8 body byte in canonical source order.

The assembler does not search-and-delete headings inside body content. It records the exact removed boundary headings in `merged/assembly.json`, along with current task, batch, chapter, section, page, chunk, chapter-output, and merged-output hashes. Re-running assembly is byte-identical.

The synthetic golden fixture includes one shared page, an adjacent cross-batch continuation, significant trailing spaces, a tab, and an identical internal section heading that must not be removed. Its assembled SHA-256 is `b6c472373dbaebb0621d91fdcb227f285af8f74cd62afa9182d865a4eb9b5b88`.

## Verification evidence

- `python3 -m unittest discover -s workflow/tests -v`: 31 synthetic legacy/batch positive and negative tests passed.
- `python3 workflow/scripts/source_md.py --help`: `check-manifest`, `check-batch`, `check`, and `assemble` are documented.
- Synthetic golden output: exact bytes and second-run stability passed; SHA-256 `b6c472373dbaebb0621d91fdcb227f285af8f74cd62afa9182d865a4eb9b5b88`.
- No production chunks, OCR, transcription, integration, cards, source media, or semantic PASS claims were produced.
