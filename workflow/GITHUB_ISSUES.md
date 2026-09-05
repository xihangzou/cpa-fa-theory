# Astra plans the repository; you launch each issue

Version 3 · 5 September 2026

This is the default operating mode for this workflow. Astra performs planning and repository/issue setup first, then stops. You choose one ready issue and manually launch it with Sol or Luna. No automatic workers, dispatch workflows, chained issue execution, or automatic model switching are installed.

## 1. Start with Astra

Use this prompt with the relevant workflow folder:

> Use GPT-6 Astra to plan this workflow and set up its GitHub repository and issues. Repository: [owner/repo; say new or existing]. Visibility for a new repository: [private unless I specify otherwise]. Source locations and editions/revisions: [exact files/folders/links]. Scope and output organization: [details]. Follow this workflow's GITHUB_ISSUES.md and content rules. Inspect the sources enough to define bounded tasks. Create the repository structure, source/rule contracts, dependency-ordered GitHub issues, and issue index. Recommend GPT-5.6 Sol or GPT-5.6 Luna for each issue. Verify published files and issues, show the ready issue links, then stop. I will manually execute individual issues. Do not launch workers or begin production conversion, integration, or card generation.

This request authorizes repository/issue setup for the specified destination. Do not ask again merely because setup creates files or issues. If the destination or required source scope is missing, prepare what can be determined and ask for the missing information before the dependent external action. Do not guess a repository name or alter the historical bookkeeping repositories. If GitHub access is unavailable, deliver the concrete scaffold and issue drafts, clearly marked not yet published.

Use one workflow repository by default for each independently requested project/stage. Reuse an existing repository when specified; check its current status, branches, policies and issues before changing it. Keep original source repositories unchanged. Repository visibility defaults to private for a new source-derived study project; a public destination must be requested.

## 2. Astra's planning responsibilities

Read enough source structure to define exact page/section/topic ranges, source roles, output paths and acceptance criteria. Planning may inspect images or Markdown to establish boundaries; it must not quietly perform all production work. Never invent source contents or source commit hashes.

Create a dependency graph whose nodes are cohesive, reviewable outcomes. Include prerequisites, exact inputs, owned paths, outputs, acceptance criteria, verification procedure, evidence required, and recommended model with a reason. Establish source/rule contracts first; place pilot and QA gates before dependent bulk work; place whole-corpus acceptance before release packaging. Serialize edits to shared registries/files, or assign batch shards and a single aggregation issue.

Plan all expected issues before dispatch. If source discovery genuinely prevents detailed downstream planning, publish bounded discovery issues plus explicitly blocked provisional nodes. Mark that the plan requires an Astra revision after discovery; do not call placeholders executable-ready. The local validator requires concrete node contracts before rendering executable issue drafts.

Use stable logical IDs such as JPG-001, INT-001, or ANKI-001 independently of GitHub numbers. A plan ID identifies a particular task graph. Keep it stable during resumption so existing issues can be found by their marker. Record revisions rather than silently replacing completed issue contracts.

## 3. Recommended worker selection

| Work | Default worker | Reason |
|---|---|---|
| Read JPGs, preserve textbook meaning, interpret tables/formulas | Sol | Source interpretation and omission review require judgment |
| Map overlapping topics, deduplicate, resolve integration structure | Sol | Similarity must be distinguished from full containment |
| Extract ALPs, design Clozes, perform source/recall/domain QA | Sol | These decisions determine learning quality |
| Exact source/file inventory, mechanical assembly, schema checks | Luna | Bounded procedure with clear outputs and checks |
| Packaging already reviewed notes, checksums, index/readback work | Luna | Deterministic work when acceptance inputs are ready |

These are staffing recommendations for this workflow, not benchmark guarantees. Either worker may be selected by the user. Astra owns the overall plan and later plan changes. If Luna encounters a semantic ambiguity or a failed criterion it cannot resolve, it records a suggested Sol rerun; you launch that rerun. Neither worker switches model, dispatches a subagent, or starts the next issue automatically.

Model names in issue bodies are recommendations, not GitHub assignees and not commands that change the active model. Choose the model when launching the task. If an Astra final review is desired, request it as a separate manual task; it is not dispatched automatically.

## 4. Repository setup before production

Create and verify these artifacts:

```text
README.md                 purpose and execution entrypoint
AGENTS.md                 manual issue execution contract
PLAN.md                   dependency order and model recommendations
SOURCES.md                exact source locations/identities and scope
plan.json                 machine-readable task graph
ISSUES.md                 real GitHub issue links, not placeholder numbers
issue-map.json            logical ID → GitHub issue URL
issue-drafts/             exact versioned issue bodies
workflow/                 this self-contained skill, rules and helpers
project/                  stage-specific editable project template
.github/ISSUE_TEMPLATE/    bounded task template (no auto-execution actions)
```

Do not copy raw PDFs/JPGs or credentials into the repository just because setup creates it. Retain source references to the designated storage. Add learner deliverables/media only when their destination is authorized. The supplied ignore file excludes bulky source/media/APKG folders by default; publish intended deliverables deliberately under the project's policy.

Use `scripts/plan_repo.py` to validate the task graph and create a new local scaffold. It rejects missing dependencies, cycles, unsupported worker names, and overlapping path ownership without ordering. It does not assess semantic completeness of the plan.

```bash
python scripts/plan_repo.py /path/to/plan.json --scaffold /path/to/new-repository
```

Astra then creates the GitHub repository using the connector, or the installed/authenticated GitHub CLI if repository creation is unavailable through the connector. For a new private repository, after creating and inspecting the initial local commit:

```bash
gh repo create OWNER/REPO --private --source /path/to/new-repository --remote origin --push
```

Use the explicit user-requested owner/name. Initialize the local Git repository on its intended branch and commit the inspected scaffold before that command. Never force-push or overwrite an existing repository. For an existing destination, integrate the scaffold into the existing checkout conservatively, retaining unrelated files, policies and branches.

Once the destination exists, publish issues with the connector or:

```bash
python workflow/scripts/publish_issues.py /path/to/repository
```

The issue publisher creates missing logical IDs, reuses matching issues, resolves dependencies to real issue URLs, and reads back each body/title. It leaves issue states unchanged and starts zero workers. After publication, commit/push the updated drafts, issue-map.json and ISSUES.md, then read back those remote files. The planning phase is complete only when the repository and real issues are verified remotely. A local scaffold alone is an incomplete setup unless access is blocked.

On an uncertain issue-create response, re-list issues and match the stable marker before retrying. Do not blindly create another issue. Duplicate markers require resolution; do not automatically delete an issue. If revising an existing plan, Astra explicitly reconciles removed or changed nodes and preserves completed work; the publisher does not silently close obsolete issues.

## 5. Planning record schema

`assets/PLAN_TEMPLATE.json` describes the required fields with placeholders. Astra replaces them with actual project data; do not publish the template as a finished plan. Every issue needs:

- stable ID, title, goal;
- worker (GPT-5.6 Sol or GPT-5.6 Luna) and worker_reason;
- depends_on (logical IDs; empty if initially ready);
- exact inputs, owned_paths, outputs;
- acceptance (observable source/content and structural criteria);
- verification (actual commands or reproducible review procedures with expected outcomes);
- evidence (source/output hashes, saved paths/commits, checks and reviews actually performed).

Set delivery_branch in plan.json to the branch that downstream issues read (normally main for a newly initialized repository). Keep owned paths specific. Use a directory prefix for subtree ownership rather than broad globs. Notes/inventory batch shards may be owned independently; a later aggregation issue alone writes their shared canonical files. Every package issue depends on final content approval/QA, and consumers check that dependency outputs are actually accessible at the declared revision.

Source files not yet produced must be named as outputs of a specific prerequisite issue, not given invented hashes. At execution time, verify and record the actual dependency output revision. Issue closure is a scheduling signal; it is not proof of output validity.

## 6. Manually execute one issue

Select the issue's recommended model, then send:

> Execute only [GitHub issue URL] in [owner/repo]. Verify its dependencies and source revision, follow the issue's scope and repository workflow rules, produce and save its outputs to the configured delivery branch, and run the required checks and reviews. Post completion evidence and close this issue only if all acceptance criteria pass and its outputs are available for downstream tasks. Otherwise leave it open and report the exact blocker. Stop after this issue. Do not execute another issue, launch workers, or change models.

For a draft-only or review-only launch, say so; that explicit scope overrides the default completion actions. Follow an existing PR policy when applicable. Do not close before outputs are integrated into the branch downstream tasks read. If PR integration needs a user action, hand off that concrete result and keep the issue open.

Completion evidence should include status (PASS/BLOCKED/FAIL), issue ID, source identity/revision, changed/output paths, saved commit, checks and actual semantic review results, remote readback, and remaining uncertainty. Never claim a source or semantic review solely from a successful script exit.

You select the next ready issue after reviewing that report. Independent issues may be launched manually in parallel only if you choose to do so; they need isolated checkouts and non-overlapping write ownership. The kit itself does not dispatch them.

## 7. Stop and resume

Astra's setup handoff contains the repository link, full issue index, initially ready issues, model recommendations, and any blocked/provisional work. It does not perform the first production issue.

Workers stop after their selected issue. A dependency change or contract mismatch is reported to you for an Astra planning revision. Successful outputs and evidence remain saved; no destructive reset or blind rerun is part of this workflow.

## Stage-specific issue graph

Astra inspects the table of contents and image inventory, establishes exact processing ranges and repository rules, then creates:

1. Source inventory/manifest verification — Luna; exact names, hashes, page scope and image accessibility.
2. One conversion issue per coherent page/section range — Sol; each owns its chunk and a separate review/evidence record. Depends on the source inventory.
3. Chapter-level source/completeness QA — Sol; depends on that chapter's chunks and owns scoped corrections plus the chapter review.
4. Task-status aggregation and clean assembly — Luna; depends on all chapter QA. This single issue updates canonical tasks.json and runs source_md.py assemble.
5. Final source/merged-text acceptance — Sol; checks no missing content or merge rewriting and records the handoff revision.

Use concrete task IDs/ranges rather than generic placeholder issues. Shared manifest/status writers must be ordered; workers can emit per-chunk status fragments for the aggregation issue instead of racing to edit tasks.json. The final issue delivers Markdown only.
