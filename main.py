"""
juju Julien BROUZES
"""
bl_info = {
    "name": "Voxel & Volume",
    "blender": (5, 0, 1),
    "category": "Object",
    "version": (0, 1, 2, 0)
}

import bpy
import sys
import os

### IMPORTATION TO LIB THANKS TO MISTRAL AI ###
#def truc():
blend_path = bpy.data.filepath


if not blend_path:
    print("ERREUR : Le fichier .blend n'est pas enregistré ! Enregistrez-le dans le même dossier que juju.py.")
    sys.exit()


script_dir = os.path.dirname(blend_path)
print("Dossier du fichier .blend :", script_dir)

if script_dir not in sys.path:
    sys.path.append(script_dir)





#if "juju.py" in os.listdir(script_dir):

#else:
#    print("ERROR")


try:
    import juju
    import GeoNode

except ModuleNotFoundError:
    print("ERROR")


### IMPORTATION TO LIB THANKS TO MISTRAL AI ###

#def simulation_node():
    #bpy.context.area.ui_type = 'GeometryNodeTree'
    #bpy.ops.node.new_geometry_nodes_modifier()
    #bpy.ops.node.add_zone(use_transform=True, input_node_type="GeometryNodeSimulationInput", output_node_type="GeometryNodeSimulationOutput", add_default_geometry_link=True)


obj = bpy.context.active_object



### CLASS ###
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

class subdivision_mesh(bpy.types.Operator):
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


### CURVES ###
class draw_curve(bpy.types.Operator):
    bl_idname = "object.draw_curve"
    bl_label = "draw_curve"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        juju.draw_curve()
        return {'FINISHED'}

class create_leaf(bpy.types.Operator):
    bl_idname = "object.create_leaf"
    bl_label = "create_leaf"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        juju.create_leaf()
        return {'FINISHED'}

class NODE_OT_create_trunk(bpy.types.Operator):
    bl_idname = "object.create_trunk"
    bl_label = "create_trunk"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        node_tree_names : dict[typing.Callable, str] = {}
        GeoNode.create_trunk(node_tree_names)
        return {'FINISHED'}

class create_bezier_curve(bpy.types.Operator):
    bl_idname = "object.create_bezier_curve"
    bl_label = "create_bezier_curve"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        juju.create_bezier_curve()
        return {'FINISHED'}


### UI BEGIN ###

class VIEW3D_PT_VoxelTerrainGeneration(bpy.types.Panel):
    bl_label = "Organics Generation"
    bl_idname = "VIEW3D_PT_Organics_Generation"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Organics Generation"
    
    def draw(self, context):
        layout = self.layout
        props = context.scene.voxel_terrain_props
        
        
        layout.operator("object.clean_scene", text="Clean Scene (beta)")
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
        layout.operator("object.subdivision_mesh", text="Subdivision_mesh")
        layout.operator("object.create_simulation_node", text="create_simulation_node")

        layout.label(text='Create Plant')
        layout.operator("object.draw_curve", text="Draw Curve")
        layout.operator("object.create_leaf", text="Draw leaf")
        layout.operator("object.create_trunk", text="create_trunk")
        layout.operator("object.create_bezier_curve", text="create_bezier_curve")

class NODE_OT_juju_operator(bpy.types.Operator):
    bl_idname = "node.juju_operator"
    bl_label = "Créer Nodes"
    bl_description = "Crée mon node group"

    @classmethod
    def poll(cls, context):
        space = context.space_data
        return space.type == 'NODE_EDITOR'

    def execute(self, context):
        # Ton code ici
        print("✅ Operator exécuté !")
        return {'FINISHED'}


# --- PANEL ---
class NODE_PT_juju_panel(bpy.types.Panel):
    bl_label = "JujuLib"
    bl_idname = "NODE_PT_juju_panel"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category = "JujuLib"

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


### UI END ###


# REGISTER
classes = [
    NODE_OT_juju_operator,
    NODE_PT_juju_panel,
]

def register():
    bpy.utils.register_class(OBJECT_OT_create_ground)
    bpy.utils.register_class(VoxelTerrainProperties)
    bpy.utils.register_class(VIEW3D_PT_VoxelTerrainGeneration)
    bpy.utils.register_class(MESH_OT_Create_Cube)
    bpy.utils.register_class(MESH_OT_Create_Sphere)
    bpy.utils.register_class(Convert_Voxel)
    bpy.utils.register_class(MESH_OT_mesh_to_Volume)
    bpy.utils.register_class(volume_to_Mesh)
    bpy.utils.register_class(MESH_OT_hide_mesh)
    bpy.utils.register_class(clean_scene)
    bpy.utils.register_class(create_simulation_node)
    bpy.types.Scene.voxel_terrain_props = bpy.props.PointerProperty(type=VoxelTerrainProperties)
    bpy.utils.register_class(subdivision_mesh)
    bpy.utils.register_class(draw_curve)
    bpy.utils.register_class(create_leaf)
    bpy.utils.register_class(NODE_OT_create_trunk)
    bpy.utils.register_class(create_bezier_curve)
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    del bpy.types.Scene.voxel_terrain_props
    bpy.utils.unregister_class(VIEW3D_PT_VoxelTerrainGeneration)
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
    bpy.utils.unregister_class(subdivision_mesh)
    bpy.utils.unregister_class(draw_curve)
    bpy.utils.unregister_class(create_leaf)
    bpy.utils.unregister_class(NODE_OT_create_trunk)
    bpy.utils.unregister_class(create_bezier_curve)

if __name__ == "__main__":
    register()
    

"""
juju Julien BROUZES
"""
