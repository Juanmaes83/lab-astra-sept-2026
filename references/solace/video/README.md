# SOLACE video references

This folder contains the two project-owned video references used by the active SOLACE photoreal benchmark.

## Authority

### `VIDEO_REFERENCIA_SOLACE_CINEMATIC_TARGET.mp4`
**AUTHORITATIVE CINEMATIC TARGET.**

Use it for:
- camera choreography;
- timing;
- framing;
- visible architecture;
- furnishings;
- material language;
- lighting;
- glazing/exterior relationship;
- atmosphere.

For the active benchmark, reproduce only the first continuous shot, approximately `00:00.000 → 00:13.967`, with the hard cut beginning around `00:14.000`.

### `VIDEO_REFERENCIA_SOLACE_BLENDER_PROCESS.mp4`
**PROCESS SUPPORT ONLY.**

It may help Astra understand Blender workflow or expected development depth, but it is never:
- geometry authority;
- camera authority;
- visual-style authority;
- SOLACE ground truth.

## Fixed frame anchors

Use the curated stills in:

`references/solace/stills/`

They are extracted from the authoritative cinematic target at `0.0 / 2.0 / 4.0 / 6.0 / 8.0 / 10.0 / 12.0 / 13.8 s` and should be used for measured camera/frame matching.

Do not overwrite generated outputs under `outputs/solace/`.
