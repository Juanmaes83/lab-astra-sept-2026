# 05 — Roadmap

## Phase 0 — Environment ready
Status: ✅ CLOSED — 2026-09-07

- OpenAI/Codex environment ready.
- Codex CLI installed and healthy.
- ChatGPT auth configured.
- `gpt-6-astra` now launches successfully in Codex CLI.
- Model-swappable architecture retained.

## Phase 1 — Blender MCP Gate 1
Status: 🟡 IN PROGRESS

Goal: prove reliable local Astra → Blender control with evidence.

1. use `Juanmaes83/blender-mcp` branch `lab/astra-sept-2026`;
2. install/update Blender addon;
3. enable Safe Mode;
4. register Blender MCP server in Codex;
5. confirm MCP health;
6. read current Blender scene without modifying it;
7. capture viewport;
8. create one bounded object/change only;
9. recapture;
10. verify identity + dimensions + visual result;
11. save evidence and PASS/FAIL record.

Completion condition:

```text
READ SCENE
+ SCREENSHOT
+ ONE CHANGE
+ SCREENSHOT
+ VERIFICATION
= PASS
```

No SOLACE work before this gate passes.

## Phase 2 — SOLACE architectural benchmark
Status: ⚪ BLOCKED BY PHASE 1

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

## Phase 3 — PROJECT-PELU handoff proof
Status: ⚪ NOT STARTED

1. package accepted GLB;
2. include `source_manifest.json` and `scene_manifest.json`;
3. include preview/camera metadata;
4. transfer package to PROJECT-PELU F2 branch;
5. verify the product consumes it without coupling to Blender;
6. preserve F1 360 fallback.

Completion condition: one LAB-produced spatial asset loads in PROJECT-PELU while F1 remains intact.

## Phase 4 — Geospatial proof
Status: ⚪ DEFERRED

Torrevieja/Altea bounded proof using open/owned geodata. Do not start while architectural F2 gates remain open.

## Phase 5 — Hero asset enrichment
Status: ⚪ DEFERRED

## Phase 6 — Blender → Unreal
Status: ⛔ BLOCKED

Only after Blender control, QA and architectural handoff are stable.

## Phase 7 — Persistence / orchestration upgrades
Status: ⚪ LATER

Rome/persistent capability, remote monitoring, spatial audio, region streaming and multi-agent orchestration only after the core proof.

## Anti-loop rule

At every phase ask:

```text
What is the smallest real artifact that proves this capability?
```

Do not spend days polishing infrastructure without reviewable output.