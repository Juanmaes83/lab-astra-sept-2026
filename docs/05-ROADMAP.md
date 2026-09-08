# 05 — Roadmap

## Phase 0 — Environment ready
Status: ✅ CLOSED — 2026-09-07

- OpenAI/Codex environment ready.
- Codex CLI installed and healthy.
- ChatGPT auth configured.
- `gpt-6-astra` launches successfully in Codex CLI.
- Model-swappable architecture retained.

## Phase 1 — Blender MCP control
Status: ✅ CLOSED — 2026-09-07

Goal: prove reliable local Astra → Blender control with evidence.

Result: PASS.

Do not repeat unless a regression appears.

## Phase 2 — SOLACE spatial reconstruction proof
Status: ✅ CLOSED AS TECHNICAL/SPATIAL PROOF

Completed:
- source floorplan/reference setup;
- recognizable SOLACE blockout;
- living/dining/kitchen relationships;
- reviewable `.blend` versions;
- GLB export / scene evidence;
- technical visual review.

Result: Astra + Blender can interpret the plan and create a controllable recognizable architectural scene.

This phase did **not** prove premium photorealism.

## Phase 3 — SOLACE video technical proofs
Status: ✅ COMPLETE AS POC / ❌ NOT ACCEPTED AS FINAL VISUAL QUALITY

Produced:
- `SOLACE_VIDEO_PROOF_v01`;
- `SOLACE_VIDEO_PROOF_v02`.

They proved spatial control, camera animation and continuous video generation, but not premium reference fidelity.

## Phase 4 — Strategy pivot: Matt Shumer reference-first workflow
Status: ✅ ADOPTED — 2026-09-08

Primary guide:

https://somethingbig.ai/3d-worlds

Canonical LAB strategy:

`docs/09-MATT-SHUMER-ASTRA-WORKFLOW.md`

Production loop:

```text
REFERENCE
→ ASSETS
→ ASSEMBLY
→ CRITIQUE
→ SHIP
```

Operational changes:

1. use `/goal` for production benchmarks when supported;
2. make real reference media the authority;
3. fan out specialized workers;
4. assign asset-domain ownership;
5. measure camera against source frames;
6. keep builder and critic separated;
7. use blind side-by-side critique where practical;
8. convert visual tells into concrete work orders;
9. consolidate critique/corrections before expensive renders;
10. reserve final PASS for human review.

## Phase 5 — SOLACE photoreal cinematic reconstruction
Status: ✅ HUMAN ACCEPTED / BENCHMARK COMPLETE — 2026-09-08

### Accepted target

```text
approximately 00:00.000 → 00:13.967
hard cut at approximately 00:14.000
30 fps
14.0 s / 420 frames
1920 × 1080
Living → Dining → Kitchen
```

### Accepted deliverables

- `outputs/solace/SOLACE_PHOTOREAL_GOAL_v01.blend`
- `outputs/solace/SOLACE_PHOTOREAL_GOAL_v01.mp4`
- delivery commit: `aec9f944ab3a5f7296f040450791d5aedd79f6ed`
- technical verification: `evidence/solace-photoreal-goal-v01/technical-verification.json`
- final run report: `evidence/runs/2026-09-08-solace-final-render-v01.md`
- human acceptance: `evidence/solace-photoreal-goal-v01/HUMAN-ACCEPTANCE.md`

### Result

Juanma reviewed the completed MP4 and approved it as sufficiently improved to close the benchmark and continue advancing the project.

This is a human-accepted reconstructed/design visualization. It does not claim exact source indistinguishability, VERIFIED_REAL status or survey/BIM accuracy.

### Freeze rule

Do not spend more Astra credits polishing SOLACE v01 by default.

Any future change must:
- have a new explicit objective;
- create a new version/goal;
- preserve accepted v01 untouched.

### Process proved

```text
REFERENCES
→ FIXED ANCHORS
→ REUSE BEST BASE
→ SPECIALIZED BUILD
→ INDEPENDENT CRITIQUE
→ CONSOLIDATED CORRECTIONS
→ HUMAN ANCHOR PREFLIGHT
→ ONE FINAL RENDER
→ HUMAN PLAYBACK ACCEPTANCE
```

## Phase 6 — Hybrid generative finishing experiment
Status: ⚪ OPTIONAL / SEPARATE EXPERIMENT

Seedance or another generative-video finishing layer may be evaluated only as a separate version/experiment.

Purpose:
- test whether a generative finishing layer can raise cinematic realism while preserving Blender-controlled geometry, composition, camera and timing.

Important:
- this is not required to validate SOLACE v01; SOLACE v01 is already accepted;
- do not attribute this step to Matt Shumer's cited workflow;
- never overwrite the accepted Blender render.

## Phase 7 — PROJECT-PELU handoff proof
Status: 🟢 UNBLOCKED / READY FOR EXPLICIT HANDOFF DECISION

SOLACE now satisfies the human-accepted-output prerequisite.

A handoff package may be prepared when explicitly approved. It should preserve:
- accepted blend/video;
- provenance;
- source/reference manifest;
- truth state;
- technical metadata;
- human acceptance record.

Do not perform product integration automatically from this roadmap update.

## Phase 8 — Geospatial proof
Status: ⚪ DEFERRED

Torrevieja/Altea bounded proof using open/owned geodata.

## Phase 9 — Blender → Unreal
Status: ⚪ DEFERRED

Unreal may be evaluated where its ecosystem materially helps larger-scale/cinematic requirements.

Do not switch engines merely to avoid solving a reference-grounded production problem.

## Persistent learning system

Every future expensive Astra run must begin from repository memory:

- `AGENTS.md`
- `docs/01-CURRENT-STATE.md`
- `docs/09-MATT-SHUMER-ASTRA-WORKFLOW.md`
- `docs/10-SOLACE-LESSONS-AND-COST-EFFICIENCY.md`
- `docs/11-ASTRA-RUN-PLAYBOOK.md`
- latest relevant `evidence/runs/*`
- relevant reference manifest

Every meaningful run must leave a concise run report/resume packet so the next session does not rediscover solved work.

## Anti-loop rule — production

The correct production pattern is:

```text
ONE HUMAN GOAL
→ HIGH-INFORMATION INTERNAL ITERATION
→ CHEAP ANCHOR PREFLIGHT
→ ONE HUMAN ECONOMIC GATE
→ ONE FINAL RENDER
→ HUMAN DECISION
→ FREEZE ACCEPTED VERSION
```

Do not create dozens of human micro-gates.

Do not keep polishing an accepted benchmark because an agent can still find differences.

Accepted outputs are frozen until a new explicit goal justifies a new version.
