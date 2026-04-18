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

def branches_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize Branches node group"""
    branches_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="Branches")

    branches_1.color_tag = 'NONE'
    branches_1.description = ""
    branches_1.default_group_node_width = 140
    branches_1.show_modifier_manage_panel = True

    # branches_1 interface

    # Socket Geometry
    geometry_socket = branches_1.interface.new_socket(name="Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    # Socket Points
    points_socket = branches_1.interface.new_socket(name="Points", in_out='INPUT', socket_type='NodeSocketGeometry')
    points_socket.attribute_domain = 'POINT'
    points_socket.description = "Points to instance on"
    points_socket.default_input = 'VALUE'
    points_socket.structure_type = 'AUTO'

    # Initialize branches_1 nodes

    # Node Instance on Points.001
    instance_on_points_001 = branches_1.nodes.new("GeometryNodeInstanceOnPoints")
    instance_on_points_001.name = "Instance on Points.001"
    # Pick Instance
    instance_on_points_001.inputs[3].default_value = False
    # Instance Index
    instance_on_points_001.inputs[4].default_value = 0

    # Node Curve Line.001
    curve_line_001 = branches_1.nodes.new("GeometryNodeCurvePrimitiveLine")
    curve_line_001.name = "Curve Line.001"
    curve_line_001.hide = True
    curve_line_001.mode = 'POINTS'
    # Start
    curve_line_001.inputs[0].default_value = (0.0, 0.0, 0.0)
    # End
    curve_line_001.inputs[1].default_value = (0.0, 0.0, 1.0)

    # Node Curve Tangent
    curve_tangent = branches_1.nodes.new("GeometryNodeInputTangent")
    curve_tangent.name = "Curve Tangent"

    # Node Curve Tangent.001
    curve_tangent_001 = branches_1.nodes.new("GeometryNodeInputTangent")
    curve_tangent_001.name = "Curve Tangent.001"

    # Node Endpoint Selection
    endpoint_selection = branches_1.nodes.new("GeometryNodeCurveEndpointSelection")
    endpoint_selection.name = "Endpoint Selection"
    # Start Size
    endpoint_selection.inputs[0].default_value = 1

    # Node Random Value.001
    random_value_001 = branches_1.nodes.new("FunctionNodeRandomValue")
    random_value_001.name = "Random Value.001"
    random_value_001.data_type = 'FLOAT'
    # Min_001
    random_value_001.inputs[2].default_value = 0.0
    # Max_001
    random_value_001.inputs[3].default_value = 5.0
    # ID
    random_value_001.inputs[7].default_value = 0
    # Seed
    random_value_001.inputs[8].default_value = 0

    # Node Realize Instances.001
    realize_instances_001 = branches_1.nodes.new("GeometryNodeRealizeInstances")
    realize_instances_001.name = "Realize Instances.001"
    realize_instances_001.realize_to_point_domain = False
    # Selection
    realize_instances_001.inputs[1].default_value = True
    # Realize All
    realize_instances_001.inputs[2].default_value = True
    # Depth
    realize_instances_001.inputs[3].default_value = 0

    # Node Resample Curve.001
    resample_curve_001 = branches_1.nodes.new("GeometryNodeResampleCurve")
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
    set_position_001 = branches_1.nodes.new("GeometryNodeSetPosition")
    set_position_001.name = "Set Position.001"
    # Position
    set_position_001.inputs[2].default_value = (0.0, 0.0, 0.0)

    # Node Noise Texture.001
    noise_texture_001 = branches_1.nodes.new("ShaderNodeTexNoise")
    noise_texture_001.name = "Noise Texture.001"
    noise_texture_001.noise_dimensions = '3D'
    noise_texture_001.noise_type = 'FBM'
    noise_texture_001.normalize = True
    # Vector
    noise_texture_001.inputs[0].default_value = (0.0, 0.0, 0.0)
    # Scale
    noise_texture_001.inputs[2].default_value = 0.5000004768371582
    # Detail
    noise_texture_001.inputs[3].default_value = 2.0
    # Roughness
    noise_texture_001.inputs[4].default_value = 0.5
    # Lacunarity
    noise_texture_001.inputs[5].default_value = 2.0
    # Distortion
    noise_texture_001.inputs[8].default_value = 0.0

    # Node Vector Math.002
    vector_math_002 = branches_1.nodes.new("ShaderNodeVectorMath")
    vector_math_002.name = "Vector Math.002"
    vector_math_002.operation = 'SUBTRACT'
    # Vector_001
    vector_math_002.inputs[1].default_value = (0.4999999701976776, 0.4999999701976776, 0.4999999701976776)

    # Node Vector Math.003
    vector_math_003 = branches_1.nodes.new("ShaderNodeVectorMath")
    vector_math_003.name = "Vector Math.003"
    vector_math_003.operation = 'MULTIPLY'
    # Vector_001
    vector_math_003.inputs[1].default_value = (1.8999998569488525, 1.8999998569488525, 1.8999998569488525)

    # Node Spline Parameter.001
    spline_parameter_001 = branches_1.nodes.new("GeometryNodeSplineParameter")
    spline_parameter_001.name = "Spline Parameter.001"

    # Node Group Output
    group_output = branches_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True

    # Node Group Input
    group_input = branches_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"

    # Set locations
    branches_1.nodes["Instance on Points.001"].location = (-40.9013671875, 133.30075073242188)
    branches_1.nodes["Curve Line.001"].location = (-452.1583251953125, -32.600494384765625)
    branches_1.nodes["Curve Tangent"].location = (-279.958251953125, -80.72085571289062)
    branches_1.nodes["Curve Tangent.001"].location = (-248.5767822265625, -204.06582641601562)
    branches_1.nodes["Endpoint Selection"].location = (-470.7269287109375, 122.4915771484375)
    branches_1.nodes["Random Value.001"].location = (-641.71044921875, 30.85589599609375)
    branches_1.nodes["Realize Instances.001"].location = (175.107666015625, 193.04429626464844)
    branches_1.nodes["Resample Curve.001"].location = (357.4560546875, 195.16763305664062)
    branches_1.nodes["Set Position.001"].location = (641.71044921875, 239.95608520507812)
    branches_1.nodes["Noise Texture.001"].location = (186.218017578125, -239.95608520507812)
    branches_1.nodes["Vector Math.002"].location = (388.995361328125, -158.32302856445312)
    branches_1.nodes["Vector Math.003"].location = (592.716552734375, -72.63211059570312)
    branches_1.nodes["Spline Parameter.001"].location = (357.516357421875, -10.585479736328125)
    branches_1.nodes["Group Output"].location = (831.71044921875, 0.0)
    branches_1.nodes["Group Input"].location = (-841.71044921875, 0.0)

    # Set dimensions
    branches_1.nodes["Instance on Points.001"].width  = 140.0
    branches_1.nodes["Instance on Points.001"].height = 100.0

    branches_1.nodes["Curve Line.001"].width  = 140.0
    branches_1.nodes["Curve Line.001"].height = 100.0

    branches_1.nodes["Curve Tangent"].width  = 140.0
    branches_1.nodes["Curve Tangent"].height = 100.0

    branches_1.nodes["Curve Tangent.001"].width  = 140.0
    branches_1.nodes["Curve Tangent.001"].height = 100.0

    branches_1.nodes["Endpoint Selection"].width  = 140.0
    branches_1.nodes["Endpoint Selection"].height = 100.0

    branches_1.nodes["Random Value.001"].width  = 140.0
    branches_1.nodes["Random Value.001"].height = 100.0

    branches_1.nodes["Realize Instances.001"].width  = 140.0
    branches_1.nodes["Realize Instances.001"].height = 100.0

    branches_1.nodes["Resample Curve.001"].width  = 140.0
    branches_1.nodes["Resample Curve.001"].height = 100.0

    branches_1.nodes["Set Position.001"].width  = 140.0
    branches_1.nodes["Set Position.001"].height = 100.0

    branches_1.nodes["Noise Texture.001"].width  = 145.0
    branches_1.nodes["Noise Texture.001"].height = 100.0

    branches_1.nodes["Vector Math.002"].width  = 140.0
    branches_1.nodes["Vector Math.002"].height = 100.0

    branches_1.nodes["Vector Math.003"].width  = 140.0
    branches_1.nodes["Vector Math.003"].height = 100.0

    branches_1.nodes["Spline Parameter.001"].width  = 140.0
    branches_1.nodes["Spline Parameter.001"].height = 100.0

    branches_1.nodes["Group Output"].width  = 140.0
    branches_1.nodes["Group Output"].height = 100.0

    branches_1.nodes["Group Input"].width  = 140.0
    branches_1.nodes["Group Input"].height = 100.0


    # Initialize branches_1 links

    # curve_line_001.Curve -> instance_on_points_001.Instance
    branches_1.links.new(
        branches_1.nodes["Curve Line.001"].outputs[0],
        branches_1.nodes["Instance on Points.001"].inputs[2]
    )
    # curve_tangent.Tangent -> instance_on_points_001.Rotation
    branches_1.links.new(
        branches_1.nodes["Curve Tangent"].outputs[0],
        branches_1.nodes["Instance on Points.001"].inputs[5]
    )
    # curve_tangent_001.Tangent -> instance_on_points_001.Scale
    branches_1.links.new(
        branches_1.nodes["Curve Tangent.001"].outputs[0],
        branches_1.nodes["Instance on Points.001"].inputs[6]
    )
    # endpoint_selection.Selection -> instance_on_points_001.Selection
    branches_1.links.new(
        branches_1.nodes["Endpoint Selection"].outputs[0],
        branches_1.nodes["Instance on Points.001"].inputs[1]
    )
    # random_value_001.Value -> endpoint_selection.End Size
    branches_1.links.new(
        branches_1.nodes["Random Value.001"].outputs[1],
        branches_1.nodes["Endpoint Selection"].inputs[1]
    )
    # instance_on_points_001.Instances -> realize_instances_001.Geometry
    branches_1.links.new(
        branches_1.nodes["Instance on Points.001"].outputs[0],
        branches_1.nodes["Realize Instances.001"].inputs[0]
    )
    # realize_instances_001.Geometry -> resample_curve_001.Curve
    branches_1.links.new(
        branches_1.nodes["Realize Instances.001"].outputs[0],
        branches_1.nodes["Resample Curve.001"].inputs[0]
    )
    # vector_math_003.Vector -> set_position_001.Offset
    branches_1.links.new(
        branches_1.nodes["Vector Math.003"].outputs[0],
        branches_1.nodes["Set Position.001"].inputs[3]
    )
    # noise_texture_001.Color -> vector_math_002.Vector
    branches_1.links.new(
        branches_1.nodes["Noise Texture.001"].outputs[1],
        branches_1.nodes["Vector Math.002"].inputs[0]
    )
    # vector_math_002.Vector -> vector_math_003.Vector
    branches_1.links.new(
        branches_1.nodes["Vector Math.002"].outputs[0],
        branches_1.nodes["Vector Math.003"].inputs[0]
    )
    # resample_curve_001.Curve -> set_position_001.Geometry
    branches_1.links.new(
        branches_1.nodes["Resample Curve.001"].outputs[0],
        branches_1.nodes["Set Position.001"].inputs[0]
    )
    # spline_parameter_001.Length -> set_position_001.Selection
    branches_1.links.new(
        branches_1.nodes["Spline Parameter.001"].outputs[1],
        branches_1.nodes["Set Position.001"].inputs[1]
    )
    # set_position_001.Geometry -> group_output.Geometry
    branches_1.links.new(
        branches_1.nodes["Set Position.001"].outputs[0],
        branches_1.nodes["Group Output"].inputs[0]
    )
    # group_input.Points -> instance_on_points_001.Points
    branches_1.links.new(
        branches_1.nodes["Group Input"].outputs[0],
        branches_1.nodes["Instance on Points.001"].inputs[0]
    )

    return branches_1

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

    # Socket Threshold
    threshold_socket = delete_points_of_curve_1.interface.new_socket(name="Threshold", in_out='INPUT', socket_type='NodeSocketFloat')
    threshold_socket.default_value = 0.2999999523162842
    threshold_socket.min_value = -10000.0
    threshold_socket.max_value = 10000.0
    threshold_socket.subtype = 'NONE'
    threshold_socket.attribute_domain = 'POINT'
    threshold_socket.default_input = 'VALUE'
    threshold_socket.structure_type = 'AUTO'

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

    # Set locations
    delete_points_of_curve_1.nodes["Spline Length"].location = (-301.7341613769531, -60.227783203125)
    delete_points_of_curve_1.nodes["Spline Parameter"].location = (-275.8704528808594, 86.1356201171875)
    delete_points_of_curve_1.nodes["Math"].location = (-2.6723670959472656, 148.23487854003906)
    delete_points_of_curve_1.nodes["Group Output"].location = (775.4073486328125, 29.20565414428711)
    delete_points_of_curve_1.nodes["Group Input"].location = (-276.4412841796875, -228.9534454345703)
    delete_points_of_curve_1.nodes["Math.001"].location = (271.9712829589844, 84.98362731933594)
    delete_points_of_curve_1.nodes["Delete Geometry"].location = (490.6053466796875, 35.42893981933594)

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
    # group_input.Threshold -> math_001.Value
    delete_points_of_curve_1.links.new(
        delete_points_of_curve_1.nodes["Group Input"].outputs[1],
        delete_points_of_curve_1.nodes["Math.001"].inputs[1]
    )
    # delete_geometry.Geometry -> group_output.Geometry
    delete_points_of_curve_1.links.new(
        delete_points_of_curve_1.nodes["Delete Geometry"].outputs[0],
        delete_points_of_curve_1.nodes["Group Output"].inputs[0]
    )
    # math_001.Value -> delete_geometry.Selection
    delete_points_of_curve_1.links.new(
        delete_points_of_curve_1.nodes["Math.001"].outputs[0],
        delete_points_of_curve_1.nodes["Delete Geometry"].inputs[1]
    )

    return delete_points_of_curve_1

def leafs_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize leafs node group"""
    leafs_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="leafs")

    leafs_1.color_tag = 'NONE'
    leafs_1.description = ""
    leafs_1.default_group_node_width = 140
    leafs_1.show_modifier_manage_panel = True

    # leafs_1 interface

    # Socket Geometry
    geometry_socket = leafs_1.interface.new_socket(name="Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    # Socket Instances
    instances_socket = leafs_1.interface.new_socket(name="Instances", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    instances_socket.attribute_domain = 'POINT'
    instances_socket.default_input = 'VALUE'
    instances_socket.structure_type = 'AUTO'

    # Socket Instance
    instance_socket = leafs_1.interface.new_socket(name="Instance", in_out='INPUT', socket_type='NodeSocketGeometry')
    instance_socket.attribute_domain = 'POINT'
    instance_socket.description = "Geometry that is instanced on the points"
    instance_socket.default_input = 'VALUE'
    instance_socket.structure_type = 'AUTO'

    # Panel Where begin leafs
    where_begin_leafs_panel = leafs_1.interface.new_panel("Where begin leafs")
    # Socket Points
    points_socket = leafs_1.interface.new_socket(name="Points", in_out='INPUT', socket_type='NodeSocketGeometry', parent = where_begin_leafs_panel)
    points_socket.attribute_domain = 'POINT'
    points_socket.description = "Points to instance on"
    points_socket.default_input = 'VALUE'
    points_socket.structure_type = 'AUTO'


    # Panel Endpoint Selection
    endpoint_selection_panel = leafs_1.interface.new_panel("Endpoint Selection")
    # Socket Start Size
    start_size_socket = leafs_1.interface.new_socket(name="Start Size", in_out='INPUT', socket_type='NodeSocketInt', parent = endpoint_selection_panel)
    start_size_socket.default_value = 0
    start_size_socket.min_value = 0
    start_size_socket.max_value = 2147483647
    start_size_socket.subtype = 'NONE'
    start_size_socket.attribute_domain = 'POINT'
    start_size_socket.description = "The amount of points to select from the start of each spline"
    start_size_socket.default_input = 'VALUE'
    start_size_socket.structure_type = 'AUTO'

    # Socket End Size
    end_size_socket = leafs_1.interface.new_socket(name="End Size", in_out='INPUT', socket_type='NodeSocketInt', parent = endpoint_selection_panel)
    end_size_socket.default_value = 1
    end_size_socket.min_value = 0
    end_size_socket.max_value = 2147483647
    end_size_socket.subtype = 'NONE'
    end_size_socket.attribute_domain = 'POINT'
    end_size_socket.description = "The amount of points to select from the end of each spline"
    end_size_socket.default_input = 'VALUE'
    end_size_socket.structure_type = 'AUTO'


    # Initialize leafs_1 nodes

    # Node Instance on Points.001
    instance_on_points_001 = leafs_1.nodes.new("GeometryNodeInstanceOnPoints")
    instance_on_points_001.name = "Instance on Points.001"
    # Pick Instance
    instance_on_points_001.inputs[3].default_value = False
    # Instance Index
    instance_on_points_001.inputs[4].default_value = 0
    # Rotation
    instance_on_points_001.inputs[5].default_value = (0.0, 0.0, 0.0)

    # Node Ico Sphere
    ico_sphere = leafs_1.nodes.new("GeometryNodeMeshIcoSphere")
    ico_sphere.name = "Ico Sphere"
    # Radius
    ico_sphere.inputs[0].default_value = 0.019999999552965164
    # Subdivisions
    ico_sphere.inputs[1].default_value = 1

    # Node Endpoint Selection
    endpoint_selection = leafs_1.nodes.new("GeometryNodeCurveEndpointSelection")
    endpoint_selection.name = "Endpoint Selection"

    # Node Random Value.001
    random_value_001 = leafs_1.nodes.new("FunctionNodeRandomValue")
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
    realize_instances_001 = leafs_1.nodes.new("GeometryNodeRealizeInstances")
    realize_instances_001.name = "Realize Instances.001"
    realize_instances_001.realize_to_point_domain = False
    # Selection
    realize_instances_001.inputs[1].default_value = True
    # Realize All
    realize_instances_001.inputs[2].default_value = True
    # Depth
    realize_instances_001.inputs[3].default_value = 0

    # Node Instance on Points.002
    instance_on_points_002 = leafs_1.nodes.new("GeometryNodeInstanceOnPoints")
    instance_on_points_002.name = "Instance on Points.002"
    # Selection
    instance_on_points_002.inputs[1].default_value = True
    # Pick Instance
    instance_on_points_002.inputs[3].default_value = False
    # Instance Index
    instance_on_points_002.inputs[4].default_value = 0

    # Node Curve Line.001
    curve_line_001 = leafs_1.nodes.new("GeometryNodeCurvePrimitiveLine")
    curve_line_001.name = "Curve Line.001"
    curve_line_001.mode = 'POINTS'
    # Start
    curve_line_001.inputs[0].default_value = (0.0, 0.0, 0.0)
    # End
    curve_line_001.inputs[1].default_value = (0.0, 0.0, 1.0)

    # Node Normal
    normal = leafs_1.nodes.new("GeometryNodeInputNormal")
    normal.name = "Normal"
    normal.legacy_corner_normals = False

    # Node Align Euler to Vector
    align_euler_to_vector = leafs_1.nodes.new("FunctionNodeAlignEulerToVector")
    align_euler_to_vector.name = "Align Euler to Vector"
    align_euler_to_vector.axis = 'Z'
    align_euler_to_vector.pivot_axis = 'AUTO'
    # Rotation
    align_euler_to_vector.inputs[0].default_value = (0.0, 0.0, 0.0)
    # Factor
    align_euler_to_vector.inputs[1].default_value = 1.0

    # Node Instance on Points.003
    instance_on_points_003 = leafs_1.nodes.new("GeometryNodeInstanceOnPoints")
    instance_on_points_003.name = "Instance on Points.003"
    # Selection
    instance_on_points_003.inputs[1].default_value = True
    # Pick Instance
    instance_on_points_003.inputs[3].default_value = False
    # Instance Index
    instance_on_points_003.inputs[4].default_value = 0

    # Node Random Value.002
    random_value_002 = leafs_1.nodes.new("FunctionNodeRandomValue")
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
    realize_instances_002 = leafs_1.nodes.new("GeometryNodeRealizeInstances")
    realize_instances_002.name = "Realize Instances.002"
    realize_instances_002.realize_to_point_domain = False
    # Selection
    realize_instances_002.inputs[1].default_value = True
    # Realize All
    realize_instances_002.inputs[2].default_value = True
    # Depth
    realize_instances_002.inputs[3].default_value = 0

    # Node Vector Math.002
    vector_math_002 = leafs_1.nodes.new("ShaderNodeVectorMath")
    vector_math_002.name = "Vector Math.002"
    vector_math_002.operation = 'MULTIPLY'
    # Vector_001
    vector_math_002.inputs[1].default_value = (2.5999999046325684, 2.5999999046325684, 2.5999999046325684)

    # Node Curve Tangent
    curve_tangent = leafs_1.nodes.new("GeometryNodeInputTangent")
    curve_tangent.name = "Curve Tangent"

    # Node Random Value.003
    random_value_003 = leafs_1.nodes.new("FunctionNodeRandomValue")
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
    group_output = leafs_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True

    # Node Group Input
    group_input = leafs_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"

    # Set locations
    leafs_1.nodes["Instance on Points.001"].location = (-415.860107421875, 74.35693359375)
    leafs_1.nodes["Ico Sphere"].location = (-657.011962890625, -130.056884765625)
    leafs_1.nodes["Endpoint Selection"].location = (-885.767578125, -112.5028076171875)
    leafs_1.nodes["Random Value.001"].location = (-655.428466796875, -338.44171142578125)
    leafs_1.nodes["Realize Instances.001"].location = (-242.8765411376953, 224.4143524169922)
    leafs_1.nodes["Instance on Points.002"].location = (232.9775390625, 233.63681030273438)
    leafs_1.nodes["Curve Line.001"].location = (-263.6514892578125, 62.43239974975586)
    leafs_1.nodes["Normal"].location = (-352.521728515625, -257.399658203125)
    leafs_1.nodes["Align Euler to Vector"].location = (-139.353515625, -63.87969970703125)
    leafs_1.nodes["Instance on Points.003"].location = (832.02734375, 342.1554870605469)
    leafs_1.nodes["Random Value.002"].location = (652.81591796875, -127.0047607421875)
    leafs_1.nodes["Realize Instances.002"].location = (558.85302734375, 302.79742431640625)
    leafs_1.nodes["Vector Math.002"].location = (325.8935546875, -241.1060791015625)
    leafs_1.nodes["Curve Tangent"].location = (153.6962890625, -342.155517578125)
    leafs_1.nodes["Random Value.003"].location = (-5.51171875, -239.08489990234375)
    leafs_1.nodes["Group Output"].location = (1022.02734375, -1.52587890625e-05)
    leafs_1.nodes["Group Input"].location = (-1167.6773681640625, -6.995377540588379)

    # Set dimensions
    leafs_1.nodes["Instance on Points.001"].width  = 140.0
    leafs_1.nodes["Instance on Points.001"].height = 100.0

    leafs_1.nodes["Ico Sphere"].width  = 140.0
    leafs_1.nodes["Ico Sphere"].height = 100.0

    leafs_1.nodes["Endpoint Selection"].width  = 140.0
    leafs_1.nodes["Endpoint Selection"].height = 100.0

    leafs_1.nodes["Random Value.001"].width  = 140.0
    leafs_1.nodes["Random Value.001"].height = 100.0

    leafs_1.nodes["Realize Instances.001"].width  = 140.0
    leafs_1.nodes["Realize Instances.001"].height = 100.0

    leafs_1.nodes["Instance on Points.002"].width  = 140.0
    leafs_1.nodes["Instance on Points.002"].height = 100.0

    leafs_1.nodes["Curve Line.001"].width  = 140.0
    leafs_1.nodes["Curve Line.001"].height = 100.0

    leafs_1.nodes["Normal"].width  = 140.0
    leafs_1.nodes["Normal"].height = 100.0

    leafs_1.nodes["Align Euler to Vector"].width  = 140.0
    leafs_1.nodes["Align Euler to Vector"].height = 100.0

    leafs_1.nodes["Instance on Points.003"].width  = 140.0
    leafs_1.nodes["Instance on Points.003"].height = 100.0

    leafs_1.nodes["Random Value.002"].width  = 140.0
    leafs_1.nodes["Random Value.002"].height = 100.0

    leafs_1.nodes["Realize Instances.002"].width  = 140.0
    leafs_1.nodes["Realize Instances.002"].height = 100.0

    leafs_1.nodes["Vector Math.002"].width  = 140.0
    leafs_1.nodes["Vector Math.002"].height = 100.0

    leafs_1.nodes["Curve Tangent"].width  = 140.0
    leafs_1.nodes["Curve Tangent"].height = 100.0

    leafs_1.nodes["Random Value.003"].width  = 140.0
    leafs_1.nodes["Random Value.003"].height = 100.0

    leafs_1.nodes["Group Output"].width  = 140.0
    leafs_1.nodes["Group Output"].height = 100.0

    leafs_1.nodes["Group Input"].width  = 140.0
    leafs_1.nodes["Group Input"].height = 100.0


    # Initialize leafs_1 links

    # ico_sphere.Mesh -> instance_on_points_001.Instance
    leafs_1.links.new(
        leafs_1.nodes["Ico Sphere"].outputs[0],
        leafs_1.nodes["Instance on Points.001"].inputs[2]
    )
    # endpoint_selection.Selection -> instance_on_points_001.Selection
    leafs_1.links.new(
        leafs_1.nodes["Endpoint Selection"].outputs[0],
        leafs_1.nodes["Instance on Points.001"].inputs[1]
    )
    # random_value_001.Value -> instance_on_points_001.Scale
    leafs_1.links.new(
        leafs_1.nodes["Random Value.001"].outputs[1],
        leafs_1.nodes["Instance on Points.001"].inputs[6]
    )
    # instance_on_points_001.Instances -> realize_instances_001.Geometry
    leafs_1.links.new(
        leafs_1.nodes["Instance on Points.001"].outputs[0],
        leafs_1.nodes["Realize Instances.001"].inputs[0]
    )
    # realize_instances_001.Geometry -> instance_on_points_002.Points
    leafs_1.links.new(
        leafs_1.nodes["Realize Instances.001"].outputs[0],
        leafs_1.nodes["Instance on Points.002"].inputs[0]
    )
    # curve_line_001.Curve -> instance_on_points_002.Instance
    leafs_1.links.new(
        leafs_1.nodes["Curve Line.001"].outputs[0],
        leafs_1.nodes["Instance on Points.002"].inputs[2]
    )
    # align_euler_to_vector.Rotation -> instance_on_points_002.Rotation
    leafs_1.links.new(
        leafs_1.nodes["Align Euler to Vector"].outputs[0],
        leafs_1.nodes["Instance on Points.002"].inputs[5]
    )
    # normal.Normal -> align_euler_to_vector.Vector
    leafs_1.links.new(
        leafs_1.nodes["Normal"].outputs[0],
        leafs_1.nodes["Align Euler to Vector"].inputs[2]
    )
    # realize_instances_002.Geometry -> instance_on_points_003.Points
    leafs_1.links.new(
        leafs_1.nodes["Realize Instances.002"].outputs[0],
        leafs_1.nodes["Instance on Points.003"].inputs[0]
    )
    # random_value_002.Value -> instance_on_points_003.Scale
    leafs_1.links.new(
        leafs_1.nodes["Random Value.002"].outputs[1],
        leafs_1.nodes["Instance on Points.003"].inputs[6]
    )
    # instance_on_points_002.Instances -> realize_instances_002.Geometry
    leafs_1.links.new(
        leafs_1.nodes["Instance on Points.002"].outputs[0],
        leafs_1.nodes["Realize Instances.002"].inputs[0]
    )
    # vector_math_002.Vector -> instance_on_points_003.Rotation
    leafs_1.links.new(
        leafs_1.nodes["Vector Math.002"].outputs[0],
        leafs_1.nodes["Instance on Points.003"].inputs[5]
    )
    # curve_tangent.Tangent -> vector_math_002.Vector
    leafs_1.links.new(
        leafs_1.nodes["Curve Tangent"].outputs[0],
        leafs_1.nodes["Vector Math.002"].inputs[0]
    )
    # random_value_003.Value -> instance_on_points_002.Scale
    leafs_1.links.new(
        leafs_1.nodes["Random Value.003"].outputs[1],
        leafs_1.nodes["Instance on Points.002"].inputs[6]
    )
    # group_input.Points -> instance_on_points_001.Points
    leafs_1.links.new(
        leafs_1.nodes["Group Input"].outputs[1],
        leafs_1.nodes["Instance on Points.001"].inputs[0]
    )
    # instance_on_points_003.Instances -> group_output.Instances
    leafs_1.links.new(
        leafs_1.nodes["Instance on Points.003"].outputs[0],
        leafs_1.nodes["Group Output"].inputs[1]
    )
    # realize_instances_001.Geometry -> group_output.Geometry
    leafs_1.links.new(
        leafs_1.nodes["Realize Instances.001"].outputs[0],
        leafs_1.nodes["Group Output"].inputs[0]
    )
    # group_input.Instance -> instance_on_points_003.Instance
    leafs_1.links.new(
        leafs_1.nodes["Group Input"].outputs[0],
        leafs_1.nodes["Instance on Points.003"].inputs[2]
    )
    # group_input.Start Size -> endpoint_selection.Start Size
    leafs_1.links.new(
        leafs_1.nodes["Group Input"].outputs[2],
        leafs_1.nodes["Endpoint Selection"].inputs[0]
    )
    # group_input.End Size -> endpoint_selection.End Size
    leafs_1.links.new(
        leafs_1.nodes["Group Input"].outputs[3],
        leafs_1.nodes["Endpoint Selection"].inputs[1]
    )

    return leafs_1

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


    branches = branches_1_node_group(node_tree_names)
    node_tree_names[branches_1_node_group] = branches.name

    getnormalize = getnormalize_1_node_group(node_tree_names)
    node_tree_names[getnormalize_1_node_group] = getnormalize.name

    delete_points_of_curve = delete_points_of_curve_1_node_group(node_tree_names)
    node_tree_names[delete_points_of_curve_1_node_group] = delete_points_of_curve.name

    leafs = leafs_1_node_group(node_tree_names)
    node_tree_names[leafs_1_node_group] = leafs.name

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
