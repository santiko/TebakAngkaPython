import random
import os

def daftar_menu():
	os.system("reset")
	print 69 * "*"
	os.system("figlet TEBAK ANGKA")
	print 30 * "*", "PILIHAN" , 30 * "*"
	print "1. TEBAK ANGKA"
	print "2. TENTANG PROGRAM"
	print "3. KELUAR"
	print 69 * "*"

def tebakAngka():
	os.system("clear")
	print 69 * "*"
	os.system("figlet Tebak Angka")
	print 69 * "*"
	angka = input("\nMasukkan 1 angka saja yang Anda pikirkan!\nr00t@l0calhost:$ ")
	acak = random.randint(1,5)*1
	if int(angka) != acak:
		raw_input("[-] Anda gagal...!\n[-] Silakan ulangi lagi..!\n[-] Angka yang keluar adalah [" + str(acak) + "]\n\nTekan [ENTER] untuk mengulangi..!")
		tebakAngka()
	elif int(angka) > '5' and int(angka) < '1':
		raw_input("Angka yang diinputkan antara 1 sampai 5..!")
	elif int(angka) == " ":
		raw_input("Tidak boleh kosong! Harus diisi..!")
	else:
		print("[+] Alhamdulillaah!\n[+] Anda beruntung kali ini...!\n[+] Angka yang keluar adalah [" + str(acak) + "]")
		tanya = raw_input("Apakah Anda ingin mengulangi lagi [Y/T]?\nr00t@l0calhost:$ ")
		if tanya == 'Y' or tanya == 'y':
			tebakAngka()
		elif tanya == 'T' or tanya == 't':
			daftar_menu()
		else:
			raw_input("Angka yang Anda ketikkan tidak ada dalam daftar menu!\nSilakan ulangi lagi..!")
			tanya

def tentangProgram():
	os.system("clear")
	print 69 * "*"
	os.system("figlet TENTANG")
	print 69 * "*"
	raw_input("[+] Nama Program: TEBAK ANGKA\n[+] Versi: 1.0.1\n[+] Pengembang: SANTIKO KUSNUL HAKIM\n[+] Bahasa Pemrograman: PYTHON\n[+] Waktu: 7 APRIL 2018\n\nTekan [ENTER] untuk kembali ke menu utama!")
	daftar_menu()

loops = True

while loops:
	daftar_menu()
	try:
		pilih = raw_input("r00t@l0calhost:$ ")
		if (pilih) == '1':
			tebakAngka()
		elif (pilih) == '2':
			tentangProgram()
		elif (pilih) == '3':
			loops = False
			os.system("python app.py")
		else:
			raw_input("Anda telah menekan tombol [ENTER] atau salah input nomor menu!")
			daftar_menu()
			#loops = False
	except KeyboardInterrupt:
		raw_input("ANDA INGIN KELUAR YAA...?\nr00t@l0calhost:$ ")
		os.system("clear")
		loops = False