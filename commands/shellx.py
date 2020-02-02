"""
	Travail avec le dossier ../data
"""
from core.func import start_terminal
from commands.command import Command

class Shell(Command):
	description = "Ouvre un terminal sur le dossier du projet spécifié. Les identifiants peuvent être utilisé aussi."

	def init(self):
		self.add_argument("dirname",help="Nom du dossier du projet")

	def execute(self):
		params = self.parse_args(self.argv)

		if params.dirname:
			key = params.dirname 
			lgz_dir = self.manager.lgz.get_dir(key)

			start_terminal(lgz_dir[2])
			