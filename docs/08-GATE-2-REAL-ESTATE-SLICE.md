# 08 — Gate 2 — Real-Estate Spatial Slice

**Status:** 🟡 PLANNED / NEXT
**Date:** 2026-09-07
**Depends on:** Gate 1 ✅ PASS

## Purpose

Prove that the Astra → Blender MCP → QA loop can produce a small but real-estate-relevant spatial asset, not only a test cube.

Gate 2 deliberately stays smaller than SOLACE. It is a bounded vertical slice that validates architecture, dimensions, capture/verification, semantic naming, export and manifest discipline before using a complex reference set.

## Target artifact

A simple architectural room shell / living-space blockout with:

- floor;
- four enclosing walls with one intentional opening;
- ceiling height defined;
- one doorway or wide opening;
- one camera/viewpoint;
- stable semantic names;
- metric dimensions;
- no decorative complexity required.

Suggested default geometry for the proof unless the human chooses another bounded size:

```text
ROOM width: 6.0 m
ROOM depth: 4.0 m
WALL height: 2.7 m
WALL thickness: 0.15 m
OPENING width: 1.2 m
OPENING height: 2.1 m
```

These are test dimensions only, not claims about a real property.

## Semantic naming

Minimum object identity:

```text
ROOM_FLOOR
WALL_NORTH
WALL_SOUTH
WALL_EAST
WALL_WEST
OPENING_MAIN
CAMERA_REVIEW
```

If Blender construction uses boolean/helper objects, helpers must be clearly prefixed, e.g. `HELPER_...`.

## Execution sequence

### Gate 2A — Clean/versioned start

1. close/discard the temporary Gate 1 scene or remove only `LAB_TEST_CUBE` in a controlled step;
2. create a fresh scene for Gate 2;
3. save a versioned LAB file only after the human approves the path/name;
4. record Blender version and unit system.

### Gate 2B — Architectural blockout

1. create the floor and four walls;
2. apply exact metric dimensions;
3. create one doorway/opening;
4. use semantic names;
5. create one review camera;
6. do not add furniture/material complexity yet.

### Gate 2C — Verify

Astra must inspect and report:

- object names;
- positions;
- scales;
- dimensions;
- wall height;
- room width/depth;
- opening size;
- adjacency/coherence;
- unexpected objects.

Then capture a fixed review viewport/camera image.

### Gate 2D — Correct

If any metric or visual issue exists:

1. identify the exact mismatch;
2. change only the affected objects;
3. recapture;
4. remeasure;
5. record before/after.

At least one explicit verification cycle is mandatory even if no correction is required.

### Gate 2E — Export candidate

1. export the accepted blockout as GLB;
2. inspect export success;
3. record file size;
4. do not call it an `ACCEPTED SPATIAL PACKAGE` yet;
5. create `scene_manifest.json` with object identity and dimensions.

## Evidence

Store under:

```text
evidence/gate-2/
```

Expected minimum:

```text
00-before.png
01-blockout.png
02-verified.png
scene_manifest.json
GATE-2-RESULT.md
```

If a correction occurs, include the intermediate capture.

## PASS criteria

- [ ] Astra controls Blender through the same Safe Mode MCP path.
- [ ] bounded room shell created.
- [ ] metric dimensions verified.
- [ ] semantic names stable.
- [ ] no unrelated scene changes.
- [ ] fixed visual evidence captured.
- [ ] explicit verify/correct decision recorded.
- [ ] GLB export succeeds.
- [ ] `scene_manifest.json` exists and matches the scene.
- [ ] human reviews the result.

## FAIL conditions

- geometry is visually plausible but dimensions are wrong;
- object identity is unstable/random;
- export cannot be reproduced;
- unrelated objects are changed;
- textual success is claimed without capture/measurement;
- the test grows into SOLACE/full-property work before this gate closes.

## After PASS

Proceed to the SOLACE benchmark using the same discipline:

```text
SOURCE MANIFEST
→ SCENE MANIFEST
→ BLOCKOUT
→ VERIFY
→ REFINE
→ ACCEPTED GLB
```
