import os
from . import utils

class lgzManager:
	""" Classe pour la gestion des dossier lgz """
	def __init__(self,cli):
		self.lgz_dirs = []
		self.lgz_dirs_name = {} # [Nom du dossier] = indice du dossier 
		self.CLI = cli
		self.update()

	@classmethod
	def safe_key(cls,key):
		""" Converti key entier si il l'est """
		try:
			key = int(key)
		except ValueError:
			pass
		return key

	def update(self):
		""" Met à jour la liste des dossiers lgz"""
		self.lgz_dirs = self.get_dirs()

	def get_index_type(self,index):
		return index.__class__.__name__

	def get_dir(self,index):
		""" Retourne un projet hébergeable enregistré """
		index = self.safe_key(index)

		if self.get_index_type(index) == "str":
			return self.lgz_dirs[self.lgz_dirs_name[index.lower()]]
		else:
			return self.lgz_dirs[index - 1]

	def get_dirs(self):
		""" Retourne la liste des projets hébergeable issus du scanne """
		lgz_file = open(self.CLI.config.get("LGZ_PROJECTS_FILE"),mode="r",encoding="utf-8")
		lgz_dirs = []
		for i, path in enumerate(lgz_file.readlines()):
			path = utils.safe_line(path)
			dirname = os.path.basename(path)
			index = i+1
			# On enregistre l'indice du dossier dans un dictionnaire avec pour clée son nom
			self.lgz_dirs_name[dirname.lower()] = i
			lgz_dirs.append((index,dirname,path))
		lgz_file.close()
		return lgz_dirs