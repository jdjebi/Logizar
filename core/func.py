import os
import sys

DEBUG = "DEBUG"
RELEASE = "RELEASE"


def start_terminal(path):
	os.system('start /D "{path}" '.format(path=path))

def get_app_root_dir(mode=DEBUG):
	""" Retourne le chemin du dossier root du cli """

	if mode == RELEASE:
		return os.path.dirname(sys.path[-1])
	else:
		return sys.path[1]	

def run(script,args):
	os.system("python commands\\{script}.py {args}".format(script=script,args=args))
