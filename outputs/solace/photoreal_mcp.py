"""Use the configured Safe Mode MCP; never register or reconfigure a server."""
import asyncio,json,os,subprocess,sys
from pathlib import Path
from mcp import ClientSession,StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    cfg=json.loads(subprocess.check_output(['cmd','/c','codex','mcp','get','blender-astra-lab','--json'],text=True))['transport']
    assert cfg['env']['BLENDER_MCP_SAFE_MODE']=='1'
    async with stdio_client(StdioServerParameters(command=cfg['command'],args=cfg['args'],env={**os.environ,**cfg['env']})) as(r,w):
        async with ClientSession(r,w) as session:
            await session.initialize()
            result=await session.call_tool('execute_blender_code',{'code':"import bpy,json\nprint(json.dumps({'file':bpy.data.filepath,'scene':bpy.context.scene.name,'version':bpy.app.version_string,'objects':len(bpy.context.scene.objects)}))",'user_prompt':'SOLACE photoreal reconstruction: inspect current working scene without changing it; production is performed in versioned background Blender instances.'})
            for b in result.content:
                if b.type=='text':print(b.text)
asyncio.run(main())
