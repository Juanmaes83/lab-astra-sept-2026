# F2-A Gate 1B — PASS

Executed 2026-09-07 via configured `blender-astra-lab` MCP stdio server, Safe Mode=1. Blender 5.2.1 LTS, addon protocol 5; successful connection at localhost:9876.

Exactly one object added: LAB_TEST_CUBE, with its own mesh LAB_TEST_CUBE_MESH. Position XYZ=(0,4,0) metres; Euler XYZ=(0,0,0) radians; scale XYZ=(1,1,1); dimensions XYZ=(2,2,2) metres. Scene unit scale is 1. Geometry contains eight vertices and six quad faces.

## Exact results

- MCP initialize: SUCCESS (`initialize.json`).
- `execute_blender_code` before inspection, creation, after inspection: all SUCCESS, isError=false (`before-state.json`, `creation.json`, `after-state.json`).
- `get_object_info` LAB_TEST_CUBE: SUCCESS, isError=false (`object-info.json`).
- `get_viewport_screenshot` before and after: both SUCCESS, isError=false (`before-viewport.json`, `after-viewport.json`).
- Automated comparison: PASS (`comparison.json`): added=[LAB_TEST_CUBE], removed=[], changed_preexisting=[], scene_settings_unchanged=true.

Comparison covers all pre-existing objects' transforms, dimensions, world matrices, selection, visibility, data references, parenting, collection membership, mesh vertices/faces/materials, camera lens and light energy. Scene units, camera assignment and active object also remain equal. Cube, Camera and Light are unchanged in these observations. The creation code uses the data API only on the new mesh/object, preserving pre-existing object selection.

## Visual verification

Personally inspected both `before-viewport.png` and `after-viewport.png`. Before: one selected cube at the origin, camera left, light upper-right. After: the same view and original objects, plus a separate unselected cube to the right along positive Y. Both cubes are clearly visible. No corrections were necessary. Exact dimensions are verified from scene data; perspective appearance is consistent with it.

No blend file was saved or overwritten. No SOLACE work started. Evidence contains the MCP client `run_gate.py` and actual tool responses; no replacement MCP was created.
