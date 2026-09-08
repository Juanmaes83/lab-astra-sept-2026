"""Assemble specialized source-grounded passes from preserved v03. Run in Blender."""
import bpy,sys,json
from pathlib import Path
BASE=Path(__file__).resolve().parent
sys.path.insert(0,str(BASE))
assert bpy.data.filepath.endswith('SOLACE_VIDEO_PROOF_v03.blend')
s=bpy.context.scene;s.frame_set(1)
work=BASE/'photoreal-work';work.mkdir(exist_ok=True)
target=work/'assembly_r01.blend'
assert not target.exists(), 'Version exists: increment assembly version, do not overwrite.'

def resize(name,loc=None,dim=None):
    o=bpy.data.objects.get(name)
    if not o:return
    if loc:o.location=loc
    if dim:o.dimensions=dim
    bpy.context.view_layer.objects.active=o
    o.select_set(True);bpy.ops.object.transform_apply(location=False,rotation=False,scale=True);o.select_set(False)

def shell():
    # Joint geometry/camera fit: these heights are reconstructed from source image ratios.
    for o in s.objects:o.select_set(False)
    for name in ['VIDEO_Social_ceiling','VIDEO_Entry_ceiling']:
        o=bpy.data.objects[name];o.location.z=3.29
    for o in s.objects:
        if o.name.startswith('V03_Visible_wing_roof'):o.location.z=3.29
        if o.name.startswith('V03_Ceiling_shadow_gap'):o.location.z=3.185
        if o.name=='V02_Ceiling_linear':o.location.z=3.18
    resize('V02_Rear_west',(7.38,16.88,1.6),(1.84,.22,3.2))
    resize('V02_Door_header',(9.05,16.88,2.925),(1.5,.22,.55))
    resize('V02_Rear_middle',(10.13,16.88,1.6),(.66,.22,3.2))
    for i,x in enumerate([8.30,9.80]):resize('V02_Door_lining'+('' if i==0 else '.001'),(x,16.73,1.325),(.055,.08,2.65))
    for name,cx,w,zmin,zmax in [('Dining',12.16,3.40,1.30,3.00),('Kitchen',16.30,3.06,1.10,3.10)]:
        resize('V02_'+name+'_window',(cx,16.88,(zmax+zmin)/2),(w,.015,zmax-zmin))
        for i,x in enumerate([cx-w/2,cx,cx+w/2]):resize('V02_'+name+'_window_vertical'+('' if i==0 else '.'+str(i).zfill(3)),(x,16.86,(zmax+zmin)/2),(.045,.07,zmax-zmin))
        for i,z in enumerate([zmin,zmax]):resize('V02_'+name+'_window_horizontal'+('' if i==0 else '.001'),(cx,16.86,z),(w,.07,.045))
        resize('V02_'+name+'_window_header',(cx,16.88,(3.2+zmax)/2),(w+.06,.22,3.2-zmax))
    for name in ['V02_Kitchen_window_pier','V02_Kitchen_tall_back']:
        o=bpy.data.objects[name];resize(name,(o.location.x,o.location.y,1.6),(o.dimensions.x,.22,3.2))
    # Static glazing; no unsupported panel-opening animation.
    for o in s.objects:
        if o.name.startswith('VIDEO_Glass_'):o.animation_data_clear()
        if o.name.startswith('VIDEO_Mullion_') and 'NORTH' not in o.name:resize(o.name,(o.location.x,o.location.y,1.6),(.04,.065,3.15))
        if o.name.startswith('VIDEO_Frame_head_') and 'NORTH' not in o.name:o.location.z=3.19
        if o.name.startswith('VIDEO_Glass_') and 'NORTH' not in o.name:resize(o.name,(o.location.x,o.location.y,1.60),(o.dimensions.x,.012,3.13))
    s.unit_settings.system='METRIC';s.unit_settings.scale_length=1

shell()
import photoreal_kitchen,photoreal_hero_assets,photoreal_look,photoreal_camera
photoreal_kitchen.build()
photoreal_hero_assets.build()
photoreal_look.build()
photoreal_camera.build()
s.render.engine='CYCLES';s.cycles.device='GPU';s.cycles.samples=192;s.cycles.use_adaptive_sampling=True;s.cycles.adaptive_threshold=.015;s.cycles.adaptive_min_samples=48;s.cycles.use_denoising=True
s.cycles.max_bounces=12;s.cycles.diffuse_bounces=5;s.cycles.glossy_bounces=5;s.cycles.transmission_bounces=10;s.cycles.transparent_max_bounces=12
s.render.resolution_x=1920;s.render.resolution_y=1080;s.render.resolution_percentage=100;s.render.fps=30;s.frame_start=1;s.frame_end=420
s.render.image_settings.file_format='PNG';s.render.filepath=str(work/'final-frames')+'/'
s.render.film_transparent=False
s['photoreal_truth']='RECONSTRUCTED_FROM_REFERENCE; camera fitted to image landmarks, physical dimensions remain estimated; HUMAN REVIEW PENDING'
s.frame_set(1)
bpy.ops.wm.save_as_mainfile(filepath=str(target),compress=True)
print('PHOTOREAL_ASSEMBLED',str(target),len(s.objects))
