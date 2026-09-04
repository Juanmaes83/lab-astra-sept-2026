# 03 — Source Repositories

Status: ACTIVE REGISTRY

## Owned primary technical sources

| Repository | Role | Priority |
|---|---|---:|
| `Juanmaes83/blender-mcp` | Blender control through MCP; current September LAB branch exists | P0 |
| `Juanmaes83/camera-to-blender` | image/photo → 3D generation → Blender ingestion pattern | P1 |
| `Juanmaes83/map3d` | OSM → 3D buildings/roads → GLB | P0 geospatial proof |
| `Juanmaes83/3DTilesRendererJS` | 3D Tiles / Google Photorealistic reference visualization | P0 geospatial proof |
| `Juanmaes83/Blosm-addon-for-Blender.-A-few-clicks-import-of-Google-3D-cities-OpenStreetMap` | Blender-native OSM/terrain/roads/buildings import patterns | P0 geospatial proof |
| `Juanmaes83/maptalks.js` | larger web 2D/3D runtime, vector tiles, 3D Tiles, GLTF | P1 after bounded proof |
| `Juanmaes83/terraink` | OSM/OpenMapTiles/OpenFreeMap/MapLibre layer and UI patterns | P1 research |
| `Juanmaes83/openfreemap` | open map stack candidate | P1 research |
| `Juanmaes83/WORLD-COSTA-BLANCA` | downstream consumer/product; geographic-world use case | CONSUMER |
| `Juanmaes83/ableton-mcp` | later sound/music/spatial-audio workflow | LATER |
| `Juanmaes83/codex-ios-assistant` | later remote monitoring/control patterns | LATER |

## External Blender / agent research

### `ahujasid/blender-mcp`
Primary upstream family for Blender MCP. Keep provenance when syncing owned fork.

### `seehiong/blender-mcp-bridge`
Research candidate for Streamable HTTP MCP bridge patterns.

### `arjun988/blender-skills`
Research candidate for Blender/archviz/director/lighting/rendering/export/QA skills.

### `RobLe3/cc-blender-skill`
Research candidate for chained Blender skills and reference-fit/QA loops.

### `webita/blender-codex-mcp`
Research candidate for Codex-specific Blender MCP integration patterns.

### `hassledzebra/codex_blender_mcp`
Secondary Codex/Blender integration reference.

## Product / workflow references

### Mini Skyline
https://miniskyline.com/es/faq

Role: product/workflow reference for:

```text
map selection
→ geographic layers
→ 3D generation
→ edit/correct
→ export
```

Not a required dependency.

## Google references

- https://developers.google.com/maps/documentation/tile/overview
- https://developers.google.com/maps/documentation/tile/3d-tiles
- https://developers.google.com/maps/documentation/tile/policies

Role: compliant visualization / geographic human reference / QA.

Do not make agent pipelines extract, trace or derive owned geometry from Google Photorealistic 3D Tiles.

## Selection rule

Do not integrate every repo.

For each capability:
1. choose one PRIMARY implementation;
2. keep alternatives as research/fallback;
3. record source path + commit before copying code;
4. prove the capability in a bounded slice before expanding.
