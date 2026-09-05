# CPA financial-accounting theory: JPG to Markdown

Planning and manual execution for six designated 2024/2025 CPA theory books. Each book will have its own source-faithful Japanese Markdown handoff. This setup contains **no production conversion, integration or cards**.

Start with the [live issue index](ISSUES.md), [plan](PLAN.md), [exact sources](SOURCES.md), and [execution contract](AGENTS.md). The graph has 226 issues: one helper-compatibility prerequisite, six inventories, 146 conversion batches, six pilot gates, 54 chapter-review groups, six assemblies, six final book acceptances and one six-book handoff index. Conversion batches cover at most 24 physical pages; small CS chapters are grouped while retaining distinct chapter/section outputs.

Seven issues are initially ready: JPG-000 (Sol) and the six book inventories (Luna). Every conversion waits for its source inventory and accepted helper compatibility. The remaining conversion batches also wait for that book's pilot QA. All work is user-launched, one selected issue at a time; no dispatch automation is installed.

## Manual launch

Choose the issue's recommended model, then use:

> Execute only [GitHub issue URL] in xihangzou/cpa-fa-theory. Verify its dependencies and source revision, follow the issue's scope and repository workflow rules, produce and save its outputs to main, and run the required checks and reviews. Post completion evidence and close this issue only if all acceptance criteria pass and its outputs are available for downstream tasks. Otherwise leave it open and report the exact blocker. Stop after this issue. Do not execute another issue, launch workers, or change models.

A draft-only or review-only launch overrides the default completion actions. Read [delivery policy](contracts/DELIVERY.md) before writes. Dependency closure is insufficient without valid output evidence at the current revision.

## Important source/layout facts

- The three textbooks and two workbooks provide 1,758 existing JPGs. Filename handling is source-specific: verify the helper-compatible page-NNN.jpg rule first, then use byte-preserving local staging with canonical names where needed; never modify designated originals.
- The compact summary provides only a 350-page PDF. Its inventory issue prepares and validates local JPGs before conversion.
- Multiple source sections can share one physical page. [JPG-000's contract](contracts/RECORDS.md) retains one page-batch owner and separate section records; conversion cannot begin until the helper implements and proves this safely.
- Raw source files, OCR scratch text, media and Anki packages are excluded from this public repository. Future Markdown stays under its separate `project/BOOK/` paths.

The copied [content workflow](workflow/WORKFLOW.md) remains the content authority. Its missing manual planning policy was recovered from the exported Version 3 workflow kit; [provenance](workflow/provenance.json) records exact origins/hashes.

Setup checks: `python3 scripts/verify_plan.py` and `python3 workflow/scripts/plan_repo.py plan.json`. These validate planning structure only and do not run the conversion pipeline.
