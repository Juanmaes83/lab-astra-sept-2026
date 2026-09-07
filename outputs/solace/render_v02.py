import bpy
prefs=bpy.context.preferences.addons['cycles'].preferences
prefs.compute_device_type='OPTIX'
prefs.get_devices()
for device in prefs.devices:device.use=device.type=='OPTIX'
s=bpy.context.scene;s.cycles.device='GPU'
print('RENDER_DEVICES',[(d.name,d.type,d.use) for d in prefs.devices])
bpy.ops.render.render(animation=True)
