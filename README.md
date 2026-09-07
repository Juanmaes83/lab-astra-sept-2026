# lab-astra-sept-2026

Experimental **Spatial Production LAB** for building and validating an AI-driven workflow around Astra, Blender, MCP, visual QA and later geospatial/Unreal experiments.

This repository remains separate from product/runtime repos. For F2 it is now formally paired with `Juanmaes83/PROJECT-PELU` as the upstream production lab that creates reviewable spatial assets; PROJECT-PELU consumes only accepted outputs.

## Objective

Build a reproducible pipeline that moves from references / plans / geodata to an editable 3D scene, visually verifies the result, corrects it iteratively, and produces reviewable spatial packages.

```text
REFERENCES / FLOORPLANS / GEODATA
              ↓
        SOURCE MANIFEST
              ↓
        SCENE / GEO MANIFEST
              ↓
       ASTRA IN CODEX CLI
              ↓
           MCP LAYER
              ↓
           BLENDER
              ↓
   CAPTURE → VERIFY → CORRECT
              ↓
        ACCEPTED ASSET
       GLB + manifests + QA
              ↓
        PROJECT-PELU
```

## Current model status — 2026-09-07

Observed on the project owner's Windows machine:

- Codex CLI is installed and healthy.
- Codex is authenticated through ChatGPT.
- `gpt-6-astra` is now selectable and launches successfully in Codex CLI.
- Current F2 execution model: **`gpt-6-astra`**.
- Architecture remains model-swappable; no pipeline contract may depend on one model forever.

The old `ASTRA ACCESS PENDING` state is closed.

## F2 relationship with PROJECT-PELU

### This LAB owns
- Astra + Blender orchestration experiments;
- Blender MCP integration;
- visual verification loops;
- source/scene/geo manifests;
- SOLACE architectural benchmark;
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

The initial handoff target is:

```text
spatial-package/
├── scene.glb
├── source_manifest.json
├── scene_manifest.json
├── metadata.json
├── cameras.json
└── preview.jpg
```

Only packages marked `ACCEPTED` by QA are eligible for PROJECT-PELU integration.

## Primary benchmarks

### Gate 1 — Blender MCP control
Before SOLACE:

```text
READ SCENE
→ CAPTURE
→ ONE BOUNDED CHANGE
→ CAPTURE
→ VERIFY
```

### Benchmark A — SOLACE
Use real-estate references to validate plan/multi-view interpretation, blockout, living+dining+kitchen fidelity, camera/light/materials and a 10–14 second walkthrough.

### Benchmark B — Torrevieja / Costa Blanca bounded area
Deferred until the architectural production gate is stable.

## Related repositories

Primary sources live in `docs/03-SOURCE-REPOS.md`.

F2 P0 dependencies:
- `Juanmaes83/blender-mcp` branch `lab/astra-sept-2026`;
- `Juanmaes83/PROJECT-PELU` branch `feat/f2-spatial-provider-readiness`.

## Governance

- Keep experiments reversible.
- Preserve source provenance and licences.
- No secrets in Git.
- Never claim visual success without capture/render evidence.
- Save/version Blender state before major mutations.
- Do not start SOLACE until Gate 1 is PASS.
- Do not start Unreal/geospatial expansion while the current gate is open.

## Current status

**ASTRA AVAILABLE / F2-A ACTIVE / BLENDER MCP GATE 1 NEXT**