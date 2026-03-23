#juju

bl_info = {
    "name": "Blender Organics Shape",
    "author": "Julien Brouzes",
    "blender": (4, 0, 0),
    "category": "Object",
    "version": (0, 4, 0, 0)
}

import bpy
from . import main


def register():
    main.register()
    #panels.register()

def unregister():
    main.unregister()
    #panels.unregister()


###
#Julien Brouzes juju
