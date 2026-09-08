import bpy,sys
from pathlib import Path
BASE=Path(__file__).resolve().parent;sys.path.insert(0,str(BASE))
assert bpy.data.filepath.endswith('assembly_r07.blend')
target=BASE/'photoreal-work/assembly_r08.blend';assert not target.exists()
import photoreal_camera_clearance
photoreal_camera_clearance.build()
bpy.context.scene.frame_set(1);bpy.ops.wm.save_as_mainfile(filepath=str(target),compress=True)
print('R08_CAMERA_CLEARANCE',str(target))
