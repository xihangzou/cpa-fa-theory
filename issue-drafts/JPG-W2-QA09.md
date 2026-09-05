<!-- learning-plan:cpa-fa-theory-jpg-md-20260905:JPG-W2-QA09 -->
# Goal
Review the whole of chapters 38, 39 (W2 physical 324-371) across chunk boundaries, with one saved verdict per chapter.

# Execution
Recommended model: GPT-5.6 Sol
Delivery branch: main
Source interpretation, layout contracts and omission review require judgment.
User launches this issue manually. Do not start another issue or switch models automatically.

# Dependencies
- https://github.com/xihangzou/cpa-fa-theory/issues/129
- https://github.com/xihangzou/cpa-fa-theory/issues/130
- https://github.com/xihangzou/cpa-fa-theory/issues/131
- https://github.com/xihangzou/cpa-fa-theory/issues/19
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
- project/W2/sources.json, batches.json, inventory-review.json and qa/pilot.json
- All section chunks/fragments/reviews for batches JPG-W2-C021, JPG-W2-C022, JPG-W2-C023
- Processing images only: W2:324-371; actual chapter titles and ranges in contracts/page-plan.json

# Owned paths
- project/W2/chunks/JPG-W2-C021/
- project/W2/fragments/JPG-W2-C021.json
- project/W2/reviews/JPG-W2-C021.json
- project/W2/chunks/JPG-W2-C022/
- project/W2/fragments/JPG-W2-C022.json
- project/W2/reviews/JPG-W2-C022.json
- project/W2/chunks/JPG-W2-C023/
- project/W2/fragments/JPG-W2-C023.json
- project/W2/reviews/JPG-W2-C023.json
- project/W2/qa/chapters/38.json
- project/W2/qa/chapters/39.json

# Outputs
- project/W2/qa/chapters/38.json
- project/W2/qa/chapters/39.json
- Scoped source-fidelity corrections and refreshed affected hashes

# Acceptance criteria
- [ ] Review every included page in each named chapter, plus its inclusion/exclusion ledger; compare the union of chunks to the complete chapter, not only each chunk in isolation.
- [ ] Verify section order and continuations, table headers, worked examples and question/answer pairs survive boundaries; all definitions/conditions/exceptions/diagram-only content have precise locators.
- [ ] Correct only the named chapters, even if a shared batch directory contains neighboring chapters. Update affected shard/review hashes and record one PASS/BLOCKED verdict per chapter. No changes to another chapter, source/rule contract, canonical tasks.json or merged files.
- [ ] A source/rule/boundary mismatch requires an Astra planning revision; do not broaden scope, weaken rules, or start assembly.

# Verification
- Run check-batch under project/W2 for every affected batch -> exit 0 with current hashes
- Image-to-chapter review of every page in the named range -> no missing or invented meaning; chapter evidence lists all reviewed chunk hashes
- git diff --check -> exit 0; verify no chapter outside the owned review scope changed

# Evidence required
- One chapter QA record per chapter with source/page coverage, section list, actual findings, corrections and approved hashes
- Commands, exit codes, final dependency/main commits and remote readback; unresolved findings explicitly block acceptance

# Completion and stop
Save only the scoped outputs using the repository delivery policy. Re-fetch remote files and compare with the intended content. Report exact output paths, commit/hash, checks, and any remaining uncertainty. Close only when all criteria pass and outputs are available downstream, if the user launch authorizes closure. Otherwise leave open. Stop after this issue.

# Blocked or failed
Preserve partial work and state the exact missing source, dependency, failed criterion, or required decision. Do not broaden source scope, begin descendants, change the assigned model, or fabricate a pass.
