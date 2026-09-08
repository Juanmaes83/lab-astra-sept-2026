"""Final bounded critic orders: chair clearance and reflection balance."""
import bpy
from pathlib import Path
BASE=Path(__file__).resolve().parent;s=bpy.context.scene
target=BASE/'photoreal-work/assembly_r12.blend'
assert not target.exists()
assert bpy.data.filepath.endswith('assembly_r11.blend')
for o in s.objects:
    if o.name.startswith('PHERO_Sling armchair') and o.type=='EMPTY':
        o.location.x=10.55;o.location.y=12.68
# Art-directed reflection exposure of the same licensed environment, not source imagery.
nt=s.world.node_tree
bg=next(n for n in nt.nodes if n.type=='BACKGROUND')
strength=bg.inputs['Strength'].default_value
lp=nt.nodes.new('ShaderNodeLightPath')
mul=nt.nodes.new('ShaderNodeMath');mul.operation='MULTIPLY';mul.inputs[1].default_value=strength*1.2
add=nt.nodes.new('ShaderNodeMath');add.operation='ADD';add.inputs[1].default_value=strength
nt.links.new(lp.outputs['Is Glossy Ray'],mul.inputs[0]);nt.links.new(mul.outputs[0],add.inputs[0]);nt.links.new(add.outputs[0],bg.inputs['Strength'])
s['reflection_exposure_note']='Same CC0 forest environment, glossy-ray strength 2.2x for reference look; reconstructed/art-directed.'
bpy.ops.wm.save_as_mainfile(filepath=str(target),compress=True)
