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
def create_trunk(node_tree_names: dict[typing.Callable, str]):
   """Initialize create_trunk node group"""
    create_trunk = bpy.data.node_groups.new(type='GeometryNodeTree', name="create_trunk")

    create_trunk.color_tag = 'NONE'
    create_trunk.description = ""
    create_trunk.default_group_node_width = 140
    create_trunk.is_modifier = True
    create_trunk.show_modifier_manage_panel = True

    # create_trunk interface

    # Socket Geometry
    geometry_socket = create_trunk.interface.new_socket(name="Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    # Socket Geometry
    geometry_socket_1 = create_trunk.interface.new_socket(name="Geometry", in_out='INPUT', socket_type='NodeSocketGeometry')
    geometry_socket_1.attribute_domain = 'POINT'
    geometry_socket_1.default_input = 'VALUE'
    geometry_socket_1.structure_type = 'AUTO'

    # Socket Scale
    scale_socket = create_trunk.interface.new_socket(name="Scale", in_out='INPUT', socket_type='NodeSocketFloat')
    scale_socket.default_value = 0.10000000149011612
    scale_socket.min_value = 0.0
    scale_socket.max_value = 3.4028234663852886e+38
    scale_socket.subtype = 'DISTANCE'
    scale_socket.attribute_domain = 'POINT'
    scale_socket.description = "Distance factor multiplied with the curve's radius attribute to define the resulting tube radius"
    scale_socket.default_input = 'VALUE'
    scale_socket.structure_type = 'AUTO'

    # Initialize create_trunk nodes

    # Node Group Input
    group_input = create_trunk.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"

    # Node Group Output
    group_output = create_trunk.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True

    # Node Curve to Tube
    curve_to_tube = create_trunk.nodes.new("GeometryNodeGroup")
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
    join_geometry = create_trunk.nodes.new("GeometryNodeJoinGeometry")
    join_geometry.name = "Join Geometry"

    # Set locations
    create_trunk.nodes["Group Input"].location = (-422.30596923828125, 42.52294921875)
    create_trunk.nodes["Group Output"].location = (398.9060974121094, 190.6674346923828)
    create_trunk.nodes["Curve to Tube"].location = (-58.119361877441406, 34.6033935546875)
    create_trunk.nodes["Join Geometry"].location = (238.68734741210938, 171.5737762451172)

    # Set dimensions
    create_trunk.nodes["Group Input"].width  = 140.0
    create_trunk.nodes["Group Input"].height = 100.0

    create_trunk.nodes["Group Output"].width  = 140.0
    create_trunk.nodes["Group Output"].height = 100.0

    create_trunk.nodes["Curve to Tube"].width  = 200.0
    create_trunk.nodes["Curve to Tube"].height = 100.0

    create_trunk.nodes["Join Geometry"].width  = 140.0
    create_trunk.nodes["Join Geometry"].height = 100.0


    # Initialize create_trunk links

    # group_input.Geometry -> curve_to_tube.Curve
    create_trunk.links.new(
        create_trunk.nodes["Group Input"].outputs[0],
        create_trunk.nodes["Curve to Tube"].inputs[0]
    )
    # group_input.Scale -> curve_to_tube.Scale
    create_trunk.links.new(
        create_trunk.nodes["Group Input"].outputs[1],
        create_trunk.nodes["Curve to Tube"].inputs[1]
    )
    # curve_to_tube.Mesh -> join_geometry.Geometry
    create_trunk.links.new(
        create_trunk.nodes["Curve to Tube"].outputs[0],
        create_trunk.nodes["Join Geometry"].inputs[0]
    )
    # join_geometry.Geometry -> group_output.Geometry
    create_trunk.links.new(
        create_trunk.nodes["Join Geometry"].outputs[0],
        create_trunk.nodes["Group Output"].inputs[0]
    )
    # group_input.Geometry -> join_geometry.Geometry
    create_trunk.links.new(
        create_trunk.nodes["Group Input"].outputs[0],
        create_trunk.nodes["Join Geometry"].inputs[0]
    )

    return create_trunk


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



if __name__ == "__main__":
    node_tree_names : dict[typing.Callable, str] = {}

    create_trunk = create_trunk(node_tree_names)
    node_tree_names[create_trunk] = create_trunk.name

    volume_simulation = volume_simulation_node_group(node_tree_names)
    node_tree_names[volume_simulation_node_group] = volume_simulation.name


    obj = bpy.context.active_object

    if obj is None:
        print("not object found")
    # else:
    #     mod = obj.modifiers.new("Curve to Tube", type='NODES')
    #     mod.node_group = create_trunk

