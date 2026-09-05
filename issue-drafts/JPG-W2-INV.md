<!-- learning-plan:cpa-fa-theory-jpg-md-20260905:JPG-W2-INV -->
# Goal
Produce a verified source manifest and batch page-ownership ledger for 財務会計論短答対策問題集　理論2; stop before conversion.

# Execution
Recommended model: GPT-5.6 Luna
Delivery branch: main
Bounded inventory, checksums, registry aggregation or assembly has deterministic acceptance checks.
User launches this issue manually. Do not start another issue or switch models automatically.

# Dependencies
None; this issue is initially ready.
Verify prerequisite outputs are saved and reviewed at the expected repository revision; a closed issue alone is insufficient.

# Source authority
- T1: /Users/xihangzou/Study/320_CPA/322_財務理論/images/cpa-fa-theory-textbook-1-jpg | 2024/2025年合格目標; published 2023-01-23; original PDF SHA-256 c09d9d91ce39de787cab04e146719d95b638134399d57112802ffacfa67243f3; image baseline in contracts/source-catalog.json | scope: Physical pages 001-362; exact conversion batches and metadata-only pages in contracts/page-plan.json. Existing JPGs are the content authority; PDF supports identity and planning only.
- T2: /Users/xihangzou/Study/320_CPA/322_財務理論/images/cpa-fa-theory-textbook-2-jpg | 2024/2025年合格目標; published 2023-05-04; original PDF SHA-256 ba4b33c8881021044b6360bfd10899f1b1f882bda3ccc7df3f1f895e9cc55ba5; image baseline in contracts/source-catalog.json | scope: Physical pages 001-450; exact conversion batches and metadata-only pages in contracts/page-plan.json. Existing JPGs are the content authority; PDF supports identity and planning only.
- T3: /Users/xihangzou/Study/320_CPA/322_財務理論/images/cpa-fa-theory-textbook-3-jpg | 2024/2025年合格目標; published 2023-02-28; original PDF SHA-256 1d9f0124a0c8ef759526decc90a1a410f694e2b7fa992b430fc413e783df85bc; image baseline in contracts/source-catalog.json | scope: Physical pages 001-344; exact conversion batches and metadata-only pages in contracts/page-plan.json. Existing JPGs are the content authority; PDF supports identity and planning only.
- W1: /Users/xihangzou/Study/320_CPA/322_財務理論/images/cpa-fa-theory-short-answer-workbook-1-jpg | 2024/2025年合格目標; published 2023-01-23; original PDF SHA-256 cd4b9e8b7be475d5e40785cddfd41e48e775b57eeaed6ffb2b90f4c21c0fd04f; image baseline in contracts/source-catalog.json | scope: Physical pages 001-204; exact conversion batches and metadata-only pages in contracts/page-plan.json. Existing JPGs are the content authority; PDF supports identity and planning only.
- W2: /Users/xihangzou/Study/320_CPA/322_財務理論/images/cpa-fa-theory-short-answer-workbook-2-jpg | 2024/2025年合格目標; published 2023-01-23; original PDF SHA-256 4344d7dc71d2193679eb9c7a0cd6a911fe3d8d2b89b4336ce51d7fca5a17245a; image baseline in contracts/source-catalog.json | scope: Physical pages 001-398; exact conversion batches and metadata-only pages in contracts/page-plan.json. Existing JPGs are the content authority; PDF supports identity and planning only.
- CS: /Users/xihangzou/Study/320_CPA/322_財務理論/03_コントレ/財務会計論コンパクトサマリー　短答論点総まとめテキスト　理論.pdf | 2024/2025年合格目標; published 2023-01-23; original PDF SHA-256 f76627b0c8e389d094c96ed9a3e8941c1f0a705d55d96dc7d1fd70a84bd7ac39; image baseline in contracts/source-catalog.json | scope: Physical pages 001-350; exact conversion batches and metadata-only pages in contracts/page-plan.json. JPGs not yet produced: prerequisite JPG-CS-INV owns preparation from this PDF.
Read workflow/SKILL.md, workflow/WORKFLOW.md, and the repository AGENTS.md. Source facts and current user instructions govern the work.

# Inputs
- AGENTS.md, contracts/CONTENT_RULES.md, contracts/RECORDS.md, contracts/DELIVERY.md
- contracts/source-catalog.json entry W2: exact PDF/JPG locations and SHA-256 baseline
- contracts/page-plan.json entry W2: all 398 physical pages, chapter starts, batch ranges, metadata-only candidates
- Edition colophon: physical 396; 2024/2025年合格目標; 2023-01-23

# Owned paths
- project/W2/sources.json
- project/W2/source-map.json
- project/W2/batches.json
- project/W2/inventory-review.json
- project/W2/pages/
- project/W2/sources/
- project/W2/local-staging/

# Outputs
- project/W2/sources.json
- project/W2/source-map.json
- project/W2/batches.json
- project/W2/inventory-review.json
- Ignored canonical image cache (local only)

# Acceptance criteria
- [ ] Existing image filenames contain a Japanese prefix and fail the helper's page-NNN.jpg-only input rule. Stage byte-identical renamed copies in ignored project/W2/local-staging/, then ingest to the local ignored canonical cache. Never rename or overwrite the designated originals, and never re-render the existing JPGs.
- [ ] Account for all 398 physical pages; verify source identity/order/dimensions/orientation/legibility and preserve originals. Every source and cached image has its actual SHA-256; no missing/duplicate number or unexpected file is ignored.
- [ ] Populate sources.json with explicit per-page printed labels (including part/chapter reset), include/exclude reasons, original identity and source-map.json with exact original filename to canonical cache filename. Do not infer a constant printed-page offset.
- [ ] Populate batches.json from the exact planned ranges. Included pages belong to one batch only. Metadata/blank/divider exclusions require image-backed reasons; chapter dividers with substantive meaning must retain that meaning.
- [ ] Verify each planned split does not strand a table, diagram, question, answer, example or condition. Record checks against the start and end images of every batch. If a boundary or metadata-only candidate contains unplanned substantive content, leave affected readiness blocked and request an Astra revision; do not expand scope silently.
- [ ] Record source inspection and chapter/section boundary evidence in inventory-review.json. Do not set chunk/task semantic status to pass and do not create chunks or merged Markdown.
- [ ] Source paths are local-only. Document a repeatable byte-preserving cache restoration procedure in source-map.json; verify its output hashes. No PDFs/JPGs committed to GitHub.

# Verification
- python3 -m json.tool project/W2/sources.json -> exit 0; independently compare every page count/name/hash against contracts/source-catalog.json
- python3 -m json.tool project/W2/batches.json -> exit 0; compare the union and intersections of processing_pages -> complete included-page coverage, pairwise disjoint owners
- Reopen colophon, every batch boundary pair and page contact sheets; full-size inspect any anomaly -> explicit legibility/identity/boundary evidence, no guessed pass
- git diff --check and git ls-files -> no whitespace errors or tracked source PDFs/JPGs

# Evidence required
- Exact source PDF/JPG inventory digests, edition locator, counts, exclusion reasons, printed-page ledger, cache restoration instructions
- Actual inspection results and unresolved source anomalies; saved main commit and remote readback

# Completion and stop
Save only the scoped outputs using the repository delivery policy. Re-fetch remote files and compare with the intended content. Report exact output paths, commit/hash, checks, and any remaining uncertainty. Close only when all criteria pass and outputs are available downstream, if the user launch authorizes closure. Otherwise leave open. Stop after this issue.

# Blocked or failed
Preserve partial work and state the exact missing source, dependency, failed criterion, or required decision. Do not broaden source scope, begin descendants, change the assigned model, or fabricate a pass.
