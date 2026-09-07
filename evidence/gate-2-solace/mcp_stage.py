import asyncio
import json
import os
import subprocess
import sys
from pathlib import Path
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

ROOT = Path(__file__).resolve().parent
async def main():
    name = sys.argv[1]
    code = (ROOT/'blender_common.py').read_text(encoding='utf-8') + '\n' + (ROOT/(name+'.py')).read_text(encoding='utf-8')
    cfg = json.loads(subprocess.check_output(['cmd','/c','codex','mcp','get','blender-astra-lab','--json'],text=True))['transport']
    assert cfg['env']['BLENDER_MCP_SAFE_MODE']=='1'
    async with stdio_client(StdioServerParameters(command=cfg['command'],args=cfg['args'],env={**os.environ,**cfg['env']})) as (r,w):
        async with ClientSession(r,w) as s:
            await s.initialize()
            result = await s.call_tool('execute_blender_code',{'code':code,'user_prompt':'Build a recognisable SOLACE Architectural Blockout in Blender from the valid uploaded floorplan image. Use metric units and semantic names; capture review views; run compare, correct, recapture; export a GLB candidate only if geometry QA passes.'})
            (ROOT/(name+'-mcp.json')).write_text(result.model_dump_json(indent=2),encoding='utf-8')
            print(result.model_dump_json(indent=2))
            assert not result.isError
            assert any('Code executed successfully:' in getattr(b,'text','') for b in result.content)
asyncio.run(main())
