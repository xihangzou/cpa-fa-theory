# Direct reviewed Markdown handoff

User-authorized reconciliation for W1/W2 on 2026-09-08.

## Purpose

The original W1/W2 plan required the legacy JPG shard -> canonical tasks -> assembler path in issues #213 and #214. The user instead supplied the source PDFs in ChatGPT, requested direct conversion to organized Markdown, then requested chapter QA (#189-#204) to be applied to those direct artifacts. Issues #213 and #214 were therefore closed `not planned` as superseded and explicitly did not claim completion of their legacy assembler criteria.

This contract makes that already-reviewed direct path a first-class canonical handoff for W1 and W2. It is an explicit user-directed scope/contract reconciliation; it does not retroactively claim that legacy shard/task/assembly artifacts exist.

## Authority and source fidelity

For this W1/W2 exception only:

1. The user-provided source PDF is the content authority used by the direct conversion and adapted chapter/final QA. Rendered PDF pages used in review are treated as the visual source for this handoff.
2. The accepted learner Markdown is the exact direct artifact identified by its filename, chapter scope, question count and SHA-256 in `project/W1/qa/final.json` or `project/W2/qa/final.json`.
3. The adapted chapter QA issues #189-#194 (W1) and #195-#204 (W2), plus the final acceptance sample/evidence in `project/W1/qa/final.json` and `project/W2/qa/final.json`, are the semantic QA chain for those artifacts.
4. `project/W1/tasks.json`, `project/W2/tasks.json`, legacy chunk/fragments/reviews, `merged/assembly.json`, and `qa/assembly.json` are not required for this direct handoff and must not be fabricated merely to satisfy the superseded pipeline.
5. A GitHub byte-for-byte mirror at `project/W1/merged/textbook.md` or `project/W2/merged/textbook.md` is optional. If present, its bytes must match the accepted SHA-256. Absence of the mirror is not a blocker when the hash-pinned direct artifact and its QA record remain available in the user-authorized artifact channel.
6. Any partial `merged/chapters/` or `_direct_payload/` files created while attempting a mirror are staging only, are not canonical, and must not be used as learner handoff evidence.
7. This exception applies only to W1/W2 and does not change the source/assembly requirements for T1/T2/T3.

## Canonical acceptance rule

W1 or W2 may be accepted when all of the following are true:

- the exact direct Markdown artifact is identified by SHA-256, filename, chapter scope and question count in `qa/final.json`;
- chapter numbering and per-chapter question numbering are complete and sequential;
- every question retains an answer section;
- unresolved markers, replacement-character mojibake, Cloze syntax, and cross-book chapter contamination are absent;
- the previously executed chapter QA is complete for every numbered chapter;
- final acceptance independently checks at least the first and last content page of every numbered chapter and all recorded risk/correction pages against rendered source pages, while accurately describing this as a final sample rather than a new full-corpus visual review;
- source identity, sample pages, known source anomalies, output hash, reviewed QA revision and limitations are recorded in `qa/final.json`;
- the acceptance record itself is saved to and read back from `main`;
- if an on-repository Markdown mirror exists, its identity is verified against the accepted artifact; if no mirror exists, `qa/final.json` must explicitly record that the hash-pinned direct artifact is the canonical learner handoff and that GitHub stores its acceptance/provenance record rather than a byte mirror.

Under this reconciled rule, #220/#221 may close `completed` after a PASS `qa/final.json` is saved and read back. The legacy #213/#214 outputs remain intentionally absent and are not prerequisites for this direct-handoff acceptance.
