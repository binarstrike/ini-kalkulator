from os import name as os_name, system as exe
from typing import Callable

def bersihkan_terminal():
	"fungsi untuk membersihkan layar terminal"
	exe('cls' if os_name == 'nt' else 'clear')	

def run(q: str, func: Callable[[], None]):
	"""
	fungsi untuk menjalankan fungsi `func` dan ketika fungsi selesai di jalankan kemudian akan
	mengajukan pertanyaan sesuai pada parameter `q` untuk menjalankan fungsi `func` lagi atau tidak
	"""
	func()
	while input(q) in ["ya", "Y", "y"]:
		func()

def print_error(err: str):
	"fungsi untuk menampilkan pesan kesalahan pada program dengan teks yang di cetak tebal dan berwarna merah"
	print(f"\n\033[91m\033[1m{err}\033[0m\n")