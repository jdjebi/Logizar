from commands.command import Command

class List(Command):
	description = "Affiche la liste des dossiers de projet hébergeable."

	def execute(self):
		lgz_dirs = self.manager.lgz.get_dirs()
		for dir in lgz_dirs:
			print("{}- {} ({})".format(dir[0],dir[1],dir[2]))
