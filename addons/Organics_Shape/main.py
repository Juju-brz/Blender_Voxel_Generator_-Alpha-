"""
juju Julien BROUZES
https://github.com/Juju-brz
"""

import bpy
import sys
import os
from . import juju
from . import GeoNode




### CLASS BEGIN ###

# class OBJECT_OT_create_ground(bpy.types.Operator):
#     bl_idname = "object.create_ground"
#     bl_label = "Create Ground"
#     bl_description = "Generate a voxel ground"
#     bl_options = {'REGISTER', 'UNDO'}
#
#     def execute(self, context):
#         props = context.scene.voxel_terrain_props
#         ground_num = int(props.ground_num_slider)
#         juju.ground_generation(ground_num)
#         return {'FINISHED'}


# class VoxelTerrainProperties(bpy.types.PropertyGroup):
#     ground_num_slider: bpy.props.IntProperty(
#         name="Ground Size",
#         description="Size_Grid",
#         default=5,
#         min=1,
#         max=20
#     )


### VOLUME CLASS BEGIN ###

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

class create_geometry_node(bpy.types.Operator):
    bl_idname = "object.create_geometry_node"
    bl_label = "create_geometry_node"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        juju.create_geometry_node()
        return {'FINISHED'}

class MESH_OT_subdivision_mesh(bpy.types.Operator):
    bl_idname = "object.subdivision_mesh"
    bl_label = "subdivision_mesh"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        juju.subdivision_mesh()
        return {'FINISHED'}

### VOLUME CLASS  END ###


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

class curve_test(bpy.types.Operator):
    bl_idname = "object.curve_test"
    bl_label = "curve_test"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        juju.curve_test()
        return {'FINISHED'}

class subdivid_curve(bpy.types.Operator):
    bl_idname = "object.subdivid_curve"
    bl_label = "subdivid_curve"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        juju.subdivid_curve()
        return {'FINISHED'}

class procedural_curve(bpy.types.Operator):
    bl_idname = "object.procedural_curve"
    bl_label = "procedural_curve"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        juju.procedural_arc_curve()
        return {'FINISHED'}

class fib_curve(bpy.types.Operator):
    bl_idname = "object.fib_curve"
    bl_label = "fib_curve"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        juju.fib_curve()
        return {'FINISHED'}

### PLANT GENERATOR  END ###

### NODES  CLASS BEGIN ###
class NODE_OT_create_trunk(bpy.types.Operator):
    bl_idname = "object.create_trunk"
    bl_label = "create_trunk"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        node_tree_names : dict[typing.Callable, str] = {}
        GeoNode.create_trunk_1_node_group(node_tree_names)
        return {'FINISHED'}


class NODE_OT_volume_simulation(bpy.types.Operator):
    bl_idname = "object.volume_simulation"
    bl_label = "volume_simulation"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        node_tree_names : dict[typing.Callable, str] = {}
        GeoNode.volume_simulation(node_tree_names)
        return {'FINISHED'}

class NODE_OT_sprinkle(bpy.types.Operator):
    bl_idname = "object.sprinkle"
    bl_label = "sprinkle"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        node_tree_names : dict[typing.Callable, str] = {}
        GeoNode.sprinkle_1_node_group(node_tree_names)
        return {'FINISHED'}

class NODE_OT_Grid_Volume(bpy.types.Operator):
    bl_idname = "object.grid_volume"
    bl_label = "grid_volume"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        node_tree_names : dict[typing.Callable, str] = {}
        GeoNode.grid_volume_1_node_group(node_tree_names)
        return {'FINISHED'}


class NODE_OT_Get_Normalize(bpy.types.Operator):
    bl_idname = "object.get_normalize"
    bl_label = "get normalize"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        node_tree_names : dict[typing.Callable, str] = {}
        GeoNode.getnormalize_1_node_group(node_tree_names)
        return {'FINISHED'}

class NODE_OT_delete_points_of_curve(bpy.types.Operator):
    bl_idname = "object.delete_points_of_curve"
    bl_label = "delete points of curve"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        node_tree_names : dict[typing.Callable, str] = {}
        GeoNode.delete_points_of_curve_1_node_group(node_tree_names)
        return {'FINISHED'}

### NODES  CLASS END ###

### CLASS END  ###

### UI BEGIN ###


### 3D PANEL BEGIN ###

class VIEW3D_PT_Organics_Generation(bpy.types.Panel):
    bl_label = "ORGANICS GENERATION"
    bl_idname = "VIEW3D_PT_Organics_Generation"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Organics Generation"
    
    def draw(self, context):
        layout = self.layout

        layout.label(text="by juju")
        layout.operator("object.create_geometry_node", text="create_Geometry_node")

class VIEW3D_PT_Volume_Generation(bpy.types.Panel):
    bl_label = "VOLUME"
    bl_idname = "VIEW3D_PT_VolumeGeneration"
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
    bl_idname = "VIEW3D_PT_PlantGeneration"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Organics Generation"

    def draw(self, context):
        layout = self.layout

        layout.label(text='Create Curve')
        layout.operator("object.draw_curve", text="Draw Curve")
        layout.operator("object.create_leaf", text="Draw leaf")
        layout.operator("object.create_bezier_curve", text="create bezier curve")


        layout.label(text='modify curve')
        layout.operator("object.create_spike_shape", text="create spike")
        layout.operator("object.subdivid_curve", text="subdivid curve")
        layout.label(text="Select Vertice of Curve on Edit Mode")
        layout.operator("object.curve_test", text="curve test")
        layout.operator("object.fib_curve", text="fib curve")


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


class NODE_PT_Organics_Generation(bpy.types.Panel):
    bl_label = "ORGANICS GENERATION"
    bl_idname = "NODE_PT_Organics_Generation"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category = "Organics Generation"


    @classmethod
    def poll(cls, context):

        space = context.space_data
        return space.type == 'NODE_EDITOR'

    def draw(self, context):
        layout = self.layout

        layout.operator("object.create_geometry_node", text="create geometry node")


class NODE_PT_Plant_Generator(bpy.types.Panel):
    bl_label = "PLANT GENERATOR"
    bl_idname = "NODE_PT_Plant_Generator"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category = "Organics Generation"


    @classmethod
    def poll(cls, context):

        space = context.space_data
        return space.type == 'NODE_EDITOR'

    def draw(self, context):
        layout = self.layout

        layout.label(text='create procedural curve')
        layout.operator("object.procedural_curve", text="Arc Curve")

        layout.label(text='modify curve')
        layout.operator("object.create_trunk", text="create_trunk")
        layout.operator("object.sprinkle", text="Spinkle")
        layout.operator("object.get_normalize", text="get normalize")
        layout.operator("object.delete_points_of_curve", text="delete points of curve")

class NODE_PT_Volume(bpy.types.Panel):
    bl_label = "VOLUME"
    bl_idname = "NODE_PT_Volume"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category = "Organics Generation"


    @classmethod
    def poll(cls, context):

        space = context.space_data
        return space.type == 'NODE_EDITOR'

    def draw(self, context):
        layout = self.layout

        layout.operator("object.volume_simulation", text="volume_simulation")
        layout.operator("object.grid_volume" , text="grid volume")


### NODE PANEL END ###

### UI END ###


### REGISTER BEGIN ###
classes = [
    NODE_OT_juju_operator,
    #NODE_PT_juju_panel,
]

def register():
    ## UI ##
    bpy.utils.register_class(VIEW3D_PT_Organics_Generation)
    bpy.utils.register_class(VIEW3D_PT_Volume_Generation)
    bpy.utils.register_class(VIEW3D_PT_PlantGeneration)
    bpy.utils.register_class(NODE_PT_Organics_Generation)
    bpy.utils.register_class(NODE_PT_Volume)
    bpy.utils.register_class(NODE_PT_Plant_Generator)


    bpy.utils.register_class(create_geometry_node)
    ## VOLUME ##
    bpy.utils.register_class(MESH_OT_mesh_to_Volume)
    bpy.utils.register_class(volume_to_Mesh)
    bpy.utils.register_class(MESH_OT_hide_mesh)
    bpy.utils.register_class(MESH_OT_subdivision_mesh)
    bpy.utils.register_class(NODE_OT_Grid_Volume)

    ## PLANT ##
    bpy.utils.register_class(draw_curve)
    bpy.utils.register_class(MESH_OT_create_leaf)
    bpy.utils.register_class(NODE_OT_create_trunk)
    bpy.utils.register_class(create_bezier_curve)
    bpy.utils.register_class(create_spike)
    bpy.utils.register_class(NODE_OT_volume_simulation)
    bpy.utils.register_class(NODE_OT_sprinkle)
    bpy.utils.register_class(curve_test)
    bpy.utils.register_class(subdivid_curve)
    bpy.utils.register_class(fib_curve)
    bpy.utils.register_class(procedural_curve)
    bpy.utils.register_class(NODE_OT_Get_Normalize)
    bpy.utils.register_class(NODE_OT_delete_points_of_curve)

    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    del bpy.types.Scene.voxel_terrain_props
    #bpy.utils.unregister_class(VIEW3D_PT_VoxelTerrainGeneration)
    #bpy.utils.unregister_class(VoxelTerrainProperties)

    ## UI ##
    bpy.utils.unregister_class(VIEW3D_PT_Organics_Generation)
    bpy.utils.unregister_class(VIEW3D_PT_Volume_Generation)
    bpy.utils.unregister_class(VIEW3D_PT_PlantGeneration)
    bpy.utils.unregister_class(NODE_PT_Organics_Generation)
    bpy.utils.unregister_class(NODE_PT_Volume)
    bpy.utils.unregister_class(NODE_PT_Plant_Generator)

    bpy.utils.unregister_class(create_geometry_node)

    ## VOLUME ##
    bpy.utils.unregister_class(MESH_OT_mesh_to_Volume)
    bpy.utils.unregister_class(volume_to_Mesh)
    bpy.utils.unregister_class(MESH_OT_hide_mesh)
    bpy.utils.unregister_class(MESH_OT_subdivision_mesh)
    bpy.utils.register_class(NODE_OT_Grid_Volume)

    ## PLANT ##
    bpy.utils.unregister_class(draw_curve)
    bpy.utils.unregister_class(MESH_OT_create_leaf)
    bpy.utils.unregister_class(NODE_OT_create_trunk)
    bpy.utils.unregister_class(create_bezier_curve)
    bpy.utils.unregister_class(create_spike)
    bpy.utils.unregister_class(NODE_OT_volume_simulation)
    bpy.utils.unregister_class(NODE_OT_sprinkle)
    bpy.utils.unregister_class(curve_test)
    bpy.utils.unregister_class(subdivid_curve)
    bpy.utils.unregister_class(fib_curve)
    bpy.utils.unregister_class(procedural_curve)
    bpy.utils.unregister_class(NODE_OT_Get_Normalize)
    bpy.utils.unregister_class(NODE_OT_delete_points_of_curve)


if __name__ == "__main__":
    register()

### REGISTER END ###

"""
juju Julien BROUZES
https://github.com/Juju-brz
"""
