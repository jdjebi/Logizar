from commands.command import Command
from commands.list import List
from core import utils
import os
import shlex
import time

class Open(Command):
	description = "Commande pour ouvrir un dossier de projet enregistré suite à un scanne à partir du nom du dossier ou son id."

	def init(self):
		self.add_argument("dirname",help="Nom du dossier du projet")

	def execute(self):

		params = self.parse_args(self.argv)
		manager = self.manager
		args = self.args

		key = params.dirname 

		try:
			lgz_dir = manager.lgz.get_dir(key)
			path = lgz_dir[2]
			os.system("start {path}".format(path=path))
		except IndexError:
			print("Le dossier d'id {} est introuvable.\n".format(key))
			List(manager,args).execute()
		except KeyError:
			print('Le dossier "{}" introuvable. Les dossiers disponibles sont listés ci-dessous.\n'.format(key))
			List(manager,args).execute()