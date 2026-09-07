import bpy
import math
import json
from mathutils import Vector

BASE='C:/Users/temp123/Documents/ChatGPT/lab-astra-sept-2026/'
EVID=BASE+'evidence/gate-2-solace/'
SOURCE='references/solace/HRUOGWHaMAATXEa.jpg'
def px(x): return (x-106)*25.4/452
def py(y): return (410-y)*17/299
def box(name,loc,dim,color=(0.68,0.67,0.59,1),role='architectural_blockout'):
    assert bpy.data.objects.get(name) is None, 'Existing semantic object: '+name
    mesh=bpy.data.meshes.new(name+'_MESH')
    mesh.from_pydata([(-.5,-.5,-.5),(.5,-.5,-.5),(.5,.5,-.5),(-.5,.5,-.5),(-.5,-.5,.5),(.5,-.5,.5),(.5,.5,.5),(-.5,.5,.5)],[],[(0,3,2,1),(4,5,6,7),(0,1,5,4),(1,2,6,5),(2,3,7,6),(3,0,4,7)])
    mesh.update()
    o=bpy.data.objects.new(name,mesh)
    bpy.context.scene.collection.objects.link(o)
    o.location=loc
    o.scale=dim
    o.color=color
    o['role']=role
    o['dimension_class']='ESTIMATED_FOR_BLOCKOUT'
    o['reference_source']=SOURCE
    return o
def rect(name,x1,y1,x2,y2,z=-.08,h=.16,color=(.74,.72,.64,1),role='space_floor'):
    return box(name,((px(x1)+px(x2))/2,(py(y1)+py(y2))/2,z),(px(x2)-px(x1),py(y1)-py(y2),h),color,role)
def wall(name,x1,y1,x2,y2):
    a=Vector((px(x1),py(y1),1.4)); b=Vector((px(x2),py(y2),1.4))
    o=box('WALL_'+name,(a+b)/2,((b-a).length,.22,2.8),(.19,.26,.24,1),'wall')
    o.rotation_euler.z=math.atan2(b.y-a.y,b.x-a.x)
    return o
def opening(name,x1,y1,x2,y2,kind='OPENING'):
    a=Vector((px(x1),py(y1),.035)); b=Vector((px(x2),py(y2),.035))
    o=box(kind+'_'+name,(a+b)/2,((b-a).length,.055,.07),(.34,.53,.52,1),'opening_threshold' if kind=='OPENING' else 'glazing_sill')
    o.rotation_euler.z=math.atan2(b.y-a.y,b.x-a.x)
    return o
def render_view(camera,path):
    s=bpy.context.scene
    s.camera=bpy.data.objects[camera]
    s.render.filepath=EVID+path
    bpy.ops.render.render(write_still=True)
def setup_render():
    s=bpy.context.scene
    s.render.engine='BLENDER_WORKBENCH'
    s.render.resolution_x=1200; s.render.resolution_y=1200; s.render.resolution_percentage=100
    s.render.image_settings.file_format='PNG'
    s.display.shading.light='STUDIO'
    s.display.shading.color_type='OBJECT'
    s.display.shading.show_shadows=True
    s.display.shading.show_cavity=True
    s.display.shading.cavity_type='BOTH'
    s.display.shading.background_type='WORLD'
    s.world.color=(.82,.82,.78)
    s.view_settings.view_transform='Standard'
    s.render.film_transparent=False

