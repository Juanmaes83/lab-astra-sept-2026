import bpy,sys,math
from pathlib import Path
BASE=Path(__file__).resolve().parent;sys.path.insert(0,str(BASE));s=bpy.context.scene
assert bpy.data.filepath.endswith('assembly_r06.blend')
target=BASE/'photoreal-work/assembly_r07.blend';assert not target.exists()
plaster=bpy.data.materials['PHOTO_Fine_warm_plaster']
def box(name,loc,dim):
    bpy.ops.mesh.primitive_cube_add(size=1,location=loc);o=bpy.context.object;o.name='R07_'+name;o.dimensions=dim;bpy.ops.object.transform_apply(location=False,rotation=False,scale=True);o.data.materials.append(plaster);return o
# Enclosed warm passage across the entire oblique sightline. No forest through service door.
box('Passage_rear',(21,18.4,1.6),(5.0,.24,3.2))
box('Passage_east',(22.5,17.6,1.6),(.24,3.5,3.2))
box('Passage_roof',(21,17.6,3.28),(5,3.5,.16))
box('Passage_floor',(21,17.6,.02),(5,3.5,.06))
head=bpy.data.objects['R02_Kitchen_door_header'];head.location.z=2.79;head.dimensions.z=.82
box('Passage_lintel_continuation',(19.8,16.35,2.85),(1.5,.24,.7))
ld=bpy.data.lights.new('R07_Passage_bounce','AREA');ld.energy=18;ld.color=(1,.70,.42);ld.shape='DISK';ld.size=1
lo=bpy.data.objects.new('R07_Passage_bounce',ld);s.collection.objects.link(lo);lo.location=(20.2,17.5,2.8)
n=s.world.node_tree.nodes;l=s.world.node_tree.links
bg=next(q for q in n if q.type=='BACKGROUND');link=bg.inputs['Color'].links[0];previous=link.from_socket;l.remove(link)
sat=n.new('ShaderNodeHueSaturation');sat.inputs['Saturation'].default_value=.55;l.new(previous,sat.inputs['Color']);l.new(sat.outputs[0],bg.inputs['Color']);bg.inputs['Strength'].default_value=.26
import photoreal_camera_final
photoreal_camera_final.build()
s.frame_set(1);bpy.ops.wm.save_as_mainfile(filepath=str(target),compress=True)
print('R07_FINAL_COMPOSITION_CORRECTIONS',str(target))
