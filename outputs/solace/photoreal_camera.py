"""Measured source landmark pose fitting. Import/build only mutates on build()."""
import math, json
from pathlib import Path

F=1920*28/36

def project(p, q):
    x,y,z,yaw,pitch,roll=q
    dx,dy,dz=p[0]-x,p[1]-y,p[2]-z
    sy,cy,sp,cp=math.sin(yaw),math.cos(yaw),math.sin(pitch),math.cos(pitch)
    right=cy*dx-sy*dy
    forward=cp*(sy*dx+cy*dy)+sp*dz
    up=-sp*(sy*dx+cy*dy)+cp*dz
    cr,sr=math.cos(roll),math.sin(roll)
    rx=cr*right+sr*up;uy=-sr*right+cr*up
    return [960+F*rx/max(.2,forward),540-F*uy/max(.2,forward)]

def obs(world,pixel,weight=1): return (world,pixel,weight)

def rect(x0,x1,y,z0,z1,pixels,w=1):
    return [obs(p,t,w) for p,t in zip([(x0,y,z1),(x1,y,z1),(x1,y,z0),(x0,y,z0)],pixels)]

def sofa(pixels):return rect(7.3,10.4,14.50,.1,1.12,pixels,.55)
def dw(pixels):return rect(10.46,13.86,16.88,1.30,3.,pixels)
def kw(pixels):return rect(14.77,17.83,16.88,1.10,3.10,pixels)
def island(pixels):return [obs(p,t,.8) for p,t in zip([(15.165,14.835,.985),(17.995,14.835,.985),(17.995,13.465,.985),(15.165,13.465,.985)],pixels)]

OPEN=sofa([(610,650),(1320,650),(1320,850),(610,850)])+dw([(1280,334),(1730,334),(1730,565),(1280,565)])+[obs((8.3,16.88,2.65),(845,380)),obs((9.8,16.88,2.65),(1085,380))]
ANCHORS=[
 (0,OPEN,[8.85,8.4,1.65,0,0,0]),
 (2,OPEN,[8.85,8.4,1.65,0,0,0]),
 (4,sofa([(398,640),(1430,640),(1430,945),(398,945)])+dw([(1320,215),(1870,225),(1870,508),(1320,508)])+[obs((8.3,16.88,2.65),(757,273)),obs((9.8,16.88,2.65),(1068,282))],[9.,10.3,1.65,0,-.08,0]),
 (6,sofa([(-80,451),(1620,451),(1620,948),(-80,948)])+[obs((8.3,16.88,0),(690,450),.5),obs((9.8,16.88,0),(1100,450),.5),obs((10.46,16.88,1.3),(1455,229),.6)],[9.2,12.,1.65,.02,-.2,0]),
 (8,[obs(p,t) for p,t in zip([(12.12,15.655,.83),(13.12,15.655,.83),(13.12,13.305,.83),(12.12,13.305,.83)],[(681,575),(1020,527),(1645,872),(910,1005)])]+[obs((10.46,16.88,1.3),(304,322)),obs((13.86,16.88,1.3),(1168,310)),obs((14.77,16.88,1.1),(1310,361)),obs((17.83,16.88,1.1),(1810,340))],[11.2,12.,1.65,.35,-.15,0]),
 (10,island([(786,623),(1522,544),(1839,591),(1018,750)])+[obs((14.77,16.88,1.1),(520,449)),obs((17.83,16.88,1.1),(1130,422))],[13.7,11.8,1.65,.40,-.1,0]),
 (12,kw([(373,40),(1140,65),(1140,550),(390,550)])+island([(237,757),(1373,719),(1685,879),(0,973)]),[16.1,11.8,1.65,.1,-.05,0]),
 (13.8,kw([(140,89),(860,89),(860,573),(153,573)])+[obs((17.995,14.835,.985),(790,765)),obs((17.995,13.465,.985),(662,945))],[18.0,12.,1.65,0,-.08,0]),
]

def residual(q,data):
    out=[]
    for p,t,w in data:
        uv=project(p,q)
        out.extend([(uv[0]-t[0])*w,(uv[1]-t[1])*w])
    # Weak physical priors; pixel data remains dominant.
    out.extend([(q[2]-1.65)*50,q[5]*450])
    return out

def linear(a,b):
    m=[list(row)+[v] for row,v in zip(a,b)];n=len(b)
    for k in range(n):
        j=max(range(k,n),key=lambda i:abs(m[i][k]));m[k],m[j]=m[j],m[k]
        if abs(m[k][k])<1e-12:return [0]*n
        d=m[k][k];m[k]=[v/d for v in m[k]]
        for i in range(n):
            if i!=k:
                d=m[i][k];m[i]=[v-d*w for v,w in zip(m[i],m[k])]
    return [row[-1] for row in m]

def fit(data,initial):
    q=list(initial);lam=.01
    for iteration in range(100):
        r=residual(q,data);loss=sum(v*v for v in r);cols=[]
        for j in range(6):
            trial=q[:];trial[j]+=.0001;rr=residual(trial,data);cols.append([(a-b)/.0001 for a,b in zip(rr,r)])
        a=[[sum(v*w for v,w in zip(cols[i],cols[j])) for j in range(6)] for i in range(6)]
        for i in range(6):a[i][i]+=lam*max(1,a[i][i])
        b=[-sum(v*w for v,w in zip(c,r)) for c in cols];delta=linear(a,b)
        candidate=[v+d for v,d in zip(q,delta)]
        candidate[2]=max(1.3,min(2.,candidate[2]));candidate[3]=max(-.5,min(1.15,candidate[3]));candidate[4]=max(-.6,min(.3,candidate[4]));candidate[5]=max(-.08,min(.08,candidate[5]))
        new=sum(v*v for v in residual(candidate,data))
        if new<loss:
            q=candidate;lam=max(1e-8,lam*.4)
            if abs(new-loss)<.00001:break
        else:lam=min(1e9,lam*6)
    return q

def solve():
    result=[]
    for sec,data,initial in ANCHORS:
        pose=fit(data,initial)
        landmarks=[{'world':p,'target':t,'projected':project(p,pose),'error_px':math.dist(project(p,pose),t)} for p,t,w in data]
        result.append({'seconds':sec,'pose':pose,'rmse_px':math.sqrt(sum(x['error_px']**2 for x in landmarks)/len(landmarks)),'landmarks':landmarks})
    return result

def build():
    import bpy
    from mathutils import Vector
    s=bpy.context.scene;cam=s.camera;solutions=solve()
    cam.animation_data_clear();cam.data.animation_data_clear();cam.data.lens=28;cam.data.sensor_width=36;cam.data.sensor_fit='HORIZONTAL';cam.data.shift_x=0;cam.data.shift_y=0;cam.rotation_mode='QUATERNION';cam.data.dof.use_dof=False
    # Smoothstep Hermite with time-aware central tangents, zero at opening hold.
    times=[a['seconds'] for a in solutions];poses=[a['pose'] for a in solutions]
    slopes=[]
    for i in range(len(poses)):
        lo=max(0,i-1);hi=min(len(poses)-1,i+1)
        slopes.append([0 if i<2 else (poses[hi][j]-poses[lo][j])/(times[hi]-times[lo]) for j in range(6)])
    for f in range(1,421):
        sec=(f-1)/30;i=next((i for i in range(7) if sec<=times[i+1]),6);dt=times[i+1]-times[i];t=(sec-times[i])/dt
        q=[(2*t**3-3*t*t+1)*poses[i][j]+(t**3-2*t*t+t)*dt*slopes[i][j]+(-2*t**3+3*t*t)*poses[i+1][j]+(t**3-t*t)*dt*slopes[i+1][j] for j in range(6)]
        x,y,z,yaw,pitch,roll=q;cam.location=(x,y,z)
        direction=Vector((math.sin(yaw)*math.cos(pitch),math.cos(yaw)*math.cos(pitch),math.sin(pitch)))
        rotation=direction.to_track_quat('-Z','Y')
        from mathutils import Quaternion
        cam.rotation_quaternion=rotation@Quaternion((0,0,1),roll)
        cam.keyframe_insert('location',frame=f);cam.keyframe_insert('rotation_quaternion',frame=f)
    s.render.fps=30;s.frame_start=1;s.frame_end=420;s.render.resolution_x=1920;s.render.resolution_y=1080;s.render.resolution_percentage=100
    base=Path(__file__).parent
    (base/'photoreal_camera_residuals.json').write_text(json.dumps({'method':'finite-difference Levenberg-Marquardt with manual source landmark targets','lens_mm':28,'window_geometry':'kitchen x14.77..17.83 z1.1..3.1; dining x10.46..13.86 z1.3..3.0; y16.88','acceptance':'not accepted; residuals expose geometry/silhouette mismatch','anchors':solutions},indent=2))
    s.frame_set(1)
    return solutions

if __name__=='__main__':
    print(json.dumps([{'seconds':a['seconds'],'pose':a['pose'],'rmse_px':a['rmse_px']} for a in solve()],indent=2))
