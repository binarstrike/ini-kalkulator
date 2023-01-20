from kalkulator import *

def main():
	while True:
		bersihkan_terminal()
		match int(input(MENU)):
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
				print("\nTerima kasih telah menggunakan kalkulator ini.")
				break
			case _:
				print("\nTerima kasih telah menggunakan kalkulator ini.")
				break
	exit(0)



if __name__ == "__main__":
	main()
