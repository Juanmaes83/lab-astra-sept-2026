import bpy
from pathlib import Path
BASE=Path(__file__).resolve().parent
target=BASE/'photoreal-work/assembly_r11.blend'
assert not target.exists()
assert bpy.data.filepath.endswith('assembly_r10.blend')
for i,z in enumerate([1.285,1.905,2.565,2.765]):
    o=bpy.data.objects[f'R10_Library_visible_strip_{i}']
    o.location.z=z;o.location.x=7.105
bpy.ops.wm.save_as_mainfile(filepath=str(target),compress=True)
