# lab-astra-sept-2026

Experimental **Spatial Production LAB** for building and validating an AI-driven workflow around Astra, Blender, MCP, reference-grounded photoreal reconstruction, independent visual critique and later geospatial/Unreal experiments.

This repository remains separate from product/runtime repos. For F2 it is formally paired with `Juanmaes83/PROJECT-PELU` as the upstream production lab that creates reviewable spatial assets; PROJECT-PELU consumes only accepted outputs.

## Objective

Prove a reproducible pipeline that moves from real references / plans / geodata to an editable 3D scene and then iterates against the reference until the result is visually convincing enough for human acceptance.

The production strategy follows Matt Shumer's reference-first Astra workflow:

**Reference → Assets → Assembly → Critique → Ship**

Primary guide:

- https://somethingbig.ai/3d-worlds
- canonical LAB adaptation: `docs/09-MATT-SHUMER-ASTRA-WORKFLOW.md`

```text
REAL REFERENCES / FLOORPLAN / VIDEO
                 ↓
        REFERENCE ANALYSIS
                 ↓
        /goal ASTRA MISSION
                 ↓
   SPECIALIZED ASSET WORKERS
                 ↓
          BLENDER + MCP
                 ↓
             ASSEMBLY
                 ↓
       RENDER / FRAME MATCH
                 ↓
    FRESH INDEPENDENT CRITIC
                 ↓
      CONSOLIDATED WORK ORDERS
                 ↺
       BUILD → CRITIQUE LOOP
                 ↓
       HUMAN ANCHOR PREFLIGHT
                 ↓
          FINAL FULL RENDER
                 ↓
      HUMAN PLAYBACK REVIEW
                 ↓
      ACCEPTED SPATIAL OUTPUT
```

## Production principles

### Reference is authority
Astra must solve outward from specific real reference media, not from a generic idea of what the scene should look like.

### Goal mode, not micro-gates
Infrastructure gates already proven must not be repeated. Production benchmarks run as one human goal with high-information internal iteration.

### Fan out specialized workers
When supported, split reference analysis, camera, architecture, hero furniture, materials, vegetation, lighting, rendering and critique into focused ownership.

### Builder does not grade itself
Use a fresh-context critic to compare generated renders against corresponding source frames. Consolidate meaningful tells into work orders before expensive rework.

### Human review is the economic gate
Before an expensive full sequence render:

```text
CHEAP ANCHORS
→ CONSOLIDATED CRITIC
→ CONSOLIDATED CORRECTION
→ HUMAN ANCHOR APPROVAL
→ ONE FINAL RENDER
```

### Persistent learning
Every expensive run must leave concise repository memory so the next session reuses solved work instead of rediscovering it:

- `docs/10-SOLACE-LESSONS-AND-COST-EFFICIENCY.md`
- `docs/11-ASTRA-RUN-PLAYBOOK.md`
- `templates/ASTRA_RUN_REPORT_TEMPLATE.md`
- `evidence/runs/`

## Environment status — 2026-09-08

Observed on the project owner's Windows machine:

- Codex CLI installed and healthy;
- ChatGPT authentication configured;
- `gpt-6-astra` available through Codex CLI;
- Blender `5.2.1 LTS` operational;
- Blender MCP connected on port `9876`;
- Safe Mode validated;
- architecture remains model-swappable.

## SOLACE benchmark — ✅ HUMAN ACCEPTED / COMPLETE

Historical technical proofs:

- `SOLACE_VIDEO_PROOF_v01`
- `SOLACE_VIDEO_PROOF_v02`

These proved basic spatial/video capability but were not accepted as photoreal outputs.

The reference-first production goal subsequently produced:

- `outputs/solace/SOLACE_PHOTOREAL_GOAL_v01.blend`
- `outputs/solace/SOLACE_PHOTOREAL_GOAL_v01.mp4`
- delivery commit: `aec9f944ab3a5f7296f040450791d5aedd79f6ed`

Technical delivery:

```text
14.000 s
420 frames
1920 × 1080
30 fps
Cycles GPU / OptiX
H.264 MP4
```

Human playback verdict on 2026-09-08:

**ACCEPTED.** The project owner judged the final video sufficiently improved to close the SOLACE v01 benchmark and continue advancing the project.

Formal acceptance:

`evidence/solace-photoreal-goal-v01/HUMAN-ACCEPTANCE.md`

Final run report:

`evidence/runs/2026-09-08-solace-final-render-v01.md`

## What SOLACE proved

The LAB demonstrated a viable end-to-end reference-grounded production workflow:

```text
AUTHORITATIVE REFERENCES
→ FIXED VISUAL ANCHORS
→ REUSE BEST EXISTING BASE
→ SPECIALIZED ASTRA/BLENDER PRODUCTION
→ INDEPENDENT CRITIQUE
→ CONSOLIDATED CORRECTIONS
→ HUMAN ANCHOR PREFLIGHT
→ FINAL RENDER
→ HUMAN PLAYBACK ACCEPTANCE
```

The major quality jump over v01/v02 came from better process—reference grounding, camera reconstruction, hero assets, materials, exterior, lighting and structured critique—not merely higher render samples.

## SOLACE freeze rule

The accepted `SOLACE_PHOTOREAL_GOAL_v01` is frozen.

Do not by default:
- rebuild it;
- rerender it;
- reopen critique;
- overwrite its accepted files;
- spend more Astra credits polishing residual differences.

Any future SOLACE change requires a new explicit objective and version while preserving accepted v01.

## F2 relationship with PROJECT-PELU

### This LAB owns
- Astra + Blender orchestration experiments;
- Blender MCP integration;
- reference-grounded asset production;
- independent visual critique loops;
- source/scene/geo manifests;
- creation of human-accepted spatial outputs;
- later geospatial and Blender→Unreal proofs.

### PROJECT-PELU owns
- runtime/product UX;
- 360/Splat/GLB viewer selection;
- SpatialAsset normalization;
- fallback to F1 panorama;
- hotspots, analytics, CTA, leads;
- provider readiness for future services.

### Handoff status

`SOLACE_PHOTOREAL_GOAL_v01` is now **eligible for PROJECT-PELU handoff consideration** because it is human accepted.

The handoff itself remains a separate explicit decision; this repository does not automatically integrate the asset into product runtime.

## Next phase

SOLACE v01 requires no further production work.

The next action must be explicitly selected from the roadmap, such as:

- PROJECT-PELU handoff proof;
- a separate optional generative-finishing experiment;
- another spatial benchmark using the learned Astra playbook;
- later geospatial / Blender→Unreal work.

See `docs/05-ROADMAP.md` and `docs/01-CURRENT-STATE.md`.

## Governance

- Keep experiments reversible.
- Preserve source provenance and licences.
- No secrets in Git.
- Never claim visual success because an agent writes `PASS` or because an MP4 exists.
- Save/version Blender state before major mutations.
- Do not repeat closed infrastructure gates unless a real regression appears.
- Do not merge without human approval.
- Freeze human-accepted benchmark versions until a new explicit goal authorizes a successor.

## Current status

**ASTRA + BLENDER MCP OPERATIONAL / SOLACE PHOTOREAL v01 HUMAN ACCEPTED / BENCHMARK COMPLETE / NEXT PHASE REQUIRES EXPLICIT SELECTION**
