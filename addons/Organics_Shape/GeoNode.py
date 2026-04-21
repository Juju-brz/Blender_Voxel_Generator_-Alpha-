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

    # Panel Value of Branche
    value_of_branche_panel = create_branches_1.interface.new_panel("Value of Branche")
    # Socket Min
    min_socket = create_branches_1.interface.new_socket(name="Min", in_out='INPUT', socket_type='NodeSocketFloat', parent = value_of_branche_panel)
    min_socket.default_value = 0.0
    min_socket.min_value = -3.4028234663852886e+38
    min_socket.max_value = 3.4028234663852886e+38
    min_socket.subtype = 'NONE'
    min_socket.attribute_domain = 'POINT'
    min_socket.default_input = 'VALUE'
    min_socket.structure_type = 'AUTO'

    # Socket Max
    max_socket = create_branches_1.interface.new_socket(name="Max", in_out='INPUT', socket_type='NodeSocketFloat', parent = value_of_branche_panel)
    max_socket.default_value = 12.399999618530273
    max_socket.min_value = -3.4028234663852886e+38
    max_socket.max_value = 3.4028234663852886e+38
    max_socket.subtype = 'NONE'
    max_socket.attribute_domain = 'POINT'
    max_socket.default_input = 'VALUE'
    max_socket.structure_type = 'AUTO'

    # Socket Seed
    seed_socket = create_branches_1.interface.new_socket(name="Seed", in_out='INPUT', socket_type='NodeSocketInt', parent = value_of_branche_panel)
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
    curve_line_001.hide = True
    curve_line_001.mode = 'POINTS'
    # Start
    curve_line_001.inputs[0].default_value = (0.0, 0.0, 0.0)
    # End
    curve_line_001.inputs[1].default_value = (0.0, 0.0, 1.0)

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

    # Node Set Position.001
    set_position_001 = create_branches_1.nodes.new("GeometryNodeSetPosition")
    set_position_001.name = "Set Position.001"
    # Position
    set_position_001.inputs[2].default_value = (0.0, 0.0, 0.0)

    # Node Noise Texture.001
    noise_texture_001 = create_branches_1.nodes.new("ShaderNodeTexNoise")
    noise_texture_001.name = "Noise Texture.001"
    noise_texture_001.noise_dimensions = '3D'
    noise_texture_001.noise_type = 'FBM'
    noise_texture_001.normalize = True
    # Vector
    noise_texture_001.inputs[0].default_value = (0.0, 0.0, 0.0)
    # Scale
    noise_texture_001.inputs[2].default_value = 0.5
    # Detail
    noise_texture_001.inputs[3].default_value = 2.0
    # Roughness
    noise_texture_001.inputs[4].default_value = 0.5
    # Lacunarity
    noise_texture_001.inputs[5].default_value = 2.0
    # Distortion
    noise_texture_001.inputs[8].default_value = 0.0

    # Node Vector Math.002
    vector_math_002 = create_branches_1.nodes.new("ShaderNodeVectorMath")
    vector_math_002.name = "Vector Math.002"
    vector_math_002.operation = 'SUBTRACT'
    # Vector_001
    vector_math_002.inputs[1].default_value = (0.5, 0.5, 0.5)

    # Node Vector Math.003
    vector_math_003 = create_branches_1.nodes.new("ShaderNodeVectorMath")
    vector_math_003.name = "Vector Math.003"
    vector_math_003.operation = 'MULTIPLY'
    # Vector_001
    vector_math_003.inputs[1].default_value = (1.9999998807907104, 1.9999998807907104, 1.9999998807907104)

    # Node Spline Parameter
    spline_parameter = create_branches_1.nodes.new("GeometryNodeSplineParameter")
    spline_parameter.name = "Spline Parameter"

    # Node Vector Math
    vector_math = create_branches_1.nodes.new("ShaderNodeVectorMath")
    vector_math.name = "Vector Math"
    vector_math.operation = 'MULTIPLY'
    # Vector_001
    vector_math.inputs[1].default_value = (1.9999998807907104, 1.9999998807907104, 1.9999998807907104)

    # Set locations
    create_branches_1.nodes["Group Input"].location = (-1447.57763671875, 570.185302734375)
    create_branches_1.nodes["Group Output"].location = (1144.09375, 530.8128051757812)
    create_branches_1.nodes["Instance on Points.001"].location = (-583.0662841796875, 584.485107421875)
    create_branches_1.nodes["Curve Line.001"].location = (-822.6689453125, 311.3088073730469)
    create_branches_1.nodes["Curve Tangent"].location = (-943.1922607421875, 149.26324462890625)
    create_branches_1.nodes["Curve Tangent.001"].location = (-747.364013671875, -68.97579956054688)
    create_branches_1.nodes["Endpoint Selection"].location = (-821.5252685546875, 464.91986083984375)
    create_branches_1.nodes["Random Value.001"].location = (-1032.1761474609375, 373.18951416015625)
    create_branches_1.nodes["Realize Instances.001"].location = (-367.1282653808594, 432.48260498046875)
    create_branches_1.nodes["Resample Curve.001"].location = (-187.12774658203125, 491.5682678222656)
    create_branches_1.nodes["Set Position.001"].location = (842.80029296875, 546.4512939453125)
    create_branches_1.nodes["Noise Texture.001"].location = (-9.942092895507812, 180.77145385742188)
    create_branches_1.nodes["Vector Math.002"].location = (456.5332336425781, 168.937744140625)
    create_branches_1.nodes["Vector Math.003"].location = (705.350830078125, 246.40878295898438)
    create_branches_1.nodes["Spline Parameter"].location = (616.0289306640625, 365.9591369628906)
    create_branches_1.nodes["Vector Math"].location = (-763.2645263671875, 229.0145263671875)

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

    create_branches_1.nodes["Set Position.001"].width  = 140.0
    create_branches_1.nodes["Set Position.001"].height = 100.0

    create_branches_1.nodes["Noise Texture.001"].width  = 145.0
    create_branches_1.nodes["Noise Texture.001"].height = 100.0

    create_branches_1.nodes["Vector Math.002"].width  = 140.0
    create_branches_1.nodes["Vector Math.002"].height = 100.0

    create_branches_1.nodes["Vector Math.003"].width  = 140.0
    create_branches_1.nodes["Vector Math.003"].height = 100.0

    create_branches_1.nodes["Spline Parameter"].width  = 140.0
    create_branches_1.nodes["Spline Parameter"].height = 100.0

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
    # vector_math_003.Vector -> set_position_001.Offset
    create_branches_1.links.new(
        create_branches_1.nodes["Vector Math.003"].outputs[0],
        create_branches_1.nodes["Set Position.001"].inputs[3]
    )
    # noise_texture_001.Color -> vector_math_002.Vector
    create_branches_1.links.new(
        create_branches_1.nodes["Noise Texture.001"].outputs[1],
        create_branches_1.nodes["Vector Math.002"].inputs[0]
    )
    # vector_math_002.Vector -> vector_math_003.Vector
    create_branches_1.links.new(
        create_branches_1.nodes["Vector Math.002"].outputs[0],
        create_branches_1.nodes["Vector Math.003"].inputs[0]
    )
    # spline_parameter.Factor -> set_position_001.Selection
    create_branches_1.links.new(
        create_branches_1.nodes["Spline Parameter"].outputs[0],
        create_branches_1.nodes["Set Position.001"].inputs[1]
    )
    # curve_tangent.Tangent -> vector_math.Vector
    create_branches_1.links.new(
        create_branches_1.nodes["Curve Tangent"].outputs[0],
        create_branches_1.nodes["Vector Math"].inputs[0]
    )
    # resample_curve_001.Curve -> set_position_001.Geometry
    create_branches_1.links.new(
        create_branches_1.nodes["Resample Curve.001"].outputs[0],
        create_branches_1.nodes["Set Position.001"].inputs[0]
    )
    # set_position_001.Geometry -> group_output.Geometry
    create_branches_1.links.new(
        create_branches_1.nodes["Set Position.001"].outputs[0],
        create_branches_1.nodes["Group Output"].inputs[0]
    )
    # group_input.Geometry -> instance_on_points_001.Points
    create_branches_1.links.new(
        create_branches_1.nodes["Group Input"].outputs[0],
        create_branches_1.nodes["Instance on Points.001"].inputs[0]
    )
    # group_input.Min -> random_value_001.Min
    create_branches_1.links.new(
        create_branches_1.nodes["Group Input"].outputs[1],
        create_branches_1.nodes["Random Value.001"].inputs[2]
    )
    # group_input.Max -> random_value_001.Max
    create_branches_1.links.new(
        create_branches_1.nodes["Group Input"].outputs[2],
        create_branches_1.nodes["Random Value.001"].inputs[3]
    )
    # group_input.Seed -> random_value_001.Seed
    create_branches_1.links.new(
        create_branches_1.nodes["Group Input"].outputs[3],
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

    # Node Reroute
    reroute = create_leafs_1.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.socket_idname = "NodeSocketGeometry"
    # Set locations
    create_leafs_1.nodes["Instance on Points.001"].location = (-1158.392822265625, 165.62789916992188)
    create_leafs_1.nodes["Ico Sphere"].location = (-1399.544677734375, -38.785919189453125)
    create_leafs_1.nodes["Endpoint Selection"].location = (-1650.6795654296875, -89.60820007324219)
    create_leafs_1.nodes["Random Value.001"].location = (-1355.1103515625, -263.7852783203125)
    create_leafs_1.nodes["Realize Instances.001"].location = (-985.4093017578125, 315.685302734375)
    create_leafs_1.nodes["Instance on Points.002"].location = (-509.5552062988281, 324.90777587890625)
    create_leafs_1.nodes["Curve Line.001"].location = (-1006.1842651367188, 153.703369140625)
    create_leafs_1.nodes["Normal"].location = (-1114.903076171875, -352.6933898925781)
    create_leafs_1.nodes["Align Euler to Vector"].location = (-873.9468383789062, -214.74588012695312)
    create_leafs_1.nodes["Instance on Points.003"].location = (132.50430297851562, 299.0303649902344)
    create_leafs_1.nodes["Random Value.002"].location = (-89.71683502197266, -35.733795166015625)
    create_leafs_1.nodes["Realize Instances.002"].location = (-183.67971801757812, 394.0683898925781)
    create_leafs_1.nodes["Vector Math.002"].location = (-416.6391906738281, -149.83511352539062)
    create_leafs_1.nodes["Curve Tangent"].location = (-588.8364868164062, -250.88455200195312)
    create_leafs_1.nodes["Random Value.003"].location = (-740.1050415039062, -389.9510803222656)
    create_leafs_1.nodes["Group Output"].location = (352.2190856933594, 750.7615356445312)
    create_leafs_1.nodes["create leafs"].location = (-2005.5418701171875, 129.36328125)
    create_leafs_1.nodes["Reroute"].location = (-343.8786926269531, 440.53350830078125)

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

    create_leafs_1.nodes["Reroute"].width  = 10.0
    create_leafs_1.nodes["Reroute"].height = 100.0


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
    # reroute.Output -> group_output.Geometry
    create_leafs_1.links.new(
        create_leafs_1.nodes["Reroute"].outputs[0],
        create_leafs_1.nodes["Group Output"].inputs[0]
    )
    # realize_instances_001.Geometry -> reroute.Input
    create_leafs_1.links.new(
        create_leafs_1.nodes["Realize Instances.001"].outputs[0],
        create_leafs_1.nodes["Reroute"].inputs[0]
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

    # Node Curve to Tube
    curve_to_tube = thickness_1.nodes.new("GeometryNodeGroup")
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
    # Socket_5
    curve_to_tube.inputs[1].default_value = 0.10000000149011612
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

    # Set locations
    thickness_1.nodes["Group Input"].location = (-459.7458190917969, -29.634382247924805)
    thickness_1.nodes["Group Output"].location = (460.1916198730469, 2.5629732608795166)
    thickness_1.nodes["Set Curve Radius"].location = (86.60769653320312, -14.69403076171875)
    thickness_1.nodes["Spline Parameter.001"].location = (-479.5445861816406, -328.39678955078125)
    thickness_1.nodes["Color Ramp"].location = (-297.80108642578125, -274.2325439453125)
    thickness_1.nodes["Map Range"].location = (-85.684814453125, -126.2535400390625)
    thickness_1.nodes["Curve to Tube"].location = (254.10528564453125, 33.93254089355469)

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

    thickness_1.nodes["Curve to Tube"].width  = 200.0
    thickness_1.nodes["Curve to Tube"].height = 100.0


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
    # curve_to_tube.Mesh -> group_output.Geometry
    thickness_1.links.new(
        thickness_1.nodes["Curve to Tube"].outputs[0],
        thickness_1.nodes["Group Output"].inputs[0]
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
    # set_curve_radius.Curve -> curve_to_tube.Curve
    thickness_1.links.new(
        thickness_1.nodes["Set Curve Radius"].outputs[0],
        thickness_1.nodes["Curve to Tube"].inputs[0]
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
