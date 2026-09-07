# 08 — Gate 2 — SOLACE Architectural Blockout

**Status:** 🟡 PLANNED / NEXT
**Date:** 2026-09-07
**Depends on:** Gate 1 ✅ PASS

## Purpose

Prove that the Astra → Blender MCP → QA loop can interpret and reconstruct a non-trivial real-estate floor plan as a coherent 3D architectural blockout.

Gate 2 is intentionally more demanding than a single-room shell. Gate 1 already proved reliable read → act → capture → verify control. Gate 2 must now prove spatial understanding on a real-estate reference with multiple rooms, circulation, courtyard, exterior areas and pool.

## Authoritative visual reference

Use this repository asset as the primary floor-plan reference:

`references/solace/HRUOGWHaMAATXEa.jpg`

Validated locally: 680 × 661 pixels, JPEG decode and SOLACE visual identity PASS. The former `references/solace/SOLACE-CONCEPT-01-FLOORPLAN.jpg` is REJECTED/CORRUPT and retained only for provenance; do not use it.

The image was supplied by the project owner as an existing SOLACE benchmark reference. Treat it as the visual authority for Gate 2 geometry. Do not invent dimensions or architectural relationships that are not legible or inferable from the reference. Where exact dimensions are unclear, record the uncertainty explicitly in the manifest rather than presenting estimates as verified facts.

## Architectural identity visible in the reference

The floor plan shows a single-level garden house organised around a large planted courtyard.

Primary spatial organisation to preserve:

- north/top arrival and ENTRY;
- central open social zone: LIVING → DINING → KITCHEN;
- COVERED OUTDOOR DINING opening toward the central courtyard;
- large PLANTED COURTYARD as the main organising void;
- west/left wing with OFFICE, FAMILY BATH, BEDROOM 02 and BEDROOM 03;
- east/right wing with PANTRY, LAUNDRY, GUEST WC, PLANT / STORE, PRIMARY BATH, DRESSING and PRIMARY BEDROOM;
- exterior PRIVATE GARDEN / OPEN LAWN / SUN TERRACE;
- LAP POOL positioned south/below the house;
- major openings, doors and circulation must preserve the reference logic.

Visible global/reference dimensions include approximately 25.40 m overall width and 17.00 m overall depth. Use only dimensions clearly visible in the source as authoritative. The pool is labelled approximately 10.0 × 3.5 m. Other room labels/dimensions should be read from the image when legible and recorded with confidence/provenance.

## Target artifact

Gate 2 must create a recognisable SOLACE architectural blockout, not a decorative archviz scene.

Minimum required geometry:

- overall house footprint;
- west wing;
- east wing;
- central living/dining/kitchen zone;
- planted courtyard void;
- covered outdoor dining zone;
- entry;
- office;
- bedrooms 02 and 03;
- primary bedroom suite zone;
- principal bathrooms/service rooms as simplified enclosed spaces;
- main internal/external circulation openings;
- simplified terrace/garden boundaries where needed for spatial reading;
- lap pool as a correctly positioned simple volume;
- one fixed top-review camera;
- one fixed perspective-review camera.

## Not required in Gate 2

Do not spend the gate on decorative detail.

Out of scope until the blockout passes:

- detailed furniture;
- final kitchen cabinetry;
- final sanitaryware;
- PBR materials;
- photorealistic vegetation;
- cinematic lighting;
- premium archviz styling;
- Unreal;
- geospatial context.

Simple placeholder furniture may be used only when it materially helps verify room function/scale, and must be semantically named as placeholder/reference geometry.

## Semantic naming

Use stable semantic identifiers. Suggested pattern:

```text
SOLACE_SITE
SOLACE_HOUSE
SPACE_ENTRY
SPACE_LIVING
SPACE_DINING
SPACE_KITCHEN
SPACE_COVERED_OUTDOOR_DINING
SPACE_PLANTED_COURTYARD
SPACE_OFFICE
SPACE_FAMILY_BATH
SPACE_BEDROOM_02
SPACE_BEDROOM_03
SPACE_PANTRY
SPACE_LAUNDRY
SPACE_GUEST_WC
SPACE_PLANT_STORE
SPACE_PRIMARY_BATH
SPACE_DRESSING
SPACE_PRIMARY_BEDROOM
SPACE_PRIVATE_GARDEN
SPACE_OPEN_LAWN
SPACE_SUN_TERRACE
POOL_LAP
CAMERA_TOP_REVIEW
CAMERA_PERSPECTIVE_REVIEW
```

Walls/openings may use predictable prefixes such as `WALL_`, `OPENING_`, `DOOR_`, `WINDOW_`, `HELPER_`.

## Execution sequence

### Gate 2A — Source inspection and plan interpretation

Before changing Blender:

1. read `AGENTS.md`, `docs/04-BENCHMARKS-AND-QA.md`, this document and the SOLACE reference image;
2. inspect the image carefully before generating geometry;
3. create/update `references/solace/source_manifest.json` or an equivalent Gate 2 source record;
4. record visible dimensions, labels, adjacency and uncertain values;
5. create a concise reconstruction plan;
6. do not begin detailed modelling until the interpretation is internally consistent.

### Gate 2B — Clean/versioned Blender start

1. preserve or discard the Gate 1 temporary scene safely;
2. create a fresh Gate 2 Blender scene;
3. metric units, scale 1;
4. no destructive overwrite of unrelated `.blend` files;
5. save a versioned LAB `.blend` only after choosing an explicit Gate 2 path/name.

### Gate 2C — Architectural blockout

Build the property in bounded passes:

1. global footprint and courtyard void;
2. west and east wings;
3. central living/dining/kitchen zone;
4. room partitions and major openings;
5. covered outdoor dining;
6. exterior terrace/garden reading;
7. lap pool;
8. review cameras.

After each major pass: inspect → capture → compare → correct.

### Gate 2D — Fixed-view QA

At minimum capture:

- a top/orthographic-like view that can be compared directly with the reference plan;
- a perspective view that demonstrates the 3D volume and courtyard organisation.

A textual claim that the plan was reconstructed is not sufficient. The top view must be recognisably the same architectural layout even without room labels.

Verify:

- overall proportions;
- central courtyard placement/scale;
- west/east wing relationships;
- living/dining/kitchen sequence;
- covered outdoor dining placement;
- room adjacency;
- openings/circulation;
- primary suite position;
- pool position and proportions;
- no unrelated objects;
- metric scale consistency.

### Gate 2E — Correct

For each mismatch:

1. name the exact discrepancy;
2. modify only affected objects;
3. recapture the same fixed view;
4. remeasure/recompare;
5. record PASS/FAIL for that discrepancy.

At least one explicit QA cycle is mandatory even if no correction is required.

### Gate 2F — Export candidate

Only after the blockout passes geometry QA:

1. create `scene_manifest.json`;
2. record semantic object identity and known/estimated dimensions;
3. export candidate GLB;
4. verify export success and file size;
5. inspect the exported GLB if practical;
6. do not call it an `ACCEPTED SPATIAL PACKAGE` until human review passes.

## Evidence

Store under:

```text
evidence/gate-2-solace/
```

Expected minimum:

```text
00-reference-analysis.md
01-top-blockout.png
02-perspective-blockout.png
03-top-verified.png
scene_manifest.json
source_manifest.json
SOLACE_BLOCKOUT_v01.glb
GATE-2-RESULT.md
```

If corrections occur, preserve intermediate captures.

## PASS criteria

- [ ] Astra remains connected to Blender through the Safe Mode MCP path.
- [ ] SOLACE reference image is actually inspected and recorded as source.
- [ ] house footprint is recognisable from the source.
- [ ] central planted courtyard is preserved as the main organising void.
- [ ] west/east wings and central social zone preserve adjacency.
- [ ] key rooms/zones are semantically named.
- [ ] major openings/circulation are coherent.
- [ ] pool placement/proportions are coherent with the reference.
- [ ] metric scale is internally consistent.
- [ ] fixed top-view comparison passes visual review.
- [ ] perspective review demonstrates coherent 3D volume.
- [ ] verify/correct loop is recorded.
- [ ] GLB export succeeds.
- [ ] manifests match the scene.
- [ ] human review approves the blockout.

## FAIL conditions

- generic house that does not resemble the SOLACE plan;
- central courtyard is lost, enclosed or materially displaced;
- rooms are plausible individually but adjacency is wrong;
- dimensions/relationships are invented and presented as verified;
- geometry is built without fixed-view comparison;
- textual success is claimed without screenshots/measurements;
- decorative work starts before architectural QA passes;
- unrelated Blender content is changed;
- export cannot be reproduced.

## After PASS

Proceed to the next SOLACE refinement gate:

```text
ACCEPTED BLOCKOUT
→ openings/detail refinement
→ living/dining/kitchen fidelity
→ materials/light/camera
→ cinematic walkthrough
→ accepted GLB / spatial package
→ PROJECT-PELU handoff
```
