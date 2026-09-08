assert bpy.context.scene.name=='SOLACE_GATE_2'
court=bpy.data.objects['SPACE_PLANTED_COURTYARD']
before=list(court.dimensions)
court.dimensions=(12.4,10.8,.06)
court['dimension_class']='VERIFIED_FROM_SOURCE_XY_ESTIMATED_Z'
court['verified_dimensions_m']=[12.4,10.8]
# Three crude reference volumes, no detailed furnishings/materials.
rect('HELPER_LIVING_SOFA_REFERENCE',233,149,291,164,z=.35,h=.70,color=(.87,.83,.70,1),role='estimated_function_scale_placeholder')
rect('HELPER_DINING_TABLE_REFERENCE',321,136,339,179,z=.37,h=.74,color=(.69,.56,.37,1),role='estimated_function_scale_placeholder')
rect('HELPER_KITCHEN_ISLAND_REFERENCE',377,150,425,172,z=.45,h=.90,color=(.69,.56,.37,1),role='estimated_function_scale_placeholder')
bpy.context.view_layer.update()
s=bpy.context.scene
s.display.shading.show_shadows=False
s.display.shading.light='FLAT'
render_view('CAMERA_TOP_REVIEW','03-top-verified.png')
s.display.shading.light='STUDIO'
s.display.shading.show_shadows=False
render_view('CAMERA_PERSPECTIVE_REVIEW','04-perspective-verified.png')
s.camera=bpy.data.objects['CAMERA_TOP_REVIEW']
s.display.shading.light='FLAT'
s['technical_status']='AWAITING_FINAL_VISUAL_QA'
bpy.ops.wm.save_as_mainfile(filepath=BASE+'outputs/solace/SOLACE_BLOCKOUT_v03.blend',check_existing=True)
print(json.dumps({'correction':'courtyard_surface_annotation_and_review_readability','courtyard_before':before,'courtyard_after':list(court.dimensions),'top_camera_location':list(bpy.data.objects['CAMERA_TOP_REVIEW'].location),'top_camera_rotation':list(bpy.data.objects['CAMERA_TOP_REVIEW'].rotation_euler),'top_camera_ortho_scale':bpy.data.objects['CAMERA_TOP_REVIEW'].data.ortho_scale,'object_count':len(s.objects)}))
