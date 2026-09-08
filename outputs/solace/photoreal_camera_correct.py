"""r02 camera correction: fit real sofa depth, not a flat full-height rectangle."""
import importlib.util
from pathlib import Path

def camera_module():
    spec=importlib.util.spec_from_file_location('solace_measured_camera',Path(__file__).with_name('photoreal_camera.py'))
    c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c)
    # Hero-asset world landmarks: back tops are at rear y14.795; turned
    # feet and timber deck are at front y14.18/14.045. The r01 flat-plane
    # fit overstated the width of the tall back and cropped the actual feet.
    points=[
        c.obs((7.42,14.795,1.12),(164,456),.8),
        c.obs((10.28,14.795,1.12),(1397,463),.8),
        c.obs((7.4696,14.18,.078),(42,925),.7),
        c.obs((10.2304,14.18,.078),(1453,946),.9),
        c.obs((10.455,14.04,.595),(1610,760),.65),
        c.obs((7.31,14.045,.2225),(0,878),.45),
        c.obs((10.39,14.045,.2225),(1550,891),.8),
        c.obs((8.3,16.88,0),(690,450),.35),
        c.obs((9.8,16.88,0),(1100,450),.35),
        c.obs((10.46,16.88,1.3),(1455,229),.45),
    ]
    c.ANCHORS[3]=(6,points,[9.2,11.35,1.85,0,-.25,0])
    return c

def build():
    c=camera_module()
    results=c.build()
    import bpy, json
    from mathutils import Vector
    # Evidence records actual evaluated world-space bounds used to audit the
    # correction, including parent transforms. It does not alter furniture.
    objects=[]
    for o in bpy.context.scene.objects:
        if o.type=='MESH' and not o.hide_render and ('Sofa' in o.name or 'sofa' in o.name):
            pts=[o.matrix_world@Vector(v) for v in o.bound_box]
            objects.append({'name':o.name,'min':[min(v[i] for v in pts) for i in range(3)],'max':[max(v[i] for v in pts) for i in range(3)]})
    (Path(__file__).parent/'photoreal_camera_correction_r02.json').write_text(json.dumps({'reason':'Independent critic found r01 sofa base cropped. Replace flat sofa rectangle with true front/rear hero-asset landmarks. Opening anchors unchanged; kitchen source fit retained because actual r01 island corners are already within approximately 15 pixels at1080p.','sofa_actual_world_bounds':objects,'corrected_anchor':results[3]},indent=2))
    return results

if __name__=='__main__':
    import json
    c=camera_module()
    print(json.dumps([{'seconds':v['seconds'],'pose':v['pose'],'rmse_px':v['rmse_px']} for v in c.solve()],indent=2))
