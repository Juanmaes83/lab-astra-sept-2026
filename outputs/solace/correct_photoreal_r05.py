import bpy,math
from pathlib import Path
BASE=Path(__file__).resolve().parent;s=bpy.context.scene
assert bpy.data.filepath.endswith('assembly_r04.blend')
target=BASE/'photoreal-work/assembly_r05.blend';assert not target.exists()
c=bpy.data.collections['PHOTO_CC0_Pine_master']
# Source blend is a three-variant display, not one tree. Instance only one variant.
for o in list(c.objects):
    if not o.name.endswith('_a'):c.objects.unlink(o)
    else:o.location=(0,0,0)
c.instance_offset=(0,0,-.015484)
for i,o in enumerate(sorted([o for o in s.objects if o.name.startswith('PHOTO_CC0_Pine_')],key=lambda o:o.name)):
    height=[3.7,4.4,3.2,4.0,4.8,3.6,4.3,3.5][i]
    factor=height/1.299;o.scale=(factor*.74,factor*.74,factor)
    o.location.y=max(22.,o.location.y)
s.frame_set(1);bpy.ops.wm.save_as_mainfile(filepath=str(target),compress=True)
print('TREE_VARIANTS_CORRECTED',str(target),flush=True)
