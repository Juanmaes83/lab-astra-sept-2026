# ASTRA RUN REPORT TEMPLATE

Purpose: persist the operational memory of every meaningful Astra production interaction so future sessions do not rediscover the same context, errors, fixes or workflow decisions.

This is not optional prose documentation. It is project memory.

Create one report per meaningful production run under:

`evidence/runs/YYYY-MM-DD-<project>-<run-id>.md`

Examples:

- `evidence/runs/2026-09-08-solace-photoreal-r09.md`
- `evidence/runs/2026-09-09-solace-final-render-v01.md`

Do not create a run report for trivial read-only checks that produce no new learning.

---

# RUN REPORT

## 1. Identity

- Date:
- Project / benchmark:
- Run ID / revision:
- Agent / model:
- Branch:
- Start commit:
- End commit:
- Human goal:

## 2. Starting state

Record only the state needed to resume this work without rediscovery.

- Input `.blend` / scene:
- Authoritative references used:
- Relevant prior run report(s):
- Known accepted state inherited:
- Known unresolved issues inherited:
- Files/assets intentionally reused:
- Files/assets intentionally rejected and why:

## 3. What this run attempted

Describe the bounded production objective in concrete terms.

Example:

> Correct the SOLACE final camera clearance and end-frame composition without rebuilding accepted living/dining/kitchen assets.

## 4. Process performed

Record the actual sequence used, not a generic summary.

For every important operation include:

1. what was inspected;
2. what decision was made;
3. what was changed;
4. how it was executed;
5. what evidence was produced.

Prefer concise bullets with paths/commands/scripts when they matter for reproducibility.

## 5. Files created or modified

| File | Action | Purpose |
| --- | --- | --- |
|  |  |  |

Include scripts, `.blend` revisions, preview folders, manifests and final outputs that materially matter.

## 6. Problems found

For each problem use this structure.

### Problem A — [short name]

**Observed symptom**  
What was visibly or technically wrong?

**Root cause**  
What actually caused it? If unknown, say `UNKNOWN` instead of guessing.

**Detection method**  
How was it discovered: reference comparison, ray cast, render, Blender error, critic, human review, etc.?

**Cost of late detection**  
What extra render / iteration / token cost did this create, if material?

## 7. Fixes applied

For each problem:

### Fix A — [short name]

- Change made:
- Script / object / material / camera affected:
- Why this fix was chosen:
- Verification performed:
- Result: `PASS / PARTIAL / FAIL`
- Reusable pattern: `YES / NO`

Never write only “fixed”. Preserve enough information for another session to reproduce the solution.

## 8. Critic / review findings

If a critic was used, record only material findings.

| Reference checkpoint | Tell / mismatch found | Work order | Resolution |
| --- | --- | --- | --- |
|  |  |  |  |

Separate:

- agent critic findings;
- human findings from Juanma + ChatGPT.

Human approval always overrides agent self-assessment.

## 9. Result of this run

- Technical result:
- Visual result:
- Best current `.blend`:
- Best current preview / anchor pack:
- Best current MP4/render:
- What is now accepted as reusable:
- What is still rejected:
- Human visual review: `PENDING / PASS / FAIL / CORRECTION REQUIRED`

## 10. Time / token / compute efficiency notes

Exact token counts should be recorded when the environment exposes them. Never invent numbers.

If exact usage is unavailable, classify each phase:

| Phase | Model/token intensity | Blender/compute intensity | Useful? | Notes |
| --- | --- | --- | --- | --- |
| Reference analysis | low/medium/high/unknown | low/medium/high | yes/no | |
| Asset creation | low/medium/high/unknown | low/medium/high | yes/no | |
| Camera | low/medium/high/unknown | low/medium/high | yes/no | |
| Preview rendering | low/medium/high/unknown | low/medium/high | yes/no | |
| Critique | low/medium/high/unknown | low/medium/high | yes/no | |
| Corrections | low/medium/high/unknown | low/medium/high | yes/no | |
| Final rendering | low/medium/high/unknown | low/medium/high | yes/no | |

Explicitly identify:

- work that should have happened earlier;
- duplicated work;
- expensive work that did not improve visual quality;
- expensive work that was justified by a material quality gain.

## 11. Process learning

### What worked

- 

### What wasted time / tokens / compute

- 

### What should happen earlier next time

- 

### What must not be repeated

- 

### New reusable rule

Write each rule as an imperative, for example:

> APPROVE THE ANCHOR PACK BEFORE STARTING A 420-FRAME FINAL RENDER.

## 12. Workflow delta

Does this run change the standard workflow?

- `NO` — no reusable change.
- `YES` — update `docs/11-ASTRA-RUN-PLAYBOOK.md` in the same interaction.

If YES, record exactly which playbook section changed and why.

## 13. Lessons delta

Does this run add a confirmed project lesson?

- `NO`
- `YES` — update `docs/10-SOLACE-LESSONS-AND-COST-EFFICIENCY.md` in the same interaction.

Do not promote a one-off hypothesis into a permanent lesson without evidence.

## 14. Resume packet for the next session

This section is mandatory and should be short enough to read first in a fresh Astra session.

### READ FIRST

- `AGENTS.md`
- `docs/09-MATT-SHUMER-ASTRA-WORKFLOW.md`
- `docs/10-SOLACE-LESSONS-AND-COST-EFFICIENCY.md`
- `docs/11-ASTRA-RUN-PLAYBOOK.md`
- this run report

### CURRENT BEST STATE

- Best `.blend`:
- Best preview:
- Best render/video:
- Current accepted revision:

### DO NOT REDO

- 

### NEXT BEST ACTION

- 

### REAL BLOCKERS

- 

---

# Completion rule

A meaningful Astra production interaction is not operationally complete until:

1. the production artifact/state is saved;
2. this run report exists;
3. reusable lessons have been promoted to the lessons document when appropriate;
4. reusable workflow changes have been promoted to the playbook when appropriate;
5. the next session has a concise resume packet.

The objective is cumulative capability: every expensive interaction must make the next interaction cheaper, faster or better.