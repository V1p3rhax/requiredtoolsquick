import os 
import time
import os.path
from os import path
input('''
Script must be ran as root.

This will install files in your current directory. Move to a directory you want files to be installed to and execute this script again.

Press Enter to continue...
''')
delete = input("Do you want to uninstall unecessary applications as well? Y/n:")

if delete == 'Y' or delete == 'y':
	os.system("sudo apt autoremove thunderbird -y")
	os.system("clear")
	os.system("sudo apt-get remove --purge libreoffice-common -y")
	os.system("clear")
	os.system("sudo apt-get remove gnome-mines -y")
	os.system("clear")
	os.system("sudo apt-get remove gnome-mahjongg -y")
	os.system("clear")
	os.system("sudo apt-get remove gnome-sudoku -y")
	os.system("clear")
	os.system("sudo apt-get remove gnome-calculator -y")
	os.system("clear")
	os.system("sudo apt-get remove cheese-common -y")
	os.system("clear")
	os.system("sudo apt-get remove cheese -y")
	os.system("clear")
	os.system("sudo apt-get remove gedit -y")
	os.system("clear")
	os.system("sudo apt-get remove gedit-common -y")
	os.system("clear")
	os.system("sudo apt-get remove gnome-todo -y")
	os.system("clear")
	os.system("sudo apt-get remove gnome-todo-common -y")
elif delete == 'N' or delete == 'n':
	print("no tools have been uninstalled if you want to uninstall run script again")
if path.exists("PhantomsecSpammer"):
	print("PhantomsecSpammer is already installed")

else:
	os.system('git clone https://github.com/anoncfw/PhantomsecSpammer')
	os.system('clear')
	print("installed Phantomsec Spammer Made By V1p3rhax")
	time.sleep(1)
if path.exists("/usr/share/doc/hexchat"):
	print("HexChat is already isntalled")
	
else:
	os.system('sudo apt-get install hexchat')
	os.system('clear')
	print('Installed hex chat')
	time.sleep(1)
if path.exists("/usr/bin/stegosuite"):
	print("stegosuite is already installed")

else:
	os.system('sudo apt-get install stegosuite')
	os.system('clear')
	print('Installed stegosuite')
if path.exists("msfinstall"):
	print("msfinstall is already downloaded")
else:
	os.system('git clone https://github.com/rapid7/metasploit-framework/wiki/Nightly-Installers')
	os.system('clear')
	print('msfvenom downloaded manual install reguired run ./msfvenom after script is done')
if path.exists("/usr/share/code"):
	print("visual studio code is already installed")
else:
	os.system("sudo apt install software-properties-common apt-transport-https wget -y")
	time.sleep(20)
	os.system("clear")
	os.system("sudo apt install code")
	os.system("clear")
	print("visual studio installed")
if path.exists("/bin/nano"):
	print("nano is already installed")
else:
	os.system("sudo apt-get install nano")
	print("nano installed")
	
if path.exists("/etc/openvpn"):
	print("openvpn already installed")
else:
	os.system("sudo apt-get install openvpn")

