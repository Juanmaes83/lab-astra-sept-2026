"""Respond to independent critic round 1; preserve assembly_r01."""
import bpy,math,sys,json,random
from pathlib import Path
from mathutils import Vector
BASE=Path(__file__).resolve().parent;sys.path.insert(0,str(BASE));s=bpy.context.scene
assert bpy.data.filepath.endswith('assembly_r01.blend')
target=BASE/'photoreal-work/assembly_r02.blend';assert not target.exists()
plaster=bpy.data.materials['PHOTO_Fine_warm_plaster'];oak=bpy.data.materials['PHOTO_Vertical_rift_oak'];stone=bpy.data.materials['PHOTO_Warm_honed_stone']
def box(name,loc,dim,m,r=.003):
    bpy.ops.mesh.primitive_cube_add(size=1,location=loc);o=bpy.context.object;o.name='R02_'+name;o.dimensions=dim;bpy.ops.object.transform_apply(location=False,rotation=False,scale=True);o.data.materials.append(m)
    if r:
        mod=o.modifiers.new('Fine_edges','BEVEL');mod.width=r;mod.segments=3;o.modifiers.new('Normals','WEIGHTED_NORMAL')
    return o
# Explicit wall-framed service doorway; no exposed exterior hole beside refrigerator.
box('Kitchen_door_left',(18.985,16.35,1.6),(.23,.22,3.2),plaster)
box('Kitchen_door_header',(19.64,16.35,2.925),(1.08,.22,.55),plaster)
box('Kitchen_door_right',(20.82,16.35,1.6),(1.30,.22,3.2),plaster)
box('Kitchen_return',(20.20,15.0,1.6),(.22,2.5,3.2),plaster)
box('Service_room_back',(19.62,18.1,1.6),(2.2,.22,3.2),plaster)
box('Service_ceiling',(19.7,17.0,3.29),(2.3,2.5,.18),plaster)
for x in [19.11,20.17]:box('Door_reveal',(x,16.26,1.325),(.035,.26,2.65),plaster)
for name,x,w in [('WALL_ENTRY_NW',7.968,1.215),('WALL_ENTRY_NE',9.933,.815)]:
    o=bpy.data.objects.get(name)
    if o:o.location.x=x;o.dimensions.x=w
# Restore roof-wall junction along the top of all visible outer side walls.
for x in [6.34,19.16]:box('Social_side_upper',(x,14.0,3.0),(.22,6,.4),plaster)
# Reference kitchen has thinner stone and understated inset fronts.
o=bpy.data.objects['VIDEO_Kitchen_island_stone'];o.dimensions.z=.045;o.location.z=.9675
for o in s.objects:
    if o.name.startswith(('PK_Island_stile','PK_Island_rail')):o.hide_render=True
    if o.name.startswith('PK_Island_panel'):
        o.location.y=13.519
    if o.name.startswith(('V02_Island_waterfall',)):
        for m in o.modifiers:
            if m.type=='BEVEL':m.width=.004
    if o.name=='PK_Bread':o.scale.x=1.18;o.scale.z=.73
    if o.type=='LIGHT' and o.name.startswith('PHOTO_'):
        if 'Living_soft' in o.name:o.data.energy*=.28
        elif 'Ceiling_linear_bounce' in o.name:o.data.energy*=.38
        elif 'overcast' in o.name:o.data.energy*=.60
        else:o.data.energy*=.75
        if 'overcast' in o.name or 'soft_practical' in o.name or 'bounce' in o.name:
            o.visible_glossy=False;o.visible_transmission=False;o.visible_camera=False
# Photographic CC0 forest fills distant exterior and genuine reflection/illumination.
env=bpy.data.images.load(str(BASE/'assets/misty_pines_4k.exr'),check_existing=True)
world=s.world;nodes=world.node_tree.nodes;links=world.node_tree.links
bg=next(n for n in nodes if n.type=='BACKGROUND')
tex=nodes.new('ShaderNodeTexEnvironment');tex.image=env
coord=nodes.new('ShaderNodeTexCoord');mapping=nodes.new('ShaderNodeMapping');mapping.inputs['Rotation'].default_value.z=math.radians(110)
links.new(coord.outputs['Generated'],mapping.inputs['Vector']);links.new(mapping.outputs['Vector'],tex.inputs['Vector']);links.new(tex.outputs['Color'],bg.inputs['Color']);bg.inputs['Strength'].default_value=.14
# Keep several true near trees for parallax. Archive r01 retains all procedural trees.
for o in list(s.objects):
    if o.name.startswith(('PHOTO_Fir_trunk_','PHOTO_Fir_foliage_')):
        index=int(o.name.rsplit('_',1)[-1])
        if index not in [1,3,6,9,12,15]:
            bpy.data.objects.remove(o,do_unlink=True)
            continue
    if o.name in ['PHOTO_Forest_floor','V02_Exterior_ground']:o.hide_render=True
# Mesh forest floor remains close to window, beyond it the HDRI forms the distance.
ground=bpy.data.materials['PHOTO_Forest_floor']
box('Near_forest_ground',(13,20,-.09),(36,6,.10),ground,.01)
# Low irregular fronds produce depth at the base of the source-like trunks.
rng=random.Random(209);leaf=bpy.data.materials['PHOTO_Fir_foliage_3'];verts=[];faces=[]
for plant in range(145):
    x=rng.uniform(3,24);y=rng.uniform(18.3,23);h=rng.uniform(.18,.6)
    for frond in range(7):
        a=frond*math.tau/7+rng.random()*.4;direction=Vector((math.cos(a),math.sin(a),0));side=Vector((-direction.y,direction.x,0));base=Vector((x,y,-.03))
        for j in range(1,10):
            t=j/10;c=base+direction*h*t+Vector((0,0,h*math.sin(t*2.1)));length=h*.24*(1-t)
            for sign in [-1,1]:
                tip=c+side*sign*length+direction*.06;k=len(verts);verts.extend([c-direction*.015,tip,c+direction*.025,c+Vector((0,0,.008))]);faces.extend([(k,k+1,k+3),(k+3,k+1,k+2)])
me=bpy.data.meshes.new('Forest_ferns');me.from_pydata(verts,[],faces);me.update();o=bpy.data.objects.new('R02_Forest_ferns',me);s.collection.objects.link(o);me.materials.append(leaf)
# Subdue ceiling without reducing localized luminous practicals.
ceiling=plaster.copy();ceiling.name='R02_Warm_ceiling';p=next(n for n in ceiling.node_tree.nodes if n.type=='BSDF_PRINCIPLED')
for link in list(p.inputs['Base Color'].links):ceiling.node_tree.links.remove(link)
p.inputs['Base Color'].default_value=(.24,.185,.13,1)
bpy.data.objects['VIDEO_Social_ceiling'].data.materials.clear();bpy.data.objects['VIDEO_Social_ceiling'].data.materials.append(ceiling)
s.view_settings.exposure=-.65
import photoreal_camera_correct
photoreal_camera_correct.build()
# Pack licensed environment; remove unreferenced generated meshes only in new saved version.
env.pack()
for me in list(bpy.data.meshes):
    if me.users==0:bpy.data.meshes.remove(me)
s.frame_set(1);bpy.ops.wm.save_as_mainfile(filepath=str(target),compress=True)
print('CORRECTED_R02',str(target),len(s.objects),flush=True)
