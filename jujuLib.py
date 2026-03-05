import bpy
## CLEAN ##
def clean_scene():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False, confirm=False)

#scene = bpy.context.scene
#locator_position = [0, 0, 0]


def create_voxel(biere, name="name"):
    biere = bpy.ops.object.modifier_add(type='REMESH')
    biere = bpy.context.object.modifiers["Remesh"].voxel_size = 0.123
    biere = bpy.ops.object.modifier_apply(modifier="Remesh")
    biere = bpy.context.active_object
    biere.name = name 


def decimate():
    bpy.ops.object.modifier_add(type='DECIMATE')
    bpy.context.object.modifiers["Decimate"].decimate_type = 'DISSOLVE'
    bpy.ops.object.modifier_apply(modifier="Decimate")


def create_cube_vox():
    biere = bpy.ops.mesh.primitive_cube_add()
    create_voxel(biere, name="voxel_cube")


def create_sphere_vox():
    biere = bpy.ops.mesh.primitive_uv_sphere_add()
    create_voxel(biere, name="voxel_sphere")
    
def ground_generation(ground_num):
    
    for i in range(-ground_num, ground_num + 1):
        for j in range(-ground_num, ground_num + 1):
            x_pos = locator_position[0] + (i * 2)
            y_pos = locator_position[1] + (j * 2)
            z_pos = locator_position[2]
            
            
            bpy.ops.mesh.primitive_cube_add(location=(x_pos, y_pos, z_pos) )
            bpy.context.object.name = f"ground"

### VOLUME ###
def mesh_to_volume():
    volume_collection = bpy.data.collections.new("volume")
    bpy.context.scene.collection.children.link(volume_collection)
    
    mesh_to_convert = bpy.context.active_object
    mesh_to_convert.name = "mesh_volume" 
    volume_collection.objects.link(bpy.context.active_object)
    bpy.ops.collection.objects_remove_active()
    bpy.ops.object.volume_add()
    #mesh_to_convert.hide_viewport = True
    bpy.ops.object.modifier_add(type='MESH_TO_VOLUME')
    bpy.context.object.modifiers["Mesh to Volume"].object = mesh_to_convert
    
    volume_collection.objects.link(bpy.context.active_object)
    bpy.ops.collection.objects_remove_active()
    
    # CREATE EMPTY
    empty = bpy.ops.object.empty_add(scale=(4, 4, 4))
    empty = volume_collection.objects.link(bpy.context.active_object)
    #empty = bpy.ops.collection.objects_remove_active()
    #bpy.ops.object.volume_add()
    bpy.ops.object.parent_set(type='OBJECT', keep_transform=True)
    toggle_mesh_visibility()

def new_collection(a, collection):
    a = collection.objects.link(bpy.context.active_object)
    
    

def toggle_mesh_visibility():
    obj = bpy.data.objects["mesh_volume"]
    obj.hide_viewport = not obj.hide_viewport


def volume_to_mesh():
    vol_to_convert = bpy.context.active_object
    bpy.ops.mesh.primitive_cube_add()
    obj = bpy.context.active_object
    obj.name = "volume_mesh"
    bpy.ops.object.modifier_add(type='VOLUME_TO_MESH')

    bpy.context.object.modifiers["Volume to Mesh"].object = vol_to_convert
    bpy.ops.object.modifier_apply(modifier="Volume to Mesh")

def simulation_node():
    bpy.context.area.ui_type = 'GeometryNodeTree'
    bpy.ops.node.new_geometry_nodes_modifier()
    #bpy.ops.node.add_zone(use_transform=True, input_node_type="GeometryNodeSimulationInput", output_node_type="GeometryNodeSimulationOutput", add_default_geometry_link=True)
    bpy.data.node_groups["Geometry Nodes"].name = "Simulation Nodes"

