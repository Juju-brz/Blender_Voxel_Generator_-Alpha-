import bpy

def creer_cube_geo():
    """Crée un node group avec un simple cube"""
    ng = bpy.data.node_groups.new("MonCube", 'GeometryNodeTree')
    nodes = ng.nodes
    links = ng.links

    # Interface
    ng.interface.new_socket("Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')

    # Nodes
    g_out = nodes.new('NodeGroupOutput')
    g_out.location = (300, 0)

    cube = nodes.new('GeometryNodeMeshCube')
    cube.location = (0, 0)

    # ✅ Size attend un Vector (x, y, z) pas un float !
    cube.inputs['Size'].default_value = (2.0, 2.0, 2.0)

    # Lien
    links.new(cube.outputs['Mesh'], g_out.inputs['Geometry'])

    return ng

def hello():
    print("Hello from jujuLib!")
