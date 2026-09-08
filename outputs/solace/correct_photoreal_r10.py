"""Opening corrections from independent source comparison; preserve r09."""
import bpy
from pathlib import Path
from mathutils import Vector
BASE=Path(__file__).resolve().parent
s=bpy.context.scene;s.frame_set(1)
target=BASE/'photoreal-work/assembly_r10.blend'
assert not target.exists()
assert bpy.data.filepath.endswith('assembly_r09.blend')
cam=s.camera
corners=cam.data.view_frame(scene=s)
left=min(v.x for v in corners);right=max(v.x for v in corners)
z=corners[0].z
for o in s.objects:
    if o.name.startswith('VIDEO_Mullion_LIVING_COURTYARD'):
        o.hide_render=True
mat=bpy.data.materials['PHOTO_Satin_black_frame']
# Image-space measured divisions projected onto the existing facade plane.
# Reconstructed geometry, not survey-verified construction dimensions.
for i,u in enumerate([280,691,716,1114,1517]):
    ray=cam.matrix_world.to_quaternion()@Vector((left+(right-left)*u/1920,0,z))
    p=cam.matrix_world.translation+ray*((10.916-cam.matrix_world.translation.y)/ray.y)
    bpy.ops.mesh.primitive_cube_add(size=1,location=(p.x,10.916,1.6))
    o=bpy.context.object;o.name=f'R10_Source_facade_mullion_{i:02d}'
    o.dimensions=(.023 if i in (1,2) else .032,.065,3.15)
    bpy.ops.object.transform_apply(location=False,rotation=False,scale=True)
    o.data.materials.append(mat)
    b=o.modifiers.new('Frame_edge','BEVEL');b.width=.002;b.segments=3
    print('SOURCE_MULLION',u,tuple(o.location),flush=True)
glass=bpy.data.materials['PHOTO_Architectural_glass'].copy();glass.name='R10_Coated_facade_glass'
bs=next(n for n in glass.node_tree.nodes if n.type=='BSDF_PRINCIPLED')
bs.inputs['Coat Weight'].default_value=.55
bs.inputs['Coat IOR'].default_value=1.8
bs.inputs['Coat Roughness'].default_value=.025
for o in s.objects:
    if o.name.startswith(('VIDEO_Glass_LIVING_COURTYARD','VIDEO_Glass_DINING_KITCHEN_COURTYARD')):
        o.data.materials.clear();o.data.materials.append(glass)
    if o.name.startswith('PHERO_Sling armchair') and o.type=='EMPTY':
        o.location.x=10.30;o.location.y=13.25
    if o.name.startswith('PHOTO_Library_strip') and o.type=='LIGHT' and not o.hide_render:
        o.data.energy*=2.8
led=bpy.data.materials.new('R10_Warm_shelf_strip');led.use_nodes=True
bs=next(n for n in led.node_tree.nodes if n.type=='BSDF_PRINCIPLED')
bs.inputs['Base Color'].default_value=(.9,.62,.3,1)
bs.inputs['Emission Color'].default_value=(1,.61,.26,1)
bs.inputs['Emission Strength'].default_value=5
for i,h in enumerate([.91,1.52,2.13,2.74]):
    bpy.ops.mesh.primitive_cube_add(size=1,location=(7.12,13.455,h))
    o=bpy.context.object;o.name=f'R10_Library_visible_strip_{i}'
    o.dimensions=(.012,2.10,.012)
    bpy.ops.object.transform_apply(location=False,rotation=False,scale=True)
    o.data.materials.append(led)
s.frame_set(1)
bpy.ops.wm.save_as_mainfile(filepath=str(target),compress=True)
print('R10_SAVED',str(target),flush=True)
