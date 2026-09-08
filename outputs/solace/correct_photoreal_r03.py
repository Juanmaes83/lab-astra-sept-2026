"""Independent critique round 2: source-relative composition and hero detail."""
import bpy,sys,math,random
from pathlib import Path
from mathutils import Vector
BASE=Path(__file__).resolve().parent;sys.path.insert(0,str(BASE));s=bpy.context.scene
assert bpy.data.filepath.endswith('assembly_r02.blend')
target=BASE/'photoreal-work/assembly_r03.blend';assert not target.exists()
def assign(o,m):o.data.materials.clear();o.data.materials.append(m)
steel=bpy.data.materials['V03_Brushed_steel'];black=bpy.data.materials['PHOTO_Satin_black_frame'];oak=bpy.data.materials['PHOTO_Vertical_rift_oak'];stone=bpy.data.materials['PHOTO_Warm_honed_stone']
def box(name,loc,dim,m,bevel=.003):
    bpy.ops.mesh.primitive_cube_add(size=1,location=loc);o=bpy.context.object;o.name='R03_'+name;o.dimensions=dim;bpy.ops.object.transform_apply(location=False,rotation=False,scale=True);assign(o,m)
    b=o.modifiers.new('Fine_edges','BEVEL');b.width=bevel;b.segments=3;o.modifiers.new('Normals','WEIGHTED_NORMAL');return o
def cylinder(name,loc,r,h,m):
    bpy.ops.mesh.primitive_cylinder_add(vertices=48,radius=r,depth=h,location=loc);o=bpy.context.object;o.name='R03_'+name;assign(o,m)
    for p in o.data.polygons:p.use_smooth=True
    return o
# Built-in bookcase ends beside the sofa rather than continuing behind its whole depth.
for o in s.objects:
    if o.name.startswith(('V02_Library_back','V02_Library_shelf')):
        o.location.y=13.455;o.dimensions.y=2.15
    if o.name.startswith(('V02_Library_upright','V02_Library_low_door','V02_Library_LED')) and o.location.y>14.54:o.hide_render=True
    if o.name.startswith('PHERO_Library bound volume') and o.location.y>14.54:
        for child in o.children_recursive:child.hide_render=True
    if o.name.startswith('PHERO_Library ceramic') and o.location.y>14.54:o.hide_render=True
    if o.name.startswith('PHOTO_Library_strip') and o.location.y>14.54:o.hide_render=True
    if o.name.startswith('PHERO_Sling armchair') and o.type=='EMPTY':o.location.y-=.65
# Foreground coffee table enters the lower edge rather than dominating the frame.
for o in s.objects:
    if o.name.startswith(('V02_Oval_coffee_top','V02_Coffee_leg','V02_Coffee_book')):o.location.y-=.28
# Source island bowl is one third across the image, not far left.
for o in s.objects:
    if o.name.startswith(('PK_Fruit_bowl','PK_Fruit')):o.location.x+=.38
    if o.name.startswith('PK_Bread'):
        o.scale.y*=1.12;o.scale.z*=1.3
        t=bpy.data.textures.new('R03_rough_crust','VORONOI');t.noise_scale=.018
        d=o.modifiers.new('Broken_crust','DISPLACE');d.texture=t;d.strength=.003
# Actual dispensing void and stainless fascia instead of bronze featureless face.
for o in s.objects:
    if o.name.startswith(('V02_Coffee_machine_front','V02_Coffee_cup')):o.hide_render=True
machine=bpy.data.objects['V02_Coffee_machine'];assign(machine,black)
box('Coffee_side_left',(16.115,16.322,1.22),(.035,.035,.40),steel)
box('Coffee_side_right',(16.385,16.322,1.22),(.035,.035,.40),steel)
box('Coffee_control_fascia',(16.25,16.317,1.372),(.27,.028,.085),steel)
box('Coffee_recess',(16.25,16.318,1.205),(.23,.023,.245),black,.008)
box('Coffee_drip_tray',(16.25,16.263,1.037),(.26,.17,.021),steel)
for i in range(9):box('Tray_slot',(16.14+i*.027,16.254,1.049),(.006,.13,.003),black,.001)
box('Coffee_display',(16.25,16.298,1.385),(.083,.003,.025),black,.002)
for x in [16.15,16.35]:
    o=cylinder('Coffee_control',(x,16.294,1.385),.014,.012,black);o.rotation_euler.x=math.pi/2
for x in [16.23,16.27]:cylinder('Coffee_spout',(x,16.265,1.282),.009,.04,steel)
# Darker restrained oak on island; retain material grain.
dark=oak.copy();dark.name='R03_Island_smoked_oak'
for n in dark.node_tree.nodes:
    if n.type=='VALTORGB':
        for e in n.color_ramp.elements:e.color=tuple(v*.65 for v in e.color[:3])+(1,)
for o in s.objects:
    if o.name.startswith(('PK_Island_panel','VIDEO_Kitchen_island_base')):assign(o,dark)
# A brighter forest sky with less massive foreground geometry; HDRI supplies irregular foliage.
for o in s.objects:
    if o.name.startswith(('PHOTO_Fir_trunk_','PHOTO_Fir_foliage_')):o.hide_render=True
bg=next(n for n in s.world.node_tree.nodes if n.type=='BACKGROUND');bg.inputs['Strength'].default_value=.32
for o in s.objects:
    if o.type=='LIGHT' and 'Living_soft_practical' in o.name:o.data.energy*=.6
s.view_settings.exposure=-.70
import photoreal_hero_correct
photoreal_hero_correct.build()
s.frame_set(1);bpy.ops.wm.save_as_mainfile(filepath=str(target),compress=True)
print('CORRECTED_R03',str(target),flush=True)
