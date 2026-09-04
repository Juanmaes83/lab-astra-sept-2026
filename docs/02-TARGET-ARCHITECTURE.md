# 02 — Target Architecture

## Principle

Separate deterministic world structure from AI judgment.

Use code/geodata for topology, coordinates, broad geometry and repeatable transforms. Use the agent for interpretation, refinement, art direction, camera, materials, troubleshooting and visual QA.

## Target stack

```text
INPUTS
├── floorplans
├── photos / multi-view references
├── OSM / Overture / DEM
├── allowed documentation
└── user brief
        ↓
SOURCE MANIFEST
        ↓
GEO / SCENE MANIFEST
        ↓
AGENT ORCHESTRATOR
Sol now / Astra later / other capable model if useful
        ↓
MCP + SKILLS
        ↓
BLENDER
        ↓
SCENE STATE + SCREENSHOT + RENDER
        ↓
VERIFIERS
├── dimensions
├── topology / adjacency
├── fixed camera comparison
├── visual reference comparison
├── human approval
└── provenance / licence checks
        ↓
ACCEPTED SCENE
        ↓
├── cinematic walkthrough
├── GLB / structured export
└── Unreal handoff later
```

## Required manifests

### source_manifest.json
Records where references came from, allowed use, date, licence/attribution and role.

### geo_manifest.json
Records geographic area, source layers, terrain, roads, buildings, water, vegetation, POIs, hero assets and fidelity tier.

### scene_manifest.json
Records Blender object identity, transforms, materials, cameras, lights, semantic role and export mapping.

## Why manifests matter

The durable system is not the `.blend` file alone. The manifests allow:
- reproducibility;
- change tracking;
- Blender → Unreal transfer;
- QA;
- model swapping;
- provenance;
- automation without losing semantic meaning.

## Visual verification loop

```text
INSPECT
→ CHANGE ONE STAGE
→ CAPTURE
→ COMPARE
→ MEASURE
→ FIX
→ RE-CAPTURE
→ ACCEPT / REJECT
```

Textual claims are not accepted as proof of scene quality.

## Unreal gate

UE5 begins only after:
1. Blender MCP control is reliable;
2. capture/QA works;
3. one SOLACE cinematic slice passes;
4. scene manifests are stable enough to preserve identity and transforms.
