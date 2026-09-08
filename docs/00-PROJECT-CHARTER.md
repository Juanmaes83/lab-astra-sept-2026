# 00 — Project Charter

## Purpose

This LAB exists to prove a reusable spatial-production workflow where an AI agent can operate Blender through MCP, work from real structured references/geodata, build editable 3D scenes and iterate visually until the result is strong enough for human acceptance.

## Core production objective

For production-quality benchmarks, the canonical loop is:

```text
REFERENCE
→ ASSETS
→ ASSEMBLY
→ CRITIQUE
→ SHIP
```

Primary external workflow guide:

- Matt Shumer — https://somethingbig.ai/3d-worlds
- LAB adaptation — `docs/09-MATT-SHUMER-ASTRA-WORKFLOW.md`

The project is successful only when the workflow produces reference-grounded results that survive visual comparison, not when the agent merely generates code, geometry or an MP4.

## Execution principle

Use one human goal and autonomous internal iteration rather than many user-facing micro-gates.

When supported:

- run the production benchmark in `/goal` mode;
- fan out specialized workers;
- anchor builders on specific reference frames/media;
- separate builder from fresh-context critic;
- turn critic tells into concrete work orders;
- iterate until a serious review candidate exists.

Human acceptance remains external to the builder.

## Current primary proof — SOLACE photoreal cinematic reconstruction

Reconstruct the first continuous SOLACE cinematic shot:

```text
Living → Dining → Kitchen
approximately 00:00.000 → 00:13.967
hard cut at approximately 00:14.000
30 fps
14.0 s review target
```

This proof now tests:

- reference-grounded spatial reconstruction;
- measured camera/lens/timing reproduction;
- premium hero-asset quality;
- materials / glazing / vegetation;
- architectural lighting and atmosphere;
- independent critique and correction;
- final human visual acceptance.

Historical Gate 1, blockout, v01 and v02 results remain evidence of technical capability but are not the active quality bar.

## Secondary proof — Torrevieja geospatial

A bounded recognizable area generated from open/owned geodata, with hero landmarks separated from procedural supporting fabric.

Deferred while SOLACE is active.

## Non-goals

- survey-grade accuracy unless explicitly required by source/task;
- BIM/cadastral/engineering claims unsupported by evidence;
- full Costa Blanca generation before a bounded geographic proof;
- switching engines merely to avoid solving the active SOLACE benchmark;
- installing every interesting mapping/agent repo;
- repeating already closed infrastructure gates without a real regression.

## Model strategy

The workflow remains model-swappable.

Current operational baseline:

`gpt-6-astra` through Codex CLI on the project owner's machine.

No long-term architecture decision may require Astra to remain the only available model.

## Completion principle

A production benchmark is not complete because an agent says `done` or because a file exists.

Completion requires:

- source-grounded visual evidence;
- relevant render/video output;
- independent critique/work-order loop where supported;
- versioned scene/output;
- final human review by Juanma + ChatGPT.

Astra must not self-mark the final cinematic benchmark as HUMAN PASS.