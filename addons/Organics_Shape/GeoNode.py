"""
juju Julien BROUZES
https://github.com/Juju-brz
"""

import bpy
import mathutils
import os
import typing

# Ok we will making group node for making like a libraries

# Made with Node to Python

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

def arc_curve_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize Arc Curve node group"""
    arc_curve_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="Arc Curve")


    arc_curve_1.color_tag = 'NONE'
    arc_curve_1.description = ""
    arc_curve_1.default_group_node_width = 140
    arc_curve_1.is_modifier = True
    arc_curve_1.show_modifier_manage_panel = True

    # arc_curve_1 interface

    # Socket Geometry
    geometry_socket = arc_curve_1.interface.new_socket(name="Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    # Socket Geometry
    geometry_socket_1 = arc_curve_1.interface.new_socket(name="Geometry", in_out='INPUT', socket_type='NodeSocketGeometry')
    geometry_socket_1.attribute_domain = 'POINT'
    geometry_socket_1.default_input = 'VALUE'
    geometry_socket_1.structure_type = 'AUTO'

    # Initialize arc_curve_1 nodes

    # Node Group Input
    group_input = arc_curve_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"

    # Node Group Output
    group_output = arc_curve_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True

    # Node Arc
    arc = arc_curve_1.nodes.new("GeometryNodeCurveArc")
    arc.name = "Arc"
    arc.mode = 'RADIUS'
    # Resolution
    arc.inputs[0].default_value = 16
    # Radius
    arc.inputs[4].default_value = 1.0
    # Start Angle
    arc.inputs[5].default_value = 0.0
    # Sweep Angle
    arc.inputs[6].default_value = 5.497786998748779
    # Connect Center
    arc.inputs[8].default_value = False
    # Invert Arc
    arc.inputs[9].default_value = False

    # Set locations
    arc_curve_1.nodes["Group Input"].location = (-406.947998046875, 77.57366943359375)
    arc_curve_1.nodes["Group Output"].location = (200.0, 0.0)
    arc_curve_1.nodes["Arc"].location = (-110.00819396972656, -69.62760162353516)

    # Set dimensions
    arc_curve_1.nodes["Group Input"].width  = 140.0
    arc_curve_1.nodes["Group Input"].height = 100.0

    arc_curve_1.nodes["Group Output"].width  = 140.0
    arc_curve_1.nodes["Group Output"].height = 100.0

    arc_curve_1.nodes["Arc"].width  = 140.0
    arc_curve_1.nodes["Arc"].height = 100.0


    # Initialize arc_curve_1 links

    # arc.Curve -> group_output.Geometry
    arc_curve_1.links.new(
        arc_curve_1.nodes["Arc"].outputs[0],
        arc_curve_1.nodes["Group Output"].inputs[0]
    )

    return arc_curve_1

def getnormalize_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize GetNormalize node group"""
    getnormalize_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="Get Normalize")

    getnormalize_1.color_tag = 'NONE'
    getnormalize_1.description = ""
    getnormalize_1.default_group_node_width = 140
    getnormalize_1.show_modifier_manage_panel = True

    # getnormalize_1 interface

    # Socket Value
    value_socket = getnormalize_1.interface.new_socket(name="Value", in_out='OUTPUT', socket_type='NodeSocketFloat')
    value_socket.default_value = 0.0
    value_socket.min_value = -3.4028234663852886e+38
    value_socket.max_value = 3.4028234663852886e+38
    value_socket.subtype = 'NONE'
    value_socket.attribute_domain = 'POINT'
    value_socket.default_input = 'VALUE'
    value_socket.structure_type = 'AUTO'

    # Initialize getnormalize_1 nodes

    # Node Spline Length
    spline_length = getnormalize_1.nodes.new("GeometryNodeSplineLength")
    spline_length.name = "Spline Length"

    # Node Spline Parameter
    spline_parameter = getnormalize_1.nodes.new("GeometryNodeSplineParameter")
    spline_parameter.name = "Spline Parameter"

    # Node Math
    math = getnormalize_1.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.operation = 'DIVIDE'
    math.use_clamp = False

    # Node Group Output
    group_output = getnormalize_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True

    # Node Group Input
    group_input = getnormalize_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"

    # Set locations
    getnormalize_1.nodes["Spline Length"].location = (-301.7341613769531, -60.227783203125)
    getnormalize_1.nodes["Spline Parameter"].location = (-275.8704528808594, 86.1356201171875)
    getnormalize_1.nodes["Math"].location = (59.46675109863281, 14.048828125)
    getnormalize_1.nodes["Group Output"].location = (465.87042236328125, 0.0)
    getnormalize_1.nodes["Group Input"].location = (-276.4412841796875, -228.9534454345703)

    # Set dimensions
    getnormalize_1.nodes["Spline Length"].width  = 140.0
    getnormalize_1.nodes["Spline Length"].height = 100.0

    getnormalize_1.nodes["Spline Parameter"].width  = 140.0
    getnormalize_1.nodes["Spline Parameter"].height = 100.0

    getnormalize_1.nodes["Math"].width  = 140.0
    getnormalize_1.nodes["Math"].height = 100.0

    getnormalize_1.nodes["Group Output"].width  = 140.0
    getnormalize_1.nodes["Group Output"].height = 100.0

    getnormalize_1.nodes["Group Input"].width  = 140.0
    getnormalize_1.nodes["Group Input"].height = 100.0


    # Initialize getnormalize_1 links

    # spline_parameter.Length -> math.Value
    getnormalize_1.links.new(
        getnormalize_1.nodes["Spline Parameter"].outputs[1],
        getnormalize_1.nodes["Math"].inputs[0]
    )
    # spline_length.Length -> math.Value
    getnormalize_1.links.new(
        getnormalize_1.nodes["Spline Length"].outputs[0],
        getnormalize_1.nodes["Math"].inputs[1]
    )
    # math.Value -> group_output.Value
    getnormalize_1.links.new(
        getnormalize_1.nodes["Math"].outputs[0],
        getnormalize_1.nodes["Group Output"].inputs[0]
    )

    return getnormalize_1

def delete_points_of_curve_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize delete points of curve node group"""
    delete_points_of_curve_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="delete points of curve")

    delete_points_of_curve_1.color_tag = 'NONE'
    delete_points_of_curve_1.description = ""
    delete_points_of_curve_1.default_group_node_width = 140
    delete_points_of_curve_1.show_modifier_manage_panel = True

    # delete_points_of_curve_1 interface

    # Socket Geometry
    geometry_socket = delete_points_of_curve_1.interface.new_socket(name="Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    # Socket Geometry
    geometry_socket_1 = delete_points_of_curve_1.interface.new_socket(name="Geometry", in_out='INPUT', socket_type='NodeSocketGeometry')
    geometry_socket_1.attribute_domain = 'POINT'
    geometry_socket_1.description = "Geometry to delete elements from"
    geometry_socket_1.default_input = 'VALUE'
    geometry_socket_1.structure_type = 'AUTO'

    # Socket value
    value_socket = delete_points_of_curve_1.interface.new_socket(name="value", in_out='INPUT', socket_type='NodeSocketFloat')
    value_socket.default_value = 0.2999999523162842
    value_socket.min_value = 0.0
    value_socket.max_value = 1.0
    value_socket.subtype = 'NONE'
    value_socket.attribute_domain = 'POINT'
    value_socket.default_input = 'VALUE'
    value_socket.structure_type = 'AUTO'

    # Socket Delete by up points
    delete_by_up_points_socket = delete_points_of_curve_1.interface.new_socket(name="Delete by up points", in_out='INPUT', socket_type='NodeSocketBool')
    delete_by_up_points_socket.default_value = False
    delete_by_up_points_socket.attribute_domain = 'POINT'
    delete_by_up_points_socket.default_input = 'VALUE'
    delete_by_up_points_socket.structure_type = 'AUTO'

    # Socket value
    value_socket_1 = delete_points_of_curve_1.interface.new_socket(name="value", in_out='INPUT', socket_type='NodeSocketFloat')
    value_socket_1.default_value = 0.30000001192092896
    value_socket_1.min_value = 0.0
    value_socket_1.max_value = 1.0
    value_socket_1.subtype = 'NONE'
    value_socket_1.attribute_domain = 'POINT'
    value_socket_1.default_input = 'VALUE'
    value_socket_1.structure_type = 'AUTO'

    # Initialize delete_points_of_curve_1 nodes

    # Node Spline Length
    spline_length = delete_points_of_curve_1.nodes.new("GeometryNodeSplineLength")
    spline_length.name = "Spline Length"

    # Node Spline Parameter
    spline_parameter = delete_points_of_curve_1.nodes.new("GeometryNodeSplineParameter")
    spline_parameter.name = "Spline Parameter"

    # Node Math
    math = delete_points_of_curve_1.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.operation = 'DIVIDE'
    math.use_clamp = False

    # Node Group Output
    group_output = delete_points_of_curve_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True

    # Node Group Input
    group_input = delete_points_of_curve_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"

    # Node Math.001
    math_001 = delete_points_of_curve_1.nodes.new("ShaderNodeMath")
    math_001.name = "Math.001"
    math_001.operation = 'LESS_THAN'
    math_001.use_clamp = True

    # Node Delete Geometry
    delete_geometry = delete_points_of_curve_1.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry.name = "Delete Geometry"
    delete_geometry.domain = 'POINT'
    delete_geometry.mode = 'ALL'

    # Node Spline Length.001
    spline_length_001 = delete_points_of_curve_1.nodes.new("GeometryNodeSplineLength")
    spline_length_001.name = "Spline Length.001"

    # Node Spline Parameter.001
    spline_parameter_001 = delete_points_of_curve_1.nodes.new("GeometryNodeSplineParameter")
    spline_parameter_001.name = "Spline Parameter.001"

    # Node Math.002
    math_002 = delete_points_of_curve_1.nodes.new("ShaderNodeMath")
    math_002.name = "Math.002"
    math_002.operation = 'DIVIDE'
    math_002.use_clamp = False

    # Node Math.003
    math_003 = delete_points_of_curve_1.nodes.new("ShaderNodeMath")
    math_003.name = "Math.003"
    math_003.operation = 'GREATER_THAN'
    math_003.use_clamp = True

    # Node Delete Geometry.001
    delete_geometry_001 = delete_points_of_curve_1.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry_001.name = "Delete Geometry.001"
    delete_geometry_001.domain = 'POINT'
    delete_geometry_001.mode = 'ALL'

    # Node Switch
    switch = delete_points_of_curve_1.nodes.new("GeometryNodeSwitch")
    switch.name = "Switch"
    switch.input_type = 'GEOMETRY'

    # Set locations
    delete_points_of_curve_1.nodes["Spline Length"].location = (-301.7341613769531, -60.227783203125)
    delete_points_of_curve_1.nodes["Spline Parameter"].location = (-275.8704528808594, 86.1356201171875)
    delete_points_of_curve_1.nodes["Math"].location = (-2.6723670959472656, 148.23487854003906)
    delete_points_of_curve_1.nodes["Group Output"].location = (851.4074096679688, 29.20565414428711)
    delete_points_of_curve_1.nodes["Group Input"].location = (-298.6804504394531, -217.08990478515625)
    delete_points_of_curve_1.nodes["Math.001"].location = (271.9712829589844, 84.98362731933594)
    delete_points_of_curve_1.nodes["Delete Geometry"].location = (490.6053466796875, 35.42893981933594)
    delete_points_of_curve_1.nodes["Spline Length.001"].location = (-58.96189880371094, -533.7186279296875)
    delete_points_of_curve_1.nodes["Spline Parameter.001"].location = (-33.09819030761719, -387.355224609375)
    delete_points_of_curve_1.nodes["Math.002"].location = (240.0998992919922, -325.2559814453125)
    delete_points_of_curve_1.nodes["Math.003"].location = (431.41180419921875, -321.224365234375)
    delete_points_of_curve_1.nodes["Delete Geometry.001"].location = (614.66650390625, -209.40208435058594)
    delete_points_of_curve_1.nodes["Switch"].location = (793.19970703125, -84.74897003173828)

    # Set dimensions
    delete_points_of_curve_1.nodes["Spline Length"].width  = 140.0
    delete_points_of_curve_1.nodes["Spline Length"].height = 100.0

    delete_points_of_curve_1.nodes["Spline Parameter"].width  = 140.0
    delete_points_of_curve_1.nodes["Spline Parameter"].height = 100.0

    delete_points_of_curve_1.nodes["Math"].width  = 140.0
    delete_points_of_curve_1.nodes["Math"].height = 100.0

    delete_points_of_curve_1.nodes["Group Output"].width  = 140.0
    delete_points_of_curve_1.nodes["Group Output"].height = 100.0

    delete_points_of_curve_1.nodes["Group Input"].width  = 140.0
    delete_points_of_curve_1.nodes["Group Input"].height = 100.0

    delete_points_of_curve_1.nodes["Math.001"].width  = 140.0
    delete_points_of_curve_1.nodes["Math.001"].height = 100.0

    delete_points_of_curve_1.nodes["Delete Geometry"].width  = 140.0
    delete_points_of_curve_1.nodes["Delete Geometry"].height = 100.0

    delete_points_of_curve_1.nodes["Spline Length.001"].width  = 140.0
    delete_points_of_curve_1.nodes["Spline Length.001"].height = 100.0

    delete_points_of_curve_1.nodes["Spline Parameter.001"].width  = 140.0
    delete_points_of_curve_1.nodes["Spline Parameter.001"].height = 100.0

    delete_points_of_curve_1.nodes["Math.002"].width  = 140.0
    delete_points_of_curve_1.nodes["Math.002"].height = 100.0

    delete_points_of_curve_1.nodes["Math.003"].width  = 140.0
    delete_points_of_curve_1.nodes["Math.003"].height = 100.0

    delete_points_of_curve_1.nodes["Delete Geometry.001"].width  = 140.0
    delete_points_of_curve_1.nodes["Delete Geometry.001"].height = 100.0

    delete_points_of_curve_1.nodes["Switch"].width  = 140.0
    delete_points_of_curve_1.nodes["Switch"].height = 100.0


    # Initialize delete_points_of_curve_1 links

    # spline_parameter.Length -> math.Value
    delete_points_of_curve_1.links.new(
        delete_points_of_curve_1.nodes["Spline Parameter"].outputs[1],
        delete_points_of_curve_1.nodes["Math"].inputs[0]
    )
    # spline_length.Length -> math.Value
    delete_points_of_curve_1.links.new(
        delete_points_of_curve_1.nodes["Spline Length"].outputs[0],
        delete_points_of_curve_1.nodes["Math"].inputs[1]
    )
    # math.Value -> math_001.Value
    delete_points_of_curve_1.links.new(
        delete_points_of_curve_1.nodes["Math"].outputs[0],
        delete_points_of_curve_1.nodes["Math.001"].inputs[0]
    )
    # group_input.Geometry -> delete_geometry.Geometry
    delete_points_of_curve_1.links.new(
        delete_points_of_curve_1.nodes["Group Input"].outputs[0],
        delete_points_of_curve_1.nodes["Delete Geometry"].inputs[0]
    )
    # group_input.value -> math_001.Value
    delete_points_of_curve_1.links.new(
        delete_points_of_curve_1.nodes["Group Input"].outputs[1],
        delete_points_of_curve_1.nodes["Math.001"].inputs[1]
    )
    # math_001.Value -> delete_geometry.Selection
    delete_points_of_curve_1.links.new(
        delete_points_of_curve_1.nodes["Math.001"].outputs[0],
        delete_points_of_curve_1.nodes["Delete Geometry"].inputs[1]
    )
    # spline_parameter_001.Length -> math_002.Value
    delete_points_of_curve_1.links.new(
        delete_points_of_curve_1.nodes["Spline Parameter.001"].outputs[1],
        delete_points_of_curve_1.nodes["Math.002"].inputs[0]
    )
    # spline_length_001.Length -> math_002.Value
    delete_points_of_curve_1.links.new(
        delete_points_of_curve_1.nodes["Spline Length.001"].outputs[0],
        delete_points_of_curve_1.nodes["Math.002"].inputs[1]
    )
    # math_002.Value -> math_003.Value
    delete_points_of_curve_1.links.new(
        delete_points_of_curve_1.nodes["Math.002"].outputs[0],
        delete_points_of_curve_1.nodes["Math.003"].inputs[0]
    )
    # math_003.Value -> delete_geometry_001.Selection
    delete_points_of_curve_1.links.new(
        delete_points_of_curve_1.nodes["Math.003"].outputs[0],
        delete_points_of_curve_1.nodes["Delete Geometry.001"].inputs[1]
    )
    # group_input.Geometry -> delete_geometry_001.Geometry
    delete_points_of_curve_1.links.new(
        delete_points_of_curve_1.nodes["Group Input"].outputs[0],
        delete_points_of_curve_1.nodes["Delete Geometry.001"].inputs[0]
    )
    # switch.Output -> group_output.Geometry
    delete_points_of_curve_1.links.new(
        delete_points_of_curve_1.nodes["Switch"].outputs[0],
        delete_points_of_curve_1.nodes["Group Output"].inputs[0]
    )
    # group_input.value -> math_003.Value
    delete_points_of_curve_1.links.new(
        delete_points_of_curve_1.nodes["Group Input"].outputs[3],
        delete_points_of_curve_1.nodes["Math.003"].inputs[1]
    )
    # group_input.Delete by up points -> switch.Switch
    delete_points_of_curve_1.links.new(
        delete_points_of_curve_1.nodes["Group Input"].outputs[2],
        delete_points_of_curve_1.nodes["Switch"].inputs[0]
    )
    # delete_geometry.Geometry -> switch.False
    delete_points_of_curve_1.links.new(
        delete_points_of_curve_1.nodes["Delete Geometry"].outputs[0],
        delete_points_of_curve_1.nodes["Switch"].inputs[1]
    )
    # delete_geometry_001.Geometry -> switch.True
    delete_points_of_curve_1.links.new(
        delete_points_of_curve_1.nodes["Delete Geometry.001"].outputs[0],
        delete_points_of_curve_1.nodes["Switch"].inputs[2]
    )

    return delete_points_of_curve_1

def create_branches_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize Create Branches node group"""
    create_branches_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="Create Branches")

    create_branches_1.color_tag = 'NONE'
    create_branches_1.description = ""
    create_branches_1.default_group_node_width = 140
    create_branches_1.is_modifier = True
    create_branches_1.show_modifier_manage_panel = True

    # create_branches_1 interface

    # Socket Geometry
    geometry_socket = create_branches_1.interface.new_socket(name="Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    # Socket Geometry
    geometry_socket_1 = create_branches_1.interface.new_socket(name="Geometry", in_out='INPUT', socket_type='NodeSocketGeometry')
    geometry_socket_1.attribute_domain = 'POINT'
    geometry_socket_1.default_input = 'VALUE'
    geometry_socket_1.structure_type = 'AUTO'

    # Socket Length of Branches
    length_of_branches_socket = create_branches_1.interface.new_socket(name="Length of Branches", in_out='INPUT', socket_type='NodeSocketVector')
    length_of_branches_socket.default_value = (0.0, 0.0, 1.0)
    length_of_branches_socket.min_value = -3.4028234663852886e+38
    length_of_branches_socket.max_value = 3.4028234663852886e+38
    length_of_branches_socket.subtype = 'TRANSLATION'
    length_of_branches_socket.attribute_domain = 'POINT'
    length_of_branches_socket.description = "Position of the second control point"
    length_of_branches_socket.default_input = 'VALUE'
    length_of_branches_socket.structure_type = 'AUTO'

    # Panel Value of Branches
    value_of_branches_panel = create_branches_1.interface.new_panel("Value of Branches")
    # Socket Min
    min_socket = create_branches_1.interface.new_socket(name="Min", in_out='INPUT', socket_type='NodeSocketFloat', parent = value_of_branches_panel)
    min_socket.default_value = 0.0
    min_socket.min_value = -3.4028234663852886e+38
    min_socket.max_value = 3.4028234663852886e+38
    min_socket.subtype = 'NONE'
    min_socket.attribute_domain = 'POINT'
    min_socket.default_input = 'VALUE'
    min_socket.structure_type = 'AUTO'

    # Socket Max
    max_socket = create_branches_1.interface.new_socket(name="Max", in_out='INPUT', socket_type='NodeSocketFloat', parent = value_of_branches_panel)
    max_socket.default_value = 1.0
    max_socket.min_value = -3.4028234663852886e+38
    max_socket.max_value = 3.4028234663852886e+38
    max_socket.subtype = 'NONE'
    max_socket.attribute_domain = 'POINT'
    max_socket.default_input = 'VALUE'
    max_socket.structure_type = 'AUTO'

    # Socket Seed
    seed_socket = create_branches_1.interface.new_socket(name="Seed", in_out='INPUT', socket_type='NodeSocketInt', parent = value_of_branches_panel)
    seed_socket.default_value = 0
    seed_socket.min_value = -10000
    seed_socket.max_value = 10000
    seed_socket.subtype = 'NONE'
    seed_socket.attribute_domain = 'POINT'
    seed_socket.default_input = 'VALUE'
    seed_socket.structure_type = 'AUTO'


    # Initialize create_branches_1 nodes

    # Node Group Input
    group_input = create_branches_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"

    # Node Group Output
    group_output = create_branches_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True

    # Node Instance on Points.001
    instance_on_points_001 = create_branches_1.nodes.new("GeometryNodeInstanceOnPoints")
    instance_on_points_001.name = "Instance on Points.001"
    # Pick Instance
    instance_on_points_001.inputs[3].default_value = False
    # Instance Index
    instance_on_points_001.inputs[4].default_value = 0

    # Node Curve Line.001
    curve_line_001 = create_branches_1.nodes.new("GeometryNodeCurvePrimitiveLine")
    curve_line_001.name = "Curve Line.001"
    curve_line_001.mode = 'POINTS'
    # Start
    curve_line_001.inputs[0].default_value = (0.0, 0.0, 0.0)

    # Node Curve Tangent
    curve_tangent = create_branches_1.nodes.new("GeometryNodeInputTangent")
    curve_tangent.name = "Curve Tangent"

    # Node Curve Tangent.001
    curve_tangent_001 = create_branches_1.nodes.new("GeometryNodeInputTangent")
    curve_tangent_001.name = "Curve Tangent.001"

    # Node Endpoint Selection
    endpoint_selection = create_branches_1.nodes.new("GeometryNodeCurveEndpointSelection")
    endpoint_selection.name = "Endpoint Selection"
    # Start Size
    endpoint_selection.inputs[0].default_value = 0

    # Node Random Value.001
    random_value_001 = create_branches_1.nodes.new("FunctionNodeRandomValue")
    random_value_001.name = "Random Value.001"
    random_value_001.data_type = 'FLOAT'
    # ID
    random_value_001.inputs[7].default_value = 0

    # Node Realize Instances.001
    realize_instances_001 = create_branches_1.nodes.new("GeometryNodeRealizeInstances")
    realize_instances_001.name = "Realize Instances.001"
    realize_instances_001.realize_to_point_domain = False
    # Selection
    realize_instances_001.inputs[1].default_value = True
    # Realize All
    realize_instances_001.inputs[2].default_value = True
    # Depth
    realize_instances_001.inputs[3].default_value = 0

    # Node Resample Curve.001
    resample_curve_001 = create_branches_1.nodes.new("GeometryNodeResampleCurve")
    resample_curve_001.name = "Resample Curve.001"
    resample_curve_001.keep_last_segment = True
    # Selection
    resample_curve_001.inputs[1].default_value = True
    # Mode
    resample_curve_001.inputs[2].default_value = 'Count'
    # Count
    resample_curve_001.inputs[3].default_value = 10
    # Length
    resample_curve_001.inputs[4].default_value = 0.10000000149011612

    # Node Vector Math
    vector_math = create_branches_1.nodes.new("ShaderNodeVectorMath")
    vector_math.name = "Vector Math"
    vector_math.operation = 'MULTIPLY'
    # Vector_001
    vector_math.inputs[1].default_value = (1.9999998807907104, 1.9999998807907104, 1.9999998807907104)

    # Set locations
    create_branches_1.nodes["Group Input"].location = (-1573.1690673828125, 732.4583740234375)
    create_branches_1.nodes["Group Output"].location = (65.77777099609375, 801.5029907226562)
    create_branches_1.nodes["Instance on Points.001"].location = (-829.55224609375, 878.2093505859375)
    create_branches_1.nodes["Curve Line.001"].location = (-1069.1549072265625, 605.0330810546875)
    create_branches_1.nodes["Curve Tangent"].location = (-1334.047607421875, 295.4117126464844)
    create_branches_1.nodes["Curve Tangent.001"].location = (-993.8499755859375, 224.74844360351562)
    create_branches_1.nodes["Endpoint Selection"].location = (-1068.01123046875, 758.6441040039062)
    create_branches_1.nodes["Random Value.001"].location = (-1272.159423828125, 711.5013427734375)
    create_branches_1.nodes["Realize Instances.001"].location = (-613.6142578125, 726.2068481445312)
    create_branches_1.nodes["Resample Curve.001"].location = (-433.61370849609375, 785.29248046875)
    create_branches_1.nodes["Vector Math"].location = (-760.9185791015625, 469.9234619140625)

    # Set dimensions
    create_branches_1.nodes["Group Input"].width  = 140.0
    create_branches_1.nodes["Group Input"].height = 100.0

    create_branches_1.nodes["Group Output"].width  = 140.0
    create_branches_1.nodes["Group Output"].height = 100.0

    create_branches_1.nodes["Instance on Points.001"].width  = 140.0
    create_branches_1.nodes["Instance on Points.001"].height = 100.0

    create_branches_1.nodes["Curve Line.001"].width  = 140.0
    create_branches_1.nodes["Curve Line.001"].height = 100.0

    create_branches_1.nodes["Curve Tangent"].width  = 140.0
    create_branches_1.nodes["Curve Tangent"].height = 100.0

    create_branches_1.nodes["Curve Tangent.001"].width  = 140.0
    create_branches_1.nodes["Curve Tangent.001"].height = 100.0

    create_branches_1.nodes["Endpoint Selection"].width  = 140.0
    create_branches_1.nodes["Endpoint Selection"].height = 100.0

    create_branches_1.nodes["Random Value.001"].width  = 140.0
    create_branches_1.nodes["Random Value.001"].height = 100.0

    create_branches_1.nodes["Realize Instances.001"].width  = 140.0
    create_branches_1.nodes["Realize Instances.001"].height = 100.0

    create_branches_1.nodes["Resample Curve.001"].width  = 140.0
    create_branches_1.nodes["Resample Curve.001"].height = 100.0

    create_branches_1.nodes["Vector Math"].width  = 140.0
    create_branches_1.nodes["Vector Math"].height = 100.0


    # Initialize create_branches_1 links

    # curve_line_001.Curve -> instance_on_points_001.Instance
    create_branches_1.links.new(
        create_branches_1.nodes["Curve Line.001"].outputs[0],
        create_branches_1.nodes["Instance on Points.001"].inputs[2]
    )
    # vector_math.Vector -> instance_on_points_001.Rotation
    create_branches_1.links.new(
        create_branches_1.nodes["Vector Math"].outputs[0],
        create_branches_1.nodes["Instance on Points.001"].inputs[5]
    )
    # curve_tangent_001.Tangent -> instance_on_points_001.Scale
    create_branches_1.links.new(
        create_branches_1.nodes["Curve Tangent.001"].outputs[0],
        create_branches_1.nodes["Instance on Points.001"].inputs[6]
    )
    # endpoint_selection.Selection -> instance_on_points_001.Selection
    create_branches_1.links.new(
        create_branches_1.nodes["Endpoint Selection"].outputs[0],
        create_branches_1.nodes["Instance on Points.001"].inputs[1]
    )
    # random_value_001.Value -> endpoint_selection.End Size
    create_branches_1.links.new(
        create_branches_1.nodes["Random Value.001"].outputs[1],
        create_branches_1.nodes["Endpoint Selection"].inputs[1]
    )
    # instance_on_points_001.Instances -> realize_instances_001.Geometry
    create_branches_1.links.new(
        create_branches_1.nodes["Instance on Points.001"].outputs[0],
        create_branches_1.nodes["Realize Instances.001"].inputs[0]
    )
    # realize_instances_001.Geometry -> resample_curve_001.Curve
    create_branches_1.links.new(
        create_branches_1.nodes["Realize Instances.001"].outputs[0],
        create_branches_1.nodes["Resample Curve.001"].inputs[0]
    )
    # curve_tangent.Tangent -> vector_math.Vector
    create_branches_1.links.new(
        create_branches_1.nodes["Curve Tangent"].outputs[0],
        create_branches_1.nodes["Vector Math"].inputs[0]
    )
    # resample_curve_001.Curve -> group_output.Geometry
    create_branches_1.links.new(
        create_branches_1.nodes["Resample Curve.001"].outputs[0],
        create_branches_1.nodes["Group Output"].inputs[0]
    )
    # group_input.Geometry -> instance_on_points_001.Points
    create_branches_1.links.new(
        create_branches_1.nodes["Group Input"].outputs[0],
        create_branches_1.nodes["Instance on Points.001"].inputs[0]
    )
    # group_input.Length of Branches -> curve_line_001.End
    create_branches_1.links.new(
        create_branches_1.nodes["Group Input"].outputs[1],
        create_branches_1.nodes["Curve Line.001"].inputs[1]
    )
    # group_input.Min -> random_value_001.Min
    create_branches_1.links.new(
        create_branches_1.nodes["Group Input"].outputs[2],
        create_branches_1.nodes["Random Value.001"].inputs[2]
    )
    # group_input.Max -> random_value_001.Max
    create_branches_1.links.new(
        create_branches_1.nodes["Group Input"].outputs[3],
        create_branches_1.nodes["Random Value.001"].inputs[3]
    )
    # group_input.Seed -> random_value_001.Seed
    create_branches_1.links.new(
        create_branches_1.nodes["Group Input"].outputs[4],
        create_branches_1.nodes["Random Value.001"].inputs[8]
    )

    return create_branches_1

def create_leafs_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize create leafs node group"""
    create_leafs_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="create leafs")

    create_leafs_1.color_tag = 'NONE'
    create_leafs_1.description = ""
    create_leafs_1.default_group_node_width = 140
    create_leafs_1.is_modifier = True
    create_leafs_1.show_modifier_manage_panel = True

    # create_leafs_1 interface

    # Socket Geometry
    geometry_socket = create_leafs_1.interface.new_socket(name="Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    # Socket Geometry
    geometry_socket_1 = create_leafs_1.interface.new_socket(name="Geometry", in_out='INPUT', socket_type='NodeSocketGeometry')
    geometry_socket_1.attribute_domain = 'POINT'
    geometry_socket_1.default_input = 'VALUE'
    geometry_socket_1.structure_type = 'AUTO'

    # Socket Branches
    branches_socket = create_leafs_1.interface.new_socket(name="Branches", in_out='INPUT', socket_type='NodeSocketGeometry')
    branches_socket.attribute_domain = 'POINT'
    branches_socket.description = "Geometry that is instanced on the points"
    branches_socket.default_input = 'VALUE'
    branches_socket.structure_type = 'AUTO'

    # Panel distance leafs
    distance_leafs_panel = create_leafs_1.interface.new_panel("distance leafs")
    # Socket Radius
    radius_socket = create_leafs_1.interface.new_socket(name="Radius", in_out='INPUT', socket_type='NodeSocketFloat', parent = distance_leafs_panel)
    radius_socket.default_value = 0.11999998986721039
    radius_socket.min_value = 0.0
    radius_socket.max_value = 3.4028234663852886e+38
    radius_socket.subtype = 'DISTANCE'
    radius_socket.attribute_domain = 'POINT'
    radius_socket.description = "Distance from the generated points to the origin"
    radius_socket.default_input = 'VALUE'
    radius_socket.structure_type = 'AUTO'


    # Panel Endpoint Selection
    endpoint_selection_panel = create_leafs_1.interface.new_panel("Endpoint Selection")
    # Socket Start Size
    start_size_socket = create_leafs_1.interface.new_socket(name="Start Size", in_out='INPUT', socket_type='NodeSocketInt', parent = endpoint_selection_panel)
    start_size_socket.default_value = 0
    start_size_socket.min_value = 0
    start_size_socket.max_value = 2147483647
    start_size_socket.subtype = 'NONE'
    start_size_socket.attribute_domain = 'POINT'
    start_size_socket.description = "The amount of points to select from the start of each spline"
    start_size_socket.default_input = 'VALUE'
    start_size_socket.structure_type = 'AUTO'

    # Socket End Size
    end_size_socket = create_leafs_1.interface.new_socket(name="End Size", in_out='INPUT', socket_type='NodeSocketInt', parent = endpoint_selection_panel)
    end_size_socket.default_value = 1
    end_size_socket.min_value = 0
    end_size_socket.max_value = 2147483647
    end_size_socket.subtype = 'NONE'
    end_size_socket.attribute_domain = 'POINT'
    end_size_socket.description = "The amount of points to select from the end of each spline"
    end_size_socket.default_input = 'VALUE'
    end_size_socket.structure_type = 'AUTO'


    # Initialize create_leafs_1 nodes

    # Node Instance on Points.001
    instance_on_points_001 = create_leafs_1.nodes.new("GeometryNodeInstanceOnPoints")
    instance_on_points_001.name = "Instance on Points.001"
    # Pick Instance
    instance_on_points_001.inputs[3].default_value = False
    # Instance Index
    instance_on_points_001.inputs[4].default_value = 0
    # Rotation
    instance_on_points_001.inputs[5].default_value = (0.0, 0.0, 0.0)

    # Node Ico Sphere
    ico_sphere = create_leafs_1.nodes.new("GeometryNodeMeshIcoSphere")
    ico_sphere.name = "Ico Sphere"
    # Subdivisions
    ico_sphere.inputs[1].default_value = 2

    # Node Endpoint Selection
    endpoint_selection = create_leafs_1.nodes.new("GeometryNodeCurveEndpointSelection")
    endpoint_selection.name = "Endpoint Selection"

    # Node Random Value.001
    random_value_001 = create_leafs_1.nodes.new("FunctionNodeRandomValue")
    random_value_001.name = "Random Value.001"
    random_value_001.data_type = 'FLOAT'
    # Min_001
    random_value_001.inputs[2].default_value = 0.0
    # Max_001
    random_value_001.inputs[3].default_value = 2.4000000953674316
    # ID
    random_value_001.inputs[7].default_value = 0
    # Seed
    random_value_001.inputs[8].default_value = 0

    # Node Realize Instances.001
    realize_instances_001 = create_leafs_1.nodes.new("GeometryNodeRealizeInstances")
    realize_instances_001.name = "Realize Instances.001"
    realize_instances_001.realize_to_point_domain = False
    # Selection
    realize_instances_001.inputs[1].default_value = True
    # Realize All
    realize_instances_001.inputs[2].default_value = True
    # Depth
    realize_instances_001.inputs[3].default_value = 0

    # Node Instance on Points.002
    instance_on_points_002 = create_leafs_1.nodes.new("GeometryNodeInstanceOnPoints")
    instance_on_points_002.name = "Instance on Points.002"
    # Selection
    instance_on_points_002.inputs[1].default_value = True
    # Pick Instance
    instance_on_points_002.inputs[3].default_value = False
    # Instance Index
    instance_on_points_002.inputs[4].default_value = 0

    # Node Curve Line.001
    curve_line_001 = create_leafs_1.nodes.new("GeometryNodeCurvePrimitiveLine")
    curve_line_001.name = "Curve Line.001"
    curve_line_001.mode = 'POINTS'
    # Start
    curve_line_001.inputs[0].default_value = (0.0, 0.0, 0.0)
    # End
    curve_line_001.inputs[1].default_value = (0.0, 0.0, 1.0)

    # Node Normal
    normal = create_leafs_1.nodes.new("GeometryNodeInputNormal")
    normal.name = "Normal"
    normal.legacy_corner_normals = False

    # Node Align Euler to Vector
    align_euler_to_vector = create_leafs_1.nodes.new("FunctionNodeAlignEulerToVector")
    align_euler_to_vector.name = "Align Euler to Vector"
    align_euler_to_vector.axis = 'Z'
    align_euler_to_vector.pivot_axis = 'AUTO'
    # Rotation
    align_euler_to_vector.inputs[0].default_value = (0.0, 0.0, 0.0)
    # Factor
    align_euler_to_vector.inputs[1].default_value = 1.0

    # Node Instance on Points.003
    instance_on_points_003 = create_leafs_1.nodes.new("GeometryNodeInstanceOnPoints")
    instance_on_points_003.name = "Instance on Points.003"
    # Selection
    instance_on_points_003.inputs[1].default_value = True
    # Pick Instance
    instance_on_points_003.inputs[3].default_value = False
    # Instance Index
    instance_on_points_003.inputs[4].default_value = 0

    # Node Random Value.002
    random_value_002 = create_leafs_1.nodes.new("FunctionNodeRandomValue")
    random_value_002.name = "Random Value.002"
    random_value_002.data_type = 'FLOAT'
    # Min_001
    random_value_002.inputs[2].default_value = 0.0
    # Max_001
    random_value_002.inputs[3].default_value = 0.10000000149011612
    # ID
    random_value_002.inputs[7].default_value = 0
    # Seed
    random_value_002.inputs[8].default_value = 58

    # Node Realize Instances.002
    realize_instances_002 = create_leafs_1.nodes.new("GeometryNodeRealizeInstances")
    realize_instances_002.name = "Realize Instances.002"
    realize_instances_002.realize_to_point_domain = False
    # Selection
    realize_instances_002.inputs[1].default_value = True
    # Realize All
    realize_instances_002.inputs[2].default_value = True
    # Depth
    realize_instances_002.inputs[3].default_value = 0

    # Node Vector Math.002
    vector_math_002 = create_leafs_1.nodes.new("ShaderNodeVectorMath")
    vector_math_002.name = "Vector Math.002"
    vector_math_002.operation = 'MULTIPLY'
    # Vector_001
    vector_math_002.inputs[1].default_value = (2.5999999046325684, 2.5999999046325684, 2.5999999046325684)

    # Node Curve Tangent
    curve_tangent = create_leafs_1.nodes.new("GeometryNodeInputTangent")
    curve_tangent.name = "Curve Tangent"

    # Node Random Value.003
    random_value_003 = create_leafs_1.nodes.new("FunctionNodeRandomValue")
    random_value_003.name = "Random Value.003"
    random_value_003.data_type = 'FLOAT'
    # Min_001
    random_value_003.inputs[2].default_value = 0.0
    # Max_001
    random_value_003.inputs[3].default_value = 0.10000000149011612
    # ID
    random_value_003.inputs[7].default_value = 0
    # Seed
    random_value_003.inputs[8].default_value = 36

    # Node Group Output
    group_output = create_leafs_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True

    # Node create leafs
    create_leafs_2 = create_leafs_1.nodes.new("NodeGroupInput")
    create_leafs_2.name = "create leafs"

    # Set locations
    create_leafs_1.nodes["Instance on Points.001"].location = (-1272.5946044921875, 248.10260009765625)
    create_leafs_1.nodes["Ico Sphere"].location = (-1508.6707763671875, 47.49530029296875)
    create_leafs_1.nodes["Endpoint Selection"].location = (-1759.8056640625, -3.3269805908203125)
    create_leafs_1.nodes["Random Value.001"].location = (-1464.2364501953125, -177.50405883789062)
    create_leafs_1.nodes["Realize Instances.001"].location = (-1094.535400390625, 401.9665222167969)
    create_leafs_1.nodes["Instance on Points.002"].location = (-618.6813354492188, 411.1889953613281)
    create_leafs_1.nodes["Curve Line.001"].location = (-1034.1002197265625, 49.658355712890625)
    create_leafs_1.nodes["Normal"].location = (-1224.0291748046875, -266.41217041015625)
    create_leafs_1.nodes["Align Euler to Vector"].location = (-983.072998046875, -128.46466064453125)
    create_leafs_1.nodes["Instance on Points.003"].location = (23.378158569335938, 385.31158447265625)
    create_leafs_1.nodes["Random Value.002"].location = (-198.84298706054688, 50.54742431640625)
    create_leafs_1.nodes["Realize Instances.002"].location = (-292.80584716796875, 480.349609375)
    create_leafs_1.nodes["Vector Math.002"].location = (-525.7653198242188, -63.55389404296875)
    create_leafs_1.nodes["Curve Tangent"].location = (-697.962646484375, -164.60333251953125)
    create_leafs_1.nodes["Random Value.003"].location = (-849.231201171875, -303.66986083984375)
    create_leafs_1.nodes["Group Output"].location = (337.794921875, 450.5766906738281)
    create_leafs_1.nodes["create leafs"].location = (-2177.1953125, 375.96258544921875)

    # Set dimensions
    create_leafs_1.nodes["Instance on Points.001"].width  = 140.0
    create_leafs_1.nodes["Instance on Points.001"].height = 100.0

    create_leafs_1.nodes["Ico Sphere"].width  = 140.0
    create_leafs_1.nodes["Ico Sphere"].height = 100.0

    create_leafs_1.nodes["Endpoint Selection"].width  = 140.0
    create_leafs_1.nodes["Endpoint Selection"].height = 100.0

    create_leafs_1.nodes["Random Value.001"].width  = 140.0
    create_leafs_1.nodes["Random Value.001"].height = 100.0

    create_leafs_1.nodes["Realize Instances.001"].width  = 140.0
    create_leafs_1.nodes["Realize Instances.001"].height = 100.0

    create_leafs_1.nodes["Instance on Points.002"].width  = 140.0
    create_leafs_1.nodes["Instance on Points.002"].height = 100.0

    create_leafs_1.nodes["Curve Line.001"].width  = 140.0
    create_leafs_1.nodes["Curve Line.001"].height = 100.0

    create_leafs_1.nodes["Normal"].width  = 140.0
    create_leafs_1.nodes["Normal"].height = 100.0

    create_leafs_1.nodes["Align Euler to Vector"].width  = 140.0
    create_leafs_1.nodes["Align Euler to Vector"].height = 100.0

    create_leafs_1.nodes["Instance on Points.003"].width  = 140.0
    create_leafs_1.nodes["Instance on Points.003"].height = 100.0

    create_leafs_1.nodes["Random Value.002"].width  = 140.0
    create_leafs_1.nodes["Random Value.002"].height = 100.0

    create_leafs_1.nodes["Realize Instances.002"].width  = 140.0
    create_leafs_1.nodes["Realize Instances.002"].height = 100.0

    create_leafs_1.nodes["Vector Math.002"].width  = 140.0
    create_leafs_1.nodes["Vector Math.002"].height = 100.0

    create_leafs_1.nodes["Curve Tangent"].width  = 140.0
    create_leafs_1.nodes["Curve Tangent"].height = 100.0

    create_leafs_1.nodes["Random Value.003"].width  = 140.0
    create_leafs_1.nodes["Random Value.003"].height = 100.0

    create_leafs_1.nodes["Group Output"].width  = 140.0
    create_leafs_1.nodes["Group Output"].height = 100.0

    create_leafs_1.nodes["create leafs"].width  = 140.0
    create_leafs_1.nodes["create leafs"].height = 100.0


    # Initialize create_leafs_1 links

    # ico_sphere.Mesh -> instance_on_points_001.Instance
    create_leafs_1.links.new(
        create_leafs_1.nodes["Ico Sphere"].outputs[0],
        create_leafs_1.nodes["Instance on Points.001"].inputs[2]
    )
    # endpoint_selection.Selection -> instance_on_points_001.Selection
    create_leafs_1.links.new(
        create_leafs_1.nodes["Endpoint Selection"].outputs[0],
        create_leafs_1.nodes["Instance on Points.001"].inputs[1]
    )
    # random_value_001.Value -> instance_on_points_001.Scale
    create_leafs_1.links.new(
        create_leafs_1.nodes["Random Value.001"].outputs[1],
        create_leafs_1.nodes["Instance on Points.001"].inputs[6]
    )
    # instance_on_points_001.Instances -> realize_instances_001.Geometry
    create_leafs_1.links.new(
        create_leafs_1.nodes["Instance on Points.001"].outputs[0],
        create_leafs_1.nodes["Realize Instances.001"].inputs[0]
    )
    # realize_instances_001.Geometry -> instance_on_points_002.Points
    create_leafs_1.links.new(
        create_leafs_1.nodes["Realize Instances.001"].outputs[0],
        create_leafs_1.nodes["Instance on Points.002"].inputs[0]
    )
    # curve_line_001.Curve -> instance_on_points_002.Instance
    create_leafs_1.links.new(
        create_leafs_1.nodes["Curve Line.001"].outputs[0],
        create_leafs_1.nodes["Instance on Points.002"].inputs[2]
    )
    # align_euler_to_vector.Rotation -> instance_on_points_002.Rotation
    create_leafs_1.links.new(
        create_leafs_1.nodes["Align Euler to Vector"].outputs[0],
        create_leafs_1.nodes["Instance on Points.002"].inputs[5]
    )
    # normal.Normal -> align_euler_to_vector.Vector
    create_leafs_1.links.new(
        create_leafs_1.nodes["Normal"].outputs[0],
        create_leafs_1.nodes["Align Euler to Vector"].inputs[2]
    )
    # realize_instances_002.Geometry -> instance_on_points_003.Points
    create_leafs_1.links.new(
        create_leafs_1.nodes["Realize Instances.002"].outputs[0],
        create_leafs_1.nodes["Instance on Points.003"].inputs[0]
    )
    # random_value_002.Value -> instance_on_points_003.Scale
    create_leafs_1.links.new(
        create_leafs_1.nodes["Random Value.002"].outputs[1],
        create_leafs_1.nodes["Instance on Points.003"].inputs[6]
    )
    # instance_on_points_002.Instances -> realize_instances_002.Geometry
    create_leafs_1.links.new(
        create_leafs_1.nodes["Instance on Points.002"].outputs[0],
        create_leafs_1.nodes["Realize Instances.002"].inputs[0]
    )
    # vector_math_002.Vector -> instance_on_points_003.Rotation
    create_leafs_1.links.new(
        create_leafs_1.nodes["Vector Math.002"].outputs[0],
        create_leafs_1.nodes["Instance on Points.003"].inputs[5]
    )
    # curve_tangent.Tangent -> vector_math_002.Vector
    create_leafs_1.links.new(
        create_leafs_1.nodes["Curve Tangent"].outputs[0],
        create_leafs_1.nodes["Vector Math.002"].inputs[0]
    )
    # random_value_003.Value -> instance_on_points_002.Scale
    create_leafs_1.links.new(
        create_leafs_1.nodes["Random Value.003"].outputs[1],
        create_leafs_1.nodes["Instance on Points.002"].inputs[6]
    )
    # create_leafs_2.Geometry -> instance_on_points_001.Points
    create_leafs_1.links.new(
        create_leafs_1.nodes["create leafs"].outputs[0],
        create_leafs_1.nodes["Instance on Points.001"].inputs[0]
    )
    # create_leafs_2.Branches -> instance_on_points_003.Instance
    create_leafs_1.links.new(
        create_leafs_1.nodes["create leafs"].outputs[1],
        create_leafs_1.nodes["Instance on Points.003"].inputs[2]
    )
    # create_leafs_2.Start Size -> endpoint_selection.Start Size
    create_leafs_1.links.new(
        create_leafs_1.nodes["create leafs"].outputs[3],
        create_leafs_1.nodes["Endpoint Selection"].inputs[0]
    )
    # create_leafs_2.End Size -> endpoint_selection.End Size
    create_leafs_1.links.new(
        create_leafs_1.nodes["create leafs"].outputs[4],
        create_leafs_1.nodes["Endpoint Selection"].inputs[1]
    )
    # create_leafs_2.Radius -> ico_sphere.Radius
    create_leafs_1.links.new(
        create_leafs_1.nodes["create leafs"].outputs[2],
        create_leafs_1.nodes["Ico Sphere"].inputs[0]
    )
    # instance_on_points_003.Instances -> group_output.Geometry
    create_leafs_1.links.new(
        create_leafs_1.nodes["Instance on Points.003"].outputs[0],
        create_leafs_1.nodes["Group Output"].inputs[0]
    )

    return create_leafs_1

def thickness_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize Thickness node group"""
    thickness_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="Thickness")

    thickness_1.color_tag = 'NONE'
    thickness_1.description = ""
    thickness_1.default_group_node_width = 140
    thickness_1.is_modifier = True
    thickness_1.show_modifier_manage_panel = True

    # thickness_1 interface

    # Socket Geometry
    geometry_socket = thickness_1.interface.new_socket(name="Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    # Socket Geometry
    geometry_socket_1 = thickness_1.interface.new_socket(name="Geometry", in_out='INPUT', socket_type='NodeSocketGeometry')
    geometry_socket_1.attribute_domain = 'POINT'
    geometry_socket_1.default_input = 'VALUE'
    geometry_socket_1.structure_type = 'AUTO'

    # Panel Panel
    panel_panel = thickness_1.interface.new_panel("Panel")
    # Socket Up Thickness
    up_thickness_socket = thickness_1.interface.new_socket(name="Up Thickness", in_out='INPUT', socket_type='NodeSocketFloat', parent = panel_panel)
    up_thickness_socket.default_value = 0.0
    up_thickness_socket.min_value = -10000.0
    up_thickness_socket.max_value = 10000.0
    up_thickness_socket.subtype = 'NONE'
    up_thickness_socket.attribute_domain = 'POINT'
    up_thickness_socket.default_input = 'VALUE'
    up_thickness_socket.structure_type = 'AUTO'

    # Socket Down Thickness
    down_thickness_socket = thickness_1.interface.new_socket(name="Down Thickness", in_out='INPUT', socket_type='NodeSocketFloat', parent = panel_panel)
    down_thickness_socket.default_value = 3.299999952316284
    down_thickness_socket.min_value = -10000.0
    down_thickness_socket.max_value = 10000.0
    down_thickness_socket.subtype = 'NONE'
    down_thickness_socket.attribute_domain = 'POINT'
    down_thickness_socket.default_input = 'VALUE'
    down_thickness_socket.structure_type = 'AUTO'


    # Initialize thickness_1 nodes

    # Node Group Input
    group_input = thickness_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"

    # Node Group Output
    group_output = thickness_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True

    # Node Set Curve Radius
    set_curve_radius = thickness_1.nodes.new("GeometryNodeSetCurveRadius")
    set_curve_radius.name = "Set Curve Radius"
    # Selection
    set_curve_radius.inputs[1].default_value = True

    # Node Spline Parameter.001
    spline_parameter_001 = thickness_1.nodes.new("GeometryNodeSplineParameter")
    spline_parameter_001.name = "Spline Parameter.001"

    # Node Color Ramp
    color_ramp = thickness_1.nodes.new("ShaderNodeValToRGB")
    color_ramp.name = "Color Ramp"
    color_ramp.color_ramp.color_mode = 'RGB'
    color_ramp.color_ramp.hue_interpolation = 'NEAR'
    color_ramp.color_ramp.interpolation = 'LINEAR'

    # Initialize color ramp elements
    color_ramp.color_ramp.elements.remove(color_ramp.color_ramp.elements[0])
    color_ramp_cre_0 = color_ramp.color_ramp.elements[0]
    color_ramp_cre_0.position = 0.0
    color_ramp_cre_0.alpha = 1.0
    color_ramp_cre_0.color = (1.0, 1.0, 1.0, 1.0)

    color_ramp_cre_1 = color_ramp.color_ramp.elements.new(1.0)
    color_ramp_cre_1.alpha = 1.0
    color_ramp_cre_1.color = (0.0, 0.0, 0.0, 1.0)


    # Node Map Range
    map_range = thickness_1.nodes.new("ShaderNodeMapRange")
    map_range.name = "Map Range"
    map_range.clamp = True
    map_range.data_type = 'FLOAT'
    map_range.interpolation_type = 'LINEAR'
    # From Min
    map_range.inputs[1].default_value = 0.0
    # From Max
    map_range.inputs[2].default_value = 1.0

    # Set locations
    thickness_1.nodes["Group Input"].location = (-705.4496459960938, -36.80598449707031)
    thickness_1.nodes["Group Output"].location = (450.5889892578125, 42.34330749511719)
    thickness_1.nodes["Set Curve Radius"].location = (-2.5598297119140625, -31.15485954284668)
    thickness_1.nodes["Spline Parameter.001"].location = (-568.7120971679688, -344.85760498046875)
    thickness_1.nodes["Color Ramp"].location = (-386.9686279296875, -290.693359375)
    thickness_1.nodes["Map Range"].location = (-174.8523406982422, -142.71437072753906)

    # Set dimensions
    thickness_1.nodes["Group Input"].width  = 140.0
    thickness_1.nodes["Group Input"].height = 100.0

    thickness_1.nodes["Group Output"].width  = 140.0
    thickness_1.nodes["Group Output"].height = 100.0

    thickness_1.nodes["Set Curve Radius"].width  = 140.0
    thickness_1.nodes["Set Curve Radius"].height = 100.0

    thickness_1.nodes["Spline Parameter.001"].width  = 140.0
    thickness_1.nodes["Spline Parameter.001"].height = 100.0

    thickness_1.nodes["Color Ramp"].width  = 146.45166015625
    thickness_1.nodes["Color Ramp"].height = 100.0

    thickness_1.nodes["Map Range"].width  = 140.0
    thickness_1.nodes["Map Range"].height = 100.0


    # Initialize thickness_1 links

    # map_range.Result -> set_curve_radius.Radius
    thickness_1.links.new(
        thickness_1.nodes["Map Range"].outputs[0],
        thickness_1.nodes["Set Curve Radius"].inputs[2]
    )
    # spline_parameter_001.Factor -> color_ramp.Factor
    thickness_1.links.new(
        thickness_1.nodes["Spline Parameter.001"].outputs[0],
        thickness_1.nodes["Color Ramp"].inputs[0]
    )
    # color_ramp.Color -> map_range.Value
    thickness_1.links.new(
        thickness_1.nodes["Color Ramp"].outputs[0],
        thickness_1.nodes["Map Range"].inputs[0]
    )
    # group_input.Geometry -> set_curve_radius.Curve
    thickness_1.links.new(
        thickness_1.nodes["Group Input"].outputs[0],
        thickness_1.nodes["Set Curve Radius"].inputs[0]
    )
    # group_input.Up Thickness -> map_range.To Min
    thickness_1.links.new(
        thickness_1.nodes["Group Input"].outputs[1],
        thickness_1.nodes["Map Range"].inputs[3]
    )
    # group_input.Down Thickness -> map_range.To Max
    thickness_1.links.new(
        thickness_1.nodes["Group Input"].outputs[2],
        thickness_1.nodes["Map Range"].inputs[4]
    )
    # set_curve_radius.Curve -> group_output.Geometry
    thickness_1.links.new(
        thickness_1.nodes["Set Curve Radius"].outputs[0],
        thickness_1.nodes["Group Output"].inputs[0]
    )

    return thickness_1

def choos_name_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize choos name node group"""
    choos_name_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="choos name")

    choos_name_1.color_tag = 'NONE'
    choos_name_1.description = ""
    choos_name_1.default_group_node_width = 140
    choos_name_1.is_modifier = True
    choos_name_1.show_modifier_manage_panel = True

    # choos_name_1 interface

    # Socket Geometry
    geometry_socket = choos_name_1.interface.new_socket(name="Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    # Socket Geometry
    geometry_socket_1 = choos_name_1.interface.new_socket(name="Geometry", in_out='INPUT', socket_type='NodeSocketGeometry')
    geometry_socket_1.attribute_domain = 'POINT'
    geometry_socket_1.description = "Points to modify the positions of"
    geometry_socket_1.default_input = 'VALUE'
    geometry_socket_1.structure_type = 'AUTO'

    # Socket Scale
    scale_socket = choos_name_1.interface.new_socket(name="Scale", in_out='INPUT', socket_type='NodeSocketFloat')
    scale_socket.default_value = 25.19999885559082
    scale_socket.min_value = -1000.0
    scale_socket.max_value = 1000.0
    scale_socket.subtype = 'NONE'
    scale_socket.attribute_domain = 'POINT'
    scale_socket.description = "Scale of the base noise octave"
    scale_socket.default_input = 'VALUE'
    scale_socket.structure_type = 'AUTO'

    # Socket Lacunarity
    lacunarity_socket = choos_name_1.interface.new_socket(name="Lacunarity", in_out='INPUT', socket_type='NodeSocketFloat')
    lacunarity_socket.default_value = 2.0
    lacunarity_socket.min_value = 0.0
    lacunarity_socket.max_value = 1000.0
    lacunarity_socket.subtype = 'NONE'
    lacunarity_socket.attribute_domain = 'POINT'
    lacunarity_socket.description = "The difference between the scale of each two consecutive octaves. Larger values corresponds to larger scale for higher octaves"
    lacunarity_socket.default_input = 'VALUE'
    lacunarity_socket.structure_type = 'AUTO'

    # Socket Distortion
    distortion_socket = choos_name_1.interface.new_socket(name="Distortion", in_out='INPUT', socket_type='NodeSocketFloat')
    distortion_socket.default_value = 0.0
    distortion_socket.min_value = -1000.0
    distortion_socket.max_value = 1000.0
    distortion_socket.subtype = 'NONE'
    distortion_socket.attribute_domain = 'POINT'
    distortion_socket.description = "Amount of distortion"
    distortion_socket.default_input = 'VALUE'
    distortion_socket.structure_type = 'AUTO'

    # Initialize choos_name_1 nodes

    # Node Group Input
    group_input = choos_name_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"

    # Node Group Output
    group_output = choos_name_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True

    # Node Set Position
    set_position = choos_name_1.nodes.new("GeometryNodeSetPosition")
    set_position.name = "Set Position"
    # Selection
    set_position.inputs[1].default_value = True
    # Position
    set_position.inputs[2].default_value = (0.0, 0.0, 0.0)

    # Node Noise Texture
    noise_texture = choos_name_1.nodes.new("ShaderNodeTexNoise")
    noise_texture.name = "Noise Texture"
    noise_texture.noise_dimensions = '3D'
    noise_texture.noise_type = 'FBM'
    noise_texture.normalize = True
    # Vector
    noise_texture.inputs[0].default_value = (0.0, 0.0, 0.0)
    # Detail
    noise_texture.inputs[3].default_value = 0.0
    # Roughness
    noise_texture.inputs[4].default_value = 0.5

    # Node Vector Math
    vector_math = choos_name_1.nodes.new("ShaderNodeVectorMath")
    vector_math.name = "Vector Math"
    vector_math.operation = 'SUBTRACT'
    # Vector_001
    vector_math.inputs[1].default_value = (0.5, 0.5, 0.5)

    # Node Vector Math.001
    vector_math_001 = choos_name_1.nodes.new("ShaderNodeVectorMath")
    vector_math_001.name = "Vector Math.001"
    vector_math_001.operation = 'MULTIPLY'
    # Vector_001
    vector_math_001.inputs[1].default_value = (1.9999998807907104, 1.9999998807907104, 1.9999998807907104)

    # Set locations
    choos_name_1.nodes["Group Input"].location = (-686.7176513671875, -66.99710083007812)
    choos_name_1.nodes["Group Output"].location = (278.9999694824219, 0.0)
    choos_name_1.nodes["Set Position"].location = (53.386329650878906, 11.726364135742188)
    choos_name_1.nodes["Noise Texture"].location = (-347.723876953125, -436.97113037109375)
    choos_name_1.nodes["Vector Math"].location = (-147.70263671875, -349.927490234375)
    choos_name_1.nodes["Vector Math.001"].location = (101.1148681640625, -272.4564208984375)

    # Set dimensions
    choos_name_1.nodes["Group Input"].width  = 140.0
    choos_name_1.nodes["Group Input"].height = 100.0

    choos_name_1.nodes["Group Output"].width  = 140.0
    choos_name_1.nodes["Group Output"].height = 100.0

    choos_name_1.nodes["Set Position"].width  = 140.0
    choos_name_1.nodes["Set Position"].height = 100.0

    choos_name_1.nodes["Noise Texture"].width  = 145.0
    choos_name_1.nodes["Noise Texture"].height = 100.0

    choos_name_1.nodes["Vector Math"].width  = 140.0
    choos_name_1.nodes["Vector Math"].height = 100.0

    choos_name_1.nodes["Vector Math.001"].width  = 140.0
    choos_name_1.nodes["Vector Math.001"].height = 100.0


    # Initialize choos_name_1 links

    # vector_math_001.Vector -> set_position.Offset
    choos_name_1.links.new(
        choos_name_1.nodes["Vector Math.001"].outputs[0],
        choos_name_1.nodes["Set Position"].inputs[3]
    )
    # noise_texture.Color -> vector_math.Vector
    choos_name_1.links.new(
        choos_name_1.nodes["Noise Texture"].outputs[1],
        choos_name_1.nodes["Vector Math"].inputs[0]
    )
    # vector_math.Vector -> vector_math_001.Vector
    choos_name_1.links.new(
        choos_name_1.nodes["Vector Math"].outputs[0],
        choos_name_1.nodes["Vector Math.001"].inputs[0]
    )
    # set_position.Geometry -> group_output.Geometry
    choos_name_1.links.new(
        choos_name_1.nodes["Set Position"].outputs[0],
        choos_name_1.nodes["Group Output"].inputs[0]
    )
    # group_input.Scale -> noise_texture.Scale
    choos_name_1.links.new(
        choos_name_1.nodes["Group Input"].outputs[1],
        choos_name_1.nodes["Noise Texture"].inputs[2]
    )
    # group_input.Lacunarity -> noise_texture.Lacunarity
    choos_name_1.links.new(
        choos_name_1.nodes["Group Input"].outputs[2],
        choos_name_1.nodes["Noise Texture"].inputs[5]
    )
    # group_input.Distortion -> noise_texture.Distortion
    choos_name_1.links.new(
        choos_name_1.nodes["Group Input"].outputs[3],
        choos_name_1.nodes["Noise Texture"].inputs[8]
    )
    # group_input.Geometry -> set_position.Geometry
    choos_name_1.links.new(
        choos_name_1.nodes["Group Input"].outputs[0],
        choos_name_1.nodes["Set Position"].inputs[0]
    )

    return choos_name_1

def seeds_of_plants_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize Seeds of Plants node group"""
    seeds_of_plants_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="Seeds of Plants")

    seeds_of_plants_1.color_tag = 'NONE'
    seeds_of_plants_1.description = ""
    seeds_of_plants_1.default_group_node_width = 140
    seeds_of_plants_1.is_modifier = True
    seeds_of_plants_1.show_modifier_manage_panel = True

    # seeds_of_plants_1 interface

    # Socket Geometry
    geometry_socket = seeds_of_plants_1.interface.new_socket(name="Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    # Socket Radius
    radius_socket = seeds_of_plants_1.interface.new_socket(name="Radius", in_out='INPUT', socket_type='NodeSocketFloat')
    radius_socket.default_value = 1.0
    radius_socket.min_value = 0.0
    radius_socket.max_value = 3.4028234663852886e+38
    radius_socket.subtype = 'DISTANCE'
    radius_socket.attribute_domain = 'POINT'
    radius_socket.description = "Distance of the points from the origin"
    radius_socket.default_input = 'VALUE'
    radius_socket.structure_type = 'AUTO'

    # Socket Density of plants
    density_of_plants_socket = seeds_of_plants_1.interface.new_socket(name="Density of plants", in_out='INPUT', socket_type='NodeSocketFloat')
    density_of_plants_socket.default_value = 3.0
    density_of_plants_socket.min_value = 0.0
    density_of_plants_socket.max_value = 3.4028234663852886e+38
    density_of_plants_socket.subtype = 'NONE'
    density_of_plants_socket.attribute_domain = 'POINT'
    density_of_plants_socket.default_input = 'VALUE'
    density_of_plants_socket.structure_type = 'AUTO'

    # Socket Curve Line Length
    curve_line_length_socket = seeds_of_plants_1.interface.new_socket(name="Curve Line Length", in_out='INPUT', socket_type='NodeSocketVector')
    curve_line_length_socket.default_value = (0.0, 0.0, 1.0)
    curve_line_length_socket.min_value = -3.4028234663852886e+38
    curve_line_length_socket.max_value = 3.4028234663852886e+38
    curve_line_length_socket.subtype = 'TRANSLATION'
    curve_line_length_socket.attribute_domain = 'POINT'
    curve_line_length_socket.description = "Position of the second control point"
    curve_line_length_socket.default_input = 'VALUE'
    curve_line_length_socket.structure_type = 'AUTO'

    # Initialize seeds_of_plants_1 nodes

    # Node Group Input
    group_input = seeds_of_plants_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"

    # Node Group Output
    group_output = seeds_of_plants_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True

    # Node Curve Circle
    curve_circle = seeds_of_plants_1.nodes.new("GeometryNodeCurvePrimitiveCircle")
    curve_circle.name = "Curve Circle"
    curve_circle.mode = 'RADIUS'
    # Resolution
    curve_circle.inputs[0].default_value = 32

    # Node Fill Curve
    fill_curve = seeds_of_plants_1.nodes.new("GeometryNodeFillCurve")
    fill_curve.name = "Fill Curve"
    # Group ID
    fill_curve.inputs[1].default_value = 0
    # Mode
    fill_curve.inputs[2].default_value = 'Triangles'
    # Fill Rule
    fill_curve.inputs[3].default_value = 'Even-Odd'

    # Node Distribute Points on Faces
    distribute_points_on_faces = seeds_of_plants_1.nodes.new("GeometryNodeDistributePointsOnFaces")
    distribute_points_on_faces.name = "Distribute Points on Faces"
    distribute_points_on_faces.distribute_method = 'RANDOM'
    distribute_points_on_faces.use_legacy_normal = False
    # Selection
    distribute_points_on_faces.inputs[1].default_value = True
    # Seed
    distribute_points_on_faces.inputs[6].default_value = 0

    # Node Instance on Points
    instance_on_points = seeds_of_plants_1.nodes.new("GeometryNodeInstanceOnPoints")
    instance_on_points.name = "Instance on Points"
    # Selection
    instance_on_points.inputs[1].default_value = True
    # Pick Instance
    instance_on_points.inputs[3].default_value = False
    # Instance Index
    instance_on_points.inputs[4].default_value = 0
    # Rotation
    instance_on_points.inputs[5].default_value = (0.0, 0.0, 0.0)

    # Node Curve Line
    curve_line = seeds_of_plants_1.nodes.new("GeometryNodeCurvePrimitiveLine")
    curve_line.name = "Curve Line"
    curve_line.mode = 'POINTS'
    # Start
    curve_line.inputs[0].default_value = (0.0, 0.0, 0.0)

    # Node Map Range
    map_range = seeds_of_plants_1.nodes.new("ShaderNodeMapRange")
    map_range.name = "Map Range"
    map_range.clamp = True
    map_range.data_type = 'FLOAT'
    map_range.interpolation_type = 'LINEAR'
    # Value
    map_range.inputs[0].default_value = 1.0
    # From Min
    map_range.inputs[1].default_value = 0.6000000238418579
    # From Max
    map_range.inputs[2].default_value = 1.0
    # To Min
    map_range.inputs[3].default_value = 0.6000000238418579
    # To Max
    map_range.inputs[4].default_value = 1.0

    # Node Realize Instances
    realize_instances = seeds_of_plants_1.nodes.new("GeometryNodeRealizeInstances")
    realize_instances.name = "Realize Instances"
    realize_instances.realize_to_point_domain = False
    # Selection
    realize_instances.inputs[1].default_value = True
    # Realize All
    realize_instances.inputs[2].default_value = True
    # Depth
    realize_instances.inputs[3].default_value = 0

    # Set locations
    seeds_of_plants_1.nodes["Group Input"].location = (-605.7672729492188, -209.76931762695312)
    seeds_of_plants_1.nodes["Group Output"].location = (749.278076171875, 57.56877136230469)
    seeds_of_plants_1.nodes["Curve Circle"].location = (-347.0433654785156, -102.14080810546875)
    seeds_of_plants_1.nodes["Fill Curve"].location = (-126.25535583496094, -14.290046691894531)
    seeds_of_plants_1.nodes["Distribute Points on Faces"].location = (64.1329345703125, 35.04779815673828)
    seeds_of_plants_1.nodes["Instance on Points"].location = (388.99993896484375, 37.398040771484375)
    seeds_of_plants_1.nodes["Curve Line"].location = (-32.5421257019043, -305.632568359375)
    seeds_of_plants_1.nodes["Map Range"].location = (189.34376525878906, -333.59674072265625)
    seeds_of_plants_1.nodes["Realize Instances"].location = (569.0000610351562, 47.354400634765625)

    # Set dimensions
    seeds_of_plants_1.nodes["Group Input"].width  = 140.0
    seeds_of_plants_1.nodes["Group Input"].height = 100.0

    seeds_of_plants_1.nodes["Group Output"].width  = 140.0
    seeds_of_plants_1.nodes["Group Output"].height = 100.0

    seeds_of_plants_1.nodes["Curve Circle"].width  = 140.0
    seeds_of_plants_1.nodes["Curve Circle"].height = 100.0

    seeds_of_plants_1.nodes["Fill Curve"].width  = 140.0
    seeds_of_plants_1.nodes["Fill Curve"].height = 100.0

    seeds_of_plants_1.nodes["Distribute Points on Faces"].width  = 170.0
    seeds_of_plants_1.nodes["Distribute Points on Faces"].height = 100.0

    seeds_of_plants_1.nodes["Instance on Points"].width  = 140.0
    seeds_of_plants_1.nodes["Instance on Points"].height = 100.0

    seeds_of_plants_1.nodes["Curve Line"].width  = 140.0
    seeds_of_plants_1.nodes["Curve Line"].height = 100.0

    seeds_of_plants_1.nodes["Map Range"].width  = 140.0
    seeds_of_plants_1.nodes["Map Range"].height = 100.0

    seeds_of_plants_1.nodes["Realize Instances"].width  = 140.0
    seeds_of_plants_1.nodes["Realize Instances"].height = 100.0


    # Initialize seeds_of_plants_1 links

    # curve_circle.Curve -> fill_curve.Curve
    seeds_of_plants_1.links.new(
        seeds_of_plants_1.nodes["Curve Circle"].outputs[0],
        seeds_of_plants_1.nodes["Fill Curve"].inputs[0]
    )
    # realize_instances.Geometry -> group_output.Geometry
    seeds_of_plants_1.links.new(
        seeds_of_plants_1.nodes["Realize Instances"].outputs[0],
        seeds_of_plants_1.nodes["Group Output"].inputs[0]
    )
    # fill_curve.Mesh -> distribute_points_on_faces.Mesh
    seeds_of_plants_1.links.new(
        seeds_of_plants_1.nodes["Fill Curve"].outputs[0],
        seeds_of_plants_1.nodes["Distribute Points on Faces"].inputs[0]
    )
    # distribute_points_on_faces.Points -> instance_on_points.Points
    seeds_of_plants_1.links.new(
        seeds_of_plants_1.nodes["Distribute Points on Faces"].outputs[0],
        seeds_of_plants_1.nodes["Instance on Points"].inputs[0]
    )
    # curve_line.Curve -> instance_on_points.Instance
    seeds_of_plants_1.links.new(
        seeds_of_plants_1.nodes["Curve Line"].outputs[0],
        seeds_of_plants_1.nodes["Instance on Points"].inputs[2]
    )
    # map_range.Result -> instance_on_points.Scale
    seeds_of_plants_1.links.new(
        seeds_of_plants_1.nodes["Map Range"].outputs[0],
        seeds_of_plants_1.nodes["Instance on Points"].inputs[6]
    )
    # instance_on_points.Instances -> realize_instances.Geometry
    seeds_of_plants_1.links.new(
        seeds_of_plants_1.nodes["Instance on Points"].outputs[0],
        seeds_of_plants_1.nodes["Realize Instances"].inputs[0]
    )
    # group_input.Radius -> curve_circle.Radius
    seeds_of_plants_1.links.new(
        seeds_of_plants_1.nodes["Group Input"].outputs[0],
        seeds_of_plants_1.nodes["Curve Circle"].inputs[4]
    )
    # group_input.Density of plants -> distribute_points_on_faces.Density
    seeds_of_plants_1.links.new(
        seeds_of_plants_1.nodes["Group Input"].outputs[1],
        seeds_of_plants_1.nodes["Distribute Points on Faces"].inputs[4]
    )
    # group_input.Curve Line Length -> curve_line.End
    seeds_of_plants_1.links.new(
        seeds_of_plants_1.nodes["Group Input"].outputs[2],
        seeds_of_plants_1.nodes["Curve Line"].inputs[1]
    )

    return seeds_of_plants_1

def noise_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize Noise node group"""
    noise_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="Noise")

    noise_1.color_tag = 'NONE'
    noise_1.description = ""
    noise_1.default_group_node_width = 140
    noise_1.show_modifier_manage_panel = True

    # noise_1 interface

    # Socket Geometry
    geometry_socket = noise_1.interface.new_socket(name="Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    # Socket Geometry
    geometry_socket_1 = noise_1.interface.new_socket(name="Geometry", in_out='INPUT', socket_type='NodeSocketGeometry')
    geometry_socket_1.attribute_domain = 'POINT'
    geometry_socket_1.description = "Points to modify the positions of"
    geometry_socket_1.default_input = 'VALUE'
    geometry_socket_1.structure_type = 'AUTO'

    # Socket Position
    position_socket = noise_1.interface.new_socket(name="Position", in_out='INPUT', socket_type='NodeSocketVector')
    position_socket.default_value = (0.5, 0.5, 0.5)
    position_socket.min_value = -10000.0
    position_socket.max_value = 10000.0
    position_socket.subtype = 'NONE'
    position_socket.attribute_domain = 'POINT'
    position_socket.default_input = 'VALUE'
    position_socket.structure_type = 'AUTO'

    # Socket Noise Amplitude
    noise_amplitude_socket = noise_1.interface.new_socket(name="Noise Amplitude", in_out='INPUT', socket_type='NodeSocketVector')
    noise_amplitude_socket.default_value = (0.7000000476837158, 0.7000000476837158, 0.7000000476837158)
    noise_amplitude_socket.min_value = -10000.0
    noise_amplitude_socket.max_value = 10000.0
    noise_amplitude_socket.subtype = 'NONE'
    noise_amplitude_socket.attribute_domain = 'POINT'
    noise_amplitude_socket.default_input = 'VALUE'
    noise_amplitude_socket.structure_type = 'AUTO'

    # Initialize noise_1 nodes

    # Node Set Position
    set_position = noise_1.nodes.new("GeometryNodeSetPosition")
    set_position.name = "Set Position"
    # Selection
    set_position.inputs[1].default_value = True
    # Position
    set_position.inputs[2].default_value = (0.0, 0.0, 0.0)

    # Node Noise Texture
    noise_texture = noise_1.nodes.new("ShaderNodeTexNoise")
    noise_texture.name = "Noise Texture"
    noise_texture.noise_dimensions = '3D'
    noise_texture.noise_type = 'FBM'
    noise_texture.normalize = True
    # Vector
    noise_texture.inputs[0].default_value = (0.0, 0.0, 0.0)
    # Scale
    noise_texture.inputs[2].default_value = 1.500000238418579
    # Detail
    noise_texture.inputs[3].default_value = 2.0
    # Roughness
    noise_texture.inputs[4].default_value = 0.5
    # Lacunarity
    noise_texture.inputs[5].default_value = 2.0
    # Distortion
    noise_texture.inputs[8].default_value = 0.0

    # Node Vector Math
    vector_math = noise_1.nodes.new("ShaderNodeVectorMath")
    vector_math.name = "Vector Math"
    vector_math.operation = 'SUBTRACT'

    # Node Vector Math.001
    vector_math_001 = noise_1.nodes.new("ShaderNodeVectorMath")
    vector_math_001.name = "Vector Math.001"
    vector_math_001.operation = 'MULTIPLY'

    # Node Group Output
    group_output = noise_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True

    # Node Group Input
    group_input = noise_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"

    # Set locations
    noise_1.nodes["Set Position"].location = (290.3138427734375, 76.607421875)
    noise_1.nodes["Noise Texture"].location = (-324.68121337890625, -187.92225646972656)
    noise_1.nodes["Vector Math"].location = (-68.87525177001953, -150.50326538085938)
    noise_1.nodes["Vector Math.001"].location = (124.138671875, -12.60015869140625)
    noise_1.nodes["Group Output"].location = (480.3138427734375, -3.0517578125e-05)
    noise_1.nodes["Group Input"].location = (-490.3138732910156, -3.0517578125e-05)

    # Set dimensions
    noise_1.nodes["Set Position"].width  = 140.0
    noise_1.nodes["Set Position"].height = 100.0

    noise_1.nodes["Noise Texture"].width  = 145.0
    noise_1.nodes["Noise Texture"].height = 100.0

    noise_1.nodes["Vector Math"].width  = 140.0
    noise_1.nodes["Vector Math"].height = 100.0

    noise_1.nodes["Vector Math.001"].width  = 140.0
    noise_1.nodes["Vector Math.001"].height = 100.0

    noise_1.nodes["Group Output"].width  = 140.0
    noise_1.nodes["Group Output"].height = 100.0

    noise_1.nodes["Group Input"].width  = 140.0
    noise_1.nodes["Group Input"].height = 100.0


    # Initialize noise_1 links

    # noise_texture.Color -> vector_math.Vector
    noise_1.links.new(
        noise_1.nodes["Noise Texture"].outputs[1],
        noise_1.nodes["Vector Math"].inputs[0]
    )
    # vector_math.Vector -> vector_math_001.Vector
    noise_1.links.new(
        noise_1.nodes["Vector Math"].outputs[0],
        noise_1.nodes["Vector Math.001"].inputs[0]
    )
    # vector_math_001.Vector -> set_position.Offset
    noise_1.links.new(
        noise_1.nodes["Vector Math.001"].outputs[0],
        noise_1.nodes["Set Position"].inputs[3]
    )
    # set_position.Geometry -> group_output.Geometry
    noise_1.links.new(
        noise_1.nodes["Set Position"].outputs[0],
        noise_1.nodes["Group Output"].inputs[0]
    )
    # group_input.Geometry -> set_position.Geometry
    noise_1.links.new(
        noise_1.nodes["Group Input"].outputs[0],
        noise_1.nodes["Set Position"].inputs[0]
    )
    # group_input.Position -> vector_math.Vector
    noise_1.links.new(
        noise_1.nodes["Group Input"].outputs[1],
        noise_1.nodes["Vector Math"].inputs[1]
    )
    # group_input.Noise Amplitude -> vector_math_001.Vector
    noise_1.links.new(
        noise_1.nodes["Group Input"].outputs[2],
        noise_1.nodes["Vector Math.001"].inputs[1]
    )

    return noise_1

def symmetry_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize Symmetry node group"""
    symmetry_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="Symmetry")

    symmetry_1.color_tag = 'NONE'
    symmetry_1.description = ""
    symmetry_1.default_group_node_width = 140
    symmetry_1.show_modifier_manage_panel = True

    # symmetry_1 interface

    # Socket Geometry
    geometry_socket = symmetry_1.interface.new_socket(name="Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    # Socket Geometry
    geometry_socket_1 = symmetry_1.interface.new_socket(name="Geometry", in_out='INPUT', socket_type='NodeSocketGeometry')
    geometry_socket_1.attribute_domain = 'POINT'
    geometry_socket_1.description = "Geometry to transform"
    geometry_socket_1.default_input = 'VALUE'
    geometry_socket_1.structure_type = 'AUTO'

    # Socket X
    x_socket = symmetry_1.interface.new_socket(name="X", in_out='INPUT', socket_type='NodeSocketBool')
    x_socket.default_value = False
    x_socket.attribute_domain = 'POINT'
    x_socket.default_input = 'VALUE'
    x_socket.structure_type = 'AUTO'

    # Socket Y
    y_socket = symmetry_1.interface.new_socket(name="Y", in_out='INPUT', socket_type='NodeSocketBool')
    y_socket.default_value = False
    y_socket.attribute_domain = 'POINT'
    y_socket.default_input = 'VALUE'
    y_socket.structure_type = 'AUTO'

    # Socket Z
    z_socket = symmetry_1.interface.new_socket(name="Z", in_out='INPUT', socket_type='NodeSocketBool')
    z_socket.default_value = False
    z_socket.attribute_domain = 'POINT'
    z_socket.default_input = 'VALUE'
    z_socket.structure_type = 'AUTO'

    # Initialize symmetry_1 nodes

    # Node Transform Geometry
    transform_geometry = symmetry_1.nodes.new("GeometryNodeTransform")
    transform_geometry.name = "Transform Geometry"
    # Mode
    transform_geometry.inputs[1].default_value = 'Components'
    # Translation
    transform_geometry.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Rotation
    transform_geometry.inputs[3].default_value = (0.0, 0.0, 0.0)

    # Node Vector Math
    vector_math = symmetry_1.nodes.new("ShaderNodeVectorMath")
    vector_math.name = "Vector Math"
    vector_math.operation = 'MULTIPLY'
    # Vector
    vector_math.inputs[0].default_value = (1.0, 1.0, 1.0)

    # Node Group Output
    group_output = symmetry_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True

    # Node Group Input
    group_input = symmetry_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"

    # Node Switch.001
    switch_001 = symmetry_1.nodes.new("GeometryNodeSwitch")
    switch_001.name = "Switch.001"
    switch_001.input_type = 'VECTOR'
    # False
    switch_001.inputs[1].default_value = (1.0, 1.0, 1.0)
    # True
    switch_001.inputs[2].default_value = (-1.0, 1.0, 1.0)

    # Node Switch.002
    switch_002 = symmetry_1.nodes.new("GeometryNodeSwitch")
    switch_002.name = "Switch.002"
    switch_002.input_type = 'VECTOR'
    # False
    switch_002.inputs[1].default_value = (1.0, 1.0, 1.0)
    # True
    switch_002.inputs[2].default_value = (1.0, 1.0, -1.0)

    # Node Switch
    switch = symmetry_1.nodes.new("GeometryNodeSwitch")
    switch.name = "Switch"
    switch.input_type = 'GEOMETRY'

    # Node Switch.003
    switch_003 = symmetry_1.nodes.new("GeometryNodeSwitch")
    switch_003.name = "Switch.003"
    switch_003.input_type = 'GEOMETRY'

    # Node Transform Geometry.001
    transform_geometry_001 = symmetry_1.nodes.new("GeometryNodeTransform")
    transform_geometry_001.name = "Transform Geometry.001"
    # Mode
    transform_geometry_001.inputs[1].default_value = 'Components'
    # Translation
    transform_geometry_001.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Rotation
    transform_geometry_001.inputs[3].default_value = (0.0, 0.0, 0.0)

    # Node Vector Math.001
    vector_math_001 = symmetry_1.nodes.new("ShaderNodeVectorMath")
    vector_math_001.name = "Vector Math.001"
    vector_math_001.operation = 'MULTIPLY'
    # Vector
    vector_math_001.inputs[0].default_value = (1.0, 1.0, 1.0)

    # Node Join Geometry
    join_geometry = symmetry_1.nodes.new("GeometryNodeJoinGeometry")
    join_geometry.name = "Join Geometry"

    # Node Switch.004
    switch_004 = symmetry_1.nodes.new("GeometryNodeSwitch")
    switch_004.name = "Switch.004"
    switch_004.input_type = 'VECTOR'
    # False
    switch_004.inputs[1].default_value = (1.0, 1.0, 1.0)
    # True
    switch_004.inputs[2].default_value = (1.0, -1.0, 1.0)

    # Node Switch.005
    switch_005 = symmetry_1.nodes.new("GeometryNodeSwitch")
    switch_005.name = "Switch.005"
    switch_005.input_type = 'GEOMETRY'

    # Node Transform Geometry.002
    transform_geometry_002 = symmetry_1.nodes.new("GeometryNodeTransform")
    transform_geometry_002.name = "Transform Geometry.002"
    # Mode
    transform_geometry_002.inputs[1].default_value = 'Components'
    # Translation
    transform_geometry_002.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Rotation
    transform_geometry_002.inputs[3].default_value = (0.0, 0.0, 0.0)

    # Node Vector Math.002
    vector_math_002 = symmetry_1.nodes.new("ShaderNodeVectorMath")
    vector_math_002.name = "Vector Math.002"
    vector_math_002.operation = 'MULTIPLY'
    # Vector
    vector_math_002.inputs[0].default_value = (1.0, 1.0, 1.0)

    # Set locations
    symmetry_1.nodes["Transform Geometry"].location = (260.3255920410156, 98.45340728759766)
    symmetry_1.nodes["Vector Math"].location = (66.31233978271484, -144.67774963378906)
    symmetry_1.nodes["Group Output"].location = (1419.62646484375, 87.79827880859375)
    symmetry_1.nodes["Group Input"].location = (-754.9551391601562, 194.3428497314453)
    symmetry_1.nodes["Switch.001"].location = (-284.60430908203125, -267.1213073730469)
    symmetry_1.nodes["Switch.002"].location = (-229.6461944580078, -988.5376586914062)
    symmetry_1.nodes["Switch"].location = (482.49310302734375, 283.4128112792969)
    symmetry_1.nodes["Switch.003"].location = (707.2330932617188, -617.5999145507812)
    symmetry_1.nodes["Transform Geometry.001"].location = (374.4142150878906, -778.29443359375)
    symmetry_1.nodes["Vector Math.001"].location = (170.35939025878906, -1016.4041137695312)
    symmetry_1.nodes["Join Geometry"].location = (1204.11474609375, 85.05091857910156)
    symmetry_1.nodes["Switch.004"].location = (-257.3050231933594, -582.5661010742188)
    symmetry_1.nodes["Switch.005"].location = (679.5742797851562, -211.62835693359375)
    symmetry_1.nodes["Transform Geometry.002"].location = (346.75537109375, -372.3228759765625)
    symmetry_1.nodes["Vector Math.002"].location = (142.70054626464844, -610.4325561523438)

    # Set dimensions
    symmetry_1.nodes["Transform Geometry"].width  = 140.0
    symmetry_1.nodes["Transform Geometry"].height = 100.0

    symmetry_1.nodes["Vector Math"].width  = 140.0
    symmetry_1.nodes["Vector Math"].height = 100.0

    symmetry_1.nodes["Group Output"].width  = 140.0
    symmetry_1.nodes["Group Output"].height = 100.0

    symmetry_1.nodes["Group Input"].width  = 140.0
    symmetry_1.nodes["Group Input"].height = 100.0

    symmetry_1.nodes["Switch.001"].width  = 140.0
    symmetry_1.nodes["Switch.001"].height = 100.0

    symmetry_1.nodes["Switch.002"].width  = 140.0
    symmetry_1.nodes["Switch.002"].height = 100.0

    symmetry_1.nodes["Switch"].width  = 140.0
    symmetry_1.nodes["Switch"].height = 100.0

    symmetry_1.nodes["Switch.003"].width  = 140.0
    symmetry_1.nodes["Switch.003"].height = 100.0

    symmetry_1.nodes["Transform Geometry.001"].width  = 140.0
    symmetry_1.nodes["Transform Geometry.001"].height = 100.0

    symmetry_1.nodes["Vector Math.001"].width  = 140.0
    symmetry_1.nodes["Vector Math.001"].height = 100.0

    symmetry_1.nodes["Join Geometry"].width  = 140.0
    symmetry_1.nodes["Join Geometry"].height = 100.0

    symmetry_1.nodes["Switch.004"].width  = 140.0
    symmetry_1.nodes["Switch.004"].height = 100.0

    symmetry_1.nodes["Switch.005"].width  = 140.0
    symmetry_1.nodes["Switch.005"].height = 100.0

    symmetry_1.nodes["Transform Geometry.002"].width  = 140.0
    symmetry_1.nodes["Transform Geometry.002"].height = 100.0

    symmetry_1.nodes["Vector Math.002"].width  = 140.0
    symmetry_1.nodes["Vector Math.002"].height = 100.0


    # Initialize symmetry_1 links

    # vector_math.Vector -> transform_geometry.Scale
    symmetry_1.links.new(
        symmetry_1.nodes["Vector Math"].outputs[0],
        symmetry_1.nodes["Transform Geometry"].inputs[4]
    )
    # group_input.Geometry -> transform_geometry.Geometry
    symmetry_1.links.new(
        symmetry_1.nodes["Group Input"].outputs[0],
        symmetry_1.nodes["Transform Geometry"].inputs[0]
    )
    # join_geometry.Geometry -> group_output.Geometry
    symmetry_1.links.new(
        symmetry_1.nodes["Join Geometry"].outputs[0],
        symmetry_1.nodes["Group Output"].inputs[0]
    )
    # group_input.X -> switch_001.Switch
    symmetry_1.links.new(
        symmetry_1.nodes["Group Input"].outputs[1],
        symmetry_1.nodes["Switch.001"].inputs[0]
    )
    # switch_001.Output -> vector_math.Vector
    symmetry_1.links.new(
        symmetry_1.nodes["Switch.001"].outputs[0],
        symmetry_1.nodes["Vector Math"].inputs[1]
    )
    # group_input.Z -> switch_002.Switch
    symmetry_1.links.new(
        symmetry_1.nodes["Group Input"].outputs[3],
        symmetry_1.nodes["Switch.002"].inputs[0]
    )
    # transform_geometry.Geometry -> switch.True
    symmetry_1.links.new(
        symmetry_1.nodes["Transform Geometry"].outputs[0],
        symmetry_1.nodes["Switch"].inputs[2]
    )
    # group_input.X -> switch.Switch
    symmetry_1.links.new(
        symmetry_1.nodes["Group Input"].outputs[1],
        symmetry_1.nodes["Switch"].inputs[0]
    )
    # vector_math_001.Vector -> transform_geometry_001.Scale
    symmetry_1.links.new(
        symmetry_1.nodes["Vector Math.001"].outputs[0],
        symmetry_1.nodes["Transform Geometry.001"].inputs[4]
    )
    # switch_002.Output -> vector_math_001.Vector
    symmetry_1.links.new(
        symmetry_1.nodes["Switch.002"].outputs[0],
        symmetry_1.nodes["Vector Math.001"].inputs[1]
    )
    # transform_geometry_001.Geometry -> switch_003.True
    symmetry_1.links.new(
        symmetry_1.nodes["Transform Geometry.001"].outputs[0],
        symmetry_1.nodes["Switch.003"].inputs[2]
    )
    # group_input.Z -> switch_003.Switch
    symmetry_1.links.new(
        symmetry_1.nodes["Group Input"].outputs[3],
        symmetry_1.nodes["Switch.003"].inputs[0]
    )
    # group_input.Geometry -> transform_geometry_001.Geometry
    symmetry_1.links.new(
        symmetry_1.nodes["Group Input"].outputs[0],
        symmetry_1.nodes["Transform Geometry.001"].inputs[0]
    )
    # vector_math_002.Vector -> transform_geometry_002.Scale
    symmetry_1.links.new(
        symmetry_1.nodes["Vector Math.002"].outputs[0],
        symmetry_1.nodes["Transform Geometry.002"].inputs[4]
    )
    # switch_004.Output -> vector_math_002.Vector
    symmetry_1.links.new(
        symmetry_1.nodes["Switch.004"].outputs[0],
        symmetry_1.nodes["Vector Math.002"].inputs[1]
    )
    # transform_geometry_002.Geometry -> switch_005.True
    symmetry_1.links.new(
        symmetry_1.nodes["Transform Geometry.002"].outputs[0],
        symmetry_1.nodes["Switch.005"].inputs[2]
    )
    # group_input.Y -> switch_004.Switch
    symmetry_1.links.new(
        symmetry_1.nodes["Group Input"].outputs[2],
        symmetry_1.nodes["Switch.004"].inputs[0]
    )
    # group_input.Geometry -> transform_geometry_002.Geometry
    symmetry_1.links.new(
        symmetry_1.nodes["Group Input"].outputs[0],
        symmetry_1.nodes["Transform Geometry.002"].inputs[0]
    )
    # switch_005.Output -> join_geometry.Geometry
    symmetry_1.links.new(
        symmetry_1.nodes["Switch.005"].outputs[0],
        symmetry_1.nodes["Join Geometry"].inputs[0]
    )
    # group_input.Y -> switch_005.Switch
    symmetry_1.links.new(
        symmetry_1.nodes["Group Input"].outputs[2],
        symmetry_1.nodes["Switch.005"].inputs[0]
    )
    # switch.Output -> join_geometry.Geometry
    symmetry_1.links.new(
        symmetry_1.nodes["Switch"].outputs[0],
        symmetry_1.nodes["Join Geometry"].inputs[0]
    )
    # switch_003.Output -> join_geometry.Geometry
    symmetry_1.links.new(
        symmetry_1.nodes["Switch.003"].outputs[0],
        symmetry_1.nodes["Join Geometry"].inputs[0]
    )

    return symmetry_1

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

    arc_curve = arc_curve_1_node_group(node_tree_names)
    node_tree_names[arc_curve_1_node_group] = arc_curve.name

    create_branches = create_branches_1_node_group(node_tree_names)
    node_tree_names[create_branches_1_node_group] = create_branches.name

    getnormalize = getnormalize_1_node_group(node_tree_names)
    node_tree_names[getnormalize_1_node_group] = getnormalize.name

    delete_points_of_curve = delete_points_of_curve_1_node_group(node_tree_names)
    node_tree_names[delete_points_of_curve_1_node_group] = delete_points_of_curve.name

    create_leafs = create_leafs_1_node_group(node_tree_names)
    node_tree_names[create_leafs_1_node_group] = create_leafs.name

    thickness = thickness_1_node_group(node_tree_names)
    node_tree_names[thickness_1_node_group] = thickness.name

    choos_name = choos_name_1_node_group(node_tree_names)
    node_tree_names[choos_name_1_node_group] = choos_name.name

    seeds_of_plants = seeds_of_plants_1_node_group(node_tree_names)
    node_tree_names[seeds_of_plants_1_node_group] = seeds_of_plants.name

    noise = noise_1_node_group(node_tree_names)
    node_tree_names[noise_1_node_group] = noise.name


    symmetry = symmetry_1_node_group(node_tree_names)
    node_tree_names[symmetry_1_node_group] = symmetry.name

    obj = bpy.context.active_object

    if obj is None:
        print("not object found")
    # else:
    #     mod = obj.modifiers.new("Curve to Tube", type='NODES')
    #     mod.node_group = create_trunk


"""
juju Julien BROUZES
https://github.com/Juju-brz
"""
