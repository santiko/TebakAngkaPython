import random
import os

def daftar_menu():
	os.system("reset")
	print 69 * "*"
	os.system("figlet MIKIR ONGKO")
	print 69 * "*"
	print "1. NEBAK ONGKO"
	print "2. SING NGGAWE PROGRAM"
	print "3. METU"
	print 69 * "*"

def tebakAngka():
	os.system("clear")
	print 69 * "*"
	os.system("figlet NEBAK ONGKO")
	print 69 * "*"
	angka = input("\nLebokno salah siji ongko ae!\nOyot@Omahku:$ ")
	acak = random.randint(1,5)*1
	if int(angka) != acak:
		raw_input("[-] Panjenengan mboten saged nggarap!\n[-] Dipun wangsuli malih mawon..!\n[-] Ongko ingkang medal [" + str(acak) + "]\n\nPitheten [ENTER] kanggo mbaleni maneh..!")
		tebakAngka()
	elif int(angka) == " ":
		raw_input("Kudu ono isine! Ora oleh kosongan!")
	else:
		print("[+] Alhamdulillaah!\n[+] Ongko engkang medal [" + str(acak) + "]")
		tanya = raw_input("Menopo panjenengan badhe mangsuli malih [Mboten/Inggih]?\nOyot@Omahku:$ ")
		if tanya == 'Inggih' or tanya == 'inggih':
			tebakAngka()
		elif tanya == 'Mboten' or tanya == 'mboten':
			daftar_menu()
		else:
			raw_input("Angka yang Anda ketikkan tidak ada dalam daftar menu!\nSilakan ulangi lagi..!")
			tanya

def tentangProgram():
	os.system("clear")
	print 69 * "*"
	os.system("figlet PROGRAMMER")
	print 69 * "*"
	raw_input("[+] Jeneng Program: MIKIR ONGKO\n[+] Versi: 1.0.1\n[+] Programmer: SANTIKO KUSNUL HAKIM\n[+] Boso Pemrograman: PYTHON\n[+] Wektu: 7 APRIL 2018\n\nPithet [ENTER] kanggo mbaleni maneh!")
	daftar_menu()

loops = True

while loops:
	daftar_menu()
	try:
		pilih = raw_input("Oyot@Omahku:$ ")
		if (pilih) == '1':
			tebakAngka()
		elif (pilih) == '2':
			tentangProgram()
		elif (pilih) == '3':
			loops = False
			os.system("python app.py")
		else:
			raw_input("Panjenengan klintu mithet ongko!")
			daftar_menu()
			#loops = False
	except KeyboardInterrupt:
		raw_input("Panjenengan badhe medal nggeh, Pak/Bu...!\nOyot@Omahku:$ ")
		os.system("clear")
		loops = False