from .utils import print_error

INFO = {
	"Nama": "Otong",
	"NIM": "98982938",
}

BENTUK_GEOMETRI = """
1. Persegi
2. Persegi Panjang
3. Segitiga

Masukan pilihan bentuk geometri [1-3] -> """

REPLACE_OPERATOR= {
	"x": "*",
	":": "/",
	"X": "*",
	"÷": "/",
}

def info():
	for k, v in INFO.items():
		print(f"{k}: {v}")

def calc():
	try:
		print("Masukan input seperti berikut: 1 + 1 atau 5 * 5")
		input_str = input("kalkulator: ")
		
		for old, new in REPLACE_OPERATOR.items():
			input_str = input_str.replace(old, new)

		result = eval(input_str) # throw SyntaxError if input_str is not a valid syntax
		print(f"{input_str} = ", result)
	except (SyntaxError,ValueError):
		print_error("nilai yang di masukan tidak valid atau bukan berupa angka")

def konverter_suhu():
	try:
		num = float(input("Masukan nilai Celcius: "))
		print(f"""
	{num}℃  = {round((4/5) * num, 2)}°R
	{num}℃  = {round((9/5) * num + 32, 2)}℉
	{num}℃  = {num + 273.15}°K
		""")
	except ValueError:
		print_error("nilai yang di masukan tidak valid atau bukan berupa angka")

def hitung_luas():
	while True:
		try:
			pil = input(BENTUK_GEOMETRI)
			match pil:
				case '1':
					s = int(input("\nMasukan sisi Persegi: "))
					print(f"\nLuas Persegi = {s * s}")
					break
				case '2':
					p = int(input("Masukan panjang Persegi Panjang: "))
					l = int(input("Masukan lebar Persegi Panjang: "))
					print(f"\nLuas Persegi Panjang = {p * l}")
					break
				case '3':
					a = int(input("Masukan alas Segitiga: "))
					t = int(input("Masukan tinggi Segitiga: "))
					print(f"\nLuas Segitiga = {0.5 * a * t}")
					break
				case _:
					print_error("input salah, masukan input dari angka 1 sampai 3 untuk memilih bentuk geometri")
					continue
		except ValueError:
			print_error("nilai yang di masukan tidak valid atau bukan berupa angka")

def bilangan_prima():
	try:
		awal = int(input("masukan nilai awal: "))
		akhir = int(input("masukan nilai akhir: "))
		prime_num = []
		for num in range(awal, akhir):
			if num == 1:
				continue
			elif num == 2:
				prime_num.append(num)
			elif num % 2 and num % 3:
				prime_num.append(num)
		print(f"\n{', '.join([str(s) for s in prime_num])}\n")
	except ValueError:
		print_error("nilai yang di masukan tidak valid atau bukan berupa angka")
		
