from commands.command import Command
import os

class Cmd(Command):
	description = "Execute les paramètres comme étant une commande du terminal windows."
	
	def init(self):
		self.add_argument("dirname",help="Nom du dossier du projet")

	def execute(self):
		os.system(self.args)