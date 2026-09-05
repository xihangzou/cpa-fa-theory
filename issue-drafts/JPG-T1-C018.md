<!-- learning-plan:cpa-fa-theory-jpg-md-20260905:JPG-T1-C018 -->
# Goal
Produce source-reviewed section chunks for 12 財務会計の概念フレームワーク, physical pages 252-271, only.

# Execution
Recommended model: GPT-5.6 Sol
Delivery branch: main
Source interpretation, layout contracts and omission review require judgment.
User launches this issue manually. Do not start another issue or switch models automatically.

# Dependencies
- https://github.com/xihangzou/cpa-fa-theory/issues/2
- https://github.com/xihangzou/cpa-fa-theory/issues/1
- https://github.com/xihangzou/cpa-fa-theory/issues/15
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
- project/T1/sources.json, source-map.json, batches.json and inventory-review.json from JPG-T1-INV
- Processing images: T1:252-271, intersected with the inventory-approved include set. Exact filenames resolve via source-map.json; no outside processing images.
- Chapter/section range: 12 財務会計の概念フレームワーク. Batch contract: contracts/page-plan.json, batch JPG-T1-C018.
- contracts/HELPER_COMPATIBILITY.md and tested helper from JPG-000
- project/T1/qa/pilot.json from JPG-T1-PILOT-QA: accepted source-specific chunk conventions

# Owned paths
- project/T1/chunks/JPG-T1-C018/
- project/T1/fragments/JPG-T1-C018.json
- project/T1/reviews/JPG-T1-C018.json

# Outputs
- project/T1/chunks/JPG-T1-C018/
- project/T1/fragments/JPG-T1-C018.json
- project/T1/reviews/JPG-T1-C018.json

# Acceptance criteria
- [ ] Create one section-sized chunk (or bounded continuation) per actual section within the owned source range; preserve # chapter, ## section, ### topic, #### subdivision. No bold, Cloze, Front/Back, integration or card output.
- [ ] Preserve definitions, distinctions, conditions, exceptions, timing, reasons, procedures, units, debit/credit/amount tables, intermediate calculations, examples and diagram-only meaning. Do not modernize the pinned edition or add other-book/web/general-knowledge facts.
- [ ] Record an ordered fragments/JPG-T1-C018.json section-task shard, unique chunk IDs, exact chapter/section IDs, original title, physical and printed page locators, and a page/region-to-chunk source map. One physical-page batch owns processing; same-page sections must each have complete, distinct semantic coverage.
- [ ] Review every included processing image against all section chunks, including margins, sidebars and exceptions. All omissions resolved; no unresolved markers on PASS. Record excluded/no-content page reasons from the manifest.
- [ ] Emit per-batch review/status evidence only. Do not edit shared sources.json, batches.json, tasks.json, another batch, merged output, or plan files.
- [ ] If an example/question/answer spans beyond this range or the source/layout contract cannot be met, leave this issue open with BLOCKED evidence for an Astra revision. Do not read outside processing scope to fill the gap.

# Verification
- python3 workflow/scripts/source_md.py check-batch project/T1 --batch JPG-T1-C018 -> exit 0 with manifest/hash/scope/schema checks; command becomes available only after JPG-000
- git diff --check -> exit 0; python3 -m json.tool project/T1/reviews/JPG-T1-C018.json -> valid review evidence
- Reopen every designated included image at readable resolution and compare each section, table, example and exception to its chunk -> no missing semantic unit and no unlabelled false statement

# Evidence required
- Source/image hashes and actual dependency commits; exact chunk/shard/review paths and output hashes
- Page-by-page source-fidelity matrix, specific numerical/diagram/question-pair checks and unresolved count
- Saved main commit; remote files re-fetched and compared; PASS/BLOCKED/FAIL with checks actually run

# Completion and stop
Save only the scoped outputs using the repository delivery policy. Re-fetch remote files and compare with the intended content. Report exact output paths, commit/hash, checks, and any remaining uncertainty. Close only when all criteria pass and outputs are available downstream, if the user launch authorizes closure. Otherwise leave open. Stop after this issue.

# Blocked or failed
Preserve partial work and state the exact missing source, dependency, failed criterion, or required decision. Do not broaden source scope, begin descendants, change the assigned model, or fabricate a pass.
