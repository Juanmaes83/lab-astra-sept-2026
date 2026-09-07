assert bpy.data.scenes.get('SOLACE_GATE_2') is None, 'Gate 2 scene already exists'
s=bpy.data.scenes.new('SOLACE_GATE_2')
bpy.context.window.scene=s
s.unit_settings.system='METRIC'; s.unit_settings.scale_length=1.0; s.unit_settings.length_unit='METERS'
s.world=bpy.data.worlds.new('SOLACE_REVIEW_WORLD')
s['source']=SOURCE
s['technical_status']='MACRO_QA_PENDING'
rect('SOLACE_SITE',40,56,644,612,z=-.30,h=.20,color=(.72,.78,.63,1),role='estimated_site')
rect('SOLACE_HOUSE',106,111,558,410,z=-.21,h=.02,color=(.72,.78,.63,1),role='footprint_reference_below_grade')
rect('SPACE_WEST_WING',106,111,220,410)
rect('SPACE_EAST_WING',446,111,558,410)
rect('SPACE_LIVING',220,111,301,218,color=(.79,.75,.63,1))
rect('SPACE_DINING',301,111,368,218,color=(.81,.77,.65,1))
rect('SPACE_KITCHEN',368,111,446,218,color=(.79,.75,.63,1))
rect('SPACE_ENTRY',237,64,290,111)
rect('SPACE_PLANTED_COURTYARD',220,218,446,410,z=-.075,h=.06,color=(.62,.74,.48,1),role='open_air_courtyard_ground')
rect('SPACE_COVERED_OUTDOOR_DINING',301,218,393,281,z=.015,h=.04,color=(.77,.75,.64,1))
rect('SPACE_OPEN_LAWN',40,423,198,610,z=-.17,h=.08,color=(.62,.73,.48,1))
rect('SPACE_PRIVATE_GARDEN',450,413,589,481,z=-.17,h=.08,color=(.65,.76,.51,1))
rect('SPACE_SUN_TERRACE',214,413,447,581,z=-.14,h=.09,color=(.77,.74,.64,1))
pool=box('POOL_LAP',(px(329),py(516),-.025),(10,3.5,.15),(.30,.61,.63,1),'lap_pool_water_blockout')
pool['dimension_class']='VERIFIED_FROM_SOURCE_XY_ESTIMATED_Z'
pool['verified_dimensions_m']=[10.0,3.5]
camdata=bpy.data.cameras.new('CAMERA_TOP_REVIEW_DATA')
cam=bpy.data.objects.new('CAMERA_TOP_REVIEW',camdata); s.collection.objects.link(cam)
cam.location=(px(342),py(333),48); cam.rotation_euler=(0,0,0)
camdata.type='ORTHO'; camdata.ortho_scale=36
cam['role']='fixed_north_up_review_camera'
camdata=bpy.data.cameras.new('CAMERA_PERSPECTIVE_REVIEW_DATA')
cam=bpy.data.objects.new('CAMERA_PERSPECTIVE_REVIEW',camdata); s.collection.objects.link(cam)
cam.location=(40,-34,36); cam.rotation_euler=(Vector((12,5,0))-cam.location).to_track_quat('-Z','Y').to_euler()
camdata.type='ORTHO'; camdata.ortho_scale=43
cam['role']='fixed_perspective_review_camera'
setup_render()
bpy.context.view_layer.update()
render_view('CAMERA_TOP_REVIEW','00-macro-top.png')
bpy.ops.wm.save_as_mainfile(filepath=BASE+'outputs/solace/SOLACE_BLOCKOUT_v01.blend',check_existing=True)
print(json.dumps({'stage':'macro','blender':bpy.app.version_string,'scene':s.name,'objects':len(s.objects),'house_dimensions':list(bpy.data.objects['SOLACE_HOUSE'].dimensions),'pool_dimensions':list(pool.dimensions),'retained_scenes':[sc.name for sc in bpy.data.scenes]}))
