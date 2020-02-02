import os
from commands.command import Command
from core.cli import DEFAULT_PROJECTS_DIR
from core import utils

class Scan(Command):
	description = "Recherche tous les dossiers hébergeable par logizar."

	def execute(self):
		nbr_lgz_dir = 0
		lgz_dir = []

		#f = open("expore.html",mode="w",encoding='utf-8')
		#Lancement du scanne
		for current_dir in DEFAULT_PROJECTS_DIR:
			print("Scanne du dossier de projets:", current_dir)
			for (root,dirs,files) in os.walk(current_dir, topdown=True): 
				#print("\t",root,files)
				if "todo.md" in files or "zar" in files:
					nbr_lgz_dir += 1
					lgz_dir.append(root)
				#print(root,files,"<br>",file=f)
				#print("<br><br>",file=f)
		#f.close()
		#os.system("start expore.html")
		print("\nFin du scanne. {} dossier(s) hébergeable trouvé.\n".format(nbr_lgz_dir))
		utils.show_list(lgz_dir)

		with open(self.manager.config.get("LGZ_PROJECTS_FILE"), mode="w", encoding="utf-8") as file:
			for dir in lgz_dir:
				print(dir,file=file)

		self.manager.lgz.update() # Mise à jour des dossiers lgz du Manager