from commands.command import Command
from core import utils
import os
import shlex
import time

class Run(Command):
	description = "Lance la chaine d'execution contenu dans le fichier zar du dossier spécifié."

	SYSTEM_COMMAND = "system"
	APP_COMMAND = "app"

	def init(self):
		self.add_argument("dirname",help="Nom du dossier du projet")

	def execute(self):
		params = self.parse_args(self.argv)
		if params.dirname:
			key = params.dirname 
			lgz_dir = self.manager.lgz.get_dir(key)
			path = lgz_dir[2]
			xchain = []
			try:
				with open(utils.join(path,"zar"),mode="r",encoding="utf-8") as file:
					lines = file.readlines()
					xchain = self.prepare_chain(lines)
			except FileNotFoundError:
				print("Le dossier \"{}\"\nne possède pas de fichier de chaine d'execution(zar)".format(path))
			self.process(xchain)

	def prepare_chain(self,lines):
		""" Prépare la chaine d'execution en créant des tuples d'execution """
		xchain = []
		for line in lines:
			line = utils.safe_line(line)
			node = (self.SYSTEM_COMMAND,line)
			if line:
				if not line.startswith("#"):
					if line.startswith("@sleep"):
						try:
							elm = line.split()
							node = (self.APP_COMMAND,elm[0],int(elm[1]),line)
							
						except Exception as e:
							print("Valeur de temporisation incorrecte.",e)
							print("Exemple: @sleep 5. Temporisation de 5 secondes")
					xchain.append(node)
		return xchain

	def process(self,xchain):
		for node in xchain:
			cmd = node[-1]
			if node[0] == self.SYSTEM_COMMAND:
				print("Execute:",cmd)
				os.system(cmd)
			elif node[0] == self.APP_COMMAND:
				if node[1] == '@sleep':
					sleep_time = node[2]
					print("Sleep for ",sleep_time," seconds")				
					time.sleep(sleep_time)
