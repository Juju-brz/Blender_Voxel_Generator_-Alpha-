import sys
import os
import sys
print(sys.executable)
# Ajoute le dossier du script courant à sys.path
script_dir = os.path.dirname(os.path.abspath(__file__))
if script_dir not in sys.path:
    sys.path.append(script_dir)

# Maintenant vous pouvez importer
import jujuLib
