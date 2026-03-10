"""
juju Julien BROUZES
"""


import bpy
import sys
import os
from . import juju
from . import GeoNode




### CLASS BEGIN ###
class OBJECT_OT_create_ground(bpy.types.Operator):
    bl_idname = "object.create_ground"
    bl_label = "Create Ground"
    bl_description = "Generate a voxel ground"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        props = context.scene.voxel_terrain_props
        ground_num = int(props.ground_num_slider)
        juju.ground_generation(ground_num)
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

class MESH_OT_Create_Cube(bpy.types.Operator):
    bl_idname = "object.create_cube_voxel"
    bl_label = "create_cube_voxel"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        
        juju.create_cube_vox()
        return {'FINISHED'}

class MESH_OT_Create_Sphere(bpy.types.Operator):
    bl_idname = "object.create_sphere_voxel"
    bl_label = "create_sphere_voxel"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        
        juju.create_sphere_vox()
        return {'FINISHED'}
    
    
class MESH_OT_mesh_to_Volume(bpy.types.Operator):
    bl_idname = "object.mesh_to_volume"
    bl_label = "mesh_to_volume"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        
        juju.mesh_to_volume()
        return {'FINISHED'}


class MESH_OT_hide_mesh(bpy.types.Operator):
    bl_idname = "object.hide_mesh"
    bl_label = "hide_mesh"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        #props = context.scene.voxel_terrain_props
        juju.toggle_mesh_visibility()
        return {'FINISHED'}


class volume_to_Mesh(bpy.types.Operator):
    bl_idname = "object.volume_to_mesh"
    bl_label = "volume_to_mesh"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        juju.volume_to_mesh()
        return {'FINISHED'}

class clean_scene(bpy.types.Operator):
    bl_idname = "object.clean_scene"
    bl_label = "clean_scene"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        juju.clean_scene()
        return {'FINISHED'}

class create_simulation_node(bpy.types.Operator):
    bl_idname = "object.create_simulation_node"
    bl_label = "create_simulation_node"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        juju.simulation_node()
        return {'FINISHED'}

class MESH_OT_subdivision_mesh(bpy.types.Operator):
    bl_idname = "object.subdivision_mesh"
    bl_label = "subdivision_mesh"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        juju.subdivision_mesh()
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
        juju.create_voxel(biere, name="name")
        return {'FINISHED'}


### PLANT GENERATOR  BEGIN ###
class draw_curve(bpy.types.Operator):
    bl_idname = "object.draw_curve"
    bl_label = "draw_curve"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        juju.draw_curve()
        return {'FINISHED'}

class MESH_OT_create_leaf(bpy.types.Operator):
    bl_idname = "object.create_leaf"
    bl_label = "create_leaf"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        juju.create_leaf(juju.create_leaf_shape)
        return {'FINISHED'}

class create_spike(bpy.types.Operator):
    bl_idname = "object.create_spike_shape"
    bl_label = "create_spike_shape"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        juju.create_leaf(juju.create_spike_shape)
        return {'FINISHED'}


class create_bezier_curve(bpy.types.Operator):
    bl_idname = "object.create_bezier_curve"
    bl_label = "create_bezier_curve"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        juju.create_bezier_curve()
        return {'FINISHED'}


### PLANT GENERATOR  END ###

### NODES  CLASS BEGIN ###
class NODE_OT_create_trunk(bpy.types.Operator):
    bl_idname = "object.create_trunk"
    bl_label = "create_trunk"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        node_tree_names : dict[typing.Callable, str] = {}
        GeoNode.create_trunk(node_tree_names)
        return {'FINISHED'}


class NODE_OT_volume_simulation(bpy.types.Operator):
    bl_idname = "object.volume_simulation"
    bl_label = "volume_simulation"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        node_tree_names : dict[typing.Callable, str] = {}
        GeoNode.volume_simulation(node_tree_names)
        return {'FINISHED'}

### NODES  CLASS END ###

### CLASS END  ###

### UI BEGIN ###


### 3D PANEL BEGIN ###
class VIEW3D_PT_VoxelTerrainGeneration(bpy.types.Panel):
    bl_label = "ORGANICS GENERATION"
    bl_idname = "VIEW3D_PT_Organics_Generation"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Organics Generation"
    
    def draw(self, context):
        layout = self.layout
        props = context.scene.voxel_terrain_props
        
        layout.operator("object.create_simulation_node", text="create_Geometry_node")
        layout.operator("object.clean_scene", text="Clean Scene (beta)")
        layout.label(text="Terrain Settings")
        layout.prop(props, "ground_num_slider", text="Grid Size")
        layout.operator("object.create_ground", text="Generate Ground")
        layout.label(text="Geometry")
        layout.operator("object.create_cube_voxel", text="Generate cube")
        layout.operator("object.create_sphere_voxel", text="Generate sphere")
        layout.operator("object.convert_voxel", text="Convert to Voxel")

class VIEW3D_PT_VolumeGeneration(bpy.types.Panel):
    bl_label = "VOLUME"
    #bl_idname = "VIEW3D_PT_Organics_Generation"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Organics Generation"

    def draw(self, context):
        layout = self.layout

        layout.label(text="Select Mesh")
        layout.operator("object.mesh_to_volume", text="mesh to Volume")
        layout.operator("object.hide_mesh", text="hide / unhide mesh")
        layout.label(text='Select volume')
        layout.operator("object.volume_to_mesh", text="volume to Mesh")
        layout.operator("object.subdivision_mesh", text="Subdivision_mesh")

class VIEW3D_PT_PlantGeneration(bpy.types.Panel):
    bl_label = "PLANT GENERATOR"
    #bl_idname = "VIEW3D_PT_Organics_Generation"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Organics Generation"

    def draw(self, context):
        layout = self.layout

        layout.label(text='Create Plant')
        layout.operator("object.draw_curve", text="Draw Curve")
        layout.operator("object.create_leaf", text="Draw leaf")
        layout.operator("object.create_bezier_curve", text="create_bezier_curve")
        layout.operator("object.create_spike_shape", text="create_spike")

### 3D PANEL END ###


### NODE PANEL BEGIN ###

class NODE_OT_juju_operator(bpy.types.Operator):
    bl_idname = "node.juju_operator"
    bl_label = "juju_operator"

    @classmethod
    def poll(cls, context):
        space = context.space_data
        return space.type == 'NODE_EDITOR'

    def execute(self, context):
        return {'FINISHED'}



class NODE_PT_juju_panel(bpy.types.Panel):
    bl_label = "Organics Generation"
    bl_idname = "NODE_PT_juju_panel"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category = "Organics Generation"


    @classmethod
    def poll(cls, context):

        space = context.space_data
        return space.type == 'NODE_EDITOR'

    def draw(self, context):
        layout = self.layout

        layout.label(text="My Nodes :", icon='NODETREE')
        layout.separator()

        # Bouton qui lance l'operator
        layout.operator("node.juju_operator", text="Create Nodes", icon='ADD')
        layout.label(text = "CURVES")
        #layout.operator("object.create_trunk", text="create_trunk")
        layout.operator("object.volume_simulation", text="volume_simulation")

class NODE_PT_Plant_Generator(bpy.types.Panel):
    bl_label = "Plant_Generator"
    bl_idname = "NODE_PT_Plant_Generatorl"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category = "Organics Generation"


    @classmethod
    def poll(cls, context):

        space = context.space_data
        return space.type == 'NODE_EDITOR'

    def draw(self, context):
        layout = self.layout

        layout.label(text="My Nodes :", icon='NODETREE')
        layout.separator()

        layout.operator("object.create_trunk", text="create_trunk")
### NODE PANEL END ###

### UI END ###


### REGISTER BEGIN ###
classes = [
    NODE_OT_juju_operator,
    NODE_PT_juju_panel,
]

def register():
    bpy.utils.register_class(VIEW3D_PT_VoxelTerrainGeneration)
    bpy.utils.register_class(VIEW3D_PT_VolumeGeneration)
    bpy.utils.register_class(VIEW3D_PT_PlantGeneration)

    bpy.utils.register_class(OBJECT_OT_create_ground)
    bpy.utils.register_class(VoxelTerrainProperties)

    bpy.utils.register_class(MESH_OT_Create_Cube)
    bpy.utils.register_class(MESH_OT_Create_Sphere)
    bpy.utils.register_class(Convert_Voxel)
    bpy.utils.register_class(MESH_OT_mesh_to_Volume)
    bpy.utils.register_class(volume_to_Mesh)
    bpy.utils.register_class(MESH_OT_hide_mesh)
    bpy.utils.register_class(clean_scene)
    bpy.utils.register_class(create_simulation_node)
    bpy.types.Scene.voxel_terrain_props = bpy.props.PointerProperty(type=VoxelTerrainProperties)
    bpy.utils.register_class(MESH_OT_subdivision_mesh)
    bpy.utils.register_class(draw_curve)
    bpy.utils.register_class(MESH_OT_create_leaf)
    bpy.utils.register_class(NODE_OT_create_trunk)
    bpy.utils.register_class(create_bezier_curve)
    bpy.utils.register_class(create_spike)
    bpy.utils.register_class(NODE_OT_volume_simulation)
    bpy.utils.register_class(NODE_PT_Plant_Generator)
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    del bpy.types.Scene.voxel_terrain_props
    bpy.utils.unregister_class(VIEW3D_PT_VoxelTerrainGeneration)
    bpy.utils.unregister_class(VIEW3D_PT_VolumeGeneration)
    bpy.utils.unregister_class(VIEW3D_PT_PlantGeneration)

    bpy.utils.unregister_class(VoxelTerrainProperties)
    bpy.utils.unregister_class(MESH_OT_Create_Cube)
    bpy.utils.unregister_class(MESH_OT_Create_Sphere)
    bpy.utils.unregister_class(Convert_Voxel)
    bpy.utils.unregister_class(MESH_OT_mesh_to_Volume)
    bpy.utils.unregister_class(volume_to_Mesh)
    bpy.utils.unregister_class(OBJECT_OT_create_ground)
    bpy.utils.unregister_class(MESH_OT_hide_mesh)
    bpy.utils.unregister_class(clean_scene)
    bpy.utils.unregister_class(create_simulation_node)
    bpy.utils.unregister_class(MESH_OT_subdivision_mesh)
    bpy.utils.unregister_class(draw_curve)
    bpy.utils.unregister_class(MESH_OT_create_leaf)
    bpy.utils.unregister_class(NODE_OT_create_trunk)
    bpy.utils.unregister_class(create_bezier_curve)
    bpy.utils.unregister_class(create_spike)
    bpy.utils.unregister_class(NODE_OT_volume_simulation)
    bpy.utils.unregister_class(NODE_PT_Plant_Generator)

if __name__ == "__main__":
    register()

### REGISTER END ###

"""
juju Julien BROUZES
"""
