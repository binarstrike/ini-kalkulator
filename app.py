import signal
from kalkulator import *

MENU = """
1. Informasi Kalkulator
2. Operasi Matematika Dasar
3. Konversi Suhu
4. Luas Geometri
5. Bilangan Prima
6. Keluar dari aplikasi

Masukan Pilihan [1-6] -> """

def main():
	while True:
		bersihkan_terminal()
		try:
			input_num = int(input(MENU))
			match input_num:
				case 1:
					run("Apakah Anda ingin melihat informasi tentang kalkulator ini lagi (ya/tidak)? ", info)
					continue
				case 2:
					run("Apakah Anda ingin menghitung kembali (ya/tidak)? ", calc)
					continue
				case 3:
					run("Apakah Anda ingin mengonversi kembali (ya/tidak)? ", konverter_suhu)
					continue
				case 4:
					run("Apakah Anda ingin menhitung luas kembali (ya/tidak)? ", hitung_luas)
					continue
				case 5:
					run("Apakah Anda ingin menampilkan bilangan prima lagi (ya/tidak)? ", bilangan_prima)
					continue
				case 6:
					program_exit(None, None)						
				case _: continue
		except ValueError: continue

def program_exit(signal, frame):
	print("\n\033[94m\033[1mTerima kasih telah menggunakan kalkulator ini.\033[0m")
	exit(0)

if __name__ == "__main__":
	signal.signal(signal.SIGINT, program_exit)
	main()
