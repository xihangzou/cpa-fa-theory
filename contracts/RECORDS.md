# Source, section and evidence records

This is the target additive record contract for JPG-000. The shipped `source_md.py` is unchanged at setup and does not yet implement batch mode or the new check commands. Consumers must verify JPG-000's accepted output at its real delivery commit before using them. Do not fabricate that commit.

## Why page batches and section tasks are separate

The original helper couples one image-processing task with one section chunk. CS physical 008 visibly contains multiple sections on one page. A physical page must have one processing owner, while each section still needs its own chunk and locator. One user-launched issue therefore owns an exact physical-page batch and emits ordered section-task records inside it. This groups source-reading responsibility; it does not merge source sections or permit duplicate processing owners. If this additive representation cannot preserve the workflow's one-owner and one-section requirements, JPG-000 must remain BLOCKED for an Astra revision, and conversion remains blocked.

## Inventory-owned records

Each `project/BOOK/sources.json` uses the supplied source/image fields: source ID, kind, origin and SHA-256, edition, optional rendering DPI, and `pages` with `id`, `pdf_page`, `printed_page`, project-relative canonical `image`, SHA-256, width, height, disposition and exclusion reason. `printed_page` is the actual printed label, qualified by source part/chapter where needed. Null means no printed label exists, never not yet checked on an accepted inventory.

`source-map.json` records the exact local original folder/file and immutable baseline digest for each canonical `pages/BOOK/page-NNN.jpg` file. Include repeatable cache restoration instructions and byte-hash verification. Existing JPGs are copied/renamed byte-for-byte into an ignored staging directory because ingest accepts only `page-NNN.jpg` names. Never rename originals. CS alone uses the pinned PDF and records the renderer, version and 300 DPI render settings plus actual generated hashes. No fake future image hashes.

`batches.json` is an ordered array. Every row has:

- `id`: the exact conversion logical issue ID from `contracts/page-plan.json`;
- `expected_pages`: all physical IDs in its frozen range;
- `processing_pages`: the expected IDs whose verified disposition is include;
- `fragment`: `fragments/ISSUE-ID.json`;
- `chapter_keys`: the planned chapter keys;
- `inventory_status`: `pass` only when identity, exclusions and safe boundaries were inspected.

All included physical pages have exactly one batch owner. Every expected page exists in the source manifest, processing is a subset of expected, and excluded pages have reasons. No worker may modify another batch's scope. An empty all-excluded batch must be explicitly reconciled by Astra rather than fabricated into a chunk.

`inventory-review.json` records the actual source identity/edition check, every physical page's inspection/disposition, batch boundary evidence, anomalies and manifest/map/batch digests. It is source-preparation evidence, not converted-content approval.

## Conversion-owned section shards

`fragments/ISSUE-ID.json` contains `batch_id`, `source_id`, `status`, `tasks` (ordered), and `review` (the matching `reviews/ISSUE-ID.json` path). Each section task has:

- unique stable `id`, `batch_id`, `chapter` and `section` IDs;
- original `title`, `expected_pages`, `processing_pages` (section's source citations, within its owning batch), `output` and `status`;
- exact `locators`: source physical ID, printed label, source section/topic/question or region description, and destination chunk heading;
- `chunk_sha256` after the semantic review actually passes.

Only the batch ledger counts physical processing ownership. Section citation lists may share a physical image inside the same owning batch, because different source sections occupy different regions. They never authorize another issue to process that image. Every included batch page must have complete content/no-content review coverage across its section records, including sidebars. Reject out-of-batch locators and unknown pages. Semantic completeness of region coverage requires a full image review.

One chunk per section or bounded continuation lives under `chunks/ISSUE-ID/`. Its YAML retains `id`, physical `pdf_pages`, actual printed `pages`, `chapter`, `section`, `title`, and `batch_id`. Reuse the same section ID and heading for a continuation; preserve original chapter/section titles. A source-derived chapter/section title is selected and locked by the pilot; an OCR-only title is not final authority. Workbooks may use a faithful section grouping of their source topical headings and complete question/answer blocks, with question numbers as topics. Never flatten a numbered source section to hide a schema limitation.

`reviews/ISSUE-ID.json` includes status, source image hashes, section output hashes, per-page and region-to-chunk coverage, actual fidelity findings/corrections, numerical/diagram/false-proposition checks, unresolved count, reviewer model, and dependency commits. Do not mark semantic PASS from file existence or a helper exit code.

## Review and canonical records

`qa/pilot.json` records the accepted pilot revision, source-specific conventions and gate verdict. Later reviewed corrections can supersede pilot chunk hashes; preserve the historical pilot evidence and identify the newer chapter approval explicitly. A historical pilot hash is not a claim that an earlier byte version is still current.

`qa/chapters/KEY.json` owns exactly one complete chapter's approval. Record only that chapter's current section chunk hashes, all included/excluded pages, review findings and corrections. QA issues can batch several small chapters, but emit separate chapter records. CS QA issues sharing a conversion batch directory are serialized; a reviewer must still change only its named chapters. Refreshed shard hashes must not invalidate unrelated unchanged chapter approvals.

The assembly issue alone writes canonical `tasks.json` by aggregating all passed section shards in page-plan order. Canonical task PASS requires current chapter approval for the chunk hash. Batch-mode `check` validates source/cache hashes, unique page-batch ownership, section citation bounds/coverage, chunk metadata, unresolved markers, statuses, and all current chapter hashes. Legacy projects without a batch ledger retain their old validation behavior.

`qa/assembly.json` records inputs, ordered section IDs, inclusion/exclusion totals, allowed structural removals, exact body comparison, rerun stability and output hashes. `merged/assembly.json` preserves ordered chapter/section/task/batch-to-page and chunk-to-output mappings, plus final SHA-256. It must not be described as word-level semantic proof.

`qa/final.json` records PASS/BLOCKED, exact source and merged hashes, reviewed delivery commit, all chapter approval references, the actual final image sample list, limits of that sample, and handoff status. Final acceptance is read-only to learner content; defects return to the owning scope.

## Required helper behavior after JPG-000

- `python3 workflow/scripts/source_md.py check-manifest project/BOOK`: validate accepted source and batch records plus local image hashes, without requiring future chunks.
- `python3 workflow/scripts/source_md.py check-batch project/BOOK --batch ISSUE-ID`: validate only that batch's section shards, chunks and review evidence against accepted source/page ownership; do not require unfinished siblings.
- `python3 workflow/scripts/source_md.py check project/BOOK`: validate canonical tasks and all current chapter gates before assembly.
- `python3 workflow/scripts/source_md.py assemble project/BOOK`: run full checks then assemble with only allowed removals, preserving all remaining chunk body content. A second run is byte-identical.

These commands are future deliverables of JPG-000, not setup checks already performed. Synthetic positive/negative and golden-output fixtures must validate them before a pilot starts. Full source semantics always require image review.

## Python environment

Use an isolated, activated Python environment with `python3 -m pip install -r workflow/requirements.txt` before helper commands. Python, Pillow/PyYAML and Poppler availability are preparation checks, not evidence of source review. The `python3` commands in issues mean that configured environment. Use local ignored scratch/cache paths and do not commit environment files.
