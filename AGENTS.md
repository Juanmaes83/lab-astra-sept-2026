# AGENTS.md

## Mission

Build and validate the smallest real spatial artifact that proves the current capability.

Primary loop:

```text
INSPECT -> ACT -> CAPTURE -> VERIFY -> CORRECT -> REPORT
```

## Current model state

- Current execution model: `gpt-6-astra` through Codex CLI.
- Astra access is confirmed on the project owner's Windows machine.
- Keep the workflow model-swappable; no architecture contract may depend permanently on Astra.
- Never claim Astra is active unless the active Codex session reports `gpt-6-astra`.

## Current active gate

**Gate 1 — Astra → Blender MCP → Capture → Verify.**

Do not begin SOLACE until:
- Blender MCP scene read succeeds;
- before screenshot exists;
- one bounded mutation succeeds;
- after screenshot exists;
- dimensions/state verification passes;
- evidence is recorded.

## Allowed work

- inspect repository files;
- write/update LAB code and documentation;
- create reversible branches/worktrees;
- run local tests;
- use configured MCP servers;
- operate Blender in bounded experiments;
- create manifests, QA evidence and preview renders;
- propose source-repo adaptations with provenance;
- produce accepted GLB/manifests for PROJECT-PELU handoff after QA.

## Human approval gates

Stop before:
- merging to protected/product branches;
- publishing/deploying externally;
- deleting important source data;
- changing permissions/secrets;
- incurring paid external-service usage beyond ordinary approved model/API use;
- irreversible Blender/project overwrites without a saved version.

## Blender rules

- Prefer Safe Mode for agent-driven Blender execution.
- Save/version the `.blend` file before major changes.
- Do not accept textual success without screenshot/render/scene-state evidence.
- Make changes in bounded stages.
- Keep semantic object names stable when possible.
- During Gate 1, modify only `LAB_TEST_CUBE` after the read-only step passes.

## PROJECT-PELU handoff rules

- This LAB produces; PROJECT-PELU consumes.
- Do not duplicate PROJECT-PELU runtime, hotspots, analytics or commercial logic here.
- Only `ACCEPTED` assets may be handed off.
- Preserve `source_manifest.json` / `scene_manifest.json` and provenance.
- F1 panorama fallback remains owned by PROJECT-PELU.

## Geospatial rules

- Target recognizability and coherent geography, not survey/BIM accuracy.
- Use open/owned geodata for editable geometry.
- Keep Google Photorealistic 3D Tiles as separate compliant visualization/human reference.
- Do not extract, trace or machine-derive owned geometry from Google Map Tiles content.

## Scope discipline

Do not expand to Unreal, geospatial world-building, Rome, Ableton, iOS remote control or region-scale streaming until the active architectural gate passes.

## Completion evidence

A task is complete only when it leaves reviewable evidence:
- commit/diff;
- test output;
- Blender scene state;
- screenshot/render;
- manifest;
- exported asset;
- explicit pass/fail record.

## Reporting

Report:
1. current state;
2. action taken;
3. evidence;
4. next blocking gate;
5. remaining risk only if material.