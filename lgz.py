import os
import re
import utils
from cutils import *
import sys

# Assure que le dossier root est bien celui du script pour garantir les liaisons relatives
app_origin_dir = sys.path[1]
os.chdir(app_origin_dir)

# Définition des constantes
DATA_DIR = os.path.abspath("data\\")

PROJECTS_FILE_PATH = os.path.join(DATA_DIR,"projects")

DEFAULT_PROJECTS_DIR = [
	"C:\\Users\\samsung\\Desktop\\Dev2",
	"C:\\wamp64\\www",
	"C:\\Users\\samsung\\dev"
]

LGZ_PROJECTS_FILE = os.path.abspath('data\\dirs.lgz')

class lgzManager:
	""" Classe pour la gestion des dossier lgz """
	def __init__(self):
		self.lgz_dirs = []
		self.lgz_dirs_name = {} # [Nom du dossier] = indice du dossier 
		self.update()

	def update(self):
		""" Met à jour la liste des dossiers lgz"""
		self.lgz_dirs = self.get_dirs()

	def get_dir(self,index):
		""" Retourne un projet hébergeable enregistré """
		try:
			# Retourne à partie de l'index du dossier
			return self.lgz_dirs[index - 1]
		except TypeError:
			# Retourne à partir du nom dossier
			return self.lgz_dirs[self.lgz_dirs_name[index.lower()]]

	def get_dirs(self):
		""" Retourne la liste des projets hébergeable issus du scanne """
		lgz_file = open(LGZ_PROJECTS_FILE,mode="r",encoding="utf-8")
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


class CliManager:
	def __init__(self):
		self.lgz = lgzManager()
	
	def init(self):
		self.lgz.update()

	def os_exec(cls,cmd):
		""" Execute les commandes contenu dans cmd_list """
		if cmd[0] != "#":
			os.system(cmd)

""" Fonctions """

""" Commandes """
def list2():
	""" Affiche les dossiers des dossiers de projet par défaut """
	index = 0
	for current_dir in DEFAULT_PROJECTS_DIR:
		dir_in = os.listdir(current_dir)
		for i, dirname in enumerate(dir_in):
			index += 1
			dirpath = utils.join(current_dir,dirname)
			print("{index}- {dirname} ({dirpath})".format(index=index,dirname=dirname,dirpath=dirpath))

def list3():
	""" Affiche la liste des dossiers de projet hébergeable """
	lgz_dirs = Manager.lgz.get_dirs()
	for dir in lgz_dirs:
		print("{}- {} ({})".format(dir[0],dir[1],dir[2]))

def open_lgz_by_id(id):
	try:
		index = int(id)
		ldir = Manager.lgz.get_dir(index)
		path = ldir[2]
		os.system("start {}".format(path))
	except IndexError:
		print("Le dossier d'id {} est introuvable.".format(index))
		list3()


def open_lgz_by_name(name):
	try:
		ldir = Manager.lgz.get_dir(name)
		path = ldir[2]
		os.system("start {}".format(path))
	except KeyError:
		print("{} introuvable.".format(name))
		list3()


def run(key_str):
	""" Lance la chaine d'execution """
	key = None
	# Si key_str est un nombre en fait une conversion sinon on l'utilise comme clé
	try:
		key = int(key_str)
	except ValueError:
		key = key_str

	dir = Manager.lgz.get_dir(key)
	path = dir[2]

	to_exec = []

	# Lecture des commandes à executer
	try:
		with open(utils.join(path,"zar"),mode="r",encoding="utf-8") as zfile:
			lines = zfile.readlines()
			for line in lines:
				zar_cmd = utils.safe_line(line)
				to_exec.append(zar_cmd)
			
		# Execution
		for cmd in to_exec:
			print("execute:",cmd)
			Manager.os_exec(cmd)
	except FileNotFoundError:
		print("Le dossier \"{}\"\nne possède pas de fichier de chaine d'execution(zar)".format(path))

def scan():
	""" Recherche tous les dossiers hébergeable par logizar """
	nbr_lgz_dir = 0
	lgz_dir = []

	#f = open("expore.html",mode="w",encoding='utf-8')
	# Lancement du scanne
	for current_dir in DEFAULT_PROJECTS_DIR:
		print("Scanne du dossier de projets:", current_dir)
		for (root,dirs,files) in os.walk(current_dir, topdown=True): 
			if "todo.md" in files:
				nbr_lgz_dir += 1
				lgz_dir.append(root)
			#print(root,files,"<br>",file=f)
			#print("<br><br>",file=f)
	#f.close()
	#os.system("start expore.html")

	print("\nFin du scanne. {} dossier(s) hébergeable trouvé.\n".format(nbr_lgz_dir))
	utils.show_list(lgz_dir)

	with open(LGZ_PROJECTS_FILE, mode="w", encoding="utf-8") as file:
		for dir in lgz_dir:
			print(dir,file=file)

	Manager.lgz.update() # Mise à jour des dossiers lgz du Manager


""" App """
Manager = CliManager()

def kernel_cli(cmd=""):
	""" Execution de la commande """

	if cmd == "exit":
		exit()

	elif cmd == "cls":
		clear()

	elif cmd == "list2":
		list2()

	elif cmd == "list3":
		list3()
		#exit()

	elif cmd == "scan":
		scan()

	elif re.match("^open: [0-9]+",cmd):
		open_lgz_by_id(cmd[6:])

	elif re.match("^open2: (.)+",cmd):
		open_lgz_by_name(cmd[7:])

	elif re.match("^run: ((.)|[0-9])+",cmd):
		run(cmd[5:])
	else:
		print("Commande inconnue")


def app_cli(cmd=""):
	Manager.init()
	clear("Logizar CLI v0.0.1")
	while True:
		if cmd == "":
			cmd = input(">> ");
		kernel_cli(cmd)
		cmd = ""

def console_cli(args):
	cmd = " ".join(args)
	kernel_cli(cmd)

		
if __name__ == "__main__":	

	Manager.init()

	args = sys.argv[1:]

	if args:
		console_cli(args)
	else:
		app_cli()