import shlex
import sys
from cutils import *
from commands.shellx import Shell
from commands.run import Run
from commands.list import List
from commands.open import Open
from commands.cmd import Cmd
from commands.scan import Scan
from commands.get import Get

def kernel_cli(manager,cmd=""):
	""" Execution de la commande """

	args = shlex.split(cmd)
	sub_args = " ".join(args[1:])

	if cmd == "exit":
		sys.exit()

	elif cmd == "cls":
		clear()

	elif args[0] == "scan":
		Scan(manager,sub_args).execute()

	elif args[0] == "cmd":
		Cmd(manager,sub_args).execute()
		
	elif args[0] == "open":
		Open(manager,sub_args).execute()

	elif args[0] == "list":
		List(manager,sub_args).execute()

	elif args[0] == "run":
		Run(manager,sub_args).execute()

	elif args[0] == "shell":
		Shell(manager,sub_args).execute()

	elif args[0] == "get":
		Get(manager,sub_args).execute()

	else:
		print("Commande inconnue")


def app_cli(manager,cmd=""):	
	manager.init()
	clear("Logizar CLI v0.0.2")
	while True:
		if cmd == "":
			cmd = input(">> ");
		kernel_cli(manager,cmd)
		cmd = ""

def console_cli(manager,args):
	cmd = " ".join(args)
	kernel_cli(manager,cmd)	