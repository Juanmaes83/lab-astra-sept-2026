import bpy,sys,json,time
from pathlib import Path
s=bpy.context.scene
p=bpy.context.preferences.addons['cycles'].preferences;p.compute_device_type='OPTIX';p.get_devices()
for d in p.devices:d.use=d.type=='OPTIX'
s.cycles.device='GPU';s.render.use_persistent_data=True
args=sys.argv[sys.argv.index('--')+1:] if '--' in sys.argv else []
mode=args[0] if args else 'preview'
out=Path(bpy.data.filepath).parent/(args[1] if len(args)>1 else 'preview_r01');out.mkdir(exist_ok=True,parents=True)
print('RENDER_DEVICE',[(d.name,d.type,d.use) for d in p.devices],flush=True)
if mode=='preview':
    s.render.resolution_percentage=50;s.cycles.samples=48;s.cycles.adaptive_min_samples=16;s.cycles.adaptive_threshold=.04
    for f in [1,61,121,181,241,301,361,415,420]:
        s.frame_set(f);s.render.filepath=str(out/f'anchor_{f:04d}.png');bpy.ops.render.render(write_still=True)
else:
    s.render.filepath=str(out)+'/'
    s.render.use_overwrite=False
    bpy.ops.render.render(animation=True)
print('RENDER_FINISHED',mode,flush=True)
