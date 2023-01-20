MENU = """
1. Informasi Kalkulator
2. Operasi Matematika
3. Konversi Suhu
4. Luas Geometri
5. Bilangan Prima
6. Keluar dari program

Masukan Pilihan [1-6] -> """

INFO = {
	"nama": "Otong",
	"NIM": "98982938",
	"kapan": "20 Januari 2023"
}

BENTUK_GEOMETRI = """
1. Persegi
2. Persegi Panjang
3. Segitiga

Masukan pilihan bentuk geometri [1-3] -> """

def info():
	print(f"""
Nama: {INFO['nama']}
NIM: {INFO['NIM']}
{INFO['kapan']}
	""")

def calc():
	x = int(input("\nMasukan operand pertama: "))
	y = int(input("Masukan operand kedua: "))
	while True:
		op = input("Operator [+ - * /]: ")
		if not op in ['+', '-', '*', '/']:
			print("Maaf, operator tidak dikenali")
			continue
		if op == '+':
			print(f"{x} {op} {y} = {x + y}")
			break
		elif op == '-':
			print(f"{x} {op} {y} = {x - y}")
			break
		elif op == '*':
			print(f"{x} {op} {y} = {x * y}")
			break
		elif op == '/':
			print(f"{x} {op} {y} = {round(float(x / y), 2)}")
			break

def konverter_suhu():
	c = input("Masukan nilai Celcius: ")
	print(f"""
{c}℃  = {round((4/5) * float(c), 2)}°R
{c}℃  = {round((9/5) * float(c) + 32, 2)}℉
{c}℃  = {float(c) + 273.15}°K
	""")

def hitung_luas():
	while True:
		pil = input(f"\n{BENTUK_GEOMETRI}")

		if pil == '1':
			s = int(input("\nMasukan sisi Persegi: "))
			print(f"Luas Persegi = {s * s}")
			break
		elif pil == '2':
			p = int(input("Masukan panjang Persegi Panjang: "))
			l = int(input("Masukan lebar Persegi Panjang: "))
			print(f"Luas Persegi Panjang = {p * l}")
			break
		elif pil == '3':
			a = int(input("Masukan alas Segitiga: "))
			t = int(input("Masukan tinggi Segitiga: "))
			print(f"Luas Segitiga = {(1/2) * a * t}")
			break
		else:
			print("Input salah, masukan input dari angka 1 sampai 3 untuk memilih bentuk geometri")
			continue

def bilangan_prima():
	awal = int(input("masukan nilai awal: "))
	akhir = int(input("masukan nilai akhir: "))
	prima = ""
	for i in range(awal, akhir):
		if i == 1:
			continue
		elif i == 2:
			prima += f"{i}"
		elif i % 2 and i % 3:
			prima += f", {i}"
	print(f"\n{prima}\n")
