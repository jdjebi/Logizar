"""
	Travail avec le dossier ../data
"""
import pyperclip
from core.func import start_terminal
from commands.command import Command

class Get(Command):
	description = "Affiche le chemin vers le dossier du projet spécifié et le copie dans le presse papier. Les identifiants peuvent être utilisé aussi."

	def init(self):
		self.add_argument("dirname",help="Nom du dossier du projet")

	def execute(self):
		params = self.parse_args(self.argv)

		if params.dirname:
			key = params.dirname 
			lgz_dir = self.manager.lgz.get_dir(key)
			path = lgz_dir[2]
			pyperclip.copy(path)
			print("Chemin vers le dossier[Copier dans le presse papier]:",path)
