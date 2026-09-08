"""CC0 Poly Haven pine integration; call build() in versioned working scene.

Leaves retain authored alpha cutout. Shared collection instances avoid mesh duplication.
Source: https://polyhaven.com/a/pine_sapling_small (Rico Cilliers, Rob Tuytel).
"""
import bpy
import math
from pathlib import Path
from mathutils import Vector

BASE = Path(__file__).resolve().parent / 'assets' / 'pine_sapling_small'


def build():
    scene = bpy.context.scene
    before_images = set(bpy.data.images)
    path = BASE / 'pine_sapling_small_2k.blend'
    with bpy.data.libraries.load(str(path), link=False) as (src, dst):
        dst.objects = list(src.objects)
    collection = bpy.data.collections.new('PHOTO_CC0_Pine_master')
    loaded = [o for o in dst.objects if o is not None]
    for ob in loaded:
        if ob.type in {'MESH', 'EMPTY', 'CURVE', 'ARMATURE'}:
            collection.objects.link(ob)
            ob.hide_render = False
    mesh_objects = [ob for ob in collection.objects if ob.type == 'MESH']
    if not mesh_objects:
        raise RuntimeError('Poly Haven pine contains no mesh objects')
    # Imported 2K shaders get compact source-authored JPG maps. Alpha stays 2K PNG.
    imported_materials = set()
    for ob in mesh_objects:
        for material in ob.data.materials:
            if material and material.use_nodes: imported_materials.add(material)
    replaced = {}
    for material in imported_materials:
        for node in list(material.node_tree.nodes):
            if node.type != 'TEX_IMAGE' or not node.image: continue
            old = node.image
            filename = Path(old.filepath.replace('\\', '/')).name
            compact = None
            for token in ['bark_diff','bark_nor_gl','bark_rough','twig_diff','twig_nor_gl','twig_rough']:
                if token in filename:
                    compact = BASE / 'review_textures' / ('pine_sapling_small_' + token + '_1k.jpg')
                    break
            # Displacement and unused mask data add no useful detail at this distance.
            if '_disp_' in filename or '_mask_' in filename:
                for link in list(node.outputs['Color'].links): material.node_tree.links.remove(link)
                material.node_tree.nodes.remove(node)
                continue
            if compact is None:
                compact = BASE / 'textures' / filename
            if not compact.exists():
                raise FileNotFoundError('Required pine texture: ' + str(compact))
            if str(compact) not in replaced:
                image = bpy.data.images.load(str(compact), check_existing=True)
                image.colorspace_settings.name = 'sRGB' if '_diff_' in filename else 'Non-Color'
                replaced[str(compact)] = image
            node.image = replaced[str(compact)]
    # Dispose only orphan images brought in by this import, never existing scene data.
    for image in list(bpy.data.images):
        if image not in before_images and image.users == 0:
            bpy.data.images.remove(image)
    points = [ob.matrix_world @ Vector(c) for ob in mesh_objects for c in ob.bound_box]
    zmin = min(p.z for p in points)
    height = max(p.z for p in points) - zmin
    xmid = (min(p.x for p in points) + max(p.x for p in points)) / 2
    ymid = (min(p.y for p in points) + max(p.y for p in points)) / 2
    if height < .1: raise RuntimeError('Invalid imported pine bounding box')
    collection.instance_offset = (xmid, ymid, zmin)
    # Irregular foreground silhouettes; HDRI supplies distant forest and sky gaps.
    sites = [(4.6,23.7,7.7,.4),(7.5,21.4,6.1,2.2),(10.3,24,8.8,4.8),
             (12.6,21.9,6.7,1.4),(15.2,23.4,8.0,3.6),(18.1,20.5,6.2,5.4),
             (20.5,23.1,8.5,.8),(23.7,21.9,7.0,2.8)]
    for i,(x,y,h,angle) in enumerate(sites):
        ob = bpy.data.objects.new('PHOTO_CC0_Pine_%02d' % i,None)
        ob.instance_type = 'COLLECTION'; ob.instance_collection = collection
        scene.collection.objects.link(ob)
        ob.location = (x,y,max(0,y-21)*.052)
        ob.rotation_euler = (math.radians((i%3-1)*1.3),0,angle)
        scale = h/height
        ob.scale = (scale*.83, scale*(.83+(i%3)*.04), scale)
        ob['provenance'] = 'https://polyhaven.com/a/pine_sapling_small | CC0'
    scene.cycles.transparent_max_bounces = max(scene.cycles.transparent_max_bounces, 12)
    triangles = sum(sum(len(p.vertices)-2 for p in ob.data.polygons) for ob in mesh_objects)
    return {'instances':len(sites),'unique_mesh_triangles':triangles,
            'original_height':height,'used_texture_bytes':sum(Path(p).stat().st_size for p in replaced),
            'source':'https://polyhaven.com/a/pine_sapling_small','license':'CC0'}
