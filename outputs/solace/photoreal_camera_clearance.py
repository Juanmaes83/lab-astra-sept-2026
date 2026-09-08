"""Physical camera clearance correction, preserving scene geometry."""
import importlib.util, json, math
from pathlib import Path
BASE=Path(__file__).parent

def solve_clearance():
    spec=importlib.util.spec_from_file_location('solace_clearance_solver',BASE/'photoreal_camera.py')
    c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c)
    source=BASE/'photoreal_camera_final_residuals.json'
    if not source.exists():source=BASE/'photoreal_camera_residuals.json'
    result=json.loads(source.read_text())['anchors']
    original=c.residual
    for index,minimum in [(5,11.25),(6,11.25),(7,11.30)]:
        data=[(v['world'],v['target'],1.) for v in result[index]['landmarks']]
        height=result[index]['pose'][2]
        def constrained(q,observations):
            return original(q,observations)+[(q[1]-minimum)*100000,(q[2]-height)*10000]
        c.residual=constrained
        initial=result[index]['pose'][:];initial[1]=minimum
        pose=c.fit(data,initial);pose[1]=minimum
        landmarks=[{'world':p,'target':t,'projected':c.project(p,pose),'error_px':math.dist(c.project(p,pose),t)} for p,t,w in data]
        result[index]={'seconds':result[index]['seconds'],'pose':pose,'rmse_px':math.sqrt(sum(a['error_px']**2 for a in landmarks)/len(landmarks)),'landmarks':landmarks,'clearance_constraint_y':minimum}
    return result

def sampled_pose(results,frame):
    times=[a['seconds'] for a in results];poses=[a['pose'] for a in results]
    slopes=[]
    for i in range(len(poses)):
        lo=max(0,i-1);hi=min(len(poses)-1,i+1)
        slopes.append([0 if i<2 else (poses[hi][j]-poses[lo][j])/(times[hi]-times[lo]) for j in range(6)])
    for axis in [1,2]:
        for i in range(1,len(poses)-1):
            left=(poses[i][axis]-poses[i-1][axis])/(times[i]-times[i-1])
            right=(poses[i+1][axis]-poses[i][axis])/(times[i+1]-times[i])
            slopes[i][axis]=0 if left*right<=0 else 2*left*right/(left+right)
    # Ease the final lateral velocity before the east-wall inner face x18.996.
    slopes[-1][0]=.35
    sec=(frame-1)/30;i=next((k for k in range(7) if sec<=times[k+1]),6);dt=times[i+1]-times[i];t=(sec-times[i])/dt
    q=[(2*t**3-3*t*t+1)*poses[i][j]+(t**3-2*t*t+t)*dt*slopes[i][j]+(-2*t**3+3*t*t)*poses[i+1][j]+(t**3-t*t)*dt*slopes[i+1][j] for j in range(6)]
    # Crossing from exterior remains in the original 4–6 s approach. From
    # 6 s onward the route must remain physically inside the social room.
    if frame>=181:q[1]=max(11.25,q[1])
    if sec>13.8:q[0]=poses[-1][0]+.35*min(sec-13.8,.30)
    return q

def build():
    import bpy
    from mathutils import Vector,Quaternion
    result=solve_clearance();s=bpy.context.scene;cam=s.camera
    cam.animation_data_clear();cam.data.animation_data_clear();cam.rotation_mode='QUATERNION';cam.data.lens=28;cam.data.sensor_width=36;cam.data.sensor_fit='HORIZONTAL';cam.data.shift_x=0;cam.data.shift_y=0;cam.data.dof.use_dof=False
    for frame in range(1,421):
        x,y,z,yaw,pitch,roll=sampled_pose(result,frame);cam.location=(x,y,z)
        direction=Vector((math.sin(yaw)*math.cos(pitch),math.cos(yaw)*math.cos(pitch),math.sin(pitch)))
        cam.rotation_quaternion=direction.to_track_quat('-Z','Y')@Quaternion((0,0,1),roll)
        cam.keyframe_insert('location',frame=frame);cam.keyframe_insert('rotation_quaternion',frame=frame)
    s.render.fps=30;s.frame_start=1;s.frame_end=420
    minimum=min(sampled_pose(result,f)[1] for f in range(181,421))
    checks={str(f):sampled_pose(result,f)[:3] for f in [181,241,301,361,415,420,424]}
    report={'method':'Physical inside-room clearance; constrained LM yaw/pitch/x at10,12,13.8 seconds with28mm lens and existing heights; y11.25/11.25/11.30; monotone y/z interpolation','anchors':result,'minimum_camera_y_after6s':minimum,'frame_position_checks':checks,'wall_north_edge_y':11.027,'minimum_geometric_y_clearance_m':minimum-11.027,'visual_verification':'Requires root-rendered endpoint415/420; numeric clearance is not a render acceptance claim'}
    (BASE/'photoreal_camera_clearance_residuals.json').write_text(json.dumps(report,indent=2))
    s['camera_clearance']='Camera center north of south-wall edge after6s; endpoint y>=11.30; geometry unchanged'
    s.frame_set(1)
    return report

if __name__=='__main__':
    r=solve_clearance()
    print(json.dumps({'corrected':[{'seconds':a['seconds'],'pose':a['pose'],'rmse_px':a['rmse_px']} for a in r[5:]],'positions':{str(f):sampled_pose(r,f)[:3] for f in [181,241,301,361,415,420,424]}},indent=2))
