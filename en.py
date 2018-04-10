import random
import os

def daftar_menu():
	os.system("reset")
	print 69 * "*"
	os.system("figlet NUMBER GUESSING")
	print 69 * "*"
	print "1. GUESS 1 NUMBER"
	print "2. ABOUT PROGRAM"
	print "3. QUIT"
	print 69 * "*"

def tebakAngka():
	os.system("clear")
	print 69 * "*"
	os.system("figlet NUMBER GUESSING")
	print 69 * "*"
	angka = input("\nInput 1 number only!!\nr00t@l0calhost:$ ")
	acak = random.randint(1,5)*1
	if int(angka) != acak:
		raw_input("[-] You got failed...!\n[-] Retry again..!\n[-] The number's out is [" + str(acak) + "]\n\nPress [ENTER] to retry it..!")
		tebakAngka()
	elif int(angka) == " ":
		raw_input("It should be filled!")
	else:
		print("[+] Alhamdulillaah!\n[+] You got WIN...!\n[+] The number is [" + str(acak) + "]")
		tanya = raw_input("Do you wanna play again [Y/N]?\nr00t@l0calhost:$ ")
		if tanya == 'Y' or tanya == 'y':
			tebakAngka()
		elif tanya == 'N' or tanya == 'n':
			daftar_menu()
		else:
			raw_input("You're wrong on typing the choice!\nPlease, try again..!")
			tanya

def tentangProgram():
	os.system("clear")
	print 69 * "*"
	os.system("figlet ABOUT")
	print 69 * "*"
	raw_input("[+] Program: NUMBER GUESSING\n[+] Versi: 1.0.1\n[+] Developer: SANTIKO KUSNUL HAKIM\n[+] Programming Language: PYTHON\n[+] Date: 7 APRIL 2018\n\nPress [ENTER] to get back the main menu!")
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
			raw_input("You've pressed [ENTER] or wrong input menu number!")
			daftar_menu()
			#loops = False
	except KeyboardInterrupt:
		raw_input("Thanks for supporting my app...?\nr00t@l0calhost:$ ")
		os.system("clear")
		loops = False