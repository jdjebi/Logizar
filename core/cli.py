import os
from .lgzmanager import lgzManager

DEFAULT_PROJECTS_DIR = [
	"C:\\Users\\samsung\\Desktop\\Dev2",
	"C:\\wamp64\\www",
	"C:\\Users\\samsung\\dev"
]
	
class CliManagerConfig:
	""" classe en charge de la sauvegarde des constantes """
	DATA_DIR = None
	PROJECTS_FILE_PATH = None
	LGZ_PROJECTS_FILE = None

	CONFIG = {}

	def init_global_vars(cls):
		cls.DATA_DIR = os.path.abspath("data\\")
		cls.PROJECTS_FILE_PATH = os.path.join(cls.DATA_DIR,"projects")
		cls.LGZ_PROJECTS_FILE = os.path.abspath('data\\dirs.lgz')

		cls.CONFIG = {
			"DATA_DIR": cls.DATA_DIR,
			"PROJECTS_FILE_PATH": cls.PROJECTS_FILE_PATH,
			"LGZ_PROJECTS_FILE": cls.LGZ_PROJECTS_FILE
		}

	def get(cls,key):
		if key == "DATA_DIR":
			return cls.DATA_DIR
		elif key == "PROJECTS_FILE_PATH":
			return cls.PROJECTS_FILE_PATH
		elif key == "LGZ_PROJECTS_FILE":
			return cls.LGZ_PROJECTS_FILE
		else:
			print("Clé {} inconnue".format(key))
			return None

	def get_conf_vars(cls):
		return cls.CONFIG


class CliManager:
	def __init__(self,app_origin_dir):

		# Défini le dossier de travail, celui du cli

		os.chdir(app_origin_dir)

		# Initialisation des variables globale
		self.config = CliManagerConfig()
		self.config.init_global_vars()

		# Initialisation du gestion des dossiers lgz
		self.lgz = lgzManager(self)

	def init(self):
		self.lgz.update()

	def os_exec(cls,cmd):
		""" Execute les commandes contenu dans cmd_list """
		if cmd[0] != "#":
			os.system(cmd)