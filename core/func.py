import os

def start_terminal(path):
	os.system('start /D "{path}" '.format(path=path))
