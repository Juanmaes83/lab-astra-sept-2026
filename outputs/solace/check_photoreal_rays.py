import bpy
from mathutils import Vector
s=bpy.context.scene;s.frame_set(420);bpy.context.view_layer.update();cam=s.camera;deps=bpy.context.evaluated_depsgraph_get()
for px,py in [(440,522),(460,496),(430,475),(500,525)]:
    x=(px/960-.5)*36/28;y=(.5-py/540)*36/28*540/960
    ray=cam.matrix_world.to_quaternion()@Vector((x,y,-1)).normalized()
    result=s.ray_cast(deps,cam.location,ray)
    print('RAY',px,py,result[4].name if result[0] else None,tuple(result[1]))
