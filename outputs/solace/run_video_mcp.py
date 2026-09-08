import asyncio,json,os,subprocess
from pathlib import Path
from mcp import ClientSession,StdioServerParameters
from mcp.client.stdio import stdio_client
async def main():
    cfg=json.loads(subprocess.check_output(['cmd','/c','codex','mcp','get','blender-astra-lab','--json'],text=True))['transport']
    assert cfg['env']['BLENDER_MCP_SAFE_MODE']=='1'
    code=Path('outputs/solace/produce_video_v01.py').read_text()
    async with stdio_client(StdioServerParameters(command=cfg['command'],args=cfg['args'],env={**os.environ,**cfg['env']})) as(r,w):
        async with ClientSession(r,w) as s:
            await s.initialize()
            result=await s.call_tool('execute_blender_code',{'code':code,'user_prompt':'Start from SOLACE_BLOCKOUT_v04.blend and produce one complete 10–14 second Living → Dining → Kitchen cinematic proof, preserve v04, save SOLACE_VIDEO_PROOF_v01.blend and render an MP4.'})
            Path('outputs/solace/video-production-mcp.json').write_text(result.model_dump_json(indent=2),encoding='utf-8')
            for b in result.content:
                if b.type=='text':print(b.text)
asyncio.run(main())
