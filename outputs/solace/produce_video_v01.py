import bpy
import math
import json
from mathutils import Vector

BASE='C:/Users/temp123/Documents/ChatGPT/lab-astra-sept-2026/'
assert bpy.data.filepath.endswith(('SOLACE_BLOCKOUT_v04.blend','SOLACE_VIDEO_PROOF_v01.blend'))
bpy.context.window_manager.windows[0].scene=bpy.data.scenes['SOLACE_GATE_2']
s=bpy.context.scene
bpy.ops.wm.save_as_mainfile(filepath=BASE+'outputs/solace/SOLACE_VIDEO_PROOF_v01.blend')
def mat(name,color,rough=.6,metal=0):
    m=bpy.data.materials.new(name);m.use_nodes=True
    m.node_tree.nodes.clear();p=m.node_tree.nodes.new('ShaderNodeBsdfPrincipled');out=m.node_tree.nodes.new('ShaderNodeOutputMaterial');m.node_tree.links.new(p.outputs[0],out.inputs[0]);p.inputs['Base Color'].default_value=(*color,1);p.inputs['Roughness'].default_value=rough;p.inputs['Metallic'].default_value=metal
    return m
plaster=mat('VIDEO_Warm_lime_plaster',(.72,.69,.60),.84)
stone=mat('VIDEO_Pale_limestone',(.58,.53,.43),.65)
oak=mat('VIDEO_Natural_oak',(.24,.13,.065),.48)
linen=mat('VIDEO_Ivory_linen',(.70,.67,.57),.95)
dark=mat('VIDEO_Bronze_frames',(.07,.065,.05),.32,.65)
leaf=mat('VIDEO_Courtyard_green',(.16,.26,.095),.9)
water=mat('VIDEO_Pool_water',(.12,.36,.37),.18)
glass=mat('VIDEO_Glass',(.88,.95,.94),.07)
glass_shader=next(n for n in glass.node_tree.nodes if n.type=='BSDF_PRINCIPLED')
glass_shader.inputs['Transmission Weight'].default_value=.97
glass_shader.inputs['IOR'].default_value=1.45
def assign(o,m):
    o.data.materials.clear();o.data.materials.append(m)
def cube(name,loc,dim,m,bevel=0):
    bpy.ops.mesh.primitive_cube_add(size=1,location=loc)
    o=bpy.context.object;o.name='VIDEO_'+name;o.dimensions=dim
    bpy.ops.object.transform_apply(location=False,rotation=False,scale=True)
    assign(o,m)
    if bevel:
        b=o.modifiers.new('Soft_edges','BEVEL');b.width=bevel;b.segments=3
        o.modifiers.new('Weighted_normals','WEIGHTED_NORMAL')
    return o
def cylinder(name,loc,radius,depth,m):
    bpy.ops.mesh.primitive_cylinder_add(vertices=32,radius=radius,depth=depth,location=loc)
    o=bpy.context.object;o.name='VIDEO_'+name;assign(o,m)
    bevel=o.modifiers.new('Soft_edges','BEVEL');bevel.width=.025;bevel.segments=2
    return o
for o in list(s.objects):
    if o.type!='MESH':continue
    if o.name.startswith('WALL_'):assign(o,plaster)
    elif o.name.startswith('WINDOW_'):assign(o,dark)
    elif o.name.startswith('SPACE_') and not any(k in o.name for k in ['GARDEN','LAWN','COURTYARD']):assign(o,stone)
    elif o.name=='POOL_LAP':assign(o,water)
    else:assign(o,leaf if o.name in ['SOLACE_SITE','SOLACE_HOUSE','SPACE_PLANTED_COURTYARD','SPACE_OPEN_LAWN','SPACE_PRIVATE_GARDEN'] else oak)
    if o.name.startswith('HELPER_') and o.name.endswith('_REFERENCE'):o.hide_render=True
# Thin unbroken visible social-zone finish, preserving the original blockout below.
cube('Social_floor',(12.8,13.95,.032),(12.7,5.95,.025),stone)
cube('Social_ceiling',(12.8,13.95,2.98),(12.7,5.95,.18),plaster)
cube('Entry_ceiling',(8.9,18.32,2.98),(3.0,2.68,.18),plaster)
# Living: low sofa, cushions, rug and coffee table; source-relative large silhouettes.
rug=mat('VIDEO_Woven_rug',(.45,.43,.36),1)
cube('Living_rug',(8.95,13.75,.060),(3.1,2.15,.025),rug,.03)
cube('Sofa_base',(8.85,14.50,.29),(3.0,.90,.43),linen,.09)
cube('Sofa_back',(8.85,14.87,.64),(3.0,.18,.64),linen,.07)
for x in [7.40,10.30]:cube('Sofa_arm',(x,14.50,.52),(.18,.92,.63),linen,.06)
for i in range(3):cube('Sofa_seat_'+str(i),(7.88+i*.96,14.43,.55),(.92,.70,.16),linen,.06)
table=cylinder('Coffee_table',(8.90,13.40,.37),.65,.10,oak);table.scale.y=.65
cylinder('Coffee_pedestal',(8.90,13.40,.19),.23,.33,dark)
# Dining aligned north/south as in source.
cube('Dining_table',(12.62,14.48,.77),(1.0,2.35,.12),oak,.05)
for y in [13.7,15.2]:cube('Dining_pedestal',(12.62,y,.39),(.55,.22,.72),oak,.025)
for row in range(3):
    y=13.65+row*.82
    for side in [-1,1]:
        x=12.62+side*.87
        cube('Dining_seat',(x,y,.47),(.47,.48,.12),linen,.06)
        cube('Dining_back',(x+side*.19,y,.75),(.10,.48,.52),oak,.04)
        for dx in [-.16,.16]:
            for dy in [-.16,.16]:cube('Chair_leg',(x+dx,y+dy,.24),(.045,.045,.43),dark,.01)
# Kitchen island and restrained north-wall cabinetry.
cube('Kitchen_island_base',(16.58,14.15,.46),(2.65,1.22,.89),oak,.025)
cube('Kitchen_island_stone',(16.58,14.15,.945),(2.83,1.37,.08),stone,.025)
for x in [15.7,16.55,17.4]:
    cylinder('Island_stool',(x,13.12,.65),.24,.10,oak)
    cylinder('Stool_leg',(x,13.12,.32),.04,.60,dark)
for i in range(6):
    x=14.80+i*.65
    cube('Kitchen_base_'+str(i),(x,16.50,.46),(.63,.62,.9),oak,.015)
cube('Kitchen_counter',(16.42,16.49,.95),(3.9,.70,.08),stone,.018)
cube('Kitchen_splash',(16.42,16.77,1.31),(3.9,.035,.65),stone)
for i in range(3):cube('Kitchen_upper_'+str(i),(15.02+i*.70,16.62,2.2),(.68,.36,.78),oak,.012)
cube('Tall_storage',(18.52,16.35,1.35),(.68,.83,2.7),oak,.02)
cube('Oven_glass',(18.52,15.925,1.30),(.54,.025,.55),dark,.01)
cube('Cooktop',(17.55,16.39,1.002),(.7,.48,.012),dark,.01)
cube('Sink_dark_basin',(15.10,16.40,1.002),(.55,.40,.014),dark,.035)
cube('Tap_stem',(15.10,16.67,1.16),(.035,.035,.35),dark,.01)
cube('Tap_spout',(15.10,16.58,1.32),(.035,.22,.035),dark,.01)
# Real glazed openings visible from the social area and garden beyond.
for name in ['LIVING_COURTYARD','DINING_KITCHEN_COURTYARD','NORTH_SOCIAL']:
    sill=bpy.data.objects['WINDOW_'+name];length=sill.dimensions.x
    x,y,z=sill.location
    cube('Glass_'+name,(x,y,1.42),(length,.025,2.65),glass)
    cube('Frame_head_'+name,(x,y,2.78),(length,.065,.08),dark)
    n=max(1,round(length/1.5))
    for i in range(n+1):cube('Mullion_'+name,(x-length/2+i*length/n,y,1.42),(.04,.065,2.7),dark)
# Garden is kept simple; only large forms visible through glazing.
for i,(x,y,r) in enumerate([(9,4.3,1.15),(15.5,3.7,.8)]):
    cylinder('Courtyard_trunk_'+str(i),(x,y,.85),.09,1.7,oak)
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=2,radius=r,location=(x,y,2.0))
    o=bpy.context.object;o.name='VIDEO_Courtyard_canopy_'+str(i);assign(o,leaf)
# Daylight only plus large soft fill; no elaborate lighting rig.
s.world.use_nodes=True
wn=s.world.node_tree.nodes;wn.clear();out=wn.new('ShaderNodeOutputWorld');bg=wn.new('ShaderNodeBackground');bg.inputs['Color'].default_value=(.65,.77,1,1);bg.inputs['Strength'].default_value=.35;s.world.node_tree.links.new(bg.outputs[0],out.inputs[0])
ld=bpy.data.lights.new('VIDEO_Sun','SUN');ld.energy=2.3;ld.angle=.12
lo=bpy.data.objects.new('VIDEO_Sun',ld);s.collection.objects.link(lo);lo.rotation_euler=(math.radians(28),math.radians(-25),math.radians(-25))
for name,loc,energy,size,target in [('Courtyard_fill',(12.7,8,5.8),1600,8,(12.7,14,1)),('Ceiling_bounce',(12.7,14.1,2.78),450,8,(12.7,14,0))]:
    ld=bpy.data.lights.new('VIDEO_'+name,'AREA');ld.energy=energy;ld.shape='DISK';ld.size=size
    lo=bpy.data.objects.new('VIDEO_'+name,ld);s.collection.objects.link(lo);lo.location=loc;lo.rotation_euler=(Vector(target)-lo.location).to_track_quat('-Z','Y').to_euler()
# One continuous eye-level move in the clear southern strip of the social bar.
cd=bpy.data.cameras.new('VIDEO_Walkthrough');cam=bpy.data.objects.new('VIDEO_Walkthrough',cd);s.collection.objects.link(cam);s.camera=cam
cd.lens=22;cd.sensor_width=36;cd.clip_start=.05;cd.clip_end=150
cam.rotation_mode='QUATERNION'
s.render.fps=24;s.frame_start=1;s.frame_end=288
for frame in range(1,289):
    t=(frame-1)/287
    u=t*t*(3-2*t)
    cam.location=(7.35+9.0*u,12.05+.12*math.sin(t*math.pi),1.62)
    target=Vector((9.15+8.45*u,14.6+.55*u,1.22))
    cam.rotation_quaternion=(target-cam.location).to_track_quat('-Z','Y')
    cam.keyframe_insert('location',frame=frame);cam.keyframe_insert('rotation_quaternion',frame=frame)
# Eevee is the proof renderer; no dependency on a configured Cycles device.
s.render.engine='BLENDER_EEVEE'
if hasattr(s,'eevee'):s.eevee.taa_render_samples=16
s.render.resolution_x=1920;s.render.resolution_y=1080;s.render.resolution_percentage=100
s.view_settings.view_transform='AgX';s.view_settings.exposure=0
s.render.image_settings.file_format='PNG'
s.render.filepath=BASE+'outputs/solace/video-proof-frames/'
s['video_proof']='12s/24fps; no walkthrough reference available; trajectory and finishes estimated from plan'
s.frame_set(1)
bpy.ops.wm.save_as_mainfile(filepath=BASE+'outputs/solace/SOLACE_VIDEO_PROOF_v01.blend')
print(json.dumps({'production':'ready','renderer':s.render.engine,'frames':288,'fps':24,'resolution':[1920,1080],'objects':len(s.objects)}))
