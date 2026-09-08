"""Bounded r03 corrections for assembly_r02; call build(), then save/version externally."""
import bpy
import math
import importlib.util
from pathlib import Path
from mathutils import Vector


def build():
    spec = importlib.util.spec_from_file_location('solace_hero_helpers', Path(__file__).with_name('photoreal_hero_assets.py'))
    h = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(h)
    h.P = 'HCR_'
    for ob in list(bpy.data.objects):
        if ob.name.startswith('HCR_'):
            bpy.data.objects.remove(ob, do_unlink=True)
    for ob in bpy.context.scene.objects:
        if ob.name.startswith('V02_Coffee_book'):
            ob.hide_render = True

    paper = h.material('Warm book pages', (.66,.635,.57), .93)
    linen = h.material('Blue grey cloth book', (.145,.20,.205), .77, True)
    cream = h.material('Cream book cloth', (.49,.435,.34), .8, True)
    sage = h.material('Sage ceramic glaze', (.24,.37,.26), .19)
    ceramic = h.material('Chalk bowl glaze', (.70,.69,.635), .25)
    coffee = h.material('Coffee surface', (.017,.009,.004), .14)
    table = bpy.data.objects.get('V02_Oval_coffee_top')
    if table:
        z = max((table.matrix_world @ Vector(c)).z for c in table.bound_box)+.001
        cx, cy = table.matrix_world.translation.x, table.matrix_world.translation.y
    else:
        cx, cy, z = 8.9,13.22,.466

    def book(name, center, angle, width, depth, thick, cover):
        g=h.group(name, center, angle)
        h.box('Bound page block',(0,0,thick/2),(width-.009,depth-.009,thick-.006),paper,.001,g)
        for zz in [.0015,thick-.0015]:
            h.box('Hardbound cloth cover',(0,0,zz),(width,depth,.003),cover,.001,g)
        h.box('Rounded cloth spine',(-width/2+.002,0,thick/2),(.005,depth,thick),cover,.002,g)
        # Discrete page layers visible along fore-edge; restrained at shot scale.
        edge=h.material('Page edge shadows',(.43,.415,.38),.95)
        for i in range(1,7):
            zz=.004+(thick-.008)*i/7
            h.curve('Page fore edge',[(width/2-.004,-depth/2+.006,zz),(width/2-.004,depth/2-.006,zz)],.00024,edge,g)
        return g

    book('Lower coffee art book',(cx-.19,cy+.025,z),math.radians(-5),.29,.22,.023,cream)
    book('Upper coffee art book',(cx-.205,cy+.031,z+.023),math.radians(2),.255,.205,.025,linen)
    # Small cup at source-left, shallow ceramic bowl at source-right.
    cup=h.group('Sage cup and saucer',(cx-.55,cy+.04,z),math.radians(-18))
    h.lathe('Cup saucer',[(0,0),(.046,0),(.071,.006),(.079,.011),(.08,.015),(.074,.016),(.047,.009),(0,.007)],(0,0,0),sage,cup)
    h.lathe('Small sage coffee cup',[(0,.009),(.031,.009),(.036,.016),(.039,.089),(.04,.093),(.034,.094),(.033,.022),(0,.018)],(0,0,0),sage,cup)
    h.curve('Cup loop handle',[(-.037,0,.077),(-.061,0,.078),(-.069,0,.056),(-.061,0,.033),(-.036,0,.034)],.0045,sage,cup)
    h.lathe('Coffee in cup',[(0,.074),(.032,.074)],(0,0,0),coffee,cup)
    h.lathe('Low coffee bowl',[(0,0),(.052,0),(.068,.014),(.113,.075),(.121,.086),(.119,.091),(.111,.089),(.099,.07),(.061,.022),(0,.015)],(cx+.40,cy+.045,z),ceramic)

    # Relax back cushion heights and faces without moving seat widths or camera fit.
    changes=[]
    for i in range(3):
        ob=bpy.data.objects.get('PHERO_Sofa back cushion %d'%i)
        if not ob:
            continue
        if not ob.get('r03_relaxed'):
            ob.scale.z *= [.90,.895,.915][i]
            ob.location.z -= [.019,.023,.017][i]
            ob.rotation_euler.y += [-.012,.008,-.007][i]
            for vert in ob.data.vertices:
                x,y,zz=vert.co
                front=max(0,min(1,-y/.10))
                # Relaxed small face undulations, two gentle lower-corner gathers.
                gather=math.exp(-((abs(x)-.37)/.07)**2-((zz+.18)/.095)**2)
                vert.co.y += front*(.0030*math.sin(19*x+i)*math.cos(10*zz+i)+.004*gather)
                vert.co.z += .0025*math.sin(x*9+i)*math.exp(-((zz-.20)/.12)**2)
            ob.data.update()
            ob['r03_relaxed']=True
        # The previous equatorial seam crossed the front panel. The real cushion
        # panel is uninterrupted; welt belongs around its rear perimeter.
        for child in ob.children:
            if child.type=='CURVE' and 'welt' in child.name:
                child.hide_render=True
        a,c=.474,.289
        pts=[]
        for k in range(80):
            t=math.tau*k/80
            pts.append((a*h.signed_pow(math.cos(t),.40),.098,c*h.signed_pow(math.sin(t),.47)))
        h.curve('Back cushion rear seam',pts,.0014,ob.data.materials[0],ob,True)
        changes.append(ob.name)
    # Also tuck decorative-cushion seams into their rear panel, retaining the seam
    # construction but removing conspicuous mid-face horizontal lines.
    for name in ['PHERO_Ivory square pillow','PHERO_Sage lumbar']:
        ob=bpy.data.objects.get(name)
        if not ob:continue
        for child in ob.children:
            if child.type=='CURVE' and 'welt' in child.name:child.hide_render=True
        a=max(abs(v.co.x) for v in ob.data.vertices)*.995
        c=max(abs(v.co.z) for v in ob.data.vertices)*.99
        y=max(v.co.y for v in ob.data.vertices)*.80
        pts=[(a*h.signed_pow(math.cos(t),.4),y,c*h.signed_pow(math.sin(t),.5)) for t in [math.tau*k/64 for k in range(64)]]
        h.curve('Decorative cushion rear seam',pts,.0011,ob.data.materials[0],ob,True)
    return {'coffee_accessories':True,'relaxed_back_cushions':changes,'source':'SOLACE_TARGET_06000ms.jpg'}
