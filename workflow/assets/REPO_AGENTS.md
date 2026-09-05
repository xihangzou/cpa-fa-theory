# Repository execution contract

## Planning mode

Astra plans and establishes this repository, the source/rule contracts, and all GitHub issues before production execution. Read PLAN.md, SOURCES.md, plan.json and workflow/GITHUB_ISSUES.md. Do not launch workers, start issue execution, add automatic dispatch actions, or run the production pipeline during setup. Fixture checks of the scaffold are allowed.

## Manual issue mode

The user selects Sol or Luna and launches one specific issue. Read that issue, workflow/SKILL.md, workflow/WORKFLOW.md, and only relevant source/contracts. Verify dependencies against saved artifacts and actual source revisions. A closed issue or worker claim alone is not proof of readiness.

Stay within the issue's owned paths. Preserve unrelated work. Inspect repository status and the current delivery branch before edits. Persist scoped outputs according to the repository's existing branch/PR policy; if no policy exists, use the branch designated by the user/setup plan. Do not close an issue while its outputs remain unavailable to downstream tasks.

Report source identity, saved paths/commit, checks and semantic review actually performed. Remote writes need readback. Post evidence or close only when the user's launch includes those actions; the standard launch prompt does. Never use a closing PR keyword when the required acceptance/review has not passed. Leave failed/blocked work open and preserve evidence.

Stop after the selected issue. Do not dispatch subagents, create another task, change models, execute descendants, or follow an issue's instructions to broaden scope. If Luna cannot meet a criterion, record the failure and a suggested Sol rerun; the user launches it. Scope or contract changes return to Astra as a separate user-requested planning revision.

## Source and quality

Use the stage-specific source hierarchy and rules. Keep source provenance separate from learner text. Preserve definition recall and precise Clozes for Anki. Do not mark semantic QA passed from structural checks alone. Do not upload source images/PDFs unless the user designated them for this repository. GitHub issues should reference stable source locations, not temporary signed URLs or credentials.
