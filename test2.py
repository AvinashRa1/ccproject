#!/usr/bin/python
import os
import subprocess

report_file = open("/home/avinash/Test1/report.txt", "w")

def report_head():
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

def check_avahi():
	try:
		subprocess.check_output(["pgrep", "avahi-daemon"])
		return True
	except subprocess.CalledProcessError:
		return False

def check_cups():
	try:
		subprocess.check_output(["pgrep", "cups"])
		return True
	except subprocess.CalledProcessError:
		return False

def check_dhcp():
	#status = os.system("dpkg-query -W -f='${binary:Package}\t${Status}\t${db:Status-Status}\n' isc-dhcp-server")
	result = os.system("dpkg -l | grep isc-dhcp-server > /dev/null 2>&1")
	if result == 0:
		return True
	else:
		return False

check_dhcp()

report_head()

if check_xserver():
	report_file.write("- X Windows System is installed. Proceeding to uninstall.\n")
	#subprocess.run(["apt", "purge", "xserver-xorg*"])
else:
	report_file.write("- X Windows System is not installed. No action needed.\n")

if check_avahi():
	report_file.write("- Avahi Server is installed. Proceeding to uninstall\n")
	subprocess.run(["systemctl", "stop", "avahi-daemon.service"])
	subprocess.run(["systemctl", "stop", "avahi-daemon.socket"])
	subprocess.run(["apt", "purge", "avahi-daemon"])
else:
	report_file.write("- Avahi Server is not installed. No action needed.\n")

if check_cups():
	report_file.write("- Common Unix Print System is installed. Proceeding to uninstall.\n")
	#subprocess.run(["apt", "purge", "cups"])
else:
	report_file.write("- Common Unix Print System is not installed. No action needed.\n")

if check_dhcp():
	report_file.write("- DHCP Server is installed. Proceeding to uninstall.\n")
	subprocess.run(["apt", "purge", "isc-dhcp-server"])
else:
	report_file.write("- DHCP is not installed. No action needed.\n")

report_file.close()
