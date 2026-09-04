# AGENTS.md

## Mission

Build and validate the smallest real spatial artifact that proves the current capability.

Primary loop:

```text
INSPECT -> ACT -> CAPTURE -> VERIFY -> CORRECT -> REPORT
```

## Current model state

- Use `gpt-5.6-sol` when Astra is unavailable.
- Treat `gpt-6-astra` as an optional upgrade, not a prerequisite.
- Never claim Astra is active unless a real inference succeeds with that model.

## Allowed work

- inspect repository files;
- write/update LAB code and documentation;
- create reversible branches/worktrees;
- run local tests;
- use configured MCP servers;
- operate Blender in bounded experiments;
- create manifests, QA evidence and preview renders;
- propose source-repo adaptations with provenance.

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

## Geospatial rules

- Target recognizability and coherent geography, not survey/BIM accuracy.
- Use open/owned geodata for editable geometry.
- Keep Google Photorealistic 3D Tiles as a separate compliant visualization/human-reference layer.
- Do not extract, trace or machine-derive owned geometry from Google Map Tiles content.
- Record source/licence/attribution in manifests.

## Scope discipline

Do not expand to Unreal, Rome, Ableton, iOS remote control or region-scale streaming until the current Blender/QA gate passes.

Do not add a framework merely because it is interesting. Close a demonstrated capability gap.

## Completion evidence

A task is complete when it leaves a reviewable artifact such as:
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
