import asyncio,json,os,subprocess
from pathlib import Path
from mcp import ClientSession,StdioServerParameters
from mcp.client.stdio import stdio_client
async def main():
    cfg=json.loads(subprocess.check_output(['cmd','/c','codex','mcp','get','blender-astra-lab','--json'],text=True))['transport']
    assert cfg['env']['BLENDER_MCP_SAFE_MODE']=='1'
    async with stdio_client(StdioServerParameters(command=cfg['command'],args=cfg['args'],env={**os.environ,**cfg['env']})) as(r,w):
        async with ClientSession(r,w) as s:
            await s.initialize()
            await s.call_tool('execute_blender_code',{'code':"import bpy\nbpy.ops.wm.open_mainfile(filepath='C:/Users/temp123/Documents/ChatGPT/lab-astra-sept-2026/outputs/solace/SOLACE_VIDEO_PROOF_v01.blend')",'user_prompt':'Produce SOLACE VIDEO PROOF v02 from v01 and the actual cinematic reference video; preserve v01.'})
            result=await s.call_tool('execute_blender_code',{'code':Path('outputs/solace/produce_video_v02.py').read_text(),'user_prompt':'Produce SOLACE VIDEO PROOF v02 from v01 and the actual cinematic reference video; preserve v01.'})
            for b in result.content:
                if b.type=='text':print(b.text)
asyncio.run(main())
