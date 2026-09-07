assert bpy.context.scene.name=='SOLACE_GATE_2'
s=bpy.context.scene
required=['ENTRY','LIVING','DINING','KITCHEN','COVERED_OUTDOOR_DINING','PLANTED_COURTYARD','OFFICE','FAMILY_BATH','BEDROOM_02','BEDROOM_03','PANTRY','LAUNDRY','GUEST_WC','PLANT_STORE','PRIMARY_BATH','DRESSING','PRIMARY_BEDROOM','PRIVATE_GARDEN','OPEN_LAWN','SUN_TERRACE']
assert all(s.objects.get('SPACE_'+n) is not None for n in required)
assert not any(o.name in ['Cube','Camera','Light','LAB_TEST_CUBE'] for o in s.objects)
assert s.unit_settings.system=='METRIC' and s.unit_settings.scale_length==1
bpy.context.view_layer.update()
assert all(abs(a-b)<.00001 for a,b in zip(s.objects['POOL_LAP'].dimensions[:2],[10,3.5]))
assert all(abs(a-b)<.00001 for a,b in zip(s.objects['SPACE_PLANTED_COURTYARD'].dimensions[:2],[12.4,10.8]))
assert all(abs(a-b)<.00001 for a,b in zip(s.objects['SOLACE_HOUSE'].dimensions[:2],[25.4,17]))
assert s.objects['SPACE_LIVING'].location.x<s.objects['SPACE_DINING'].location.x<s.objects['SPACE_KITCHEN'].location.x
assert s.objects['POOL_LAP'].location.y<s.objects['SPACE_PLANTED_COURTYARD'].location.y
assert s.objects['SPACE_ENTRY'].location.y>s.objects['SPACE_DINING'].location.y
# Export flat color swatches only; no textures or premium materials.
palette={}
for o in s.objects:
    if o.type=='MESH':
        key=tuple(round(c,3) for c in o.color)
        if key not in palette:
            mat=bpy.data.materials.new('SOLACE_FLAT_'+str(len(palette)))
            mat.diffuse_color=key
            mat.roughness=1.0
            palette[key]=mat
        o.data.materials.append(palette[key])
    if o.type=='CAMERA':
        o['reference_source']=SOURCE
        o['dimension_class']='ESTIMATED_FOR_BLOCKOUT'
house=s.objects['SOLACE_HOUSE']
house['dimension_class']='VERIFIED_FROM_SOURCE_XY_ESTIMATED_Z'
house['verified_dimensions_m']=[25.4,17.0]
objects=[]
for o in s.objects:
    annotated=o.name in ['SOLACE_HOUSE','POOL_LAP','SPACE_PLANTED_COURTYARD']
    objects.append({'semantic_name':o.name,'type':o.type,'role':o.get('role','review_camera'),'transform':{'position_m':list(o.location),'rotation_euler_radians':list(o.rotation_euler),'scale':list(o.scale)},'dimensions_m':list(o.dimensions),'dimension_classification':{'x':'VERIFIED_FROM_SOURCE' if annotated else 'ESTIMATED_FOR_BLOCKOUT','y':'VERIFIED_FROM_SOURCE' if annotated else 'ESTIMATED_FOR_BLOCKOUT','z':'ESTIMATED_FOR_BLOCKOUT'},'transform_classification':'ESTIMATED_FOR_BLOCKOUT','verification_confidence':'high_annotation_only' if annotated else 'medium_visual_blockout','reference_source':SOURCE,'camera_ortho_scale':o.data.ortho_scale if o.type=='CAMERA' else None})
manifest={'project':'SOLACE — THE GARDEN HOUSE / CONCEPT 01','scene':s.name,'blender_version':bpy.app.version_string,'source':SOURCE,'technical_gate_2_candidate':'PASS','human_review':'PENDING','units':{'system':s.unit_settings.system,'scale_length':s.unit_settings.scale_length},'blend':'outputs/solace/SOLACE_BLOCKOUT_v04.blend','export':'evidence/gate-2-solace/SOLACE_BLOCKOUT_v01.glb','object_count':len(objects),'objects':objects,'limitations':['Concept drawing, not survey/BIM.','All room partitions, door/window widths, exterior boundaries and heights estimated.','Courtyard annotation constrains planted surface; gallery wall clear width remains approximately 12.59 m from image strokes.','Coverage is an open frame; window sills indicate simplified glazing gaps, not detailed window assemblies.','Gate 1 scene retained separately in blend, excluded from active-scene GLB.']}
s['technical_status']='TECHNICAL_PASS_HUMAN_REVIEW_PENDING'
bpy.ops.wm.save_as_mainfile(filepath=BASE+'outputs/solace/SOLACE_BLOCKOUT_v04.blend',check_existing=True)
export_result=bpy.ops.export_scene.gltf(filepath=EVID+'SOLACE_BLOCKOUT_v01.glb',export_format='GLB',use_active_scene=True,export_cameras=True,export_extras=True)
assert 'FINISHED' in export_result
print('GATE_MANIFEST='+json.dumps(manifest))
