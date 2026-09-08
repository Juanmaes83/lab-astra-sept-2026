import bpy
import math
import random
import json
from mathutils import Vector
BASE='C:/Users/temp123/Documents/ChatGPT/lab-astra-sept-2026/'
s=bpy.data.scenes['SOLACE_GATE_2'];bpy.context.window_manager.windows[0].scene=s
assert bpy.data.filepath.endswith('SOLACE_VIDEO_PROOF_v01.blend')
bpy.ops.wm.save_as_mainfile(filepath=BASE+'outputs/solace/SOLACE_VIDEO_PROOF_v02.blend')
random.seed(21)
def mat(name,c,r=.6,metal=0):
    m=bpy.data.materials.new('V02_'+name);m.use_nodes=True;m.node_tree.nodes.clear()
    p=m.node_tree.nodes.new('ShaderNodeBsdfPrincipled');o=m.node_tree.nodes.new('ShaderNodeOutputMaterial');m.node_tree.links.new(p.outputs[0],o.inputs[0]);p.inputs['Base Color'].default_value=(*c,1);p.inputs['Roughness'].default_value=r;p.inputs['Metallic'].default_value=metal
    return m,p
oak,p=mat('Smoked_honey_oak',(.28,.16,.075),.42)
n=oak.node_tree.nodes;l=oak.node_tree.links
tex=n.new('ShaderNodeTexNoise');tex.inputs['Scale'].default_value=3;tex.inputs['Detail'].default_value=3
coord=n.new('ShaderNodeTexCoord');scale=n.new('ShaderNodeVectorMath');scale.operation='MULTIPLY';scale.inputs[1].default_value=(2,65,5);l.new(coord.outputs['Generated'],scale.inputs[0]);l.new(scale.outputs[0],tex.inputs['Vector'])
ramp=n.new('ShaderNodeValToRGB');ramp.color_ramp.elements[0].color=(.12,.055,.025,1);ramp.color_ramp.elements[1].color=(.38,.23,.12,1);l.new(tex.outputs['Fac'],ramp.inputs[0]);l.new(ramp.outputs[0],p.inputs['Base Color'])
bump=n.new('ShaderNodeBump');bump.inputs['Strength'].default_value=.13;bump.inputs['Distance'].default_value=.008;l.new(tex.outputs['Fac'],bump.inputs['Height']);l.new(bump.outputs[0],p.inputs['Normal'])
plaster,p=mat('Warm_plaster',(.53,.46,.36),.85)
noise=plaster.node_tree.nodes.new('ShaderNodeTexNoise');noise.inputs['Scale'].default_value=180
bump=plaster.node_tree.nodes.new('ShaderNodeBump');bump.inputs['Strength'].default_value=.09;bump.inputs['Distance'].default_value=.007;plaster.node_tree.links.new(noise.outputs['Fac'],bump.inputs['Height']);plaster.node_tree.links.new(bump.outputs[0],p.inputs['Normal'])
linen,p=mat('Soft_cream_weave',(.68,.63,.51),.93);p.inputs['Sheen Weight'].default_value=.3
noise=linen.node_tree.nodes.new('ShaderNodeTexNoise');noise.inputs['Scale'].default_value=230
bump=linen.node_tree.nodes.new('ShaderNodeBump');bump.inputs['Strength'].default_value=.18;bump.inputs['Distance'].default_value=.003;linen.node_tree.links.new(noise.outputs['Fac'],bump.inputs['Height']);linen.node_tree.links.new(bump.outputs[0],p.inputs['Normal'])
stone,p=mat('Ivory_stone',(.73,.69,.58),.32)
green,p=mat('Muted_sage_cushion',(.14,.20,.12),.9);p.inputs['Sheen Weight'].default_value=.35
bronze,p=mat('Brushed_bronze',(.13,.085,.04),.28,.75)
black,p=mat('Black_frames',(.018,.022,.021),.27,.5)
leaves,p=mat('Forest_leaf',(.06,.12,.065),.8)
bark,p=mat('Bark',(.075,.055,.035),.95)
glass,p=mat('Clear_glazing',(.96,.98,1),.025);p.inputs['Transmission Weight'].default_value=1;p.inputs['IOR'].default_value=1.45
ceramic,p=mat('Ceramic',(.82,.78,.64),.25)
emissive,p=mat('Warm_LED',(1,.70,.38),.4);p.inputs['Emission Color'].default_value=(1,.65,.28,1);p.inputs['Emission Strength'].default_value=5
def assign(o,m):o.data.materials.clear();o.data.materials.append(m)
def box(name,loc,dim,m,bev=.01):
    bpy.ops.mesh.primitive_cube_add(size=1,location=loc);o=bpy.context.object;o.name='V02_'+name;o.dimensions=dim;bpy.ops.object.transform_apply(location=False,rotation=False,scale=True);assign(o,m)
    if bev:
        b=o.modifiers.new('Rounded_edges','BEVEL');b.width=bev;b.segments=4;o.modifiers.new('Normals','WEIGHTED_NORMAL')
    return o
def cyl(name,loc,r,h,m):
    bpy.ops.mesh.primitive_cylinder_add(vertices=32,radius=r,depth=h,location=loc);o=bpy.context.object;o.name='V02_'+name;assign(o,m)
    b=o.modifiers.new('Edge','BEVEL');b.width=.014;b.segments=3
    for p in o.data.polygons:p.use_smooth=True
    return o
def sphere(name,loc,dim,m):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=24,ring_count=12,location=loc);o=bpy.context.object;o.name='V02_'+name;o.scale=dim;assign(o,m)
    for p in o.data.polygons:p.use_smooth=True
    return o
def beam(name,a,b,r,m):
    a=Vector(a);b=Vector(b);o=cyl(name,(a+b)/2,r,(b-a).length,m);o.rotation_euler=(b-a).to_track_quat('Z','Y').to_euler();return o
def hide(prefixes):
    for o in s.objects:
        if any(o.name.startswith(pre) for pre in prefixes):o.hide_render=True
# Update the existing visible architecture and furniture, retaining v01 layout.
for o in list(s.objects):
    if o.type!='MESH':continue
    if o.name.startswith('WALL_') or o.name in ['VIDEO_Social_ceiling','VIDEO_Entry_ceiling']:assign(o,plaster)
    elif any(k in o.name for k in ['Sofa','Dining_seat']):assign(o,linen)
    elif o.name.startswith('VIDEO_') and any(k in o.name for k in ['Kitchen_base','Kitchen_upper','Tall_storage','Dining_table','Dining_back','Dining_pedestal','Island_stool','Kitchen_island_base']):assign(o,oak)
    elif o.name.startswith('VIDEO_') and any(k in o.name for k in ['Glass_']):assign(o,glass)
    elif o.name.startswith('VIDEO_') and any(k in o.name for k in ['Kitchen_counter','Kitchen_island_stone']):assign(o,stone)
hide(['VIDEO_Sofa_back','VIDEO_Coffee_table','VIDEO_Coffee_pedestal','VIDEO_Kitchen_upper','VIDEO_Living_rug','WALL_NORTH_SOCIAL','VIDEO_Glass_NORTH_SOCIAL','VIDEO_Frame_head_NORTH_SOCIAL','VIDEO_Mullion_NORTH_SOCIAL'])
# Film-first north wall: sofa doorway and the two window masses actually seen in target.
box('Rear_west',(7.48,16.88,1.4),(2.1,.22,2.8),plaster)
box('Door_header',(9.05,16.88,2.68),(1.05,.22,.30),plaster)
box('Rear_middle',(10.01,16.88,1.4),(.85,.22,2.8),plaster)
box('Dining_window_sillwall',(12.16,16.88,.65),(3.46,.22,1.3),plaster)
box('Dining_window_header',(12.16,16.88,2.78),(3.46,.22,.20),plaster)
box('Kitchen_window_pier',(14.32,16.88,1.4),(.86,.22,2.8),plaster)
box('Kitchen_window_sillwall',(16.30,16.88,.55),(3.12,.22,1.1),plaster)
box('Kitchen_window_header',(16.30,16.88,2.78),(3.12,.22,.20),plaster)
box('Kitchen_tall_back',(18.47,16.88,1.4),(1.20,.22,2.8),plaster)
for name,cx,width,zmin in [('Dining',12.16,3.40,1.30),('Kitchen',16.30,3.06,1.10)]:
    box(name+'_window',(cx,16.88,(2.68+zmin)/2),(width,.015,2.68-zmin),glass,0)
    for x in [cx-width/2,cx,cx+width/2]:box(name+'_window_vertical',(x,16.86,(2.68+zmin)/2),(.045,.07,2.68-zmin),black)
    for z in [zmin,2.68]:box(name+'_window_horizontal',(cx,16.86,z),(width,.07,.045),black)
    box(name+'_sill',(cx,16.75,zmin-.03),(width+.10,.34,.07),stone)
for x in [8.51,9.59]:box('Door_lining',(x,16.73,1.25),(.055,.08,2.5),oak)
# Oak boards, subtle alternating tones and real narrow seams.
for row in range(28):
    y=11.05+row*.21
    for col in range(7):
        x=6.49+col*1.82+(row%3)*.45
        x1=max(6.45,x-1.82);x2=min(19.12,x)
        if x2>x1:box('Oak_floorboard',((x1+x2)/2,y,.068),(x2-x1-.003,.207,.024),oak,.003)
# Continuous base ensures no construction holes at staggered ends.
assign(bpy.data.objects['VIDEO_Social_floor'],oak)
# Softer sofa silhouette and walnut platform; separate pillowy back cushions.
assign(bpy.data.objects['VIDEO_Sofa_base'],oak)
bpy.data.objects['VIDEO_Sofa_base'].dimensions.z=.24;bpy.data.objects['VIDEO_Sofa_base'].location.z=.35
for i in range(3):
    o=box('Sofa_back_cushion',(7.88+i*.96,14.83,.85),(.94,.24,.62),linen,.115);o.rotation_euler.x=math.radians(-7)
for x,m in [(7.8,linen),(9.7,green)]:
    o=box('Throw_cushion',(x,14.48,.80),(.48,.19,.43),m,.095);o.rotation_euler.x=-.18;o.rotation_euler.y=.14
for x in [7.58,10.10]:
    for y in [14.2,14.80]:cyl('Sofa_foot',(x,y,.13),.045,.22,oak)
table=cyl('Oval_coffee_top',(8.9,13.22,.43),1,.07,stone);table.scale=(1.0,.49,1)
for x in [8.35,9.45]:cyl('Coffee_leg',(x,13.22,.23),.17,.39,oak)
for i in range(2):box('Coffee_book',(8.8+i*.32,13.18,.49+i*.015),(.26,.18,.035),green if i else oak,.006)
# Tall left bookcase, warm shelf strips: dominant source silhouette.
box('Library_back',(6.60,14.53,1.43),(.14,4.30,2.78),oak)
for y in [12.38,13.45,14.53,15.61,16.68]:box('Library_upright',(6.85,y,1.43),(.55,.05,2.78),oak)
for z in [.12,.70,1.32,1.94,2.60,2.80]:box('Library_shelf',(6.85,14.53,z),(.55,4.30,.055),oak)
for y in [12.90,14.00,15.06,16.1]:
    box('Library_low_door',(7.145,y,.39),(.045,.98,.54),oak)
    for z in [1.31,1.93,2.59]:box('Library_LED',(7.02,y,z),(.015,.93,.012),emissive,0)
bookmats=[mat('Book_'+str(i),c,.9)[0] for i,c in enumerate([(.26,.22,.15),(.14,.19,.17),(.53,.47,.34),(.13,.12,.09),(.35,.20,.12)])]
for shelf in [.74,1.36,1.98]:
    for i in range(23):
        y=12.5+i*.175;h=random.uniform(.18,.38)
        box('Library_book',(6.97,y,shelf+h/2),(.22,random.uniform(.045,.11),h),random.choice(bookmats),.003)
# Low open armchair beside sofa, matching a visible source silhouette.
box('Armchair_seat',(10.55,13.55,.48),(.67,.70,.15),green,.06)
box('Armchair_back',(10.55,13.88,.79),(.67,.12,.49),oak,.06)
for x in [10.19,10.91]:
    beam('Armchair_arm',(x,13.23,.70),(x,13.90,.70),.035,oak)
    for y in [13.3,13.83]:beam('Armchair_leg',(x,y,.10),(x,y,.67),.026,oak)
# Slimmer chair backs, wood frames rather than primitive dark posts.
for o in s.objects:
    if o.name.startswith('VIDEO_Dining_back'):o.dimensions.z=.27;o.location.z=.79
    if o.name.startswith('VIDEO_Chair_leg'):assign(o,oak)
# Waterfall stone island, cabinet fronts and hardware.
box('Island_waterfall_left',(15.19,14.15,.49),(.09,1.37,.92),stone,.015)
box('Island_waterfall_right',(17.97,14.15,.49),(.09,1.37,.92),stone,.015)
for i in range(6):
    x=14.8+i*.65
    box('Cabinet_handle',(x+.20,16.172,.70),(.025,.035,.20),bronze,.008)
    box('Island_front',(15.48+i*.40,13.532,.48),(.392,.018,.78),oak,.006)
# Small composition-defining table settings and island props.
for row in range(3):
    y=13.65+row*.82
    for side in [-1,1]:
        x=12.62+side*.32
        cyl('Dining_plate',(x,y,.847),.135,.022,ceramic)
        cyl('Dining_tumbler',(x-side*.1,y+.23,.90),.045,.11,glass)
        box('Cutlery',(x+side*.19,y,.845),(.018,.20,.012),bronze,.004)
cyl('Vase_base',(12.62,14.48,.98),.13,.31,ceramic)
sphere('Vase_body',(12.62,14.48,1.03),(.17,.17,.21),ceramic)
for i in range(4):beam('Vase_stem',(12.62,14.48,1.15),(12.62+(i-2)*.10,14.48,1.55+random.random()*.2),.005,oak)
cyl('Island_bowl',(16.00,14.30,1.04),.20,.07,oak)
for i in range(3):sphere('Bowl_fruit',(15.91+i*.08,14.30,1.095),(.065,.06,.045),green)
box('Cutting_board',(17.12,14.28,1.002),(.50,.30,.025),oak,.04)
sphere('Bread',(17.12,14.28,1.085),(.20,.10,.075),oak)
box('Coffee_machine',(16.25,16.48,1.22),(.32,.28,.42),black,.035)
box('Coffee_machine_front',(16.25,16.329,1.23),(.27,.012,.31),bronze,.01)
cyl('Coffee_cup',(16.25,16.25,1.04),.045,.065,ceramic)
# Source-style suspended linear light and gentle warm strips.
box('Dining_pendant',(12.62,14.48,2.36),(.13,2.25,.055),bronze)
box('Dining_pendant_diffuser',(12.62,14.48,2.329),(.09,2.18,.012),emissive,0)
for y in [13.6,15.35]:beam('Pendant_wire',(12.62,y,2.40),(12.62,y,2.89),.006,black)
box('Ceiling_linear',(12.6,16.52,2.878),(10.9,.025,.01),emissive,0)
# Exterior backdrop comprises true coarse 3D trees, visible through rear windows.
box('Exterior_ground',(12.5,25,-.04),(36,22,.12),leaves,.02)
box('Boundary_wall',(12.5,31,1.0),(36,.18,2.0),plaster)
for i in range(48):
    x=random.uniform(-3,29);y=random.uniform(19.5,30);h=random.uniform(4,7)
    beam('Forest_trunk',(x,y,0),(x+.15,y,h),random.uniform(.06,.13),bark)
    for j in range(3):
        dx=random.uniform(-.8,.8);dy=random.uniform(-.8,.8);z=h-1.7+j*.65
        beam('Forest_branch',(x,y,z-.5),(x+dx,y+dy,z+.3),.035,bark)
        bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=2,radius=1,location=(x+dx,y+dy,z+.5));o=bpy.context.object;o.name='V02_Foliage';o.scale=(random.uniform(.7,1.3),random.uniform(.6,1.2),random.uniform(.45,.9));assign(o,leaves)
# Lighting balances muted exterior daylight with warm interior, as observed.
for o in s.objects:
    if o.type=='LIGHT':o.hide_render=True
s.world.use_nodes=True
bg=next(n for n in s.world.node_tree.nodes if n.type=='BACKGROUND');bg.inputs['Color'].default_value=(.55,.68,.85,1);bg.inputs['Strength'].default_value=.32
def area(name,loc,target,power,size,color):
    ld=bpy.data.lights.new('V02_'+name,'AREA');ld.energy=power;ld.shape='DISK';ld.size=size;ld.color=color;o=bpy.data.objects.new('V02_'+name,ld);s.collection.objects.link(o);o.location=loc;o.rotation_euler=(Vector(target)-o.location).to_track_quat('-Z','Y').to_euler()
    o.visible_glossy=False;o.visible_transmission=False;o.visible_camera=False
area('Courtyard_daylight',(11,8,5),(11,14,1),1100,7,(.8,.88,1))
area('Rear_daylight',(13,19,5),(13,14,1),1400,8,(.75,.84,1))
area('Interior_warm',(12,14,2.75),(12,14,0),220,7,(1,.73,.46))
area('Pendant_light',(12.6,14.5,2.28),(12.6,14.5,0),80,2,(1,.76,.50))
ld=bpy.data.lights.new('V02_Sun','SUN');ld.energy=1.0;ld.angle=.15;lo=bpy.data.objects.new('V02_Sun',ld);s.collection.objects.link(lo);lo.rotation_euler=(.5,-.3,-.5)
# Reference begins outside, then moves forward and arcs right. Film timing manually inferred.
cam=s.camera;cam.animation_data_clear();cam.data.lens=27;cam.rotation_mode='QUATERNION'
keys=[(0,(8.85,8.55,1.58),(9.0,14.55,1.25)),(3,(8.90,11.50,1.58),(9.25,14.55,1.23)),(5.7,(10.15,12.05,1.58),(11.30,14.8,1.20)),(8.6,(12.90,12.10,1.58),(15.30,15.65,1.20)),(12.9583,(16.20,12.12,1.58),(16.80,16.20,1.25))]
def interp(values,i,t):
    a=Vector(values[max(0,i-1)]);b=Vector(values[i]);c=Vector(values[i+1]);d=Vector(values[min(len(values)-1,i+2)])
    return .5*((2*b)+(-a+c)*t+(2*a-5*b+4*c-d)*t*t+(-a+3*b-3*c+d)*t*t*t)
positions=[k[1] for k in keys];targets=[k[2] for k in keys]
for frame in range(1,313):
    sec=(frame-1)/24;i=next((j for j in range(len(keys)-1) if sec<=keys[j+1][0]),len(keys)-2);t=(sec-keys[i][0])/(keys[i+1][0]-keys[i][0]);t=max(0,min(1,t))
    cam.location=interp(positions,i,t);cam.rotation_quaternion=(interp(targets,i,t)-cam.location).to_track_quat('-Z','Y');cam.keyframe_insert('location',frame=frame);cam.keyframe_insert('rotation_quaternion',frame=frame)
# Glazing starts in front of camera; sliding entrance panels open before crossing.
for o in s.objects:
    if o.name.startswith('VIDEO_Glass_LIVING_COURTYARD'):
        x=o.location.x;o.keyframe_insert('location',frame=1);o.location.x=x+3.8;o.keyframe_insert('location',frame=58)
s.render.engine='CYCLES';s.cycles.samples=32;s.cycles.use_denoising=True;s.cycles.max_bounces=6;s.cycles.transparent_max_bounces=8
s.render.resolution_x=1920;s.render.resolution_y=1080;s.render.resolution_percentage=100;s.render.fps=24;s.frame_start=1;s.frame_end=312
s.view_settings.view_transform='AgX';s.view_settings.exposure=-.3
s.render.image_settings.file_format='PNG';s.render.filepath=BASE+'outputs/solace/video-proof-v02-frames/'
s.frame_set(1)
s['video_proof']='v02 target cinematic video 0-13s; manually estimated camera and materials; human review pending'
bpy.ops.wm.save_as_mainfile(filepath=BASE+'outputs/solace/SOLACE_VIDEO_PROOF_v02.blend')
print(json.dumps({'ready':True,'objects':len(s.objects),'renderer':'CYCLES','frames':312}))
