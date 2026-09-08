"""Final bounded correction: preserve assembled anchors, fit sofa at 1.80 m."""
import importlib.util, json, math
from pathlib import Path
BASE=Path(__file__).parent

def solve_final():
    spec=importlib.util.spec_from_file_location('solace_camera_correction_final',BASE/'photoreal_camera_correct.py')
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    c=mod.camera_module()
    current=json.loads((BASE/'photoreal_camera_residuals.json').read_text())
    solutions=current['anchors']
    # Only true furniture points. Rear floor/reveal correspondence is ambiguous
    # and cannot constrain the camera without creating a false height dip.
    data=c.ANCHORS[3][1][:7]
    old_residual=c.residual
    def fixed_height(q,observations):
        out=old_residual(q,observations)
        out.append((q[2]-1.8)*10000)
        return out
    c.residual=fixed_height
    pose=c.fit(data,[9.3,11.5,1.8,-.025,-.28,0])
    landmarks=[{'world':p,'target':t,'projected':c.project(p,pose),'error_px':math.dist(c.project(p,pose),t)} for p,t,w in data]
    solutions[3]={'seconds':6,'pose':pose,'rmse_px':math.sqrt(sum(v['error_px']**2 for v in landmarks)/len(landmarks)),'landmarks':landmarks}
    return solutions

def build():
    import bpy
    from mathutils import Vector, Quaternion
    results=solve_final();times=[a['seconds'] for a in results];poses=[a['pose'] for a in results]
    slopes=[]
    for i in range(len(poses)):
        lo=max(0,i-1);hi=min(len(poses)-1,i+1)
        slopes.append([0 if i<2 else (poses[hi][j]-poses[lo][j])/(times[hi]-times[lo]) for j in range(6)])
    # Shape-preserving height derivatives prevent overshoot/bobbing between
    # held or nearly level anchors while preserving every approved endpoint.
    for i in range(1,len(poses)-1):
        left=(poses[i][2]-poses[i-1][2])/(times[i]-times[i-1])
        right=(poses[i+1][2]-poses[i][2])/(times[i+1]-times[i])
        slopes[i][2]=0 if left*right<=0 else 2*left*right/(left+right)
    s=bpy.context.scene;cam=s.camera;cam.animation_data_clear();cam.data.animation_data_clear()
    cam.data.lens=28;cam.data.sensor_width=36;cam.data.sensor_fit='HORIZONTAL';cam.data.shift_x=0;cam.data.shift_y=0;cam.rotation_mode='QUATERNION';cam.data.dof.use_dof=False
    for frame in range(1,421):
        sec=(frame-1)/30;i=next((k for k in range(7) if sec<=times[k+1]),6);dt=times[i+1]-times[i];t=(sec-times[i])/dt
        q=[(2*t**3-3*t*t+1)*poses[i][j]+(t**3-2*t*t+t)*dt*slopes[i][j]+(-2*t**3+3*t*t)*poses[i+1][j]+(t**3-t*t)*dt*slopes[i+1][j] for j in range(6)]
        x,y,z,yaw,pitch,roll=q;cam.location=(x,y,z)
        direction=Vector((math.sin(yaw)*math.cos(pitch),math.cos(yaw)*math.cos(pitch),math.sin(pitch)))
        cam.rotation_quaternion=direction.to_track_quat('-Z','Y')@Quaternion((0,0,1),roll)
        cam.keyframe_insert('location',frame=frame);cam.keyframe_insert('rotation_quaternion',frame=frame)
    s.render.fps=30;s.frame_start=1;s.frame_end=420
    report={'method':'Final six-second sofa front/rear landmark LM solve with camera-height constraint1.80m; other anchors copied from assembled residual record; monotone height interpolation','lens_mm':28,'acceptance':'Human visual review pending; residuals remain reconstruction evidence, not acceptance','anchors':results}
    (BASE/'photoreal_camera_final_residuals.json').write_text(json.dumps(report,indent=2))
    s['camera_final']='Source landmark pose fit; 6s height1.8m; false doorway floor constraints removed; height overshoot prevented'
    s.frame_set(1)
    return results

if __name__=='__main__':
    result=solve_final()[3]
    print(json.dumps(result,indent=2))
