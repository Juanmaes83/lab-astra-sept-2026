import asyncio
import base64
import json
import os
import subprocess
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

ROOT = Path(__file__).resolve().parent
PROMPT = "READ ONLY: Inspect the currently open Blender scene. Do not modify anything. Report all scene objects, their transforms and dimensions when available, and whether the Blender MCP connection succeeds. Then capture one viewport screenshot."

async def main():
    config = json.loads(subprocess.check_output(["cmd", "/c", "codex", "mcp", "get", "blender-astra-lab", "--json"], text=True))
    transport = config["transport"]
    params = StdioServerParameters(command=transport["command"], args=transport["args"], env={**os.environ, **transport["env"]})
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            init = await session.initialize()
            (ROOT / "initialize.json").write_text(init.model_dump_json(indent=2), encoding="utf-8")
            print("MCP initialize: SUCCESS", flush=True)
            async def call(name, args):
                result = await session.call_tool(name, args)
                (ROOT / (name + ".json")).write_text(result.model_dump_json(indent=2), encoding="utf-8")
                print(name, result.model_dump_json(), flush=True)
                return result
            scene = await call("get_scene_info", {"user_prompt": PROMPT})
            if scene.isError or any("Error getting scene info" in getattr(c, "text", "") for c in scene.content):
                return
            code = "import bpy\nimport json\ns = bpy.context.scene\nprint(json.dumps({'scene': s.name, 'units': {'system': s.unit_settings.system, 'scale_length': s.unit_settings.scale_length, 'length_unit': s.unit_settings.length_unit}, 'camera': s.camera.name if s.camera else None, 'objects': [{'name': o.name, 'type': o.type, 'location': list(o.location), 'rotation_mode': o.rotation_mode, 'rotation_euler_radians': list(o.rotation_euler), 'scale': list(o.scale), 'dimensions': list(o.dimensions), 'matrix_world': [list(row) for row in o.matrix_world], 'hide_viewport': o.hide_viewport, 'visible': o.visible_get()} for o in s.objects]}, indent=2))"
            await call("execute_blender_code", {"code": code, "user_prompt": PROMPT})
            shot = await session.call_tool("get_viewport_screenshot", {"max_size": 1600, "user_prompt": PROMPT})
            for block in shot.content:
                if block.type == "image":
                    path = ROOT / "viewport.png"
                    path.write_bytes(base64.b64decode(block.data))
                    print("get_viewport_screenshot: SUCCESS " + str(path), flush=True)
                elif block.type == "text":
                    print(block.text, flush=True)
            (ROOT / "screenshot-result.json").write_text(json.dumps({'isError': shot.isError, 'content_types': [b.type for b in shot.content], 'text': [b.text for b in shot.content if b.type == 'text']}, indent=2), encoding="utf-8")

asyncio.run(main())
