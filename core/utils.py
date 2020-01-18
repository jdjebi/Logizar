import os

def get_listdir(path):
	return os.listdir(path)

def show_list(lst,showindex=True,style="-"):
	index = ""
	for i, elm in enumerate(lst):
		if showindex:
			index = i + 1
		print("{index}{style} {elm}".format(index=index,style=style,elm=elm))

def join(a,b):
	return os.path.join(a,b)

def safe_line(line):
	return line.replace("\n",'')