# F2-A Gate 1A — PASS

Observed 2026-09-07. Read-only inspection via the configured `blender-astra-lab` stdio MCP server, with `BLENDER_MCP_SAFE_MODE=1`. Blender handshake reported 5.2.1 LTS, addon protocol 5, localhost:9876.

## Tool results

- MCP initialize: SUCCESS (`initialize.json`).
- `get_scene_info`: SUCCESS, `isError=false`, three objects (`get_scene_info.json`).
- `execute_blender_code`: SUCCESS, `isError=false`; only queried bpy scene properties and printed JSON (`execute_blender_code.json`).
- `get_viewport_screenshot`: SUCCESS, one PNG image, `isError=false` (`screenshot-result.json`, `viewport.png`).
- Visual inspection: PASS. The captured viewport shows one selected cube centered at the axis intersection, a camera wireframe to the left, and a light icon above/right. This matches the three reported scene objects. Exact numeric transforms are established by scene data, not measurable from this perspective screenshot.

Scene: `Scene`. Units: METRIC, METERS, scale_length=1. Active scene camera: `Camera`. All objects report visible=true and hide_viewport=false.

| Object | Type | Location XYZ (m) | Euler XYZ (radians) | Scale XYZ | Dimensions XYZ (m) |
| --- | --- | --- | --- | --- | --- |
| Cube | MESH | 0, 0, 0 | 0, 0, 0 | 1, 1, 1 | 2, 2, 2 |
| Light | LIGHT | 4.076245, 1.005454, 5.903862 | 0.650328, 0.055217, 1.866391 | 1, 1, 1 | 0, 0, 0 |
| Camera | CAMERA | 7.358891, -6.925791, 4.958309 | 1.109319, 0, 0.814928 | 1, 1, 1 | 0, 0, 0 |

Zero dimensions for camera/light are Blender's reported non-mesh dimensions, not their viewport icon sizes. Full precision and world matrices are retained in `execute_blender_code.json`.

No scene object was created or modified; no blend file was saved. Gate 1B was not started. `inspect_mcp.py` is the evidence-producing MCP client, not a replacement server.
