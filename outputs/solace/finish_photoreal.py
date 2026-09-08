"""Versioned final delivery settings and packed-file audit; never overwrite history."""
import bpy,json
from pathlib import Path
BASE=Path(__file__).resolve().parent;s=bpy.context.scene
target=BASE/'SOLACE_PHOTOREAL_GOAL_v01.blend'
assert not target.exists(),'Final version exists; do not overwrite.'
s.render.engine='CYCLES';s.cycles.device='GPU';s.cycles.samples=256;s.cycles.adaptive_threshold=.012;s.cycles.adaptive_min_samples=64;s.cycles.use_denoising=True
s.render.resolution_x=1920;s.render.resolution_y=1080;s.render.resolution_percentage=100;s.render.fps=30;s.render.fps_base=1;s.frame_start=1;s.frame_end=420
s.render.image_settings.file_format='PNG';s.render.image_settings.color_mode='RGB';s.render.image_settings.color_depth='8';s.render.filepath=str(BASE/'photoreal-work/final-frames')+'/'
s.render.use_file_extension=True;s.render.use_sequencer=False
s.camera.data.dof.use_dof=True;s.camera.data.dof.aperture_fstop=9
# Focus plane follows measured hero target distance, not arbitrary breathing.
for f in range(1,421):
    s.frame_set(f);sec=(f-1)/30
    from mathutils import Vector
    u=max(0,min(1,(sec-6)/2));u=u*u*(3-2*u)
    v=max(0,min(1,(sec-9)/2));v=v*v*(3-2*v)
    target_point=Vector((8.85,14.5,.8)).lerp(Vector((12.62,14.48,.85)),u).lerp(Vector((16.4,15.6,1.15)),v)
    s.camera.data.dof.focus_distance=(target_point-s.camera.location).length;s.camera.data.keyframe_insert('dof.focus_distance',frame=f)
for im in bpy.data.images:
    if im.users>0 and im.source=='FILE' and not im.packed_file:im.pack()
missing=[im.name for im in bpy.data.images if im.users>0 and im.source=='FILE' and not im.packed_file]
assert not missing,missing
s['photoreal_candidate']='Reference-grounded reconstruction after specialized workers and independent critique; HUMAN VISUAL REVIEW PENDING; not exact asset/BIM fidelity.'
s.frame_set(1);bpy.ops.wm.save_as_mainfile(filepath=str(target),compress=True)
data={'blend':target.name,'blender':bpy.app.version_string,'renderer':s.render.engine,'device':'RTX 5070 Ti / OPTIX','frames':420,'fps':30,'duration':14,'resolution':[1920,1080],'max_samples':256,'adaptive_threshold':.012,'minimum_samples':64,'denoising':True,'packed_images':sum(bool(i.packed_file) for i in bpy.data.images),'unpacked_required_images':missing,'human_review':'PENDING'}
(BASE/'photoreal_delivery.json').write_text(json.dumps(data,indent=2))
print('FINAL_VERSION_SAVED',json.dumps(data),flush=True)
