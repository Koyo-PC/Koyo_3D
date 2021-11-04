import os
import bpy
import time

localPath = os.path.dirname(bpy.data.filepath)

# collection_N = bpy.data.collections.get("Normal")
collection_N_1 = bpy.data.collections.get("Normal_1F")
collection_N_2 = bpy.data.collections.get("Normal_2F")
collection_N_3 = bpy.data.collections.get("Normal_3F")
collection_N_4 = bpy.data.collections.get("Normal_4F")
collection_N_C = bpy.data.collections.get("Normal_Ceiling")

# collection_S = bpy.data.collections.get("Special")
collection_S_1 = bpy.data.collections.get("Special_1F")
collection_S_2 = bpy.data.collections.get("Special_2F")
collection_S_3 = bpy.data.collections.get("Special_3F")
collection_S_4 = bpy.data.collections.get("Special_4F")
collection_S_C = bpy.data.collections.get("Special_Ceiling")

collection_B_1_1F = bpy.data.collections.get("Bridge1_1F")
collection_B_1_C = bpy.data.collections.get("Bridge1_C")

collection_B_2_1F = bpy.data.collections.get("Bridge2_1F")
collection_B_2_C = bpy.data.collections.get("Bridge2_C")

collection_C_1 = bpy.data.collections.get("Cafe_1F")
collection_C_2 = bpy.data.collections.get("Cafe_2F")
collection_C_C = bpy.data.collections.get("Cafe_Ceiling")

collection_G_1 = bpy.data.collections.get("Gym_1F")
collection_G_C = bpy.data.collections.get("Gym_Ceiling")

collection_Ground = bpy.data.collections.get("NatureObjects")

collection_A_B_1F = bpy.data.collections.get("Auditorium_B_1F")
collection_A_B_C = bpy.data.collections.get("Auditorium_B_Ceiling")
collection_A_1F = bpy.data.collections.get("Auditorium_1F")
collection_A_C = bpy.data.collections.get("Auditorium_Ceiling")

def selectCollection(collection):
    time.sleep(.1)
    for obj in collection.all_objects:
        obj.select_set(True)


def deselectAll():
    bpy.ops.object.select_all(action='DESELECT')
    time.sleep(.1)


def export_targets_obj(arg_filepath, collection):

    time.sleep(.1)
    collection.hide_render = False
    time.sleep(.1)
    collection.hide_select = False
    time.sleep(.1)
    collection.hide_viewport = False
    time.sleep(.1)
    deselectAll()
    selectCollection(collection)

    # https://docs.blender.org/api/2.82a/bpy.ops.export_scene.html#bpy.ops.export_scene.obj
    bpy.ops.export_scene.obj(
        filepath=arg_filepath,
        filter_glob="*.obj",
        use_selection=True,
        axis_forward='X',
        use_uvs=False,
        use_materials=False,
        use_triangles=True
    )

# -----
print(localPath)

export_targets_obj(localPath + "/exports/3dMap_south_1F.obj", collection_N_1)
export_targets_obj(localPath + "/exports/3dMap_south_2F.obj", collection_N_2)
export_targets_obj(localPath + "/exports/3dMap_south_3F.obj", collection_N_3)
export_targets_obj(localPath + "/exports/3dMap_south_4F.obj", collection_N_4)
export_targets_obj(localPath + "/exports/3dMap_south_ceiling.obj", collection_N_C)
export_targets_obj(localPath + "/exports/3dMap_north_1F.obj", collection_S_1)
export_targets_obj(localPath + "/exports/3dMap_north_2F.obj", collection_S_2)
export_targets_obj(localPath + "/exports/3dMap_north_3F.obj", collection_S_3)
export_targets_obj(localPath + "/exports/3dMap_north_4F.obj", collection_S_4)
export_targets_obj(localPath + "/exports/3dMap_north_ceiling.obj", collection_S_C)

export_targets_obj(localPath + "/exports/3dMap_east_bridge.obj", collection_B_1_1F)
export_targets_obj(localPath + "/exports/3dMap_east_ceiling.obj", collection_B_1_C)
export_targets_obj(localPath + "/exports/3dMap_west_bridge.obj", collection_B_2_1F)
export_targets_obj(localPath + "/exports/3dMap_west_ceiling.obj", collection_B_2_C)

export_targets_obj(localPath + "/exports/3dMap_cafe_1F.obj", collection_C_1)
export_targets_obj(localPath + "/exports/3dMap_cafe_2F.obj", collection_C_2)
export_targets_obj(localPath + "/exports/3dMap_cafe_ceiling.obj", collection_C_C)
export_targets_obj(localPath + "/exports/3dMap_gym.obj", collection_G_1)
export_targets_obj(localPath + "/exports/3dMap_gym_ceiling.obj", collection_G_C)
export_targets_obj(localPath + "/exports/3dMap_ground.obj", collection_Ground)
export_targets_obj(localPath + "/exports/3dMap_audi_bridge.obj", collection_A_B_1F)
export_targets_obj(localPath + "/exports/3dMap_audi_bridge_ceiling.obj", collection_A_B_C)
export_targets_obj(localPath + "/exports/3dMap_audi.obj", collection_A_1F)
export_targets_obj(localPath + "/exports/3dMap_audi_ceiling.obj", collection_A_C)