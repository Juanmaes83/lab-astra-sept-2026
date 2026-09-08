import bpy,math
from pathlib import Path
BASE=Path(__file__).resolve().parent;s=bpy.context.scene
assert bpy.data.filepath.endswith('assembly_r05.blend')
target=BASE/'photoreal-work/assembly_r06.blend';assert not target.exists()
n=s.world.node_tree.nodes;l=s.world.node_tree.links
mapping=next(q for q in n if q.type=='MAPPING');mapping.inputs['Rotation'].default_value=(math.radians(28),0,math.radians(35))
bg=next(q for q in n if q.type=='BACKGROUND');env=next(q for q in n if q.type=='TEX_ENVIRONMENT')
grade=n.new('ShaderNodeMixRGB');grade.blend_type='MULTIPLY';grade.inputs[0].default_value=1;grade.inputs[2].default_value=(.65,.82,1,1);l.new(env.outputs[0],grade.inputs[1]);l.new(grade.outputs[0],bg.inputs['Color']);bg.inputs['Strength'].default_value=.3
s.frame_set(1);bpy.ops.wm.save_as_mainfile(filepath=str(target),compress=True)
print('R06_ENVIRONMENT_FRAMING',str(target))
