"""
juju Julien BROUZES
"""
bl_info = {
    "name": "Voxel & Volume",
    "blender": (5, 0, 1),
    "category": "Object",
    "version": (0, 0, 1, 0)
}

import bpy


## CLEAN ##
#bpy.ops.object.select_all(action='SELECT')
#bpy.ops.object.delete(use_global=False, confirm=False)

scene = bpy.context.scene
locator_position = [0, 0, 0]


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

## VOLUME ##
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
    bpy.ops.object.empty_add(scale=(4, 4, 4))
    volume_collection.objects.link(bpy.context.active_object)
    #bpy.ops.object.volume_add()
    bpy.ops.object.parent_set(type='OBJECT', keep_transform=True)
    toggle_mesh_visibility()

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



### CLASS ###
class OBJECT_OT_create_ground(bpy.types.Operator):
    bl_idname = "object.create_ground"
    bl_label = "Create Ground"
    bl_description = "Generate a voxel ground"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        props = context.scene.voxel_terrain_props
        ground_num = int(props.ground_num_slider)
        ground_generation(ground_num)
        return {'FINISHED'}


class VoxelTerrainProperties(bpy.types.PropertyGroup):
    ground_num_slider: bpy.props.IntProperty(
        name="Ground Size",
        description="Size_Grid",
        default=5,
        min=1,
        max=20
    )
    
### GEOMETRY CLASS BEGIN ###

class Create_Cube(bpy.types.Operator):
    bl_idname = "object.create_cube_voxel"
    bl_label = "create_cube_voxel"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        
        create_cube_vox()
        return {'FINISHED'}

class Create_Sphere(bpy.types.Operator):
    bl_idname = "object.create_sphere_voxel"
    bl_label = "create_sphere_voxel"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        
        create_sphere_vox()
        return {'FINISHED'}
    
    
class mesh_to_Volume(bpy.types.Operator):
    bl_idname = "object.mesh_to_volume"
    bl_label = "mesh_to_volume"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        
        mesh_to_volume()
        return {'FINISHED'}


class hide_mesh(bpy.types.Operator):
    bl_idname = "object.hide_mesh"
    bl_label = "hide_mesh"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        #props = context.scene.voxel_terrain_props
        toggle_mesh_visibility()
        return {'FINISHED'}


class volume_to_Mesh(bpy.types.Operator):
    bl_idname = "object.volume_to_mesh"
    bl_label = "volume_to_mesh"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        #props = context.scene.voxel_terrain_props
        volume_to_mesh()
        return {'FINISHED'}


### GEOMETRY CLASS  END ###

## Voxel ##
class Convert_Voxel(bpy.types.Operator):
    bl_idname = "object.convert_voxel"
    bl_label = "convert_voxel"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        #props = context.scene.voxel_terrain_props
        biere = bpy.context.active_object
        create_voxel(biere, name="name")
        return {'FINISHED'}


### UI BEGIN ###

class VIEW3D_PT_VoxelTerrainGeneration(bpy.types.Panel):
    bl_label = "Voxel & Volume Generation"
    bl_idname = "VIEW3D_PT_Voxel_Terrain_Generation"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Voxel Terrain"
    
    def draw(self, context):
        layout = self.layout
        props = context.scene.voxel_terrain_props
        
        
        layout.label(text="Terrain Settings")
        layout.prop(props, "ground_num_slider", text="Grid Size")
        layout.operator("object.create_ground", text="Generate Ground")
        layout.label(text="Geometry")
        layout.operator("object.create_cube_voxel", text="Generate cube")
        layout.operator("object.create_sphere_voxel", text="Generate sphere")
        layout.operator("object.convert_voxel", text="Convert to Voxel")
        layout.label(text="VOLUME")
        layout.label(text="Select Mesh")
        layout.operator("object.mesh_to_volume", text="mesh to Volume")
        layout.operator("object.hide_mesh", text="hide / unhide mesh")
        layout.label(text='Select volume')
        layout.operator("object.volume_to_mesh", text="volume to Mesh")
        
        #layout.label(text='truc')
        #object.volume_to_mesh
        #layout.operator
        

### UI END ###



# REGISTER
def register():
    bpy.utils.register_class(OBJECT_OT_create_ground)
    bpy.utils.register_class(VoxelTerrainProperties)
    bpy.utils.register_class(VIEW3D_PT_VoxelTerrainGeneration)
    bpy.utils.register_class(Create_Cube)
    bpy.utils.register_class(Create_Sphere)
    bpy.utils.register_class(Convert_Voxel)
    bpy.utils.register_class(mesh_to_Volume)
    bpy.utils.register_class(volume_to_Mesh)
    bpy.utils.register_class(hide_mesh)
    
    bpy.types.Scene.voxel_terrain_props = bpy.props.PointerProperty(type=VoxelTerrainProperties)

def unregister():
    del bpy.types.Scene.voxel_terrain_props
    bpy.utils.unregister_class(VIEW3D_PT_VoxelTerrainGeneration)
    bpy.utils.unregister_class(VoxelTerrainProperties)
    bpy.utils.unregister_class(Create_Cube)
    bpy.utils.unregister_class(Create_Sphere)
    bpy.utils.unregister_class(Convert_Voxel)
    bpy.utils.unregister_class(mesh_to_Volume)
    bpy.utils.unregister_class(volume_to_Mesh)
    bpy.utils.unregister_class(OBJECT_OT_create_ground)
    bpy.utils.unregister_class(hide_mesh)

if __name__ == "__main__":
    register()
    

"""
juju Julien BROUZES
"""