import bpy
s=bpy.context.scene
for o in s.objects:
    if o.type=='LIGHT' and o.name.startswith('V02_') and o.data.type=='AREA':
        o.visible_glossy=False
        o.visible_transmission=False
        o.visible_camera=False
    if o.name.startswith('VIDEO_Sofa_base'):
        o.location.z=.35
        o.dimensions.z=.24
s.cycles.device='GPU'
bpy.ops.wm.save_as_mainfile(filepath=bpy.data.filepath)
