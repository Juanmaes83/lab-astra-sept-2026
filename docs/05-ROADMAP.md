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

Result:

Astra + Blender can interpret the plan and create a controllable recognizable architectural scene.

This phase did **not** prove premium photorealism.

## Phase 3 — SOLACE video technical proofs
Status: ✅ COMPLETE AS POC / ❌ NOT ACCEPTED AS FINAL VISUAL QUALITY

Produced:

- `SOLACE_VIDEO_PROOF_v01`;
- `SOLACE_VIDEO_PROOF_v02`.

What they proved:
- Blender can produce the continuous route;
- camera animation can be authored;
- living/dining/kitchen can be rendered as one video;
- source video can influence the reconstruction.

What they did not prove:
- reference-matched camera timing;
- premium hero assets;
- premium materials;
- photoreal glazing/vegetation;
- premium lighting/atmosphere;
- final commercial visual quality.

Human verdict: v02 is a technical proof, not an accepted cinematic reconstruction.

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

1. use `/goal` for the production benchmark when supported;
2. make real reference media the authority;
3. fan out specialized workers;
4. assign asset-domain ownership;
5. measure camera against source frames;
6. keep builder and critic separated;
7. use blind side-by-side critique where practical;
8. convert every tell into a concrete work order;
9. iterate internally until a serious reference-fidelity candidate exists;
10. reserve final PASS for Juanma + ChatGPT.

## Phase 5 — SOLACE photoreal cinematic reconstruction
Status: 🟡 READY — WAITING FOR JUANMA APPROVAL TO EXECUTE

This is the current active production phase.

### Human goal

Reconstruct the first continuous SOLACE cinematic shot at premium/reference-grounded quality.

Target:

```text
approximately 00:00.000 → 00:13.967
hard cut at approximately 00:14.000
30 fps
14.0 s / 420 frames
Living → Dining → Kitchen
```

### Production domains

Preferred specialized workers:

1. reference/frame analyst;
2. camera/lens/timing;
3. architecture/openings;
4. living hero assets;
5. dining hero assets;
6. kitchen hero assets;
7. materials/surface detail;
8. glazing/exterior/vegetation;
9. lighting/atmosphere;
10. rendering/finishing;
11. fresh independent critic.

### Reuse rule

Start from the strongest useful existing SOLACE scene, including v02 assets where they accelerate the build.

Do not rebuild from zero by default.

But previous generated geometry has no authority over the real references.

### Camera requirement

Solve the camera from the real video using source-frame anchors around:

```text
0.0
2.0
4.0
6.0
8.0
10.0
12.0
13.8 seconds
```

Do not accept another `manually inferred` path without actual frame comparison.

### Visual-quality requirement

The scene must progress beyond blockout/procedural-placeholder appearance in the hero-visible shot.

A final full render is justified only after camera and visible asset quality survive internal critique.

### Critique loop

```text
BUILD
→ RENDER CHECKPOINT
→ BLIND/FRESH CRITIC
→ TELLS
→ WORK ORDERS
→ RESPONSIBLE WORKER
↺
```

The loop is autonomous inside the single human goal. It is not a chain of user-facing micro-gates.

### Ship condition

Ship one serious candidate with:

- versioned final `.blend`;
- final MP4;
- correct 14-second / 30-fps timing;
- materially reference-matched camera progression;
- hero-visible assets no longer reading as crude primitives;
- premium-enough materials/lighting/exterior for a meaningful human comparison;
- concise critic/work-order record;
- pushed commit;
- `HUMAN VISUAL REVIEW: PENDING`.

## Phase 6 — Hybrid generative finishing experiment
Status: ⚪ OPTIONAL / AFTER BLENDER PHOTOREAL GOAL RESULT

Seedance 2.5 or another generative-video finishing layer may be evaluated after the Matt Shumer-style Astra/Blender benchmark produces a controlled candidate.

Purpose:
- test whether a generative finishing layer can raise photoreal/cinematic quality while preserving Blender-controlled geometry, composition, camera and timing.

Important:
- this is not currently part of Matt Shumer's cited workflow;
- do not attribute it to him;
- do not use it to hide a fundamentally wrong camera or spatial reconstruction.

## Phase 7 — PROJECT-PELU handoff proof
Status: ⚪ BLOCKED UNTIL HUMAN-ACCEPTED SPATIAL OUTPUT

Only after SOLACE proves a sufficiently strong production package should the LAB hand an accepted asset to PROJECT-PELU.

## Phase 8 — Geospatial proof
Status: ⚪ DEFERRED

Torrevieja/Altea bounded proof using open/owned geodata.

## Phase 9 — Blender → Unreal
Status: ⚪ DEFERRED

Matt Shumer's workflow supports choosing Unreal where its ecosystem materially helps large-scale/cinematic requirements, but SOLACE remains a focused Blender benchmark for now.

Do not switch engines merely to avoid solving the current shot.

## Anti-loop rule — revised

The previous question:

> What is the smallest real artifact that proves this capability?

was useful for infrastructure proof but became too conservative for the photoreal benchmark.

For production, use instead:

> What is the single human goal, and what autonomous internal iterations are necessary to meet the real reference bar?

Do not create 50 human approval gates.

Do not stop after the first technically valid render either.

The correct pattern is:

```text
ONE HUMAN GOAL
→ MANY INTERNAL SPECIALIZED ITERATIONS IF NEEDED
→ ONE SERIOUS REVIEW CANDIDATE
→ HUMAN DECISION
```