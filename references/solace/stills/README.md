# SOLACE cinematic anchor stills

These stills are extracted from the authoritative cinematic target:

`references/solace/video/VIDEO_REFERENCIA_SOLACE_CINEMATIC_TARGET.mp4`

They are **reference assets, not generated target art**. Their purpose is to stop Astra from treating the video loosely and to provide fixed screen-space checkpoints for camera, architecture, furniture, material, lighting and atmosphere matching.

## Extraction

- Source recording: `1990 × 1426`, `30 fps`
- Active cinematic picture crop: `x=0, y=156, w=1990, h=1120`
- Reference delivery: `1920 × 1080`
- JPEG quality: high-quality reference export
- First continuous shot: approximately `0.000 → 13.967 s`
- Hard cut: approximately `14.000 s`

## Anchor set

| Time | Source frame | File | Primary visual role |
|---:|---:|---|---|
| 0.0 s | 0 | `SOLACE_TARGET_00000ms.jpg` | Exterior/glazing opening composition; library left, sofa center, dining right |
| 2.0 s | 60 | `SOLACE_TARGET_02000ms.jpg` | Exterior approach; mullions/reflections and interior depth |
| 4.0 s | 120 | `SOLACE_TARGET_04000ms.jpg` | Living approach; sofa/library and rear doorway |
| 6.0 s | 180 | `SOLACE_TARGET_06000ms.jpg` | Living hero; sofa dominates, dining transition not yet advanced |
| 8.0 s | 240 | `SOLACE_TARGET_08000ms.jpg` | Dining hero; table/chairs dominant, kitchen entering |
| 10.0 s | 300 | `SOLACE_TARGET_10000ms.jpg` | Dining → Kitchen transition; island entering foreground |
| 12.0 s | 360 | `SOLACE_TARGET_12000ms.jpg` | Kitchen hero; island, rear sink/window, tall units/opening |
| 13.8 s | 414 | `SOLACE_TARGET_13800ms.jpg` | Kitchen end frame immediately before hard cut |

`SOLACE_TARGET_CONTACT_SHEET.jpg` is a convenience overview only. The eight individual stills are the authoritative fixed checkpoints.

## Astra rule

At every checkpoint Astra should compare the Blender render against the corresponding still using stable screen-space landmarks:

- glazing mullions;
- library edges/shelves;
- sofa silhouette and scale;
- rear doorway;
- dining table/chairs;
- kitchen island;
- rear windows;
- tall cabinetry/opening.

Astra must not call a camera match complete merely because the path passes Living → Dining → Kitchen. Timing, field of view and composition must be matched against these anchors.

See also:

- `docs/09-MATT-SHUMER-ASTRA-WORKFLOW.md`
- `references/solace/REFERENCE-MANIFEST.json`
