import argparse
import shlex

class Command(argparse.ArgumentParser):
	description = "Commande de base"

	def __init__(self,manager,argv):
		super().__init__(description=self.description)
		self.manager = manager
		self.args = argv
		self.argv = shlex.split(argv)
		self.init()

	def init(self):
		pass

	def execute(self):
		pass

	def exit(self,code,error_msg):
		print(error_msg)