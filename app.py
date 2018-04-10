import random
import os


def bhs():
	os.system("reset")
	print 69 * "*"
	os.system("figlet BAHASA")
	print 69 * "*"
	print("1. BAHASA INDONESIA")
	print("2. BAHASA INGGRIS")
	print("3. BAHASA JAWA")
	print 69 * "*"
	pilih = raw_input("SILAKAN PILIH BAHASA YANG ANDA GUNAKAN: ")
	if (pilih) == '1':
		os.system("python in.py")
	elif (pilih) == '2':
		os.system("python en.py")
	elif (pilih) == '3':
		os.system("python jw.py")
	else:
		utama = False

utama = True

while utama:
	try:
		os.system("clear")
		print 69 * "*"
		os.system("figlet CYBER APPS")
		print 69 * "*"
		print "L O G I N"
		print 69 * "*"
		print "(?) user = user"
		print "(?) pass = 1234"
		print "(?) untuk keluar, tekan [CTRL]+[C]"
		print 69 * "*"
		user = raw_input("Username: ")
		pssw = raw_input("Password: ")
		print 69 * "*"
		if (user) == "user" and (pssw) == "1234":
			bhs()
		else:
			utama
	except KeyboardInterrupt:
		os.system("clear")
		raw_input("[+] TERIMA KASIH TELAH MENGGUNAKAN APLIKASI INI\n[+] TEKAN [ENTER] UNTUK KELUAR")
		utama = False

