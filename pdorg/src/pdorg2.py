
import os


os.chdir("../../")

try:
	os.mkdir("snapchat")
except FileExistsError:
	pass

