import asyncio
import base64
import json
import os
import subprocess
from pathlib import Path
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

ROOT = Path(__file__).resolve().parent
PROMPT = "Create exactly one cube named LAB_TEST_CUBE. Dimensions exactly 2m x 2m x 2m. Do not modify any object other than LAB_TEST_CUBE. Keep Cube, Camera and Light unchanged. After creation inspect LAB_TEST_CUBE, capture a new viewport screenshot, compare before vs after and verify that the only intentional scene change is the addition of LAB_TEST_CUBE."
SNAPSHOT = '''import bpy
import json
s = bpy.context.scene
print(json.dumps({'scene': s.name, 'units': [s.unit_settings.system, s.unit_settings.scale_length, s.unit_settings.length_unit], 'camera': s.camera.name if s.camera else None, 'active': bpy.context.view_layer.objects.active.name if bpy.context.view_layer.objects.active else None, 'objects': {o.name: {'type': o.type, 'location': list(o.location), 'rotation': list(o.rotation_euler), 'rotation_mode': o.rotation_mode, 'scale': list(o.scale), 'dimensions': list(o.dimensions), 'matrix_world': [list(r) for r in o.matrix_world], 'selected': o.select_get(), 'hide_viewport': o.hide_viewport, 'hide_render': o.hide_render, 'visible': o.visible_get(), 'data': o.data.name if o.data else None, 'parent': o.parent.name if o.parent else None, 'collections': [c.name for c in o.users_collection], 'materials': [m.name if m else None for m in o.data.materials] if o.type == 'MESH' else [], 'vertices': [list(v.co) for v in o.data.vertices] if o.type == 'MESH' else [], 'faces': [list(p.vertices) for p in o.data.polygons] if o.type == 'MESH' else [], 'lens': o.data.lens if o.type == 'CAMERA' else None, 'energy': o.data.energy if o.type == 'LIGHT' else None} for o in s.objects}}, indent=2))
'''
CREATE = '''import bpy
import json
assert bpy.context.mode == 'OBJECT', 'Object mode required'
assert bpy.data.objects.get('LAB_TEST_CUBE') is None, 'LAB_TEST_CUBE already exists; no mutation performed'
assert bpy.context.scene.unit_settings.scale_length == 1.0, 'Expected unit scale 1'
mesh = bpy.data.meshes.new('LAB_TEST_CUBE_MESH')
mesh.from_pydata([(-1,-1,-1), (1,-1,-1), (1,1,-1), (-1,1,-1), (-1,-1,1), (1,-1,1), (1,1,1), (-1,1,1)], [], [(0,3,2,1), (4,5,6,7), (0,1,5,4), (1,2,6,5), (2,3,7,6), (3,0,4,7)])
mesh.update()
obj = bpy.data.objects.new('LAB_TEST_CUBE', mesh)
bpy.context.scene.collection.objects.link(obj)
obj.location = (0.0, 4.0, 0.0)
bpy.context.view_layer.update()
print(json.dumps({'created': obj.name, 'position': list(obj.location), 'rotation': list(obj.rotation_euler), 'scale': list(obj.scale), 'dimensions': list(obj.dimensions)}))
'''

async def main():
    cfg = json.loads(subprocess.check_output(['cmd','/c','codex','mcp','get','blender-astra-lab','--json'], text=True))['transport']
    assert cfg['env']['BLENDER_MCP_SAFE_MODE'] == '1'
    async with stdio_client(StdioServerParameters(command=cfg['command'], args=cfg['args'], env={**os.environ, **cfg['env']})) as (r,w):
        async with ClientSession(r,w) as session:
            init = await session.initialize()
            (ROOT/'initialize.json').write_text(init.model_dump_json(indent=2), encoding='utf-8')
            async def call(label, name, args):
                result = await session.call_tool(name, {**args, 'user_prompt': PROMPT})
                if name == 'get_viewport_screenshot':
                    for b in result.content:
                        if b.type == 'image': (ROOT/(label+'.png')).write_bytes(base64.b64decode(b.data))
                    saved = {'isError': result.isError, 'types': [b.type for b in result.content], 'text': [b.text for b in result.content if b.type == 'text']}
                    (ROOT/(label+'.json')).write_text(json.dumps(saved,indent=2),encoding='utf-8')
                else:
                    (ROOT/(label+'.json')).write_text(result.model_dump_json(indent=2),encoding='utf-8')
                assert not result.isError, str(result)
                if name == 'execute_blender_code':
                    value = '\n'.join(b.text for b in result.content if b.type == 'text')
                    assert value.startswith('Code executed successfully:'), value
                    print(label + ': SUCCESS', flush=True)
                    return json.loads(value.split(':',1)[1])
                print(label + ': SUCCESS', flush=True)
                return result
            before = await call('before-state','execute_blender_code',{'code': SNAPSHOT})
            assert 'LAB_TEST_CUBE' not in before['objects']
            await call('before-viewport','get_viewport_screenshot',{'max_size':1600})
            created = await call('creation','execute_blender_code',{'code': CREATE})
            after = await call('after-state','execute_blender_code',{'code': SNAPSHOT})
            comparison = {'added': sorted(set(after['objects'])-set(before['objects'])), 'removed': sorted(set(before['objects'])-set(after['objects'])), 'changed_preexisting': [n for n,v in before['objects'].items() if after['objects'].get(n)!=v], 'scene_settings_unchanged': all(before[k]==after[k] for k in ('scene','units','camera','active')), 'cube': after['objects'].get('LAB_TEST_CUBE')}
            (ROOT/'comparison.json').write_text(json.dumps(comparison,indent=2),encoding='utf-8')
            await call('object-info','get_object_info',{'object_name':'LAB_TEST_CUBE'})
            await call('after-viewport','get_viewport_screenshot',{'max_size':1600})
            assert comparison['added']==['LAB_TEST_CUBE'] and not comparison['removed'] and not comparison['changed_preexisting'] and comparison['scene_settings_unchanged']
            assert comparison['cube']['dimensions']==[2.0,2.0,2.0]
            print(json.dumps(comparison,indent=2),flush=True)

asyncio.run(main())
