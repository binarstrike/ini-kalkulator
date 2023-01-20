from platform import system as OS
from os import system

def bersihkan_terminal():
	if OS() in ["Linux", "Darwin"]:
		system("clear")
	elif OS() == "Windows":
		system("cls")
	else:
		system("clear")
		

def run(q: str, f):
	f()
	while input(q) in ["ya", "Y", "y"]:
		f()
