import bpy,json
from pathlib import Path
s=bpy.context.scene
p=Path(__file__).parent/'photoreal_scene_inventory.json'
data={'file':bpy.data.filepath,'scene':s.name,'camera':s.camera.name,'objects':[{'name':o.name,'type':o.type,'location':list(o.location),'rotation':list(o.rotation_euler),'dimensions':list(o.dimensions),'hidden':o.hide_render,'materials':[m.name for m in o.data.materials if m] if hasattr(o.data,'materials') else []} for o in s.objects]}
p.write_text(json.dumps(data,indent=2))
print('INVENTORY',p,len(s.objects))
