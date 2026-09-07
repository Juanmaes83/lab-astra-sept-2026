# 05 — Roadmap

## Phase 0 — Environment ready
Status: ✅ CLOSED — 2026-09-07

- OpenAI/Codex environment ready.
- Codex CLI installed and healthy.
- ChatGPT auth configured.
- `gpt-6-astra` launches successfully in Codex CLI.
- Model-swappable architecture retained.

## Phase 1 — Blender MCP Gate 1
Status: ✅ CLOSED — 2026-09-07

Goal: prove reliable local Astra → Blender control with evidence.

Completed:
1. `Juanmaes83/blender-mcp` branch `lab/astra-sept-2026` used as source;
2. Blender 5.2.1 LTS installed;
3. MCP addon enabled;
4. Safe Mode enabled;
5. 69 Safe Mode tests PASS;
6. Blender MCP registered in Codex as `blender-astra-lab`;
7. MCP connected on port 9876;
8. Gate 1A read-only scene inspection PASS;
9. viewport capture PASS;
10. Gate 1B bounded mutation PASS;
11. `LAB_TEST_CUBE` created at `(0,4,0)` with dimensions `2 × 2 × 2 m`;
12. Cube, Camera and Light remained unchanged;
13. before/after capture and verification PASS;
14. no `.blend` file overwritten;
15. PASS record stored in `evidence/gate-1/gate-1-result.md`.

Completion condition:

```text
READ SCENE
+ SCREENSHOT
+ ONE CHANGE
+ SCREENSHOT
+ VERIFICATION
= PASS
```

Gate result: **PASS**.

## Phase 2 — Gate 2 / Smallest useful real-estate spatial slice
Status: 🟡 NEXT

Goal: move from infrastructure proof to a reviewable real-estate spatial artifact without jumping directly to a full reconstruction.

Proposed slice:
1. start from a clean/versioned Blender scene;
2. create a bounded architectural composition representing a simple room shell / living-space blockout;
3. use stable semantic object names;
4. verify dimensions and adjacency;
5. capture fixed-view evidence;
6. perform one correction loop if needed;
7. save a versioned `.blend` only after review;
8. export a first candidate GLB;
9. record scene metadata in a minimal `scene_manifest.json`;
10. classify result PASS/FAIL before expanding to SOLACE.

Completion condition:

```text
BOUNDED REAL-ESTATE SCENE
+ DIMENSION CHECK
+ VISUAL CAPTURE
+ CORRECTION LOOP
+ GLB EXPORT
+ MANIFEST
= PASS
```

This phase is intentionally small. It proves that the Astra→Blender loop can create an asset that is relevant to PROJECT-PELU, not just a test cube.

## Phase 3 — SOLACE architectural benchmark
Status: ⚪ BLOCKED BY GATE 2

1. upload/reference original SOLACE media;
2. create source manifest;
3. create scene manifest v0;
4. build broad blockout;
5. validate spatial relationships;
6. detail living/dining/kitchen;
7. camera/light/material pass;
8. visual comparison loop;
9. render 10–14 second walkthrough;
10. export accepted GLB + manifests for PROJECT-PELU handoff.

Completion condition: recognizably coherent architectural slice with review evidence and an `ACCEPTED SPATIAL PACKAGE`.

## Phase 4 — PROJECT-PELU handoff proof
Status: ⚪ NOT STARTED

1. package accepted GLB;
2. include `source_manifest.json` and `scene_manifest.json`;
3. include preview/camera metadata;
4. transfer package to PROJECT-PELU F2 branch;
5. verify the product consumes it without coupling to Blender;
6. preserve F1 360 fallback.

Completion condition: one LAB-produced spatial asset loads in PROJECT-PELU while F1 remains intact.

## Phase 5 — Geospatial proof
Status: ⚪ DEFERRED

Torrevieja/Altea bounded proof using open/owned geodata. Do not start while architectural F2 gates remain open.

## Phase 6 — Hero asset enrichment
Status: ⚪ DEFERRED

## Phase 7 — Blender → Unreal
Status: ⛔ BLOCKED

Only after Blender control, QA and architectural handoff are stable.

## Phase 8 — Persistence / orchestration upgrades
Status: ⚪ LATER

Rome/persistent capability, remote monitoring, spatial audio, region streaming and multi-agent orchestration only after the core proof.

## Anti-loop rule

At every phase ask:

```text
What is the smallest real artifact that proves this capability?
```

Do not spend days polishing infrastructure without reviewable output.
