# 04 — Benchmarks and QA

## Benchmark A — SOLACE

Purpose: reproduce the Thomas/Astra architectural workflow at bounded scope.

### Available reference types
- floorplan / concept plan;
- living reference;
- kitchen reference;
- exterior/pool reference;
- Blender/Cycles comparison board;
- Unreal Engine 5 comparison board;
- process video;
- final walkthrough video.

### First accepted slice
Living + dining + kitchen only.

Target video: approximately 10–14 seconds.

### Gates

#### G0 — Agent runtime
Codex session works with currently available model.

#### G1 — Blender connectivity
Agent can inspect scene and capture viewport without modifying it.

#### G2 — Closed loop
Agent makes one bounded change, captures result, verifies it, and reports exact state.

#### G3 — Blockout
Broad SOLACE geometry / spatial relationships are recognizable and coherent.

#### G4 — Visual slice
Living/dining/kitchen composition, materials and camera are recognizably aligned with references.

#### G5 — Cinematic
Stable 10–14 second walkthrough with no obvious geometry/camera failures.

#### G6 — Unreal
Blocked until G0–G5 pass.

## Benchmark B — Torrevieja / Costa Blanca

Purpose: prove that open/owned geodata can create a recognizable geographic base without survey-grade requirements.

### Fidelity budget

High fidelity:
- coastline / beach sequence;
- marina / port;
- lagoons / major water;
- major promenade;
- identity landmarks / defining silhouettes.

Coherent/approximate:
- principal roads;
- blocks / districts;
- major green structure.

Procedural/plausible:
- secondary buildings;
- generic façades;
- minor props;
- generic vegetation.

### First comparison
Use one bounded area and compare:
1. `map3d` — OSM → GLB/blockout;
2. Blosm — OSM/terrain → Blender-native scene;
3. `3DTilesRendererJS` — Google Photorealistic / 3D Tiles human reference view.

## Visual QA rule

Every meaningful build stage must leave evidence:

```text
STATE
+ SCREENSHOT/RENDER
+ MEASUREMENTS/MANIFEST WHERE RELEVANT
+ PASS/FAIL NOTE
```

No stage passes because an agent writes “done”.
