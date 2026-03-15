import bpy
import mathutils
import os
import typing

# Ok we will making group node for making like a libraries

"""
# Import node groups from Blender essentials library
datafiles_path = bpy.utils.system_resource('DATAFILES')
lib_relpath = "assets/nodes/geometry_nodes_essentials.blend"
lib_path = os.path.join(datafiles_path, lib_relpath)
with bpy.data.libraries.load(lib_path, link=True)  as (data_src, data_dst):
    data_dst.node_groups = []
    if "Curve to Tube" in data_src.node_groups:
        data_dst.node_groups.append("Curve to Tube")

"""
def load_essential_node_groups():

    required_node_groups = ["Curve to Tube"]

    datafiles_path = bpy.utils.system_resource('DATAFILES')
    if not datafiles_path:

        return False

    lib_relpath = "assets/nodes/geometry_nodes_essentials.blend"
    lib_path = os.path.join(datafiles_path, lib_relpath)

    if not os.path.exists(lib_path):

        return False


    with bpy.data.libraries.load(lib_path, link=True) as (data_src, data_dst):
        data_dst.node_groups = []
        for node_group_name in required_node_groups:
            if node_group_name in data_src.node_groups and node_group_name not in bpy.data.node_groups:
                data_dst.node_groups.append(node_group_name)

    missing = [name for name in required_node_groups if name not in bpy.data.node_groups]
    if missing:
        print(f"ERROR is : {missing}")
        return False

    return True

def create_trunk_1_node_group(node_tree_names: dict[typing.Callable, str]):
    load_essential_node_groups()
    """Initialize create_trunk node group"""
    create_trunk_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="create_trunk")

    create_trunk_1.color_tag = 'NONE'
    create_trunk_1.description = ""
    create_trunk_1.default_group_node_width = 140
    create_trunk_1.is_modifier = True
    create_trunk_1.show_modifier_manage_panel = True

    # create_trunk_1 interface

    # Socket Geometry
    geometry_socket = create_trunk_1.interface.new_socket(name="Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    # Socket Geometry
    geometry_socket_1 = create_trunk_1.interface.new_socket(name="Geometry", in_out='INPUT', socket_type='NodeSocketGeometry')
    geometry_socket_1.attribute_domain = 'POINT'
    geometry_socket_1.default_input = 'VALUE'
    geometry_socket_1.structure_type = 'AUTO'

    # Socket Scale
    scale_socket = create_trunk_1.interface.new_socket(name="Scale", in_out='INPUT', socket_type='NodeSocketFloat')
    scale_socket.default_value = 0.10000000149011612
    scale_socket.min_value = 0.0
    scale_socket.max_value = 3.4028234663852886e+38
    scale_socket.subtype = 'DISTANCE'
    scale_socket.attribute_domain = 'POINT'
    scale_socket.description = "Distance factor multiplied with the curve's radius attribute to define the resulting tube radius"
    scale_socket.default_input = 'VALUE'
    scale_socket.structure_type = 'AUTO'

    # Initialize create_trunk_1 nodes

    # Node Group Input
    group_input = create_trunk_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"

    # Node Group Output
    group_output = create_trunk_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True

    # Node Curve to Tube
    curve_to_tube = create_trunk_1.nodes.new("GeometryNodeGroup")
    curve_to_tube.name = "Curve to Tube"
    # Finding linked library node group
    for node_group in bpy.data.node_groups:
        if (
            node_group.name == "Curve to Tube"
            and node_group.bl_idname == 'GeometryNodeTree'
        ):
            curve_to_tube.node_tree = node_group
    if curve_to_tube.node_tree is None:
        print("Couldn't find node group Curve to Tube, failing")
        return
    # Socket_4
    curve_to_tube.inputs[2].default_value = 'Round'
    # Socket_26
    curve_to_tube.inputs[3].default_value = 'Object'
    # Socket_2
    curve_to_tube.inputs[6].default_value = 8
    # Socket_11
    curve_to_tube.inputs[7].default_value = True
    # Socket_36
    curve_to_tube.inputs[8].default_value = True
    # Socket_32
    curve_to_tube.inputs[9].default_value = 'Evaluated'
    # Socket_33
    curve_to_tube.inputs[10].default_value = 10
    # Socket_37
    curve_to_tube.inputs[11].default_value = 0.10000000149011612
    # Socket_38
    curve_to_tube.inputs[12].default_value = 1.0
    # Socket_39
    curve_to_tube.inputs[13].default_value = True
    # Socket_10
    curve_to_tube.inputs[14].default_value = 'Flat'
    # Socket_25
    curve_to_tube.inputs[15].default_value = 'Object'
    # Socket_28
    curve_to_tube.inputs[20].default_value = 12
    # Socket_15
    curve_to_tube.inputs[21].default_value = False
    # Socket_13
    curve_to_tube.inputs[22].default_value = True
    # Socket_14
    curve_to_tube.inputs[23].default_value = False
    # Socket_30
    curve_to_tube.inputs[24].default_value = True
    # Socket_31
    curve_to_tube.inputs[25].default_value = True
    # Socket_17
    curve_to_tube.inputs[26].default_value = "UVMap"
    # Socket_19
    curve_to_tube.inputs[27].default_value = 'Length'
    # Socket_20
    curve_to_tube.inputs[28].default_value = 'Factor'
    # Socket_29
    curve_to_tube.inputs[29].default_value = True

    # Node Join Geometry
    join_geometry = create_trunk_1.nodes.new("GeometryNodeJoinGeometry")
    join_geometry.name = "Join Geometry"

    # Set locations
    create_trunk_1.nodes["Group Input"].location = (-340.0, 0.0)
    create_trunk_1.nodes["Group Output"].location = (335.7822570800781, 139.33546447753906)
    create_trunk_1.nodes["Curve to Tube"].location = (-102.19905853271484, 8.371559143066406)
    create_trunk_1.nodes["Join Geometry"].location = (156.1344757080078, 84.99462890625)

    # Set dimensions
    create_trunk_1.nodes["Group Input"].width  = 140.0
    create_trunk_1.nodes["Group Input"].height = 100.0

    create_trunk_1.nodes["Group Output"].width  = 140.0
    create_trunk_1.nodes["Group Output"].height = 100.0

    create_trunk_1.nodes["Curve to Tube"].width  = 200.0
    create_trunk_1.nodes["Curve to Tube"].height = 100.0

    create_trunk_1.nodes["Join Geometry"].width  = 140.0
    create_trunk_1.nodes["Join Geometry"].height = 100.0


    # Initialize create_trunk_1 links

    # join_geometry.Geometry -> group_output.Geometry
    create_trunk_1.links.new(
        create_trunk_1.nodes["Join Geometry"].outputs[0],
        create_trunk_1.nodes["Group Output"].inputs[0]
    )
    # group_input.Geometry -> curve_to_tube.Curve
    create_trunk_1.links.new(
        create_trunk_1.nodes["Group Input"].outputs[0],
        create_trunk_1.nodes["Curve to Tube"].inputs[0]
    )
    # group_input.Scale -> curve_to_tube.Scale
    create_trunk_1.links.new(
        create_trunk_1.nodes["Group Input"].outputs[1],
        create_trunk_1.nodes["Curve to Tube"].inputs[1]
    )
    # curve_to_tube.Mesh -> join_geometry.Geometry
    create_trunk_1.links.new(
        create_trunk_1.nodes["Curve to Tube"].outputs[0],
        create_trunk_1.nodes["Join Geometry"].inputs[0]
    )
    # group_input.Geometry -> join_geometry.Geometry
    create_trunk_1.links.new(
        create_trunk_1.nodes["Group Input"].outputs[0],
        create_trunk_1.nodes["Join Geometry"].inputs[0]
    )

    return create_trunk_1


def volume_simulation(node_tree_names: dict[typing.Callable, str]):
    """Initialize volume_simulation node group"""
    volume_simulation = bpy.data.node_groups.new(type='GeometryNodeTree', name="volume_simulation")

    volume_simulation.color_tag = 'NONE'
    volume_simulation.description = ""
    volume_simulation.default_group_node_width = 140
    volume_simulation.is_modifier = True
    volume_simulation.show_modifier_manage_panel = True

    # volume_simulation interface

    # Socket Geometry
    geometry_socket = volume_simulation.interface.new_socket(name="Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    # Socket Geometry
    geometry_socket_1 = volume_simulation.interface.new_socket(name="Geometry", in_out='INPUT', socket_type='NodeSocketGeometry')
    geometry_socket_1.attribute_domain = 'POINT'
    geometry_socket_1.default_input = 'VALUE'
    geometry_socket_1.structure_type = 'AUTO'

    # Socket Translation
    translation_socket = volume_simulation.interface.new_socket(name="Translation", in_out='INPUT', socket_type='NodeSocketVector')
    translation_socket.default_value = (0.0, 0.0, 0.009999999776482582)
    translation_socket.min_value = -3.4028234663852886e+38
    translation_socket.max_value = 3.4028234663852886e+38
    translation_socket.subtype = 'TRANSLATION'
    translation_socket.attribute_domain = 'POINT'
    translation_socket.default_input = 'VALUE'
    translation_socket.structure_type = 'AUTO'

    # Initialize volume_simulation nodes

    # Node Group Input
    group_input = volume_simulation.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"

    # Node Group Output
    group_output = volume_simulation.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True

    # Node Simulation Input
    simulation_input = volume_simulation.nodes.new("GeometryNodeSimulationInput")
    simulation_input.name = "Simulation Input"
    # Node Simulation Output
    simulation_output = volume_simulation.nodes.new("GeometryNodeSimulationOutput")
    simulation_output.name = "Simulation Output"
    simulation_output.active_index = 0
    simulation_output.state_items.clear()
    # Create item "Geometry"
    simulation_output.state_items.new('GEOMETRY', "Geometry")
    simulation_output.state_items[0].attribute_domain = 'POINT'
    # Skip
    simulation_output.inputs[0].default_value = False

    # Node Transform Geometry
    transform_geometry = volume_simulation.nodes.new("GeometryNodeTransform")
    transform_geometry.name = "Transform Geometry"
    # Mode
    transform_geometry.inputs[1].default_value = 'Components'
    # Rotation
    transform_geometry.inputs[3].default_value = (0.0, 0.0, 0.0)
    # Scale
    transform_geometry.inputs[4].default_value = (1.0, 1.0, 1.0)

    # Process zone input Simulation Input
    simulation_input.pair_with_output(simulation_output)

    # Skip
    simulation_output.inputs[0].default_value = False


    # Set locations
    volume_simulation.nodes["Group Input"].location = (-340.0, 0.0)
    volume_simulation.nodes["Group Output"].location = (400.1388244628906, -12.126993179321289)
    volume_simulation.nodes["Simulation Input"].location = (-182.5281982421875, 14.331893920898438)
    volume_simulation.nodes["Simulation Output"].location = (177.47181701660156, 14.331893920898438)
    volume_simulation.nodes["Transform Geometry"].location = (-3.0, -5.512275695800781)

    # Set dimensions
    volume_simulation.nodes["Group Input"].width  = 140.0
    volume_simulation.nodes["Group Input"].height = 100.0

    volume_simulation.nodes["Group Output"].width  = 140.0
    volume_simulation.nodes["Group Output"].height = 100.0

    volume_simulation.nodes["Simulation Input"].width  = 140.0
    volume_simulation.nodes["Simulation Input"].height = 100.0

    volume_simulation.nodes["Simulation Output"].width  = 140.0
    volume_simulation.nodes["Simulation Output"].height = 100.0

    volume_simulation.nodes["Transform Geometry"].width  = 140.0
    volume_simulation.nodes["Transform Geometry"].height = 100.0


    # Initialize volume_simulation links

    # transform_geometry.Geometry -> simulation_output.Geometry
    volume_simulation.links.new(
        volume_simulation.nodes["Transform Geometry"].outputs[0],
        volume_simulation.nodes["Simulation Output"].inputs[1]
    )
    # group_input.Geometry -> simulation_input.Geometry
    volume_simulation.links.new(
        volume_simulation.nodes["Group Input"].outputs[0],
        volume_simulation.nodes["Simulation Input"].inputs[0]
    )
    # simulation_output.Geometry -> group_output.Geometry
    volume_simulation.links.new(
        volume_simulation.nodes["Simulation Output"].outputs[0],
        volume_simulation.nodes["Group Output"].inputs[0]
    )
    # simulation_input.Geometry -> transform_geometry.Geometry
    volume_simulation.links.new(
        volume_simulation.nodes["Simulation Input"].outputs[1],
        volume_simulation.nodes["Transform Geometry"].inputs[0]
    )
    # group_input.Translation -> transform_geometry.Translation
    volume_simulation.links.new(
        volume_simulation.nodes["Group Input"].outputs[1],
        volume_simulation.nodes["Transform Geometry"].inputs[2]
    )

    return volume_simulation

def sprinkle_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize Sprinkle node group"""
    sprinkle_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="Sprinkle")

    sprinkle_1.color_tag = 'NONE'
    sprinkle_1.description = ""
    sprinkle_1.default_group_node_width = 140
    sprinkle_1.is_modifier = True
    sprinkle_1.show_modifier_manage_panel = True

    # sprinkle_1 interface

    # Socket Geometry
    geometry_socket = sprinkle_1.interface.new_socket(name="Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    # Socket Geometry
    geometry_socket_1 = sprinkle_1.interface.new_socket(name="Geometry", in_out='INPUT', socket_type='NodeSocketGeometry')
    geometry_socket_1.attribute_domain = 'POINT'
    geometry_socket_1.default_input = 'VALUE'
    geometry_socket_1.structure_type = 'AUTO'

    # Socket Density
    density_socket = sprinkle_1.interface.new_socket(name="Density", in_out='INPUT', socket_type='NodeSocketFloat')
    density_socket.default_value = 10.0
    density_socket.min_value = 0.0
    density_socket.max_value = 3.4028234663852886e+38
    density_socket.subtype = 'NONE'
    density_socket.attribute_domain = 'POINT'
    density_socket.default_input = 'VALUE'
    density_socket.structure_type = 'AUTO'

    # Socket Seed
    seed_socket = sprinkle_1.interface.new_socket(name="Seed", in_out='INPUT', socket_type='NodeSocketInt')
    seed_socket.default_value = 0
    seed_socket.min_value = -2147483648
    seed_socket.max_value = 2147483647
    seed_socket.subtype = 'NONE'
    seed_socket.attribute_domain = 'POINT'
    seed_socket.default_input = 'VALUE'
    seed_socket.structure_type = 'AUTO'

    # Initialize sprinkle_1 nodes

    # Node Group Input
    group_input = sprinkle_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"

    # Node Group Output
    group_output = sprinkle_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True

    # Node Distribute Points on Faces
    distribute_points_on_faces = sprinkle_1.nodes.new("GeometryNodeDistributePointsOnFaces")
    distribute_points_on_faces.name = "Distribute Points on Faces"
    distribute_points_on_faces.distribute_method = 'RANDOM'
    distribute_points_on_faces.use_legacy_normal = False
    # Selection
    distribute_points_on_faces.inputs[1].default_value = True

    # Node Join Geometry
    join_geometry = sprinkle_1.nodes.new("GeometryNodeJoinGeometry")
    join_geometry.name = "Join Geometry"

    # Set locations
    sprinkle_1.nodes["Group Input"].location = (-340.0, 0.0)
    sprinkle_1.nodes["Group Output"].location = (259.3060607910156, 0.0)
    sprinkle_1.nodes["Distribute Points on Faces"].location = (-141.48202514648438, -85.64603424072266)
    sprinkle_1.nodes["Join Geometry"].location = (79.3060531616211, 39.9681510925293)

    # Set dimensions
    sprinkle_1.nodes["Group Input"].width  = 140.0
    sprinkle_1.nodes["Group Input"].height = 100.0

    sprinkle_1.nodes["Group Output"].width  = 140.0
    sprinkle_1.nodes["Group Output"].height = 100.0

    sprinkle_1.nodes["Distribute Points on Faces"].width  = 170.0
    sprinkle_1.nodes["Distribute Points on Faces"].height = 100.0

    sprinkle_1.nodes["Join Geometry"].width  = 140.0
    sprinkle_1.nodes["Join Geometry"].height = 100.0


    # Initialize sprinkle_1 links

    # join_geometry.Geometry -> group_output.Geometry
    sprinkle_1.links.new(
        sprinkle_1.nodes["Join Geometry"].outputs[0],
        sprinkle_1.nodes["Group Output"].inputs[0]
    )
    # group_input.Geometry -> distribute_points_on_faces.Mesh
    sprinkle_1.links.new(
        sprinkle_1.nodes["Group Input"].outputs[0],
        sprinkle_1.nodes["Distribute Points on Faces"].inputs[0]
    )
    # distribute_points_on_faces.Points -> join_geometry.Geometry
    sprinkle_1.links.new(
        sprinkle_1.nodes["Distribute Points on Faces"].outputs[0],
        sprinkle_1.nodes["Join Geometry"].inputs[0]
    )
    # group_input.Density -> distribute_points_on_faces.Density
    sprinkle_1.links.new(
        sprinkle_1.nodes["Group Input"].outputs[1],
        sprinkle_1.nodes["Distribute Points on Faces"].inputs[4]
    )
    # group_input.Seed -> distribute_points_on_faces.Seed
    sprinkle_1.links.new(
        sprinkle_1.nodes["Group Input"].outputs[2],
        sprinkle_1.nodes["Distribute Points on Faces"].inputs[6]
    )
    # group_input.Geometry -> join_geometry.Geometry
    sprinkle_1.links.new(
        sprinkle_1.nodes["Group Input"].outputs[0],
        sprinkle_1.nodes["Join Geometry"].inputs[0]
    )

    return sprinkle_1

def grid_volume_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize Grid_Volume node group"""
    grid_volume_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="Grid_Volume")

    grid_volume_1.color_tag = 'NONE'
    grid_volume_1.description = ""
    grid_volume_1.default_group_node_width = 140
    grid_volume_1.is_modifier = True
    grid_volume_1.show_modifier_manage_panel = True

    # grid_volume_1 interface

    # Socket Geometry
    geometry_socket = grid_volume_1.interface.new_socket(name="Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    # Socket Geometry
    geometry_socket_1 = grid_volume_1.interface.new_socket(name="Geometry", in_out='INPUT', socket_type='NodeSocketGeometry')
    geometry_socket_1.attribute_domain = 'POINT'
    geometry_socket_1.default_input = 'VALUE'
    geometry_socket_1.structure_type = 'AUTO'

    # Socket Voxel Size
    voxel_size_socket = grid_volume_1.interface.new_socket(name="Voxel Size", in_out='INPUT', socket_type='NodeSocketFloat')
    voxel_size_socket.default_value = 0.06000000238418579
    voxel_size_socket.min_value = 0.009999999776482582
    voxel_size_socket.max_value = 3.4028234663852886e+38
    voxel_size_socket.subtype = 'DISTANCE'
    voxel_size_socket.attribute_domain = 'POINT'
    voxel_size_socket.default_input = 'VALUE'
    voxel_size_socket.structure_type = 'AUTO'

    # Socket Band Width
    band_width_socket = grid_volume_1.interface.new_socket(name="Band Width", in_out='INPUT', socket_type='NodeSocketInt')
    band_width_socket.default_value = 2
    band_width_socket.min_value = 1
    band_width_socket.max_value = 100
    band_width_socket.subtype = 'NONE'
    band_width_socket.attribute_domain = 'POINT'
    band_width_socket.description = "Width of the active voxel surface, in voxels"
    band_width_socket.default_input = 'VALUE'
    band_width_socket.structure_type = 'AUTO'

    # Socket Threshold
    threshold_socket = grid_volume_1.interface.new_socket(name="Threshold", in_out='INPUT', socket_type='NodeSocketFloat')
    threshold_socket.default_value = 12.0
    threshold_socket.min_value = -3.4028234663852886e+38
    threshold_socket.max_value = 3.4028234663852886e+38
    threshold_socket.subtype = 'NONE'
    threshold_socket.attribute_domain = 'POINT'
    threshold_socket.description = "Values larger than the threshold are inside the generated mesh"
    threshold_socket.default_input = 'VALUE'
    threshold_socket.structure_type = 'AUTO'

    # Socket Adaptivity
    adaptivity_socket = grid_volume_1.interface.new_socket(name="Adaptivity", in_out='INPUT', socket_type='NodeSocketFloat')
    adaptivity_socket.default_value = 1.0
    adaptivity_socket.min_value = 0.0
    adaptivity_socket.max_value = 1.0
    adaptivity_socket.subtype = 'FACTOR'
    adaptivity_socket.attribute_domain = 'POINT'
    adaptivity_socket.default_input = 'VALUE'
    adaptivity_socket.structure_type = 'AUTO'

    # Initialize grid_volume_1 nodes

    # Node Group Input
    group_input = grid_volume_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"

    # Node Group Output
    group_output = grid_volume_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True

    # Node Mesh to SDF Grid
    mesh_to_sdf_grid = grid_volume_1.nodes.new("GeometryNodeMeshToSDFGrid")
    mesh_to_sdf_grid.name = "Mesh to SDF Grid"

    # Node Grid to Mesh
    grid_to_mesh = grid_volume_1.nodes.new("GeometryNodeGridToMesh")
    grid_to_mesh.name = "Grid to Mesh"

    # Node Grid Laplacian
    grid_laplacian = grid_volume_1.nodes.new("GeometryNodeGridLaplacian")
    grid_laplacian.name = "Grid Laplacian"

    # Set locations
    grid_volume_1.nodes["Group Input"].location = (-500.4462585449219, 17.07179832458496)
    grid_volume_1.nodes["Group Output"].location = (259.1262512207031, 59.60945510864258)
    grid_volume_1.nodes["Mesh to SDF Grid"].location = (-228.1107177734375, 15.155731201171875)
    grid_volume_1.nodes["Grid to Mesh"].location = (116.16053009033203, -26.823486328125)
    grid_volume_1.nodes["Grid Laplacian"].location = (-48.14565658569336, 25.491989135742188)

    # Set dimensions
    grid_volume_1.nodes["Group Input"].width  = 140.0
    grid_volume_1.nodes["Group Input"].height = 100.0

    grid_volume_1.nodes["Group Output"].width  = 140.0
    grid_volume_1.nodes["Group Output"].height = 100.0

    grid_volume_1.nodes["Mesh to SDF Grid"].width  = 140.0
    grid_volume_1.nodes["Mesh to SDF Grid"].height = 100.0

    grid_volume_1.nodes["Grid to Mesh"].width  = 140.0
    grid_volume_1.nodes["Grid to Mesh"].height = 100.0

    grid_volume_1.nodes["Grid Laplacian"].width  = 140.0
    grid_volume_1.nodes["Grid Laplacian"].height = 100.0


    # Initialize grid_volume_1 links

    # group_input.Geometry -> mesh_to_sdf_grid.Mesh
    grid_volume_1.links.new(
        grid_volume_1.nodes["Group Input"].outputs[0],
        grid_volume_1.nodes["Mesh to SDF Grid"].inputs[0]
    )
    # grid_laplacian.Laplacian -> grid_to_mesh.Grid
    grid_volume_1.links.new(
        grid_volume_1.nodes["Grid Laplacian"].outputs[0],
        grid_volume_1.nodes["Grid to Mesh"].inputs[0]
    )
    # mesh_to_sdf_grid.SDF Grid -> grid_laplacian.Grid
    grid_volume_1.links.new(
        grid_volume_1.nodes["Mesh to SDF Grid"].outputs[0],
        grid_volume_1.nodes["Grid Laplacian"].inputs[0]
    )
    # grid_to_mesh.Mesh -> group_output.Geometry
    grid_volume_1.links.new(
        grid_volume_1.nodes["Grid to Mesh"].outputs[0],
        grid_volume_1.nodes["Group Output"].inputs[0]
    )
    # group_input.Voxel Size -> mesh_to_sdf_grid.Voxel Size
    grid_volume_1.links.new(
        grid_volume_1.nodes["Group Input"].outputs[1],
        grid_volume_1.nodes["Mesh to SDF Grid"].inputs[1]
    )
    # group_input.Band Width -> mesh_to_sdf_grid.Band Width
    grid_volume_1.links.new(
        grid_volume_1.nodes["Group Input"].outputs[2],
        grid_volume_1.nodes["Mesh to SDF Grid"].inputs[2]
    )
    # group_input.Threshold -> grid_to_mesh.Threshold
    grid_volume_1.links.new(
        grid_volume_1.nodes["Group Input"].outputs[3],
        grid_volume_1.nodes["Grid to Mesh"].inputs[1]
    )
    # group_input.Adaptivity -> grid_to_mesh.Adaptivity
    grid_volume_1.links.new(
        grid_volume_1.nodes["Group Input"].outputs[4],
        grid_volume_1.nodes["Grid to Mesh"].inputs[2]
    )

    return grid_volume_1

if __name__ == "__main__":
    node_tree_names : dict[typing.Callable, str] = {}

    create_trunk = create_trunk_1_node_group(node_tree_names)
    node_tree_names[create_trunk_1_node_group] = create_trunk.name

    volume_simulation = volume_simulation_node_group(node_tree_names)
    node_tree_names[volume_simulation_node_group] = volume_simulation.name

    sprinkle = sprinkle_1_node_group(node_tree_names)
    node_tree_names[sprinkle_1_node_group] = sprinkle.name

    grid_volume = grid_volume_1_node_group(node_tree_names)
    node_tree_names[grid_volume_1_node_group] = grid_volume.name

    obj = bpy.context.active_object

    if obj is None:
        print("not object found")
    # else:
    #     mod = obj.modifiers.new("Curve to Tube", type='NODES')
    #     mod.node_group = create_trunk

