# 06 — Geospatial Strategy

## Goal

Create geographically recognizable, visually convincing world bases without pretending to be a survey, cadastral model, BIM model or engineering dataset.

## Quality target

```text
PERCEPTUAL FIDELITY
+
GEOGRAPHIC COHERENCE
+
RECOGNIZABILITY
+
VISUAL QUALITY
```

## Production split

### Tier A — Hero geography / identity anchors
High fidelity where practical:
- coastline;
- port / marina;
- lagoons / major water;
- major promenades;
- iconic landmarks;
- defining terrain silhouettes.

### Tier B — Structural geography
Coherent / approximately faithful:
- principal roads;
- district/block structure;
- major green corridors;
- coast-to-city relationships.

### Tier C — Supporting fabric
Procedural / plausible:
- secondary buildings;
- generic façades;
- minor props;
- generic vegetation;
- non-iconic roofs.

## Preferred base sources

Open/owned data should establish editable geometry:
- OpenStreetMap;
- Overture Maps where useful;
- DEM/terrain sources;
- open tiles / OpenMapTiles / OpenFreeMap where appropriate;
- owned mapping code.

## Google Photorealistic 3D Tiles

Use as a **separate visualization / human-reference / geographic QA layer** under current Google Maps Platform terms.

Do not use it as the source for:
- automatic geometry extraction;
- tracing into owned meshes;
- machine-derived geodata;
- offline asset harvesting.

Our owned `3DTilesRendererJS` provides a practical route for compliant visualization experiments.

## Mini Skyline reference

https://miniskyline.com/es/faq

Useful capability pattern:

```text
SELECT AREA
→ LOAD GEOGRAPHIC LAYERS
→ GENERATE 3D BASE
→ EDIT / CORRECT
→ EXPORT
```

The project should reproduce this capability pattern with owned/open components where practical rather than depend on Mini Skyline.

## First proof

Compare three narrow paths on one bounded area:

### Path A — `map3d`
OSM → 3D buildings/roads → GLB.

### Path B — Blosm
OSM/terrain → Blender-native scene.

### Path C — `3DTilesRendererJS`
Google Photorealistic/3D Tiles → live visual reference.

The expected outcome may be hybrid rather than one winner:
- one geometry generator;
- one Blender authoring route;
- one visual-reference route.

## Proposed `geo_manifest.json`

```json
{
  "area_id": "torrevieja-core-v0",
  "bbox": [],
  "crs": "WGS84",
  "sources": [],
  "terrain": {},
  "roads": [],
  "buildings": [],
  "water": [],
  "vegetation": [],
  "pois": [],
  "hero_assets": [],
  "licenses": [],
  "attribution": [],
  "fidelity": {
    "identity_anchors": "high",
    "structural_geography": "coherent",
    "supporting_fabric": "procedural"
  }
}
```

## Relationship to WORLD-COSTA-BLANCA

This LAB owns the generic technical experiment.

`WORLD-COSTA-BLANCA` may consume a successful geospatial pipeline later, but product-specific world logic, buyer systems, storytelling and geographic presentation remain in that repository.
