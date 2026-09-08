"""SOLACE source 0/8/12 s look pass. Original procedural assets; no third-party inputs.

Import in versioned v03-derived scene, then build(). Does not save or render.
World axes and practical locations follow produce_video_v03.py.
"""
import bpy
import math
import random
from mathutils import Vector


def mat(name, a, b=None, scale=(1, 1, 1), rough=.5, distance=.0003, metal=0):
    m = bpy.data.materials.new('PHOTO_' + name)
    m.use_nodes = True
    n, l = m.node_tree.nodes, m.node_tree.links
    p = next(q for q in n if q.type == 'BSDF_PRINCIPLED')
    p.inputs['Base Color'].default_value = (*a, 1)
    p.inputs['Roughness'].default_value = rough
    p.inputs['Metallic'].default_value = metal
    if b:
        t = n.new('ShaderNodeTexCoord')
        v = n.new('ShaderNodeVectorMath'); v.operation = 'MULTIPLY'
        v.inputs[1].default_value = scale
        l.new(t.outputs['Object'], v.inputs[0])
        noise = n.new('ShaderNodeTexNoise')
        noise.inputs['Scale'].default_value = 1
        noise.inputs['Detail'].default_value = 4
        noise.inputs['Roughness'].default_value = .72
        l.new(v.outputs[0], noise.inputs['Vector'])
        ramp = n.new('ShaderNodeValToRGB')
        ramp.color_ramp.elements[0].position = .20
        ramp.color_ramp.elements[1].position = .80
        ramp.color_ramp.elements[0].color = (*a, 1)
        ramp.color_ramp.elements[1].color = (*b, 1)
        l.new(noise.outputs['Fac'], ramp.inputs[0])
        l.new(ramp.outputs[0], p.inputs['Base Color'])
        bump = n.new('ShaderNodeBump')
        bump.inputs['Strength'].default_value = .17
        bump.inputs['Distance'].default_value = distance
        l.new(noise.outputs['Fac'], bump.inputs['Height'])
        l.new(bump.outputs[0], p.inputs['Normal'])
        remap = n.new('ShaderNodeMapRange')
        remap.inputs['To Min'].default_value = max(.02, rough-.06)
        remap.inputs['To Max'].default_value = min(1, rough+.06)
        l.new(noise.outputs['Fac'], remap.inputs['Value'])
        l.new(remap.outputs[0], p.inputs['Roughness'])
    return m


def assign(o, material):
    o.data.materials.clear()
    o.data.materials.append(material)


def mesh(name, verts, faces, materials):
    data = bpy.data.meshes.new('PHOTO_' + name)
    data.from_pydata(verts, [], faces); data.update()
    ob = bpy.data.objects.new('PHOTO_' + name, data)
    bpy.context.scene.collection.objects.link(ob)
    for m in materials: data.materials.append(m)
    return ob


def branch_geometry(verts, faces, a, b, radius, end_radius):
    direction = (b-a).normalized()
    u = direction.cross(Vector((0, 1, .1))).normalized()
    v = direction.cross(u)
    k = len(verts)
    for c, r in [(a, radius), (b, end_radius)]:
        for j in range(7):
            verts.append(c+r*(u*math.cos(j*math.tau/7)+v*math.sin(j*math.tau/7)))
    for j in range(7): faces.append((k+j,k+(j+1)%7,k+7+(j+1)%7,k+7+j))


def forest(bark, leaves, ground):
    rng = random.Random(9274)
    # Irregular ground rises behind sparse foreground trunks, matching rear windows.
    verts, faces = [], []
    for j in range(21):
        for i in range(26):
            x, y = -13+i*2.4, 17.2+j*1.75
            z = max(0, y-21)*.052 + .10*math.sin(x*.45+y*.22)
            verts.append((x, y, z-.08))
    for j in range(20):
        for i in range(25):
            k=j*26+i; faces.append((k,k+1,k+27,k+26))
    mesh('Forest_floor', verts, faces, [ground])
    # Distinct trunk depth layers; foreground never becomes a hedge wall.
    sites = [(rng.uniform(-5,31), rng.uniform(20.0,24),rng.uniform(6.5,10)) for _ in range(17)]
    sites += [(rng.uniform(-10,37),rng.uniform(25,36),rng.uniform(8,13)) for _ in range(42)]
    sites += [(rng.uniform(-15,40),rng.uniform(37,48),rng.uniform(10,15)) for _ in range(32)]
    # Reflected trees outside the front glazing; keep circulation opening clear.
    sites += [(x, y, rng.uniform(7,10)) for x,y in [(-1,3),(3,1),(18,0),(22,4),(26,7),(3,7)]]
    for idx,(x,y,h) in enumerate(sites):
        z0=max(0,y-21)*.052
        trunk_v,trunk_f,leaf_v,leaf_f=[],[],[],[]
        lean=Vector((rng.uniform(-.35,.35),rng.uniform(-.35,.35),0))
        base=Vector((x,y,z0))
        for j in range(8):
            a=base+Vector((0,0,h*j/8))+lean*j/8
            b=base+Vector((0,0,h*(j+1)/8))+lean*(j+1)/8
            branch_geometry(trunk_v,trunk_f,a,b,.10*(1-j/9),.10*(1-(j+1)/9))
        # Tapered asymmetrical tiers and branchlets, no canopy hulls or billboards.
        for j in range(30):
            height=h*(.27+.70*j/30)
            angle=j*2.399+rng.uniform(-.4,.4)
            radius=h*.21*(1-height/h)**.55*rng.uniform(.65,1.3)
            start=base+Vector((0,0,height))+lean*height/h
            ray=Vector((math.cos(angle),math.sin(angle),rng.uniform(-.22,.04)))
            end=start+ray*radius
            branch_geometry(trunk_v,trunk_f,start,end,.023*(1-height/h)+.006,.0015)
            side=Vector((-ray.y,ray.x,.10))
            for k in range(2,10):
                center=start+(end-start)*k/10
                extent=radius*(1-k/11)*.48
                for sign in [-1,1]:
                    tip=center+side*sign*extent+ray*.22
                    branch_geometry(trunk_v,trunk_f,center,tip,.006,.0008)
                    # Sprays contain folded narrow foliage: irregular real edge silhouette.
                    for t in range(11):
                        c=center+(tip-center)*(t+.2)/11
                        for ss in [-1,1]:
                            u=(ray*ss+side*sign*.25+Vector((0,0,rng.uniform(-.3,.3)))).normalized()
                            length=rng.uniform(.07,.15)
                            width=rng.uniform(.013,.027)
                            vv=u.cross(Vector((0,0,1))).normalized()*width
                            p=len(leaf_v)
                            leaf_v.extend([c,c+u*length*.45+vv,c+u*length+Vector((0,0,.01)),c+u*length*.45-vv,c+u*length*.5+Vector((0,0,.013))])
                            leaf_f.extend([(p,p+1,p+4),(p+1,p+2,p+4),(p+2,p+3,p+4),(p+3,p,p+4)])
        mesh('Fir_trunk_%02d'%idx,trunk_v,trunk_f,[bark])
        ob=mesh('Fir_foliage_%02d'%idx,leaf_v,leaf_f,leaves)
        for poly in ob.data.polygons: poly.material_index=rng.randrange(len(leaves))


def area(name, loc, target, power, size, color, size_y=None):
    d=bpy.data.lights.new('PHOTO_'+name,'AREA')
    d.energy=power; d.color=color
    d.shape='RECTANGLE' if size_y else 'DISK'
    d.size=size
    if size_y: d.size_y=size_y
    o=bpy.data.objects.new('PHOTO_'+name,d)
    bpy.context.scene.collection.objects.link(o)
    o.location=loc
    o.rotation_euler=(Vector(target)-Vector(loc)).to_track_quat('-Z','Y').to_euler()
    return o


def build():
    s=bpy.context.scene
    oak=mat('Oiled_oak',(.24,.135,.068),(.39,.26,.14),(.55,125,95),.39,.00025)
    vertical=mat('Vertical_rift_oak',(.23,.125,.059),(.365,.235,.12),(120,95,.6),.42,.00025)
    plaster=mat('Fine_warm_plaster',(.57,.535,.465),(.63,.60,.535),(145,145,145),.82,.00016)
    stone=mat('Warm_honed_stone',(.53,.505,.445),(.65,.625,.56),(13,13,13),.37,.00014)
    linen=mat('Ivory_linen',(.60,.575,.515),(.72,.69,.62),(520,520,520),.86,.00025)
    next(q for q in linen.node_tree.nodes if q.type=='BSDF_PRINCIPLED').inputs['Sheen Weight'].default_value=.3
    bark=mat('Fir_bark',(.035,.029,.023),(.13,.105,.078),(80,80,3),.91,.007)
    ground=mat('Forest_floor',(.018,.031,.024),(.068,.08,.053),(5,5,5),.96,.012)
    glass=mat('Architectural_glass',(.965,.985,1),rough=.018)
    gp=next(q for q in glass.node_tree.nodes if q.type=='BSDF_PRINCIPLED')
    gp.inputs['Transmission Weight'].default_value=1
    gp.inputs['IOR'].default_value=1.5
    black=mat('Satin_black_frame',(.012,.015,.014),rough=.28,metal=.65)
    leaves=[]
    for j in range(5):
        m=mat('Fir_foliage_'+str(j),(.015+j*.007,.032+j*.01,.024+j*.006),rough=.68)
        p=next(q for q in m.node_tree.nodes if q.type=='BSDF_PRINCIPLED')
        p.inputs['Subsurface Weight'].default_value=.035
        leaves.append(m)
    replacements={'V03_Natural_oiled_oak':oak,'V03_Rift_cut_vertical_oak':vertical,
        'V03_Limewash':plaster,'V03_Woven_ivory':linen,'V03_Honed_limestone':stone,
        'V03_Low_iron_glass':glass,'V03_Anodized_bronze_black':black,
        'V02_Smoked_honey_oak':oak,'V02_Warm_plaster':plaster,'V02_Soft_cream_weave':linen,
        'V02_Ivory_stone':stone,'V02_Clear_glazing':glass,'V02_Black_frames':black}
    for o in list(s.objects):
        if o.type=='LIGHT': o.hide_render=True
        if o.name.startswith(('V03_Courtyard_olive','V03_Rear_garden','V03_Courtyard_grasses',
            'V02_Forest_','V02_Foliage','VIDEO_Courtyard_canopy','VIDEO_Courtyard_trunk',
            'V02_Boundary_wall','V03_Covered_dining_shade')): o.hide_render=True
        if o.type in {'MESH','CURVE'}:
            for slot in o.material_slots:
                if slot.material and slot.material.name in replacements: slot.material=replacements[slot.material.name]
        if o.name in ['V02_Exterior_ground','SPACE_PLANTED_COURTYARD','SPACE_OPEN_LAWN','SPACE_PRIVATE_GARDEN'] and o.type=='MESH': assign(o,ground)
    forest(bark,leaves,ground)
    world=s.world; world.use_nodes=True
    n,l=world.node_tree.nodes,world.node_tree.links
    bg=next(node for node in n if node.type=='BACKGROUND')
    for link in list(bg.inputs['Color'].links): l.remove(link)
    bg.inputs['Color'].default_value=(.32,.43,.55,1)
    bg.inputs['Strength'].default_value=.22
    # Large cool aperture light, kept subdued relative to the tungsten practicals.
    area('Rear_overcast',(13.5,18.6,5.1),(13.5,14.4,1),850,9,(.68,.79,1),4)
    area('Courtyard_overcast',(11,7.2,5),(11.5,13,1),650,8,(.72,.83,1),5)
    warm=(1,.70,.43)
    area('Ceiling_linear_bounce',(12.7,16.36,2.76),(12.7,13.4,.6),300,10.5,warm,.12)
    area('Living_soft_practical',(8.75,14.0,2.65),(8.7,14.5,.55),135,2.6,warm,1.8)
    area('Dining_diffuser',(12.62,14.48,2.30),(12.62,14.48,.8),95,.085,(1,.77,.53),2.14)
    area('Kitchen_task',(16.4,16.15,2.69),(16.4,15.4,.8),115,3.5,(1,.78,.56),.10)
    for y in [12.9,14,15.06,16.1]:
        for z in [1.28,1.9,2.56]:
            area('Library_strip',(7.03,y,z),(6.64,y,z-.3),5,.018,(1,.72,.43),.89)
    # Diffusers are actual visible luminous surfaces and create credible window reflections.
    for o in s.objects:
        if o.name=='V02_Ceiling_linear': o.hide_render=False
    led=bpy.data.materials.get('V02_Warm_LED')
    if led:
        p=next(q for q in led.node_tree.nodes if q.type=='BSDF_PRINCIPLED')
        p.inputs['Emission Color'].default_value=(1,.77,.52,1)
        p.inputs['Emission Strength'].default_value=7
    s.view_settings.view_transform='AgX'
    s.view_settings.exposure=-.25
    s['PHOTO_look_reference']='Source 0/8/12 s: dark conifer exterior, warm visible linear practicals; original procedural geometry/materials.'
    return {'forest_trees':97,'materials':'PHOTO_','exposure':s.view_settings.exposure}
