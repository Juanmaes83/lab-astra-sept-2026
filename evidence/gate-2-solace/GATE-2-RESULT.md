# SOLACE Gate 2 architectural blockout

TECHNICAL GATE 2 CANDIDATE: **PASS**

HUMAN REVIEW: **PENDING**

Date: 2026-09-07. Candidate only; not an ACCEPTED SPATIAL PACKAGE.

## Runtime and source

- Blender: **5.2.1 LTS**, returned by actual MCP execution.
- Codex: orchestration and tools successful. Owner and AGENTS.md identify `gpt-6-astra`; active model identifier was not independently queried in this run, so no new model-access claim is made.
- MCP: configured `blender-astra-lab`, prepared LAB implementation, Safe Mode=1, localhost:9876, addon protocol 5. All four staged execute_blender_code calls succeeded with isError=false. Gate 1/setup not repeated.
- Git: safe fast-forward to `6c61ee33f0c4f8616abbe87c43d8a2017abe1a6f`; local evidence retained; no push/publication.
- Active source: `references/solace/HRUOGWHaMAATXEa.jpg`, 57,654 bytes, 680 x 661 pixels, header FF D8 FF E0 00 10 4A 46, normal decoding and visual SOLACE identity PASS. Blob `89d1474815c61631c63accfbc0e26cecfb37a8ee`.
- Source manifest and Gate 2 document corrected to active reference. Old canonical JPG retained as REJECTED/CORRUPT. Previous blocker report preserved in HISTORY-image-blocker.md.

## Geometry and saves

Fresh active scene SOLACE_GATE_2: 137 objects, 135 meshes and two cameras. Contains all 20 requested SPACE zones, west/east slabs, galleries and services, 64 wall segments, 18 opening thresholds, 14 glazing sills, covered dining frame, pool and simple exterior ground zones. Three crude solid shapes distinguish living/dining/kitchen; no detailed furniture.

North entry; west-to-east living/dining/kitchen across north bar; south-open planted courtyard; four west rooms with courtyard-side gallery; east services above primary bath/dressing/bedroom; southern pool, southwest lawn and southeast private garden. Courtyard is unroofed. Coverage represented by an open frame.

Metric scale 1. Original Gate 1 scene retained separately in blend and excluded from active scene and export. No unrelated blend overwritten. New checkpoints:

- outputs/solace/SOLACE_BLOCKOUT_v01.blend: macro.
- outputs/solace/SOLACE_BLOCKOUT_v02.blend: partitions.
- outputs/solace/SOLACE_BLOCKOUT_v03.blend: corrections.
- **outputs/solace/SOLACE_BLOCKOUT_v04.blend: final candidate**, 171,060 bytes.

## Measurements and QA

VERIFIED_FROM_SOURCE means a readable concept annotation, not surveyed geometry. All individual room dimensions, wall axes/thickness/height, door and window widths, exterior boundaries and depth representations are ESTIMATED_FOR_BLOCKOUT. Full per-axis classifications and transforms are in scene_manifest.json.

| Check | Evidence | Result |
| --- | --- | --- |
| Main body footprint reference | 25.3999996 x 17.0 m; excludes north entry projection | PASS |
| Planted courtyard surface | 12.3999996 x 10.8000002 m after correction | PASS |
| Courtyard void | between wings, social bar north, open south | PASS |
| Gallery wall clear span | approx. 12.59 m, image-stroke estimate distinct from 12.40 m planted patch | PASS with recorded uncertainty |
| Pool | 10.0 x 3.5 m; east-west, south of courtyard | PASS |
| West wing | office, bath, bedroom 02, bedroom 03; east-side gallery and door gaps | PASS |
| East wing | pantry/laundry, WC/store, bath/dressing/primary; west-side suite gallery | PASS |
| Social zone | living X < dining X < kitchen X in north band | PASS |
| Covered dining | north end of courtyard, adjacent social zone | PASS |
| Circulation | west gallery, east service passage and suite gallery; actual wall gaps | PASS for blockout |
| Exterior | lawn SW, private garden SE, central terrace and pool | PASS for estimated boundaries |
| Units/scope | metric scale 1, requested zones present, no Gate 1 objects active | PASS |

Known annotation constraints: body 25.40 x 17.00 m, courtyard planting 12.40 x 10.80 m, pool 10.0 x 3.5 m. Small room annotation text was not promoted to verified dimensions. Wall height 2.8 m and thickness 0.22 m are estimates.

## Compare → correct → recapture

1. Inspected 00-macro-top.png: U footprint, north entry and pool coherent; divisions pending.
2. Built partitions; captured 01-top-blockout.png and 02-perspective-blockout.png. Viewed these and the source directly. Room ordering and main gaps correspond.
3. D01: pixel-derived courtyard patch 12.70 x 10.916 m differed from readable 12.40 x 10.80 annotation. Modified only SPACE_PLANTED_COURTYARD XY dimensions, preserved position. Remeasure PASS at 1e-5 m numerical tolerance. Gallery wall axes remain explicitly estimated.
4. D02: long shadows obscured top-view partitions. Disabled shadows and used flat shading. Camera unchanged: position (13.2619467,4.3779263,48), rotation (0,0,0), ortho scale 36. Recapture readability PASS.
5. D03: empty social band did not distinguish functions visually. Added three simple reference blocks at source-inferred sofa/table/island positions. No boundary changes; order readability PASS.
6. Personally inspected final 03-top-verified.png and 04-perspective-verified.png: recognizable unlabeled source layout at blockout fidelity; open courtyard and coherent volume. No further material macro discrepancy identified.

## Evidence and export

- 00-reference-analysis.md: interpretation and uncertainty; prior history retained.
- 00-macro-top.png, 01-top-blockout.png, 02-perspective-blockout.png: intermediate views.
- **03-top-verified.png**, **04-perspective-verified.png**: final review views.
- stage1-mcp.json through stage4-mcp.json: actual successful tool responses.
- scene_manifest.json: 137 object records from scene state.
- source_manifest.json: active and rejected source provenance.
- glb-verification.json: binary and semantic checks.

Images are actual Blender Workbench camera renders, not synthetic illustrations.

**evidence/gate-2-solace/SOLACE_BLOCKOUT_v01.glb: 185,324 bytes.** Blender exporter FINISHED. Independent binary inspection confirms glTF 2 header/length, 137 nodes, 135 meshes, two cameras, all manifest names, no Gate 1 nodes and no external buffer dependencies. No independent rendered reimport; export verification is structural/semantic.

## Remaining risks / next gate

Owner visual approval pending. Source is a 680 x 661 concept image, not construction documentation. Roofless blockout; window sills/thresholds simplify openings, covered dining is an open frame, pool a shallow visualization volume, exterior boundaries rectangular approximations. Gallery boundary interpretation differs from the explicitly sized planted patch and is not claimed exact. Basic flat export color swatches only; no textures, premium materials, detailed furnishings, cinematics, Unreal or PROJECT-PELU handoff.

Stop for owner review of final top and perspective. Do not mark ACCEPTED until approved.
