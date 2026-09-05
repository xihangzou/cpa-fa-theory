---
name: jpg-to-md
description: Convert designated textbook page JPGs into verified structured Markdown chunks and a clean per-textbook Markdown file, following the bookkeeping source-conversion workflow.
---

# JPGs to Markdown

Read [WORKFLOW.md](WORKFLOW.md). Run only the requested source-conversion scope and stop after verified Markdown and its source/QA records. Do not integrate different textbooks or create Anki cards in this workflow.

Use exact processing image sets, physical page IDs, and separate printed labels. Preserve definitions, conditions, exceptions, calculations, useful examples, and diagram-only meaning. Images are the content authority; OCR is only a draft. Resolve uncertainty against the designated source instead of supplementing from another textbook or general knowledge.

Produce one reviewed chunk per bounded section/task. Assemble one textbook’s chunks without rewriting body content. Review source fidelity before setting task status to pass; automatic checks cannot prove semantic completeness.

The optional PDF ingest helper is preparation for users who have not yet produced page JPGs. For existing repository tasks, respect current source-folder and Processing images rules and verify remote saves when authorized. Output only this stage’s deliverables.
