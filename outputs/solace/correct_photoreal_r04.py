"""Critique round3: scanned textile, asymmetric seats, table silhouette, authored forest."""
import bpy,sys,math
from pathlib import Path
BASE=Path(__file__).resolve().parent;sys.path.insert(0,str(BASE));s=bpy.context.scene
assert bpy.data.filepath.endswith('assembly_r03.blend')
target=BASE/'photoreal-work/assembly_r04.blend';assert not target.exists()
# Independent seat compression rather than identical inflated cushions.
for o in s.objects:
    if o.name.startswith('PHERO_Sofa seat') and o.type=='MESH':
        idx=int(o.name.split('seat ')[1].split('.')[0]);phase=[.3,1.7,3.4][idx]
        for v in o.data.vertices:
            x,y,z=v.co
            if z>0:
                crown=math.exp(-((x-.06*math.sin(phase))/.31)**2-((y+.05)/.27)**2)
                v.co.z=z*1.18-.018*crown+.004*math.sin(x*17+phase)*math.exp(-(y/.35)**2)
                v.co.y+=.007*math.sin(x*15+phase)*max(0,1-(y/.45)**2)
        o.scale.x=.976;o.location.z+=.008;o.rotation_euler.x=[-.015,.012,-.026][idx]
# Scan-derived weave relief. Preserve source color; no blue diffuse map substitution.
weave=bpy.data.images.load(str(BASE/'assets/rough_linen_rough_2k.jpg'),check_existing=True);weave.colorspace_settings.name='Non-Color'
for m in bpy.data.materials:
    if m.name.startswith(('PHERO_Ivory cotton','PHERO_Sage lumbar','PHOTO_Ivory_linen')):
        n=m.node_tree.nodes;l=m.node_tree.links;p=next(q for q in n if q.type=='BSDF_PRINCIPLED')
        coord=n.new('ShaderNodeTexCoord');mapping=n.new('ShaderNodeMapping');mapping.inputs['Scale'].default_value=(3.33,3.33,3.33);l.new(coord.outputs['Object'],mapping.inputs['Vector'])
        tex=n.new('ShaderNodeTexImage');tex.image=weave;tex.projection='BOX';tex.projection_blend=.25;l.new(mapping.outputs['Vector'],tex.inputs['Vector'])
        bump=n.new('ShaderNodeBump');bump.inputs['Distance'].default_value=.00045;bump.inputs['Strength'].default_value=.24;l.new(tex.outputs['Color'],bump.inputs['Height']);l.new(bump.outputs[0],p.inputs['Normal'])
        rough=n.new('ShaderNodeMapRange');rough.inputs['To Min'].default_value=.70;rough.inputs['To Max'].default_value=.94;l.new(tex.outputs['Color'],rough.inputs['Value']);l.new(rough.outputs[0],p.inputs['Roughness'])
# 1.4 x 2.6 m source-anchored broad table, round 18cm corners (not a bevelled box).
old=bpy.data.objects['PHERO_Dining solid oak top'];old.hide_render=True
verts=[];faces=[];r=.18;hx=.7;hy=1.30;N=12
ring=[]
for cx,cy,start in [(hx-r,hy-r,0),(-hx+r,hy-r,90),(-hx+r,-hy+r,180),(hx-r,-hy+r,270)]:
    for i in range(N+1):
        a=math.radians(start+i*90/N);ring.append((cx+r*math.cos(a),cy+r*math.sin(a)))
for z in [.758,.828]:verts.extend([(x,y,z) for x,y in ring])
n=len(ring);faces.append(tuple(range(n-1,-1,-1)));faces.append(tuple(range(n,2*n)))
for i in range(n):faces.append((i,(i+1)%n,(i+1)%n+n,i+n))
me=bpy.data.meshes.new('R04_Rounded_dining_top');me.from_pydata(verts,[],faces);me.update();o=bpy.data.objects.new('R04_Rounded_dining_top',me);s.collection.objects.link(o);o.parent=old.parent;me.materials.append(old.data.materials[0]);b=o.modifiers.new('Small_edge_ease','BEVEL');b.width=.006;b.segments=3;o.modifiers.new('Normals','WEIGHTED_NORMAL')
for o in s.objects:
    if o.name.startswith('PHERO_Dining chair') and o.type=='EMPTY':o.location.x+=.15 if o.location.x>12.62 else -.15
    if o.name.startswith('PHERO_Dining tapered leg'):o.location.x*=1.25
# New environment has irregular crown/sky gaps instead of foggy pine trunks.
env=bpy.data.images.load(str(BASE/'assets/forest_slope_4k.exr'),check_existing=True)
for n in s.world.node_tree.nodes:
    if n.type=='TEX_ENVIRONMENT':n.image=env
    if n.type=='MAPPING':n.inputs['Rotation'].default_value=(0,0,math.radians(35))
bg=next(n for n in s.world.node_tree.nodes if n.type=='BACKGROUND');bg.inputs['Strength'].default_value=.15
import photoreal_forest_asset
photoreal_forest_asset.build()
for image in bpy.data.images:
    if image.users>0 and image.source=='FILE':image.pack()
for image in list(bpy.data.images):
    if image.users==0:bpy.data.images.remove(image)
s.frame_set(1);bpy.ops.wm.save_as_mainfile(filepath=str(target),compress=True)
print('CORRECTED_R04',str(target),flush=True)
