import os
import subprocess
from utils import safe_line
import sys
import ctypes

exit()

#import psutil

def is_admin():
	try:
		#return True
		return ctypes.windll.shell32.IsUserAnAdmin()
	except :
		return False


if is_admin():

	print('yes')

	ENV_PATH = os.environ.get('PATH')

	lgz_script_dir = os.getcwd()

	separator = ";"

	if ENV_PATH[-1] != ";":
		add_separator = ""

	cmd_to_update_path = 'setx PATH /M {path}{separator}{dir}'.format(path=ENV_PATH,separator=separator,dir=lgz_script_dir)


	print(cmd_to_update_path)
	subprocess.call(cmd_to_update_path)

else:
	ctypes.windll.shell32.ShellExecuteW(None,'runas',sys.executable,__file__,None,1)

os.system("PAUSE")