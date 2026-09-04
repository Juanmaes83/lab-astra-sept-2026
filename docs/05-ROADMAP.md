# 05 — Roadmap

## Phase 0 — Environment ready
Status: MOSTLY COMPLETE

- OpenAI SDK installed.
- API key validated.
- Codex CLI installed.
- Codex Doctor healthy.
- Sol available.
- Astra access tested and currently pending.

## Phase 1 — Blender MCP connection
Goal: reliable local control.

1. clone/use `Juanmaes83/blender-mcp` September LAB;
2. install/update Blender addon;
3. enable Safe Mode;
4. register the Blender MCP server in Codex;
5. confirm `/mcp` health;
6. read current Blender scene;
7. capture viewport;
8. create one bounded object;
9. recapture and verify.

Completion condition: the full read → act → capture → verify loop works.

## Phase 2 — SOLACE benchmark

1. upload/reference original SOLACE media;
2. create source manifest;
3. create scene manifest v0;
4. build broad blockout;
5. validate spatial relationships;
6. detail living/dining/kitchen;
7. camera/light/material pass;
8. visual comparison loop;
9. render 10–14 second walkthrough.

Completion condition: recognizably coherent architectural slice with review evidence.

## Phase 3 — Geospatial proof

1. define bounded Torrevieja/Altea area;
2. test `map3d` path;
3. test Blosm path;
4. test `3DTilesRendererJS` reference path;
5. compare speed, editability, fidelity and exportability;
6. define `geo_manifest.json`;
7. choose primary owned-geometry path;
8. build one recognizable geographic slice.

Completion condition: recognizable world base generated without manual city-by-city modeling.

## Phase 4 — Hero asset enrichment

1. identify identity-defining landmarks;
2. collect permitted references;
3. reconstruct/refine hero assets;
4. proceduralize supporting fabric;
5. visual QA against references.

## Phase 5 — Blender → Unreal

Blocked until the Blender pipeline is stable.

1. define export contract from `scene_manifest.json`;
2. preserve transforms/material identity/cameras;
3. import/reconstruct in UE5;
4. add collisions/navigation;
5. compare equivalent cameras;
6. package first walkable proof.

## Phase 6 — Persistence / orchestration upgrades

Only after core proof:
- Rome or similar persistent capability layer;
- remote monitoring via iOS patterns;
- Ableton/spatial audio;
- larger-region streaming/runtime;
- multi-agent orchestration.

## Anti-loop rule

Do not spend days perfecting infrastructure before a visible output exists.

At every phase ask:

```text
What is the smallest real artifact that proves this capability?
```
