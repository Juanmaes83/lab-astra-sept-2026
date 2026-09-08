# lab-astra-sept-2026

Experimental **Spatial Production LAB** for building and validating an AI-driven workflow around Astra, Blender, MCP, reference-grounded photoreal reconstruction, independent visual critique and later geospatial/Unreal experiments.

This repository remains separate from product/runtime repos. For F2 it is formally paired with `Juanmaes83/PROJECT-PELU` as the upstream production lab that creates reviewable spatial assets; PROJECT-PELU consumes only accepted outputs.

## Objective

Prove a reproducible pipeline that moves from real references / plans / geodata to an editable 3D scene and then iterates against the reference until the result is visually convincing enough to ship for human review.

The current production strategy follows Matt Shumer's reference-first Astra workflow:

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
           WORK ORDERS
                 ↺
       BUILD → CRITIQUE LOOP
                 ↓
              SHIP
                 ↓
      JUANMA + CHATGPT REVIEW
                 ↓
      ACCEPTED SPATIAL OUTPUT
```

## Production principles

### Reference is authority
Astra must solve outward from specific real reference media, not from a generic idea of what the scene should look like.

### Goal mode, not micro-gates
Infrastructure gates already proven must not be repeated. Production benchmarks run as one human goal with autonomous internal iteration. A file existing is not success; visual fidelity is the success criterion.

### Fan out specialized workers
When supported, split reference analysis, camera, architecture, hero furniture, materials, vegetation, lighting, rendering and critique into focused workers. One agent holding the full scene in context is expected to cut corners.

### Builder does not grade itself
Use a fresh-context critic to compare generated renders against the corresponding real reference. Every visual tell becomes a concrete work order.

### Blender is not a primitive shortcut
Procedural Blender/Python is allowed and encouraged, but hero-visible final assets must not remain crude cubes/cylinders simply because they are fast to create.

### Human acceptance remains external
Astra can iterate internally, but final cinematic PASS belongs to Juanma + ChatGPT.

## Current model status — 2026-09-08

Observed on the project owner's Windows machine:

- Codex CLI installed and healthy;
- ChatGPT authentication configured;
- `gpt-6-astra` launches successfully in Codex CLI;
- Blender `5.2.1 LTS` operational;
- Blender MCP connected on port `9876`;
- Safe Mode validated;
- current execution model: **`gpt-6-astra`**;
- architecture remains model-swappable.

## Current SOLACE status

Infrastructure proof is complete.

Completed:
- Gate 1 Blender/MCP control: PASS;
- SOLACE floorplan interpretation/blockout: PASS as spatial proof;
- `SOLACE_VIDEO_PROOF_v01.mp4`: rendered;
- authoritative cinematic and Blender/process reference videos are stored in `references/solace/video/`;
- `SOLACE_VIDEO_PROOF_v02.mp4`: rendered from the cinematic reference.

Important conclusion:

`v01` and `v02` are **historical technical proofs, not photoreal accepted outputs**.

They prove spatial control and video generation, but they do not meet the premium visual benchmark. The next SOLACE execution is therefore a **reference-first photoreal reconstruction goal**, not another Gate 1/Gate 2 exercise.

## SOLACE benchmark target

Authoritative video:

`references/solace/video/VIDEO_REFERENCIA_SOLACE_CINEMATIC_TARGET.mp4`

First continuous shot:

```text
approximately 00:00.000 → 00:13.967
hard cut at approximately 00:14.000
30 fps
14.0 s target
Living → Dining → Kitchen
```

The target is not merely a smooth walkthrough. Camera choreography, visible architecture, hero furnishings, materials, glazing, vegetation, lighting and atmosphere must be recognizably aligned with the real reference.

## F2 relationship with PROJECT-PELU

### This LAB owns
- Astra + Blender orchestration experiments;
- Blender MCP integration;
- reference-grounded asset production;
- independent visual critique loops;
- source/scene/geo manifests;
- SOLACE architectural/cinematic benchmark;
- creation of `ACCEPTED SPATIAL PACKAGE` outputs;
- later geospatial and Blender→Unreal proofs.

### PROJECT-PELU owns
- runtime/product UX;
- 360/Splat/GLB viewer selection;
- SpatialAsset normalization;
- fallback to F1 panorama;
- hotspots, analytics, CTA, leads;
- provider readiness for Marble/Atlas.

### Handoff rule

No half-finished `.blend` scene is considered a product asset.

Only packages marked `ACCEPTED` by human QA are eligible for PROJECT-PELU integration.

## Related repositories

Primary sources live in `docs/03-SOURCE-REPOS.md`.

F2 dependencies:
- `Juanmaes83/blender-mcp` branch `lab/astra-sept-2026`;
- `Juanmaes83/PROJECT-PELU` branch `feat/f2-spatial-provider-readiness`.

The Blender MCP source declares support for Blender scene control plus asset/model-generation integrations including Poly Haven, Sketchfab, Poly Pizza, Hyper3D Rodin and Hunyuan3D. Availability/licensing must still be verified before use in a production run.

## Governance

- Keep experiments reversible.
- Preserve source provenance and licences.
- No secrets in Git.
- Never claim visual success because an agent writes `PASS` or because an MP4 exists.
- Save/version Blender state before major mutations.
- Do not repeat closed infrastructure gates unless a real regression appears.
- Do not merge without human approval.
- Do not start unrelated Unreal/geospatial expansion while SOLACE photoreal reconstruction is the active benchmark.

## Current status

**ASTRA + BLENDER MCP OPERATIONAL / SOLACE TECHNICAL POC COMPLETE / PHOTOREAL RECONSTRUCTION STRATEGY ACTIVE / HUMAN APPROVAL REQUIRED BEFORE NEXT ASTRA EXECUTION**