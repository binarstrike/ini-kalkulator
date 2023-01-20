from sys import platform
from os import system

def bersihkan_terminal():
	if(platform in ["linux", "linux2"]):
		system("clear")
	else:
		system("cls")

def run(q: str, f):
	f()
	while input(q) in ["ya", "Y", "y"]:
		f()
	else:
		pass
