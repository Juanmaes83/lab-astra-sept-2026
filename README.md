# lab-astra-sept-2026

Experimental repository for building and validating an AI-driven spatial production workflow around Blender, MCP, geospatial data, visual QA and later Unreal Engine.

This repository is the **project-level LAB**. It is intentionally broader than `blender-mcp` and separate from product repos such as `WORLD-COSTA-BLANCA`.

## Objective

Build a reproducible pipeline that can move from references / plans / geodata to an editable 3D scene, visually verify the result, correct it iteratively, and produce:

1. cinematic architectural walkthroughs;
2. recognizable geographic/world scenes;
3. later, walkable real-time Unreal experiences.

```text
REFERENCES / FLOORPLANS / GEODATA
              ↓
        SOURCE MANIFEST
              ↓
         GEO / SCENE MANIFEST
              ↓
      AGENT (Sol / Astra later)
              ↓
           MCP LAYER
              ↓
           BLENDER
              ↓
   CAPTURE → VERIFY → CORRECT
              ↓
       CINEMATIC OUTPUT
              ↓
        UE5 (later gate)
```

## Current model status — 2026-09-04

Observed on the project owner's Windows machine:

- OpenAI Python SDK installed and API key validated.
- `gpt-6-astra` direct API request currently returns `404 model_not_found`.
- Codex CLI `0.153.2` is installed and healthy.
- Codex is authenticated through ChatGPT.
- Attempting `gpt-6-astra` through Codex/ChatGPT currently returns `400 invalid_request_error` / model not supported with a ChatGPT account.
- Current working Codex model: `gpt-5.6-sol`.
- Conclusion: **Astra rollout/access pending; infrastructure work proceeds with Sol and should be model-swappable.**

Do not block the project waiting for Astra.

## Project boundaries

### This repository owns
- agent + Blender orchestration experiments;
- MCP integration strategy;
- visual verification loops;
- SOLACE benchmark;
- geospatial bootstrap experiments;
- scene/source/geo manifests;
- Blender → cinematic output proof;
- future Blender → Unreal transfer experiments.

### This repository does not own
- the Blender MCP upstream implementation itself;
- WORLD COSTA BLANCA product/business logic;
- Sarah Katerina buyer logic;
- final Unreal product runtime until Blender gates pass.

## Primary benchmarks

### Benchmark A — SOLACE
Use the Thomas/Astra real-estate references to validate:
- plan / multi-view interpretation;
- blockout;
- living + dining + kitchen fidelity;
- camera / lighting / materials;
- 10–14 second cinematic walkthrough;
- inspect → capture → compare → correct loop.

### Benchmark B — Torrevieja / Costa Blanca bounded area
Use open/owned geodata to validate:
- recognizable coastline / major structure;
- buildings / roads / terrain bootstrap;
- hero landmarks vs procedural background fabric;
- Blender authoring from a geographic base;
- optional Google Photorealistic 3D Tiles as a separate visualization / human-reference layer.

The target is **recognizability + geographic coherence + visual quality**, not survey/BIM/cadastral accuracy.

## Related repositories

Primary technical sources and research candidates are recorded in [`docs/03-SOURCE-REPOS.md`](docs/03-SOURCE-REPOS.md).

Important owned sources include:
- `Juanmaes83/blender-mcp`
- `Juanmaes83/camera-to-blender`
- `Juanmaes83/map3d`
- `Juanmaes83/3DTilesRendererJS`
- `Juanmaes83/Blosm-addon-for-Blender.-A-few-clicks-import-of-Google-3D-cities-OpenStreetMap`
- `Juanmaes83/maptalks.js`
- `Juanmaes83/WORLD-COSTA-BLANCA`

## Governance

- Keep experiments reversible.
- Preserve source provenance and licences.
- Do not put API keys/secrets in Git.
- Do not claim visual success without capture/render evidence.
- Do not use Google Photorealistic 3D Tiles as an extraction/tracing source for owned geometry.
- Do not begin UE5 until Blender control + QA is stable.
- Prefer one bounded vertical slice over broad unfinished infrastructure.

## Documents

1. [`docs/00-PROJECT-CHARTER.md`](docs/00-PROJECT-CHARTER.md)
2. [`docs/01-CURRENT-STATE.md`](docs/01-CURRENT-STATE.md)
3. [`docs/02-TARGET-ARCHITECTURE.md`](docs/02-TARGET-ARCHITECTURE.md)
4. [`docs/03-SOURCE-REPOS.md`](docs/03-SOURCE-REPOS.md)
5. [`docs/04-BENCHMARKS-AND-QA.md`](docs/04-BENCHMARKS-AND-QA.md)
6. [`docs/05-ROADMAP.md`](docs/05-ROADMAP.md)
7. [`docs/06-GEOSPATIAL-STRATEGY.md`](docs/06-GEOSPATIAL-STRATEGY.md)

## Current status

**REPOSITORY INITIALIZED / ASTRA ACCESS PENDING / SOL + CODEX READY / BLENDER MCP INTEGRATION NEXT**
