import sys
from core.cli import CliManager
from core import kernel
from core import func

default_cmd = ""

# Récupération du chemin du dossier de la cli
app_origin_dir = func.get_app_root_dir(func.DEBUG)

Manager = CliManager(app_origin_dir)

if __name__ == "__main__":	
	Manager.init()
	args = sys.argv[1:]
	if args:
		kernel.console_cli(Manager,args)
	else:
		kernel.app_cli(Manager,default_cmd)