import os

def br():
	print()

def clear(msg=""):
	os.system("cls")
	if msg:
		print(msg)