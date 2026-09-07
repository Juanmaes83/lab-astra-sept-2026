import json
import struct
from pathlib import Path
root=Path(__file__).resolve().parent
result=json.loads((root/'stage4-mcp.json').read_text(encoding='utf-8'))
text='\n'.join(b['text'] for b in result['content'] if b['type']=='text')
manifest=json.loads(text.split('GATE_MANIFEST=',1)[1].strip())
(root/'scene_manifest.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False),encoding='utf-8')
source=json.loads((root.parent.parent/'references/solace/source_manifest.json').read_text(encoding='utf-8'))
(root/'source_manifest.json').write_text(json.dumps(source,indent=2,ensure_ascii=False),encoding='utf-8')
glb=(root/'SOLACE_BLOCKOUT_v01.glb').read_bytes()
magic,version,length=struct.unpack_from('<4sII',glb)
assert magic==b'glTF' and version==2 and length==len(glb)
chunk_len,chunk_type=struct.unpack_from('<II',glb,12)
assert chunk_type==0x4E4F534A
doc=json.loads(glb[20:20+chunk_len])
names={n.get('name') for n in doc['nodes']}
expected={o['semantic_name'] for o in manifest['objects']}
assert expected.issubset(names),expected-names
assert not names.intersection({'Cube','Camera','Light','LAB_TEST_CUBE'})
assert all('uri' not in b for b in doc.get('buffers',[]))
report={'status':'PASS','file':'SOLACE_BLOCKOUT_v01.glb','size_bytes':len(glb),'glb_version':version,'nodes':len(doc['nodes']),'meshes':len(doc['meshes']),'cameras':len(doc.get('cameras',[])),'all_manifest_names_present':True,'unrelated_gate1_nodes':False,'external_buffer_dependencies':False,'method':'GLB header/chunk and semantic JSON inspection; not an independent rendered reimport'}
(root/'glb-verification.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report,indent=2))
