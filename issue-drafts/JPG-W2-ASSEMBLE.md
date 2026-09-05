<!-- learning-plan:cpa-fa-theory-jpg-md-20260905:JPG-W2-ASSEMBLE -->
# Goal
Aggregate the approved section-task shards and mechanically assemble only 財務会計論短答対策問題集　理論2 into clean per-chapter and per-book Markdown.

# Execution
Recommended model: GPT-5.6 Luna
Delivery branch: main
Bounded inventory, checksums, registry aggregation or assembly has deterministic acceptance checks.
User launches this issue manually. Do not start another issue or switch models automatically.

# Dependencies
- JPG-W2-QA01
- JPG-W2-QA02
- JPG-W2-QA03
- JPG-W2-QA04
- JPG-W2-QA05
- JPG-W2-QA06
- JPG-W2-QA07
- JPG-W2-QA08
- JPG-W2-QA09
- JPG-W2-QA10
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
- contracts/page-plan.json explicit chapter/batch/source order
- project/W2/sources.json, batches.json, fragments/, chunks/, reviews/, qa/chapters/
- Accepted helper and contracts/HELPER_COMPATIBILITY.md from JPG-000

# Owned paths
- project/W2/tasks.json
- project/W2/merged/
- project/W2/qa/assembly.json

# Outputs
- project/W2/tasks.json
- project/W2/merged/textbook.md
- project/W2/merged/chapter-*.md
- project/W2/merged/assembly.json
- project/W2/qa/assembly.json

# Acceptance criteria
- [ ] This is the sole post-inventory canonical tasks.json writer. Aggregate all section shards in physical/chapter/section order; set pass only from matching, current semantic QA evidence.
- [ ] Revalidate all image and chunk hashes, unique included-page batch ownership, complete section locators and chapter gate hashes. No missing/outdated QA, unresolved marker, orphan chunk or duplicate processing page is accepted.
- [ ] Run the helper assembler once validations pass. Strip YAML and only duplicated continuation boundary chapter/section headings. Do not rewrite, summarize, merge concepts, deduplicate body text or combine different books.
- [ ] Verify the assembled body against ordered reviewed chunk bodies after only the explicitly allowed removals; rerunning assembly must be byte-identical. Preserve CS part-qualified chapter/section IDs when applicable.

# Verification
- python3 workflow/scripts/source_md.py check project/W2 -> exit 0; every semantic gate also independently verified
- python3 workflow/scripts/source_md.py assemble project/W2 -> exit 0; rerun and compare SHA-256 -> unchanged
- Compare merged/textbook.md and merged/assembly.json to every ordered source chunk -> only allowed structural removals; git diff --check -> exit 0

# Evidence required
- Input chunk/QA hashes, canonical task count, expected/included/excluded page totals, manifest coverage report
- Assembly command results, before/after second-run hashes, exact body comparison and output SHA-256; saved main commit and remote readback

# Completion and stop
Save only the scoped outputs using the repository delivery policy. Re-fetch remote files and compare with the intended content. Report exact output paths, commit/hash, checks, and any remaining uncertainty. Close only when all criteria pass and outputs are available downstream, if the user launch authorizes closure. Otherwise leave open. Stop after this issue.

# Blocked or failed
Preserve partial work and state the exact missing source, dependency, failed criterion, or required decision. Do not broaden source scope, begin descendants, change the assigned model, or fabricate a pass.
