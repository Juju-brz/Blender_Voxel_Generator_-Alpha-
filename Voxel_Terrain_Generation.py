"""
juju Julien BROUZES
"""

import bpy

# Nettoyage de la scène
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False, confirm=False)

# Paramètres
locator_position = [0, 0, 0]

#voxel_shape = null

def create_voxel(biere, name="name"):
    biere = bpy.ops.object.modifier_add(type='REMESH')
    biere = bpy.context.object.modifiers["Remesh"].voxel_size = 0.123
    biere = bpy.ops.object.modifier_apply(modifier="Remesh")
    biere = bpy.context.active_object
    biere.name = name 

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


    
class OBJECT_OT_create_ground(bpy.types.Operator):
    bl_idname = "object.create_ground"
    bl_label = "Create Ground"
    bl_description = "Generate a voxel ground"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        props = context.scene.voxel_terrain_props
        # Utiliser la valeur du slider
        ground_num = int(props.ground_num_slider)
        ground_generation(ground_num)
        return {'FINISHED'}


class VoxelTerrainProperties(bpy.types.PropertyGroup):
    ground_num_slider: bpy.props.IntProperty(
        name="Ground Size",
        description="Taille de la grille (nombre de cubes depuis le centre)",
        default=5,
        min=1,
        max=20
    )
    
### GEOMETRY CLASS ###

class Create_Cube(bpy.types.Operator):
    bl_idname = "object.create_cube_voxel"
    bl_label = "create_cube_voxel"
    bl_description = "Generate a voxel ground"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        props = context.scene.voxel_terrain_props
        # Utiliser la valeur du slider
        create_cube_vox()
        return {'FINISHED'}

class Create_Sphere(bpy.types.Operator):
    bl_idname = "object.create_sphere_voxel"
    bl_label = "create_sphere_voxel"
    bl_description = "Generate a voxel ground"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        props = context.scene.voxel_terrain_props
        # Utiliser la valeur du slider
        create_sphere_vox()
        return {'FINISHED'}

### GEOMETRY CLASS ###


### UI ###

class VIEW3D_PT_VoxelTerrainGeneration(bpy.types.Panel):
    bl_label = "Voxel Terrain Generation"
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
        layout.operator("object.create_cube_voxel", text="Generate cube")
        layout.operator("object.create_sphere_voxel", text="Generate sphere")


### UI ###



# REGISTER
def register():
    bpy.utils.register_class(OBJECT_OT_create_ground)
    bpy.utils.register_class(VoxelTerrainProperties)
    bpy.utils.register_class(VIEW3D_PT_VoxelTerrainGeneration)
    bpy.utils.register_class(Create_Cube)
    bpy.utils.register_class(Create_Sphere)
    bpy.types.Scene.voxel_terrain_props = bpy.props.PointerProperty(type=VoxelTerrainProperties)

def unregister():
    del bpy.types.Scene.voxel_terrain_props
    bpy.utils.unregister_class(VIEW3D_PT_VoxelTerrainGeneration)
    bpy.utils.unregister_class(VoxelTerrainProperties)
    bpy.utils.unregister_class(Create_Cube)
    bpy.utils.unregister_class(Create_Sphere)
    bpy.utils.unregister_class(OBJECT_OT_create_ground)

if __name__ == "__main__":
    register()