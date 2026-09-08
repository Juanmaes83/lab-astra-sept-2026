"""Source-guided living/dining assets; invoke build() in the versioned scene.

References: SOLACE_TARGET_04000ms, 06000ms, 08000ms.jpg.
No import side effects, source-file writes, or render configuration changes.
"""
import bpy
import math
import random
from mathutils import Vector

P = 'PHERO_'


def material(name, color, roughness=.5, fabric=False):
    m = bpy.data.materials.get(P + name) or bpy.data.materials.new(P + name)
    m.use_nodes = True
    n, l = m.node_tree.nodes, m.node_tree.links
    n.clear()
    out = n.new('ShaderNodeOutputMaterial')
    bs = n.new('ShaderNodeBsdfPrincipled')
    bs.inputs['Base Color'].default_value = (*color, 1)
    bs.inputs['Roughness'].default_value = roughness
    l.new(bs.outputs[0], out.inputs[0])
    tex = n.new('ShaderNodeTexCoord')
    noise = n.new('ShaderNodeTexNoise')
    noise.inputs['Scale'].default_value = 480 if fabric else 8
    noise.inputs['Detail'].default_value = 2
    l.new(tex.outputs['Object'], noise.inputs['Vector'])
    bump = n.new('ShaderNodeBump')
    bump.inputs['Strength'].default_value = .24 if fabric else .08
    bump.inputs['Distance'].default_value = .00035 if fabric else .0001
    l.new(noise.outputs['Fac'], bump.inputs['Height'])
    l.new(bump.outputs[0], bs.inputs['Normal'])
    if fabric:
        bs.inputs['Sheen Weight'].default_value = .26
        bs.inputs['Sheen Roughness'].default_value = .8
        bs.inputs['Specular IOR Level'].default_value = .28
        # Crossed yarns at submillimetre scale over the softer fibre noise.
        wave = n.new('ShaderNodeTexWave')
        wave.wave_type = 'BANDS'
        wave.bands_direction = 'X'
        wave.inputs['Scale'].default_value = 700
        l.new(tex.outputs['Object'], wave.inputs['Vector'])
        micro = n.new('ShaderNodeBump')
        micro.inputs['Strength'].default_value = .12
        micro.inputs['Distance'].default_value = .00016
        l.new(wave.outputs['Color'], micro.inputs['Height'])
        l.new(bump.outputs[0], micro.inputs['Normal'])
        l.new(micro.outputs[0], bs.inputs['Normal'])
    return m


def mesh(name, verts, faces, mat, parent=None):
    me = bpy.data.meshes.new(P + name)
    me.from_pydata(verts, [], faces)
    me.update()
    ob = bpy.data.objects.new(P + name, me)
    bpy.context.scene.collection.objects.link(ob)
    me.materials.append(mat)
    ob.parent = parent
    for f in me.polygons:
        f.use_smooth = True
    return ob


def group(name, loc=(0, 0, 0), angle=0):
    ob = bpy.data.objects.new(P + name, None)
    bpy.context.scene.collection.objects.link(ob)
    ob.location = loc
    ob.rotation_euler.z = angle
    return ob


def box(name, loc, dim, mat, radius=.008, parent=None):
    bpy.ops.mesh.primitive_cube_add(size=1)
    ob = bpy.context.object
    ob.name = P + name
    ob.dimensions = dim
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    ob.parent = parent
    ob.location = loc
    ob.data.materials.append(mat)
    if radius:
        mod = ob.modifiers.new('Machined edge radius', 'BEVEL')
        mod.width = radius
        mod.segments = 4
        ob.modifiers.new('Planar face normals', 'WEIGHTED_NORMAL')
    return ob


def curve(name, points, radius, mat, parent=None, cyclic=False):
    cu = bpy.data.curves.new(P + name, 'CURVE')
    cu.dimensions = '3D'
    cu.bevel_depth = radius
    cu.bevel_resolution = 3
    sp = cu.splines.new('BEZIER')
    sp.bezier_points.add(len(points) - 1)
    for p, co in zip(sp.bezier_points, points):
        p.co = co
        p.handle_left_type = p.handle_right_type = 'AUTO'
    sp.use_cyclic_u = cyclic
    ob = bpy.data.objects.new(P + name, cu)
    bpy.context.scene.collection.objects.link(ob)
    ob.parent = parent
    cu.materials.append(mat)
    return ob


def signed_pow(x, p):
    return math.copysign(abs(x) ** p, x)


def cushion(name, loc, dim, mat, parent=None, exp=.36, seed=0):
    """Continuous sewn cushion mesh, rounded plan and crowned top/bottom.

    Superellipse rings produce inflated fabric rather than a bevelled cube;
    low-amplitude gathering follows the side seam and decays onto the face.
    """
    nu, nv = 96, 40
    a, b, c = (v / 2 for v in dim)
    verts, faces = [], []
    for j in range(1, nv):
        phi = -math.pi / 2 + math.pi * j / nv
        cp = abs(math.cos(phi)) ** exp
        z = c * signed_pow(math.sin(phi), .56)
        for i in range(nu):
            t = math.tau * i / nu
            x = a * cp * signed_pow(math.cos(t), exp)
            y = b * cp * signed_pow(math.sin(t), exp)
            gather = .0015 * math.sin(t * 29 + seed) * math.exp(-abs(phi) * 5)
            # Small relaxed fabric irregularity, no exaggerated tufting.
            x += gather * math.cos(t)
            y += gather * math.sin(t)
            zz = z + .0018 * math.sin(4*t + seed) * cp
            verts.append((x, y, zz))
    for j in range(nv - 2):
        for i in range(nu):
            k = j * nu + i
            nxt = j * nu + (i+1) % nu
            faces.append((k, nxt, nxt + nu, k + nu))
    bottom = len(verts)
    verts.extend([(0, 0, -c), (0, 0, c)])
    for i in range(nu):
        faces.append((bottom, (i+1) % nu, i))
        faces.append((bottom+1, (nv-2)*nu+i, (nv-2)*nu+(i+1)%nu))
    ob = mesh(name, verts, faces, mat, parent)
    ob.location = loc
    # Sewn perimeter welt at the middle of the cushion wall.
    pts = [(a*signed_pow(math.cos(t),exp)*1.002,
            b*signed_pow(math.sin(t),exp)*1.002, 0)
           for t in [math.tau*i/64 for i in range(64)]]
    curve(name + '_welt', pts, .0016, mat, ob, True)
    return ob


def tapered_leg(name, start, end, r0, r1, mat, parent=None):
    a, b = Vector(start), Vector(end)
    axis = (b-a).normalized()
    u = axis.cross(Vector((0,1,0))).normalized()
    v = axis.cross(u)
    verts, faces = [], []
    for pos, radius in [(a,r0),(a+(b-a)*.04,r0),(b-(b-a)*.03,r1),(b,r1*.90)]:
        verts.extend([pos+radius*(u*math.cos(t)+v*math.sin(t))
                      for t in [math.tau*i/24 for i in range(24)]])
    for j in range(3):
        for i in range(24):
            faces.append((j*24+i,j*24+(i+1)%24,(j+1)*24+(i+1)%24,(j+1)*24+i))
    faces += [tuple(reversed(range(24))), tuple(range(72,96))]
    return mesh(name, verts, faces, mat, parent)


def bent_back(name, parent, wood, width=.51, height=.20, z=.79):
    # Broad steam-bent plywood band measured from the 8 s reference.
    # Local rear is +Y; the arc wraps forward at its edges.
    verts, faces = [], []
    radius = width/.98
    count = 40
    for i in range(count+1):
        a = -.51 + 1.02*i/count
        for rr, zz in [(radius-.012,z-height/2),(radius+.012,z-height/2),
                       (radius+.012,z+height/2),(radius-.012,z+height/2)]:
            verts.append((rr*math.sin(a), rr*math.cos(a)-radius+.245,
                          zz+.012*math.cos(a*2)))
    for i in range(count):
        for j in range(4):
            faces.append((i*4+j,i*4+(j+1)%4,(i+1)*4+(j+1)%4,(i+1)*4+j))
    faces.extend([(3,2,1,0),tuple(range(count*4,count*4+4))])
    ob = mesh(name, verts, faces, wood, parent)
    bevel = ob.modifiers.new('Plywood eased edges', 'BEVEL')
    bevel.width = .003
    bevel.segments = 3
    ob.modifiers.new('Broad band normals', 'WEIGHTED_NORMAL')
    return ob


def lathe(name, profile, loc, mat, parent=None):
    verts, faces = [], []
    n = 64
    for r,z in profile:
        verts.extend([(r*math.cos(math.tau*i/n),r*math.sin(math.tau*i/n),z) for i in range(n)])
    for j in range(len(profile)-1):
        for i in range(n):
            faces.append((j*n+i,j*n+(i+1)%n,(j+1)*n+(i+1)%n,(j+1)*n+i))
    ob = mesh(name, verts, faces, mat, parent)
    ob.location = loc
    return ob


def build():
    random.seed(418)
    # Rerunnable, only the module-owned objects are removed.
    for ob in list(bpy.data.objects):
        if ob.name.startswith(P):
            bpy.data.objects.remove(ob, do_unlink=True)
    hide = ('VIDEO_Sofa', 'V02_Sofa', 'V02_Throw', 'V03_Sofa_piping',
            'VIDEO_Dining_table', 'VIDEO_Dining_pedestal', 'VIDEO_Dining_seat',
            'VIDEO_Dining_back', 'VIDEO_Chair_leg', 'V03_Chair', 'V03_Bentwood',
            'V02_Armchair', 'V02_Library_book', 'V02_Vase', 'V02_Dining_plate',
            'V02_Dining_tumbler', 'V02_Cutlery')
    for ob in bpy.context.scene.objects:
        if ob.name.startswith(hide):
            ob.hide_render = True
    ivory = material('Ivory cotton linen', (.68,.635,.54), .87, True)
    sage = material('Sage lumbar textile', (.18,.245,.175), .88, True)
    leather = material('Cognac saddle leather', (.14,.078,.043), .48)
    oak = bpy.data.materials.get('V03_Natural_oiled_oak') or material('Oak', (.30,.19,.10),.4)
    walnut = material('Walnut frame', (.16,.082,.039),.39)
    porcelain = material('Ivory porcelain', (.79,.76,.67), .24)
    glass = material('Smoky glass', (.64,.69,.64), .035)
    gb = next(n for n in glass.node_tree.nodes if n.type == 'BSDF_PRINCIPLED')
    gb.inputs['Transmission Weight'].default_value = 1
    gb.inputs['IOR'].default_value = 1.46
    silver = material('Brushed cutlery', (.55,.54,.50), .22)
    next(n for n in silver.node_tree.nodes if n.type == 'BSDF_PRINCIPLED').inputs['Metallic'].default_value = 1
    pages = material('Book paper', (.60,.57,.49),.94)
    paper_colors = [(.15,.19,.17),(.40,.36,.28),(.63,.61,.53),(.18,.14,.10),(.36,.24,.16)]
    jackets = [material('Book jacket %d'%i,c,.77) for i,c in enumerate(paper_colors)]

    sofa = group('Sofa', (8.85,14.5,0))
    box('Sofa timber plinth',(0,0,.275),(3.08,.91,.105),walnut,.014,sofa)
    cushion('Sofa upholstered deck',(0,0,.35),(3.12,.94,.105),ivory,sofa,exp=.20)
    for x in [-1.36,1.36]:
        for y in [-.32,.32]:
            tapered_leg('Sofa turned foot',(x*1.015,y,.078),(x,y,.28),.035,.048,walnut,sofa)
    for i,x in enumerate([-.965,0,.965]):
        cushion('Sofa seat %d'%i,(x,-.075,.478),(.945,.76,.19),ivory,sofa,seed=i)
        back = cushion('Sofa back cushion %d'%i,(x,.295,.83),(.955,.255,.585),ivory,sofa,exp=.40,seed=i+4)
        back.rotation_euler.x = math.radians(-8)
    for x in [-1.505,1.505]:
        arm = cushion('Sofa upholstered arm',(x,-.005,.595),(.205,.93,.47),ivory,sofa,exp=.38)
        arm.rotation_euler.y = math.copysign(.035,x)
    throw = cushion('Ivory square pillow',(-1.08,.075,.735),(.39,.16,.39),ivory,sofa,exp=.40)
    throw.rotation_euler = (math.radians(-11),math.radians(-4),math.radians(3))
    lumbar = cushion('Sage lumbar',(.99,.07,.706),(.44,.18,.28),sage,sofa,exp=.43)
    lumbar.rotation_euler.x = -.12
    # Draped linen on left seat, a source-visible soft interruption.
    verts, faces = [], []
    for j in range(25):
        t=j/24
        for i in range(17):
            u=i/16
            x=-1.39+.36*u
            y=.22-.65*t
            z=.586+.15*math.exp(-((t-.08)/.20)**2)+.009*math.sin(u*17+t*3)
            verts.append((x,y,z))
    for j in range(24):
        for i in range(16):
            k=j*17+i
            faces.append((k,k+1,k+18,k+17))
    cloth=mesh('Folded throw',verts,faces,ivory,sofa)
    sol=cloth.modifiers.new('Fabric thickness','SOLIDIFY');sol.thickness=.0015
    sub=cloth.modifiers.new('Soft folds','SUBSURF');sub.levels=1

    lounge=group('Sling armchair',(10.55,13.33,0),math.radians(155))
    for x in [-.335,.335]:
        curve('Lounge continuous side',[(x,-.34,.09),(x,-.28,.47),(x,-.25,.68),
                                      (x,.12,.70),(x,.34,.75),(x,.39,.91)],.032,walnut,lounge)
        tapered_leg('Lounge rear leg',(x,.41,.08),(x,.19,.66),.023,.032,walnut,lounge)
        curve('Lounge lower rail',[(x,-.27,.42),(x,.28,.38)],.024,walnut,lounge)
    for y,z in [(-.27,.43),(.30,.43),(.37,.88)]:
        curve('Lounge crossrail',[(-.33,y,z),(.33,y,z)],.024,walnut,lounge)
    # Suspended leather has a visibly curved seat/back instead of thick blocks.
    verts=[];faces=[]
    for j in range(32):
        t=j/31
        y=-.29+.66*t
        z=.43-.045*math.sin(min(t/.65,1)*math.pi) if t<.65 else .42+(t-.65)/.35*.45
        for i in range(25):
            u=i/24
            verts.append((-.30+.60*u,y,z-.025*math.sin(u*math.pi)))
    for j in range(31):
        for i in range(24):
            k=j*25+i;faces.append((k,k+1,k+26,k+25))
    sling=mesh('Leather sling',verts,faces,leather,lounge)
    sol=sling.modifiers.new('Leather thickness','SOLIDIFY');sol.thickness=.004
    sub=sling.modifiers.new('Relaxed leather','SUBSURF');sub.levels=1

    dining=group('Dining table',(12.62,14.48,0))
    # Rounded plan, shallow eased edge, as seen at 8 s.
    top=box('Dining solid oak top',(0,0,.793),(1.10,2.50,.075),oak,.045,dining)
    for x in [-.41,.41]:
        for y in [-1.08,1.08]:
            tapered_leg('Dining tapered leg',(x*1.06,y*1.025,.08),(x,y,.765),.026,.046,oak,dining)
    for x in [-.40,.40]:box('Dining apron',(x,0,.713),(.028,2.17,.105),oak,.006,dining)
    for side in [-1,1]:
        for row in range(3):
            chair=group('Dining chair',(12.62+side*.87,13.65+row*.82,0),-side*math.pi/2)
            box('Chair seat frame',(0,0,.432),(.46,.455,.042),oak,.030,chair)
            cushion('Chair ivory seat',(0,-.006,.475),(.445,.439,.064),ivory,chair,exp=.28,seed=row)
            for x in [-.207,.207]:
                tapered_leg('Chair front leg',(x*1.17,-.255,.078),(x,-.176,.432),.016,.024,oak,chair)
                curve('Chair back upright',[(x*1.17,.30,.08),(x,.196,.435),(x,.221,.72),(x,.227,.893)],.019,oak,chair)
                curve('Chair side stretcher',[(x,-.18,.36),(x,.21,.36)],.013,oak,chair)
            bent_back('Chair curved solid back',chair,oak)
    # Seven source-style pieces on the tabletop, avoiding floating disc plates.
    for side in [-1,1]:
        for y in [13.67,15.28]:
            x=12.62+side*.32
            lathe('Dinner plate',[(0,.001),(.10,.001),(.135,.009),(.148,.018),(.15,.023),(.145,.026),(.13,.018),(.095,.008),(0,.008)],(x,y,.833),porcelain)
            lathe('Water tumbler',[(0,0),(.038,0),(.04,.006),(.042,.112),(.039,.114),(.037,.012),(0,.012)],(x-side*.09,y+.215,.833),glass)
            curve('Dinner knife',[(x+side*.185,y-.093,.844),(x+side*.185,y+.05,.844),(x+side*.19,y+.095,.844)],.003,silver)
            curve('Dinner fork handle',[(x-side*.182,y-.095,.844),(x-side*.182,y+.055,.844)],.003,silver)
            for off in [-.006,-.002,.002,.006]:
                curve('Fork tine',[(x-side*.182,y+.05,.844),(x-side*.182+off,y+.066,.847),(x-side*.182+off,y+.098,.847)],.00085,silver)
    lathe('Dining vase',[(0,0),(.09,0),(.125,.025),(.145,.12),(.135,.23),(.085,.30),(.061,.35),(.061,.365),(.05,.365),(.05,.343),(.07,.294),(.12,.22),(.13,.12),(.11,.035),(0,.017)],(12.62,14.74,.833),porcelain)
    lathe('Dining timber bowl',[(0,0),(.08,0),(.13,.022),(.19,.09),(.192,.10),(.182,.104),(.15,.06),(.09,.014),(0,.012)],(12.62,14.16,.833),oak)

    # Retain source-aligned carcass and warm shelves; replace repetitive book grid.
    for level,z in enumerate([.74,1.36,1.98]):
        for bay,y0 in enumerate([12.52,13.60,14.68,15.76]):
            count=[7,3,6,4][(bay+level)%4]
            y=y0
            for i in range(count):
                width=random.uniform(.032,.065);h=random.uniform(.205,.365);depth=random.uniform(.19,.25)
                g=group('Library bound volume',(6.98,y+width/2,z))
                if i==count-1:g.rotation_euler.x=random.uniform(-.075,.075)
                jacket=jackets[(bay+i+level)%len(jackets)]
                box('Book page block',(0,0,h/2),(depth-.012,width-.006,h-.014),pages,.001,g)
                for yy in [-width/2,width/2]:box('Book cover',(0,yy,h/2),(depth,.0025,h),jacket,.001,g)
                box('Book spine',(depth/2-.002,0,h/2),(.004,width,h),jacket,.002,g)
                for zz in [h*.16,h*.82]:box('Spine emboss',(depth/2+.0007,0,zz),(.001,width*.6,.003),pages,.0005,g)
                y+=width+.008
            if count<=4:
                lathe('Library ceramic',[(0,0),(.06,0),(.086,.06),(.07,.17),(.045,.22),(.04,.23),(.034,.23),(.034,.20),(.055,.15),(.068,.065),(0,.015)],(6.97,y0+.63,z),porcelain)
    bpy.context.scene['hero_assets_reference']='04000/06000/08000ms source frames; PHERO mesh assets; human review pending'
    return {'prefix':P,'objects':sum(o.name.startswith(P) for o in bpy.context.scene.objects)}
