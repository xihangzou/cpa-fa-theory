<!-- learning-plan:cpa-fa-theory-jpg-md-20260905:JPG-HANDOFF -->
# Goal
Verify whole-corpus completion across all six book handoffs and publish a Markdown-only delivery index after every final acceptance gate passes.

# Execution
Recommended model: GPT-5.6 Luna
Delivery branch: main
Bounded inventory, checksums, registry aggregation or assembly has deterministic acceptance checks.
User launches this issue manually. Do not start another issue or switch models automatically.

# Dependencies
- JPG-T1-ACCEPT
- JPG-T2-ACCEPT
- JPG-T3-ACCEPT
- JPG-W1-ACCEPT
- JPG-W2-ACCEPT
- JPG-CS-ACCEPT
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
- All six project/BOOK/qa/final.json records and their pinned merged/source hashes
- contracts/source-catalog.json, contracts/page-plan.json and the complete plan graph

# Owned paths
- HANDOFF.md
- delivery/manifest.json

# Outputs
- HANDOFF.md with six per-book links, editions, counts and reviewed commit/SHA-256
- delivery/manifest.json with six independently accepted outputs

# Acceptance criteria
- [ ] All six final approvals refer to accessible main revisions and current exact output bytes; no missing source, chapter gate or failed acceptance.
- [ ] Index six separate textbook.md files without concatenating, integrating, renumbering or deduplicating their content. CS parts remain distinct within CS.
- [ ] No raw PDF/JPG/media/APKG, Anki/Cloze data or automated dispatch configuration is published. No ZIP/package is needed.
- [ ] Report verification and stop at this Markdown handoff. No automatic issue execution, model changes or new downstream tasks.

# Verification
- Independently recompute and compare six merged-file SHA-256 values to final QA -> all agree
- Read back every indexed file from GitHub at its declared revision -> links resolve and bytes match
- git diff --check -> exit 0; git ls-files -> no forbidden raw source/media/card files

# Evidence required
- Six output identities, source editions, exact verified revisions, aggregate chapter/page counts and remote readback results
- Whole-corpus PASS/BLOCKED status and saved index commit; no fabricated completion for an unfinished book

# Completion and stop
Save only the scoped outputs using the repository delivery policy. Re-fetch remote files and compare with the intended content. Report exact output paths, commit/hash, checks, and any remaining uncertainty. Close only when all criteria pass and outputs are available downstream, if the user launch authorizes closure. Otherwise leave open. Stop after this issue.

# Blocked or failed
Preserve partial work and state the exact missing source, dependency, failed criterion, or required decision. Do not broaden source scope, begin descendants, change the assigned model, or fabricate a pass.
