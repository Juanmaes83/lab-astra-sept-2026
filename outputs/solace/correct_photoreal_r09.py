import bpy,bmesh
from pathlib import Path
BASE=Path(__file__).resolve().parent;s=bpy.context.scene
assert bpy.data.filepath.endswith('assembly_r08.blend')
target=BASE/'photoreal-work/assembly_r09.blend';assert not target.exists()
# Ray-cast audit identified the apparent loose panels as unfinished rows of v02 flooring.
oak=bpy.data.materials['PHOTO_Oiled_oak']
for row in range(28):
    start=17.41+(row%3)*.45;end=19.12
    bpy.ops.mesh.primitive_cube_add(size=1,location=((start+end)/2,11.05+row*.21,.068));o=bpy.context.object;o.name='R09_Completed_floor_row';o.dimensions=(end-start-.003,.207,.024);bpy.ops.object.transform_apply(location=False,rotation=False,scale=True);o.data.materials.append(oak)
    b=o.modifiers.new('Board_edge','BEVEL');b.width=.003;b.segments=3;o.modifiers.new('Normals','WEIGHTED_NORMAL')
# Clear near-fern leaves from the existing enclosed entry corridor.
o=bpy.data.objects['R02_Forest_ferns'];bm=bmesh.new();bm.from_mesh(o.data)
bad=[f for f in bm.faces if 7.1<f.calc_center_median().x<10.7 and f.calc_center_median().y<20.3]
bmesh.ops.delete(bm,geom=bad,context='FACES');bm.to_mesh(o.data);bm.free()
s.frame_set(1);bpy.ops.wm.save_as_mainfile(filepath=str(target),compress=True)
print('R09_TECHNICAL_FIXES',len(bad),'fern faces cleared',flush=True)
