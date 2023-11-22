#!/usr/bin/python
import os
import subprocess

report_file = open("/home/avinash/Test1/report.txt", "w")

def report_head():
	report_file.write("\n")
	report_file.write("-----------------------------------------------------------------------\n")
	report_file.write("                           Services Compliance                         \n")
	report_file.write("-----------------------------------------------------------------------\n")

def report_line():
	report_file.write("-----------------------------------------------------------------------\n")

def check_xserver():
	try:
		subprocess.check_output(["pgrep", "xserver-xorg*"])
		return True
	except subprocess.CalledProcessError:
		return False

def ask_xserver():
	while True:
		choice = input("The script will remove X Windows Server. Do you want to remove it y/n ")
		if choice.lower() == "y":
			return True
		elif choice.lower() == "n":
			return False
		else:
			print("Please Enter a Valid Input")

def check_avahi():
	result = os.system("dpkg -l | grep avahi-daemon > /dev/null 2>&1")
	if result == 0:
		return True
	else:
		return False

def ask_avahi():
	while True:
		choice = input("The script will remove Avahi Server. Do you want to remove it y/n ")
		if choice.lower() == "y":
			return True
		elif choice.lower() == "n":
			return False
		else:
			print("Please Enter a Valid Input")

#def check_cups(): #has issues
#	result = os.system("dpkg -l | grep cups > /dev/null 2>&1")
#	if result == 0:
#		return True
#	else:
#		return False

def check_dhcp():
	result = os.system("dpkg -l | grep isc-dhcp-server > /dev/null 2>&1")
	if result == 0:
		return True
	else:
		return False

def ask_dhcp():
	while True:
		choice = input("The script will remove DHCP Server. Do you want to remove it y/n ")
		if choice.lower() == "y":
			return True
		elif choice.lower() == "n":
			return False
		else:
			print("Please Enter a Valid Input")

def check_ldap():
	result = os.system("dpkg -l | grep slapd > /dev/null 2>&1")
	if result == 0:
		return True
	else:
		return False

def ask_ldap():
	while True:
		choice = input("The script will remove Lightweight Directory Access Protocol (LDAP). Do you want to remove it? y/n ")
		if choice.lower() == "y":
			return True
		elif choice.lower() == "n":
			return False
		else:
			print("Please Enter a Valid Input")

def check_nfs():
	result = os.system("dpkg -l | grep nfs-kernel-server > /dev/null 2>&1")
	if result == 0:
		return True
	else:
		return False

def ask_nfs():
	while True:
		choice = input("The script will remove Network File System (NFS). Do you want to remove it y/n ")
		if choice.lower() == "y":
			return True
		elif choice.lower() == "n":
			return False
		else:
			print("Please Enter a Valid Input")

def check_dns():
	try:
		subprocess.check_output(["dpkg", "-l", "bind9"], stderr=subprocess.STDOUT)
		return True
	except subprocess.CalledProcessError:
		return False

def ask_dns():
	while True:
		choice = input("The script will remove Domain Name Server (DNS). Do you want to remove it y/n ")
		if choice.lower() == "y":
			return True
		elif choice.lower() == "n":
			return False
		else:
			print("Please Enter a Valid Input")

def check_vsftpd():
	result = os.system("dpkg -l | grep vsftpd > /dev/null 2>&1")
	if result == 0:
		return True
	else:
		return False

def ask_vsftpd():
	while True:
		choice = input("The script will remove FTP Server. Do you want to remove it y/n ")
		if choice.lower() == "y":
			return True
		elif choice.lower() == "n":
			return False
		else:
			print("Please Enter a Valid Input")

def check_http():
	try:
		subprocess.check_output(["dpkg", "-l", "apache2"], stderr=subprocess.STDOUT)
		return True
	except subprocess.CalledProcessError:
		return False

def ask_http():
	while True:
		choice = input("The script will remove HTTP Server. Do you want to remove it y/n ")
		if choice.lower() == "y":
			return True
		elif choice.lower() == "n":
			return False
		else:
			print("Please Enter a Valid Input")

report_head()

if check_xserver():
	if ask_xserver():
		report_file.write("- X Windows System is installed. Proceeding to uninstall.\n")
		#subprocess.run(["apt", "purge", "xserver-xorg*"])
	else:
		report_file.write("- X Windows was not removed due to user input.\n")
else:
	report_file.write("- X Windows System is not installed. No action needed.\n")

if check_avahi():
	if ask_avahi():
		report_file.write("- Avahi Server is installed. Proceeding to uninstall\n")
		subprocess.run(["systemctl", "stop", "avahi-daemon.service"])
		subprocess.run(["systemctl", "stop", "avahi-daemon.socket"])
		subprocess.run(["apt", "purge", "avahi-daemon"])
	else:
		report_file.write("- Avahi Server was not removed due to user input.\n")
else:
	report_file.write("- Avahi Server is not installed. No action needed.\n")

#if check_cups():
#	report_file.write("- Common Unix Print System is installed. Proceeding to uninstall.\n")
	#subprocess.run(["apt", "purge", "cups"])
#else:
#	report_file.write("- Common Unix Print System is not installed. No action needed.\n")

if check_dhcp():
	if ask_dhcp():
		report_file.write("- DHCP Server is installed. Proceeding to uninstall.\n")
		subprocess.run(["apt", "purge", "isc-dhcp-server"])
	else:
		report_file.write("- DHCP Server was not removed due to user input.\n")
else:
	report_file.write("- DHCP is not installed. No action needed.\n")

if check_ldap():
	if ask_ldap():
		report_file.write("- Lightweight Directory Access Protocol is installed. Proceeding to uninstall\n")
		subprocess.run(["apt", "purge", "slapd"])
	else:
		report_file.write("- Lightweight Directory Access Protocol was not removed due to user input\n")
else:
	report_file.write("- Lightweight Directory Access Protocol is not installed. No action needed\n")

if check_nfs():
	if ask_nfs():
		report_file.write("- Network File System is installed. Proceeding to uninstall\n")
		subprocess.run(["apt", "purge", "nfs-kernel-server"])
	else:
		report_file.write("- Network File System was not removed due to user input\n")
else:
	report_file.write("- Network File System is not installed. No action needed\n")

if check_dns():
	if ask_dns():
		report_file.write("- DNS Server is installed. Proceeding to uninstall.\n")
		subprocess.run(["apt", "purge", "bind9"])
	else:
		report_file.write("- DNS Server was not removed due to user input.\n")
else:
	report_file.write("- DNS Server is not installed. No action is needed.\n")

if check_vsftpd():
	if ask_vsftpd():
		report_file.write("- FTP Server is installed. Proceeding to uninstall.\n")
		subprocess.run(["apt", "purge", "vsftpd"])
	else:
		report_file.write("- FTP Server was not removed due to user input.\n")
else:
	report_file.write("- FTP Server is not installed. No action is needed.\n")

if check_http():
	if ask_http():
		report_file.write("- HTTP Server is installed. Proceeding to uninstall.\n")
		subprocess.run(["apt", "purge", "apache2"])
	else:
		report_file.write("- HTTP Server was not removed due to user input.\n")
else:
	report_file.write("- HTTP Server is not installed. No action is needed.\n")

report_file.write("\n")

report_file.close()
