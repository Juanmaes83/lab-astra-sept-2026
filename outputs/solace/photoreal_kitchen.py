"""Source-anchor kitchen detailing. Dimensions reconstructed, not construction verified."""
import bpy, math, random
from mathutils import Vector

def build():
    s=bpy.context.scene
    def mat(name,c,rough=.4,metal=0):
        m=bpy.data.materials.new('PK_'+name);m.use_nodes=True
        p=next(n for n in m.node_tree.nodes if n.type=='BSDF_PRINCIPLED');p.inputs['Base Color'].default_value=(*c,1);p.inputs['Roughness'].default_value=rough;p.inputs['Metallic'].default_value=metal
        return m
    oak=bpy.data.materials['V03_Rift_cut_vertical_oak'];stone=bpy.data.materials['V03_Honed_limestone'];steel=bpy.data.materials['V03_Brushed_steel'];black=bpy.data.materials['V03_Anodized_bronze_black'];ceramic=bpy.data.materials.get('V03_Warm_porcelain') or mat('Warm_porcelain',(.79,.76,.67),.24);glass=bpy.data.materials['V03_Low_iron_glass']
    bronze=mat('Satin_brass',(.31,.19,.072),.29,.78)
    bottle=mat('Bottle_green',(.025,.052,.022),.17);p=next(n for n in bottle.node_tree.nodes if n.type=='BSDF_PRINCIPLED');p.inputs['Transmission Weight'].default_value=.65;p.inputs['IOR'].default_value=1.48
    paper=mat('Cotton_label',(.65,.61,.48),.85)
    bread=mat('Baked_crust',(.36,.18,.065),.8)
    n=bread.node_tree.nodes;l=bread.node_tree.links;noise=n.new('ShaderNodeTexNoise');noise.inputs['Scale'].default_value=75;noise.inputs['Detail'].default_value=4;b=n.new('ShaderNodeBump');b.inputs['Distance'].default_value=.003;b.inputs['Strength'].default_value=.4;l.new(noise.outputs['Fac'],b.inputs['Height']);l.new(b.outputs[0],next(q for q in n if q.type=='BSDF_PRINCIPLED').inputs['Normal'])
    def assign(o,m):o.data.materials.clear();o.data.materials.append(m)
    def box(name,loc,dim,m,r=.004):
        bpy.ops.mesh.primitive_cube_add(size=1,location=loc);o=bpy.context.object;o.name='PK_'+name;o.dimensions=dim;bpy.ops.object.transform_apply(location=False,rotation=False,scale=True);assign(o,m)
        if r:
            b=o.modifiers.new('Machined_edge','BEVEL');b.width=r;b.segments=4;o.modifiers.new('Corner_normals','WEIGHTED_NORMAL')
        return o
    def lathe(name,loc,profile,m,segments=64):
        verts=[(r*math.cos(i*math.tau/segments),r*math.sin(i*math.tau/segments),z) for r,z in profile for i in range(segments)]
        faces=[]
        for j in range(len(profile)-1):
            for i in range(segments):faces.append((j*segments+i,j*segments+(i+1)%segments,(j+1)*segments+(i+1)%segments,(j+1)*segments+i))
        me=bpy.data.meshes.new(name);me.from_pydata(verts,[],faces);me.update();o=bpy.data.objects.new('PK_'+name,me);s.collection.objects.link(o);o.location=loc;assign(o,m)
        for f in me.polygons:f.use_smooth=True
        return o
    def rail(name,a,b,r,m):
        a=Vector(a);b=Vector(b);o=lathe(name,(a+b)/2,[(r,-(b-a).length/2),(r,(b-a).length/2)],m,24);o.rotation_euler=(b-a).to_track_quat('Z','Y').to_euler();return o
    def hide(pre):
        for o in s.objects:
            if o.name.startswith(pre):o.hide_render=True
    hide(('VIDEO_Oven','V03_Oven','V02_Island_front','V02_Island_bowl','V02_Cutting_board','V02_Bread','V02_Bowl_fruit','V02_Cabinet_handle','V03_Drawer_reveal','V03_Hob_ring'))
    # Source oven is below the hob, not inside the tall refrigerator.
    for o in s.objects:
        if o.name.startswith('VIDEO_Kitchen_base_'):
            o.dimensions.y=.58;o.location.y=16.51
    for x in [14.64,15.27,15.9,16.53,17.16,17.79]:
        if 17<x<17.5:continue
        box('Cabinet_front',(x,16.205,.54),(.617,.022,.755),oak,.002)
        rail('Pull',(x+.19,16.17,.51),(x+.19,16.17,.71),.009,bronze)
    box('Oven_recess',(17.22,16.18,.54),(.61,.04,.68),black)
    box('Oven_glass',(17.22,16.15,.49),(.53,.016,.43),black,.014)
    box('Oven_steel_trim',(17.22,16.135,.79),(.58,.019,.1),steel)
    rail('Oven_pull',(17.0,16.09,.72),(17.44,16.09,.72),.011,steel)
    for x in [17.02,17.42]:
        o=lathe('Oven_dial',(x,16.10,.79),[(.024,0),(.024,.018)],black);o.rotation_euler.x=math.pi/2
    hob=bpy.data.objects.get('VIDEO_Cooktop');hob.location.x=17.22
    for x in [17.04,17.4]:
        for y in [16.27,16.5]:lathe('Induction_ring',(x,y,1.009),[(.083,0),(.085,.0005)],steel)
    # Full-height closed refrigerator and precise split line, as visible at 12s.
    tall=bpy.data.objects['VIDEO_Tall_storage'];tall.dimensions=(.75,.83,2.70)
    for z,h in [(1.64,2.06),(.28,.60)]:box('Tall_front',(18.52,15.915,z),(.742,.025,h),oak,.002)
    rail('Tall_pull',(18.73,15.86,.8),(18.73,15.86,1.35),.01,bronze)
    # Thin waterfall top and framed broad dark island panels.
    for i in range(3):
        x=15.68+i*.88;box('Island_panel',(x,13.521,.48),(.865,.024,.78),oak,.003)
        for xx in [x-.405,x+.405]:box('Island_stile',(xx,13.503,.48),(.035,.018,.75),oak,.002)
        for z in [.12,.84]:box('Island_rail',(x,13.503,z),(.84,.018,.035),oak,.002)
    # Rolled-edge bowl, bottles, plate stack, board and bread define kitchen composition.
    lathe('Fruit_bowl',(15.70,14.12,.988),[(0,0),(.08,0),(.15,.025),(.24,.10),(.25,.125),(.244,.133),(.234,.125),(.14,.041),(.08,.019),(0,.019)],oak)
    for i,(dx,dy) in enumerate([(-.07,0),(.07,.02),(0,-.05)]):
        bpy.ops.mesh.primitive_uv_sphere_add(segments=32,ring_count=20,radius=.06,location=(15.7+dx,14.12+dy,1.065));o=bpy.context.object;o.name='PK_Fruit';o.scale.z=.85;assign(o,bottle)
        for f in o.data.polygons:f.use_smooth=True
    board=box('Bread_board',(16.45,14.30,1.003),(.57,.35,.028),oak,.025)
    bpy.ops.mesh.primitive_uv_sphere_add(segments=48,ring_count=24,location=(16.4,14.30,1.078));o=bpy.context.object;o.name='PK_Bread';o.scale=(.21,.105,.078);bpy.ops.object.transform_apply(location=False,rotation=False,scale=True);assign(o,bread)
    for f in o.data.polygons:f.use_smooth=True
    tex=bpy.data.textures.new('PK_crust','CLOUDS');tex.noise_scale=.035;d=o.modifiers.new('Crust_pores','DISPLACE');d.texture=tex;d.strength=.005
    box('Knife_blade',(16.52,14.09,1.025),(.20,.021,.003),steel,.001);box('Knife_handle',(16.7,14.09,1.03),(.14,.026,.018),oak,.006)
    box('Plate_board',(17.36,14.2,1.003),(.49,.38,.03),oak,.04)
    for j in range(4):lathe('Stacked_plate',(17.36,14.2,1.022+j*.009),[(0,0),(.085,0),(.14,.008),(.153,.017),(.15,.022),(.12,.021),(.08,.012),(0,.012)],ceramic)
    for x in [17.2,17.35]:lathe('Pepper_mill',(x,14.62,.99),[(0,0),(.035,0),(.041,.018),(.03,.09),(.026,.14),(.039,.18),(.04,.205),(.025,.224),(0,.23)],oak)
    for name,x,y,h in [('Wine',17.65,14.57,.36),('Water',16.18,13.86,.27)]:
        lathe(name,(x,y,.987),[(0,0),(.043,0),(.052,.016),(.052,h*.63),(.027,h*.77),(.018,h*.81),(.018,h),(.014,h+.004),(.014,h-.06)],bottle if name=='Wine' else glass)
        lathe(name+'_label',(x,y,1.06),[(.0525,0),(.0525,.085)],paper)
    lathe('Tumbler',(15.97,13.81,.987),[(.033,0),(.039,.005),(.043,.12),(.039,.12),(.035,.014),(0,.014)],glass)
    # Folded linen with deliberately slight waviness, not perfectly flat card.
    verts=[];faces=[]
    for j in range(12):
        for i in range(16):verts.append((16.65+i*.017,13.64+j*.017,.99+.0015*math.sin(i*.7+j*.4)))
    for j in range(11):
        for i in range(15):k=j*16+i;faces.append((k,k+1,k+17,k+16))
    me=bpy.data.meshes.new('PK_napkin');me.from_pydata(verts,[],faces);o=bpy.data.objects.new('PK_Napkin',me);s.collection.objects.link(o);assign(o,bpy.data.materials['V03_Woven_ivory']);so=o.modifiers.new('Cloth_thickness','SOLIDIFY');so.thickness=.001
    # Baseboard/door linings give architectural contact and scale cues.
    plaster=bpy.data.materials['V03_Limewash']
    for x,w in [(7.48,2.0),(10.01,.78),(12.16,3.4),(14.32,.8)]:box('Rear_skirting',(x,16.75,.105),(w,.035,.1),oak,.003)
    s['photoreal_kitchen']='Source 8/10/12/13.8s: oven under hob; full-height refrigerator; broad panel island; modeled rolled-rim ceramics/glass and source-relative props. Geometry estimated, not BIM.'
