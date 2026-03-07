import bpy
import mathutils
import os
import typing

# Ok we will making group node for making like a libraries


# Import node groups from Blender essentials library
datafiles_path = bpy.utils.system_resource('DATAFILES')
lib_relpath = "assets/nodes/geometry_nodes_essentials.blend"
lib_path = os.path.join(datafiles_path, lib_relpath)
with bpy.data.libraries.load(lib_path, link=True)  as (data_src, data_dst):
    data_dst.node_groups = []
    if "Curve to Tube" in data_src.node_groups:
        data_dst.node_groups.append("Curve to Tube")


def create_trunk(node_tree_names: dict[typing.Callable, str]):
    #create node
    geometry_nodes_002_1  = bpy.ops.node.new_geometry_nodes_modifier()

    """Initialize Geometry Nodes.002 node group"""
    geometry_nodes_002_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="create_trunk")

    geometry_nodes_002_1.color_tag = 'NONE'
    geometry_nodes_002_1.description = ""
    geometry_nodes_002_1.default_group_node_width = 140
    geometry_nodes_002_1.is_modifier = True
    geometry_nodes_002_1.show_modifier_manage_panel = True

    # geometry_nodes_002_1 interface

    # Socket Geometry
    geometry_socket = geometry_nodes_002_1.interface.new_socket(name="Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    # Socket Geometry
    geometry_socket_1 = geometry_nodes_002_1.interface.new_socket(name="Geometry", in_out='INPUT', socket_type='NodeSocketGeometry')
    geometry_socket_1.attribute_domain = 'POINT'
    geometry_socket_1.default_input = 'VALUE'
    geometry_socket_1.structure_type = 'AUTO'

    # Initialize geometry_nodes_002_1 nodes

    # Node Group Input
    group_input = geometry_nodes_002_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"

    # Node Group Output
    group_output = geometry_nodes_002_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True

    # Node Curve to Tube
    curve_to_tube = geometry_nodes_002_1.nodes.new("GeometryNodeGroup")
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
    curve_to_tube.inputs[1].default_value = 0.07000000029802322
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
    join_geometry = geometry_nodes_002_1.nodes.new("GeometryNodeJoinGeometry")
    join_geometry.name = "Join Geometry"

    # Set locations
    geometry_nodes_002_1.nodes["Group Input"].location = (-340.0, 0.0)
    geometry_nodes_002_1.nodes["Group Output"].location = (296.19354248046875, 177.71116638183594)
    geometry_nodes_002_1.nodes["Curve to Tube"].location = (-90.85443878173828, 19.948917388916016)
    geometry_nodes_002_1.nodes["Join Geometry"].location = (153.02301025390625, 94.2607192993164)

    # Set dimensions
    geometry_nodes_002_1.nodes["Group Input"].width  = 140.0
    geometry_nodes_002_1.nodes["Group Input"].height = 100.0

    geometry_nodes_002_1.nodes["Group Output"].width  = 140.0
    geometry_nodes_002_1.nodes["Group Output"].height = 100.0

    geometry_nodes_002_1.nodes["Curve to Tube"].width  = 200.0
    geometry_nodes_002_1.nodes["Curve to Tube"].height = 100.0

    geometry_nodes_002_1.nodes["Join Geometry"].width  = 140.0
    geometry_nodes_002_1.nodes["Join Geometry"].height = 100.0


    # Initialize geometry_nodes_002_1 links

    # group_input.Geometry -> curve_to_tube.Curve
    geometry_nodes_002_1.links.new(
        geometry_nodes_002_1.nodes["Group Input"].outputs[0],
        geometry_nodes_002_1.nodes["Curve to Tube"].inputs[0]
    )
    # group_input.Geometry -> join_geometry.Geometry
    geometry_nodes_002_1.links.new(
        geometry_nodes_002_1.nodes["Group Input"].outputs[0],
        geometry_nodes_002_1.nodes["Join Geometry"].inputs[0]
    )
    # join_geometry.Geometry -> group_output.Geometry
    geometry_nodes_002_1.links.new(
        geometry_nodes_002_1.nodes["Join Geometry"].outputs[0],
        geometry_nodes_002_1.nodes["Group Output"].inputs[0]
    )
    # curve_to_tube.Mesh -> join_geometry.Geometry
    geometry_nodes_002_1.links.new(
        geometry_nodes_002_1.nodes["Curve to Tube"].outputs[0],
        geometry_nodes_002_1.nodes["Join Geometry"].inputs[0]
    )

    return geometry_nodes_002_1


if __name__ == "__main__":
    node_tree_names : dict[typing.Callable, str] = {}

    geometry_nodes_002 = create_trunk(node_tree_names)
    node_tree_names[create_trunk] = geometry_nodes_002.name

    obj = bpy.context.active_object

    if obj is None:
        print("not object found")
    else:
        mod = obj.modifiers.new("Curve to Tube", type='NODES')
        mod.node_group = geometry_nodes_002

