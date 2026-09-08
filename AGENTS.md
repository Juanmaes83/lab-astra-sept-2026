# AGENTS.md

## Mission

Build reference-grounded spatial/cinematic outputs that prove real visual capability, not merely tool connectivity or file production.

Canonical reference-first production method:

```text
REFERENCE → ASSETS → ASSEMBLY → CRITIQUE → SHIP
```

Canonical strategy:

`docs/09-MATT-SHUMER-ASTRA-WORKFLOW.md`

Primary external guide:

https://somethingbig.ai/3d-worlds

## Current model state

- Current execution model: `gpt-6-astra` through Codex CLI when the active session reports it.
- Astra access is confirmed on the project owner's Windows machine.
- Blender 5.2.1 LTS + Blender MCP are operational.
- Keep the workflow model-swappable; no architecture contract may depend permanently on Astra.

## Closed historical gates

Gate 1 / Blender MCP connectivity is CLOSED.

SOLACE floorplan/blockout proof is CLOSED as a spatial capability proof.

Do NOT repeat setup, Gate 1, test-cube work, blockout existence checks, viewer QA or other historical infrastructure tasks unless an actual regression blocks a new goal.

## SOLACE benchmark state — frozen accepted output

**SOLACE PHOTOREAL GOAL v01 is HUMAN ACCEPTED / BENCHMARK COMPLETE.**

Accepted deliverables:

- `outputs/solace/SOLACE_PHOTOREAL_GOAL_v01.blend`
- `outputs/solace/SOLACE_PHOTOREAL_GOAL_v01.mp4`
- delivery commit: `aec9f944ab3a5f7296f040450791d5aedd79f6ed`
- human acceptance: `evidence/solace-photoreal-goal-v01/HUMAN-ACCEPTANCE.md`
- final run report: `evidence/runs/2026-09-08-solace-final-render-v01.md`

Target achieved for this benchmark:

- authoritative source: `references/solace/video/VIDEO_REFERENCIA_SOLACE_CINEMATIC_TARGET.mp4`;
- first continuous shot approximately `00:00.000 → 00:13.967`;
- 14.000 s;
- 420 frames;
- 1920 × 1080;
- 30 fps;
- Living → Dining → Kitchen;
- Cycles GPU / OptiX.

Historical `SOLACE_VIDEO_PROOF_v01` and `v02` remain technical proofs only and must not replace the accepted photoreal v01.

## SOLACE freeze rule

Do NOT, by default:

- rebuild the accepted scene;
- rerender the accepted sequence;
- regenerate its anchor pack;
- reopen its critic loop;
- spend Astra credits polishing residual reflections/furniture/forest differences;
- overwrite the accepted `.blend` or `.mp4`.

Any future SOLACE work requires a new explicit objective and a new version/goal while preserving accepted v01.

A new Astra session must not infer that additional SOLACE polishing is the next task.

## Goal-mode execution for future benchmarks

Use `/goal` when supported for substantial production benchmarks.

Do not stop merely because:
- a `.blend` exists;
- an MP4 exists;
- Blender rendered without error;
- a generic route is present.

Do not continue indefinitely either. The economic production pattern is:

```text
ONE HUMAN GOAL
→ HIGH-INFORMATION INTERNAL ITERATION
→ CHEAP ANCHOR PACK
→ CONSOLIDATED CRITIC
→ CONSOLIDATED CORRECTION
→ HUMAN ANCHOR REVIEW
→ ONE FINAL RENDER
→ HUMAN PLAYBACK DECISION
→ FREEZE ACCEPTED VERSION
```

## Reference rules

Reference truth order for reference-grounded reconstruction:

1. authoritative target media;
2. verified plan/floorplan or other owned source constraints;
3. supplied still references;
4. process/support references;
5. generated outputs as implementation history only.

Never let previous generated work overrule real source evidence.

## Specialized workers

When supported, fan out focused ownership rather than having one builder cut corners across the full scene.

Typical domains:

1. reference + frame analysis;
2. camera / lens / timing;
3. architecture + openings;
4. hero assets;
5. materials + surface detail;
6. glazing + exterior + vegetation;
7. lighting + exposure + atmosphere;
8. render / finishing;
9. independent visual critic.

Each worker owns fidelity of its domain; the main agent owns prioritization and assembly.

## Builder / critic separation

The builder must not grade its own work.

Use a fresh-context critic when supported. Convert meaningful visible tells into concrete work orders, but consolidate criticism before triggering expensive rework.

The critic does not own cost policy and does not authorize another full render.

## Blender rules

- Prefer Safe Mode for agent-driven Blender execution.
- Save/version `.blend` before major mutations.
- Procedural does not justify primitive hero assets.
- Cubes/cylinders are acceptable for blocking, hidden support and cheap previews; hero-visible final assets require credible geometry/material response.
- Do not assume more render samples can fix weak geometry/materials.
- Reuse accepted work where it accelerates a new goal; do not rebuild blindly from zero.
- Camera must be measured against source frames where reference matching matters.

## Cost discipline

Astra is expensive. Spend its budget on differential work that materially improves the active goal:

- reference interpretation;
- camera reconstruction;
- asset modeling;
- materials;
- lighting;
- rendering orchestration;
- independent critique and consolidated correction.

Do not spend Astra tokens on:
- repeated setup checks;
- viewer/Vercel housekeeping;
- long documentation narration;
- work ChatGPT + Juanma can do outside Blender;
- polishing an already accepted benchmark without a new objective.

Before an expensive final sequence render, follow `docs/11-ASTRA-RUN-PLAYBOOK.md`.

## Persistent learning protocol — mandatory

This LAB learns across sessions through repository memory, not assumed model memory.

At the start of every meaningful production session, read:

1. `AGENTS.md`;
2. `docs/01-CURRENT-STATE.md`;
3. `docs/09-MATT-SHUMER-ASTRA-WORKFLOW.md`;
4. `docs/10-SOLACE-LESSONS-AND-COST-EFFICIENCY.md`;
5. `docs/11-ASTRA-RUN-PLAYBOOK.md`;
6. the latest relevant report under `evidence/runs/`;
7. the relevant source/reference manifest.

At the end of every meaningful production interaction:

1. create/update a run report using `templates/ASTRA_RUN_REPORT_TEMPLATE.md`;
2. record what was attempted, how it was done, problems found, root causes, fixes and verification;
3. record avoidable time/tokens/compute when known;
4. preserve a concise resume packet: best current state, accepted work, unresolved issues, `DO NOT REDO`, and next best action;
5. update the lessons file only when a reusable lesson is confirmed;
6. update the playbook only when the standard workflow changes;
7. update current state when project state materially changes.

Do not paste full terminal transcripts into run reports. The purpose is to reduce future context cost, not create documentation bloat.

## Human approval gates

Stop before:
- merging;
- destructive overwrite of important source data without saved version;
- publishing externally beyond already approved review channels;
- changing permissions/secrets;
- paid external-service usage outside the approved budget;
- an expensive final full render before required human anchor approval.

Final visual acceptance belongs to Juanma + ChatGPT / project owner review.

Before human acceptance, report `HUMAN VISUAL REVIEW: PENDING`.
After explicit human acceptance, preserve the acceptance record and freeze that version.

## PROJECT-PELU handoff rules

- This LAB produces; PROJECT-PELU consumes.
- Do not duplicate PROJECT-PELU runtime, hotspots, analytics or commercial logic here.
- Only human-`ACCEPTED` assets may be handed off.
- Preserve provenance and source manifests.
- F1 panorama fallback remains owned by PROJECT-PELU.

`SOLACE_PHOTOREAL_GOAL_v01` is now eligible for handoff consideration, but no handoff occurs automatically. Require an explicit handoff decision.

## Geospatial rules

- Target recognizability and coherent geography, not survey/BIM accuracy unless sources support it.
- Use open/owned geodata for editable geometry.
- Keep Google Photorealistic 3D Tiles as separate compliant visualization/human reference.
- Do not extract, trace or machine-derive owned geometry from Google Map Tiles content.

## Scope discipline

The SOLACE benchmark is complete. Do not reopen it by default.

Future work must follow the explicitly selected next phase/project rather than falling back to old SOLACE polishing, old gates or unrelated experiments.

## Completion evidence

A production goal is reviewable when it leaves:
- versioned `.blend`/scene artifact as applicable;
- final render/video as applicable;
- relevant source/reference mapping;
- concise critic/work-order record;
- commit SHA;
- explicit human-review state.

A human-accepted goal additionally leaves a human acceptance record and becomes frozen unless a new explicit version is authorized.

## Reporting

Keep final Astra reporting concise:
1. result path(s);
2. technical facts;
3. commit SHA;
4. unresolved material limitations;
5. human visual review state;
6. next action only if explicitly authorized.
