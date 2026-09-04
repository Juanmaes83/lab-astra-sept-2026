# 00 — Project Charter

## Purpose

This LAB exists to prove a reusable spatial-production workflow where an AI agent can operate Blender through MCP, work from structured references/geodata, verify what it built visually, correct errors, and produce reviewable outputs.

## Core objective

Prove the loop:

```text
INPUT
→ STRUCTURE
→ BUILD
→ CAPTURE
→ VERIFY
→ CORRECT
→ ACCEPT
```

The project is successful only when the loop works on real spatial tasks, not when the agent merely generates code.

## First two proofs

### P1 — SOLACE architectural proof
A bounded real-estate scene reconstructed from plan + multi-view references, with a 10–14 second walkthrough.

### P2 — Torrevieja geospatial proof
A bounded recognizable area generated from open/owned geodata, with hero landmarks separated from procedural supporting fabric.

## Non-goals

- survey-grade accuracy;
- BIM/cadastral/engineering deliverables;
- full Costa Blanca generation before a bounded proof;
- Unreal before Blender control + QA is stable;
- installing every interesting mapping/agent repo;
- blocking progress on GPT-6 Astra rollout.

## Model strategy

The workflow must be model-swappable.

Current operational baseline: `gpt-5.6-sol` in Codex.

Desired later upgrade: `gpt-6-astra` when access is actually enabled.

No architecture decision may depend on Astra being available today.

## Completion principle

A stage is not complete because an agent says it is complete.

It is complete only when there is reviewable evidence: scene state, screenshot/render, dimensions/manifest checks, or executable output.
