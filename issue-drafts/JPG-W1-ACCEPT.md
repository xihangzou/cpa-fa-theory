<!-- learning-plan:cpa-fa-theory-jpg-md-20260905:JPG-W1-ACCEPT -->
# Goal
Accept the complete W1 Markdown handoff only after verifying source completeness and that assembly did not rewrite reviewed text.

# Execution
Recommended model: GPT-5.6 Sol
Delivery branch: main
Source interpretation, layout contracts and omission review require judgment.
User launches this issue manually. Do not start another issue or switch models automatically.

# Dependencies
- https://github.com/xihangzou/cpa-fa-theory/issues/213
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
- project/W1/sources.json, batches.json, tasks.json, all source/chunk/chapter QA and merged/assembly.json
- project/W1/merged/textbook.md and chapter outputs; original designated images for all disputed/sampled claims

# Owned paths
- project/W1/qa/final.json

# Outputs
- project/W1/qa/final.json with approved source/output hashes and handoff revision

# Acceptance criteria
- [ ] Audit every chapter approval against current chunks and image hashes and check the full merged body against the approved ordered chunks. Confirm all planned chapters/front matter and exclusions are accounted for.
- [ ] Independently inspect at least the first and last content page of every chapter and every recorded risk/exception/diagram/pair-boundary example against images and merged text; report the exact sampled pages. Prior chapter QA supplies full-page review, and this final sample must not be described as another full-corpus visual review.
- [ ] Zero unresolved markers, missing semantic reviews, stale hashes, unlabelled false propositions, cross-book integration or cards. Any defect leaves this issue open and records owning issue/correction scope; this acceptance issue must not silently edit source chunks.
- [ ] Record source edition and identity, full merged SHA-256, exact reviewed main commit and downstream-only Markdown handoff status.

# Verification
- python3 workflow/scripts/source_md.py check project/W1 -> exit 0; verify approval hashes still match
- Whole-output comparison against allowed assembly transformation -> exact agreement; stated image samples -> all faithful
- Remote main readback -> output bytes and recorded handoff revision match

# Evidence required
- Exact reviewed commit, merged/source hashes, chapter evidence coverage, explicit sampled page list, semantic findings and limitations
- Final PASS/BLOCKED verdict; stop without downstream integration or Anki/card production

# Completion and stop
Save only the scoped outputs using the repository delivery policy. Re-fetch remote files and compare with the intended content. Report exact output paths, commit/hash, checks, and any remaining uncertainty. Close only when all criteria pass and outputs are available downstream, if the user launch authorizes closure. Otherwise leave open. Stop after this issue.

# Blocked or failed
Preserve partial work and state the exact missing source, dependency, failed criterion, or required decision. Do not broaden source scope, begin descendants, change the assigned model, or fabricate a pass.
