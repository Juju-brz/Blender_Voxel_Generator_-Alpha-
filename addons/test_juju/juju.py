import bpy
import math

#obj = bpy.context.active_object
#blend_path = bpy.data.filepath

#locator_position = [0, 0, 0]
## CLEAN ##
def clean_scene():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False, confirm=False)

#scene = bpy.context.scene
#locator_position = [0, 0, 0]


def create_voxel(biere, name="name"):
    biere = bpy.ops.object.modifier_add(type='REMESH')
    biere = bpy.context.object.modifiers["Remesh"].voxel_size = 0.123
    biere = bpy.ops.object.modifier_apply(modifier="Remesh")
    biere = bpy.context.active_object
    biere.name = name


def decimate():
    bpy.ops.object.modifier_add(type='DECIMATE')
    bpy.context.object.modifiers["Decimate"].decimate_type = 'DISSOLVE'
    bpy.ops.object.modifier_apply(modifier="Decimate")


def create_cube_vox():
    biere = bpy.ops.mesh.primitive_cube_add()
    create_voxel(biere, name="voxel_cube")


def create_sphere_vox():
    biere = bpy.ops.mesh.primitive_uv_sphere_add()
    create_voxel(biere, name="voxel_sphere")

def ground_generation(ground_num):

    for i in range(-ground_num, ground_num + 1):
        for j in range(-ground_num, ground_num + 1):
            x_pos = locator_position[0] + (i * 2)
            y_pos = locator_position[1] + (j * 2)
            z_pos = locator_position[2]


            bpy.ops.mesh.primitive_cube_add(location=(x_pos, y_pos, z_pos) )
            bpy.context.object.name = f"ground"

### VOLUME ###
def volume_displacement():
    #bpy.context.space_data.context = 'MODIFIER'
    bpy.ops.object.modifier_add(type='VOLUME_DISPLACE')
    #bpy.ops.texture.new()
    tex = bpy.data.textures.new("VolumeTex", type='CLOUDS')
    #mod = obj.modifiers["Volume Displace"]
    #mod.texture = tex
    #text = bpy.data.textures.new("VolumeTex", type='CLOUDS')

def mesh_to_volume():
    volume_collection = bpy.data.collections.new("volume")
    bpy.context.scene.collection.children.link(volume_collection)

    mesh_to_convert = bpy.context.active_object
    mesh_to_convert.name = "mesh_volume"
    volume_collection.objects.link(bpy.context.active_object)
    bpy.ops.collection.objects_remove_active()
    bpy.ops.object.volume_add()
    #mesh_to_convert.hide_viewport = True
    bpy.ops.object.modifier_add(type='MESH_TO_VOLUME')
    bpy.context.object.modifiers["Mesh to Volume"].object = mesh_to_convert

    volume_collection.objects.link(bpy.context.active_object)
    bpy.ops.collection.objects_remove_active()

    ## FUNCTION ##
    volume_displacement()

    # CREATE EMPTY
    empty = bpy.ops.object.empty_add(scale=(4, 4, 4))
    empty = volume_collection.objects.link(bpy.context.active_object)
    #empty = bpy.ops.collection.objects_remove_active()
    #bpy.ops.object.volume_add()
    bpy.ops.object.parent_set(type='OBJECT', keep_transform=True)
    toggle_mesh_visibility()

def new_collection(a, collection):
    a = collection.objects.link(bpy.context.active_object)



def toggle_mesh_visibility():
    obj = bpy.context.active_object
    obj = bpy.data.objects["mesh_volume"]
    obj.hide_viewport = not obj.hide_viewport


def volume_to_mesh():
    obj = bpy.context.active_object
    vol_to_convert = bpy.context.active_object
    bpy.ops.mesh.primitive_cube_add()
    obj = bpy.context.active_object
    obj.name = "volume_mesh"
    bpy.ops.object.modifier_add(type='VOLUME_TO_MESH')

    bpy.context.object.modifiers["Volume to Mesh"].object = vol_to_convert
    bpy.ops.object.modifier_apply(modifier="Volume to Mesh")
    subdivision_mesh()

def simulation_node():
    bpy.context.area.ui_type = 'GeometryNodeTree'
    screen = bpy.context.window.screen

    #viewport = next(area for area in screen.areas if area.type == 'VIEW_3D')


    #with bpy.context.temp_override(area=viewport):
        #bpy.ops.screen.area_split(direction='VERTICAL', factor=0.5)


    #screen.areas[0].type = 'NODE_EDITOR'
    bpy.ops.node.new_geometry_nodes_modifier()
    #bpy.ops.node.add_zone(use_transform=True, input_node_type="GeometryNodeSimulationInput", output_node_type="GeometryNodeSimulationOutput", add_default_geometry_link=True)
    bpy.data.node_groups["Geometry Nodes"].name = "Simulation Nodes"
    #bpy.ops.node.add_node(settings=[{"name":"node_tree", "value":"bpy.data.node_groups['Simulation Nodes']"}, {"name":"width", "value":"140"}, {"name":"name", "value":"'Simulation Nodes'"}], use_transform=True, type="GeometryNodeGroup")



def subdivision_mesh():
    obj = bpy.context.active_object
    obj = bpy.ops.object.modifier_add(type='SUBSURF')
    obj = bpy.context.object.modifiers["Subdivision"].levels = 3

#curve = 0
def draw_curve():
    bpy.ops.curve.primitive_bezier_curve_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
    obj = bpy.ops.object.editmode_toggle()
    obj = bpy.ops.curve.delete(type='VERT')
    #obj.name = "plant"
    curve = obj
    bpy.ops.wm.tool_set_by_id(name="builtin.draw")

#def select_curve():
    #curve = obj

def create_leaf(shapefunc):
    obj = bpy.context.active_object
    curve = obj
    #tree = obj
    shapefunc()
    bpy.ops.object.modifier_add_node_group(asset_library_type='ESSENTIALS', asset_library_identifier="", relative_asset_identifier="nodes/geometry_nodes_essentials.blend/NodeTree/Array")
    #bpy.context.object.modifiers["Array"]["Socket_2"] = 'Curve'
    bpy.context.object.modifiers["Array"]["Socket_2"] = 2 #SHAPE
    #bpy.context.object.modifiers["Array"]["Socket_33"] = 'Distance'
    bpy.context.object.modifiers["Array"]["Socket_33"] = 0 #COUNT METHOD
    bpy.context.object.modifiers["Array"]["Socket_27"] = bpy.data.objects["curve"] #tree
    bpy.context.object.modifiers["Array"]["Socket_17"] = True
    bpy.context.object.modifiers["Array"]["Socket_15"][0] = 140.
    bpy.context.object.modifiers["Array"]["Socket_15"][1] = 140.
    bpy.context.object.modifiers["Array"]["Socket_15"][2] = 140.

def create_leaf_shape():
    obj = bpy.context.active_object
    bpy.ops.mesh.primitive_plane_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(0.3, 0.3, 0.3))
    obj = bpy.context.object.scale[1] = 0.3
    obj = bpy.context.object.scale[2] = 0.3
    obj = bpy.context.object.scale[0] = 0.3

    obj =  bpy.ops.object.transforms_to_deltas(mode='ALL')

def create_spike_shape():
    obj = bpy.context.active_object
    bpy.ops.mesh.primitive_cone_add()
    obj = bpy.context.object.scale[1] = 0.3
    obj = bpy.context.object.scale[2] = 0.3
    obj = bpy.context.object.scale[0] = 0.3

def curve_test():
    #fibonnaci
    val0 = 1.0
    val1 = 1.0
    old_value = 1.0
    #bpy.ops.curve.extrude_move(CURVE_OT_extrude={"mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(-0.554322, -0.620455, 0.0231373)})
    for i in range(4):
        bpy.ops.curve.extrude_move(CURVE_OT_extrude={"mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(val0, val0, val0)})
        old_value = val0
        val0 += val1
        #val0 = val0 * -val0 # POS TO NEG
        val1 = old_value
        print(val0)

def create_bezier_curve():
    bpy.ops.curve.primitive_bezier_curve_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
    bpy.ops.object.editmode_toggle()
    #bpy.ops.curve.delete(type='VERT')
    bpy.ops.transform.translate(value=(-1, 0, 0))

def fib_curve():
    val0 = 1.0
    val1 = 1.0
    old_value = 1.0
    angle = 0.0
    angle_step = math.pi / 4

    for i in range(8):

        x = val0 * math.cos(angle)
        y = val0 * math.sin(angle)
        z = 0.1


        bpy.ops.curve.extrude_move(
            CURVE_OT_extrude={"mode": 'TRANSLATION'},
            TRANSFORM_OT_translate={"value": (x, y, z)}
        )


        angle += angle_step


        old_value = val0
        val0 += val1
        val1 = old_value
        print(val0)
