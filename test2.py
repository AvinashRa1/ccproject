#!/usr/bin/python
import os
import subprocess
import pkg_resources
import time
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

endpath = os.getcwd() + "/report.txt"
report_file = open(endpath, "w")

#Function Section

# ================================= Special Services Section ====================================

colorama_init()

def ask_choice():
	print(f"\n{Fore.RED}== Please choose one of the following scans that you wish to conduct! =={Style.RESET_ALL}\n")
	print("1 - Special Services Scan.\n")
	print("2 - Firewall Configuration Scan.\n")
	print("e - Exit Scan.\n")
	choice = input("Please enter the number of the Scan you wish to conduct: ")
	return choice

def ask_scan_type():
	print("\n================================== SCAN TYPE =====================================\n")
	print(f"{Fore.RED}== Please Choose one of the following scans that you wish to conduct! =={Style.RESET_ALL}\n")
	print("1 - Scan only if the system is Compliant.\n")
	print("2 - Conduct the Scan and make changes.\n")
	print("e - Exit the Script\n")
	choice = input("Please Enter your choice: ")
	return choice

def services_report_head():
	report_file.write("\n")
	report_file.write("====================================================================================\n")
	report_file.write("                                  Services Compliance                               \n")
	report_file.write("====================================================================================\n")

def services_output_head():
	print(f"{Fore.RED}=============================== Services Compliance =============================={Style.RESET_ALL}\n")
	report_file.write(f"{Fore.RED}=============================== Services Compliance =============================={Style.RESET_ALL}\n")

def runningservices_output_head():
	print(f"\n{Fore.RED}================================ Running Services =============================={Style.RESET_ALL}\n")
	report_file.write(f"\n{Fore.RED}================================ Running Services =============================={Style.RESET_ALL}\n")

def ask(name):
	while True:
		choice = input("The script will remove " + str(name) + " . Do you want to remove it y/n ")
		if choice.lower() == "y":
			return True
		elif choice.lower() == "n":
			return False
		else:
			print("Please enter a valid input")

# ======================================= Service Check Functions =================================

def check_xserver():
	try:
		subprocess.check_output(["pgrep", "xserver-xorg*"])
		return True
	except subprocess.CalledProcessError:
		return False

def check_avahi():
	result = os.system("dpkg -l | grep avahi-daemon > /dev/null 2>&1")
	if result == 0:
		return True
	else:
		return False

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

def check_ldap():
	result = os.system("dpkg -l | grep slapd > /dev/null 2>&1")
	if result == 0:
		return True
	else:
		return False

def check_nfs():
	result = os.system("dpkg -l | grep nfs-kernel-server > /dev/null 2>&1")
	if result == 0:
		return True
	else:
		return False

def check_dns():
	try:
		subprocess.check_output(["dpkg", "-l", "bind9"], stderr=subprocess.STDOUT)
		return True
	except subprocess.CalledProcessError:
		return False

def check_vsftpd():
	result = os.system("dpkg -l | grep vsftpd > /dev/null 2>&1")
	if result == 0:
		return True
	else:
		return False

def check_http():
	try:
		subprocess.check_output(["dpkg", "-l", "apache2"], stderr=subprocess.STDOUT)
		return True
	except subprocess.CalledProcessError:
		return False

def check_imap_pop3():
	result = os.system("dpkg -l | grep dovecot-imapd dovecot-pop3d > /dev/null 2>&1")
	if result == 0:
		return True
	else:
		return False

def check_samba():
	result = os.system("dpkg -l | grep samba > /dev/null 2>&1")
	if result == 0:
		return True
	else:
		return False

def check_squid():
	result = os.system("dpkg -l | grep squid > /dev/null 2>&1")
	if result == 0:
		return True
	else:
		return False

def check_snmp():
	result = os.system("dpkg -l | grep snmpd > /dev/null 2>&1")
	if result == 0:
		return True
	else:
		return False

def check_nis():
	result = os.system("dpkg -l | grep -w nis > /dev/null 2>&1")
	if result == 0:
		return True
	else:
		return False

def check_dnsmasq():
	result = os.system("dpkg -l | grep dnsmasq > /dev/null 2>&1")
	if result == 0:
		return True
	else:
		return False

def check_rsync():
	result = os.system("dpkg -l | grep rsync > /dev/null 2>&1")
	if result == 0:
		return True
	else:
		return False

# ======================================= Service Scan Functions =================================

def scan_xserver():
	if check_xserver():
		print(f"- X Windows System is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
		report_file.write(f"\n- X Windows System is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
	else:
		print("- X Windows System is not installed. No action is needed.\n")
		report_file.write("\n- X Windows Systtem is not install. No action is needed.\n")

def scan_avahi():
	if check_avahi():
		print(f"- Avahi Server is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
		report_file.write(f"\n- Avahi Server is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
	else:
		print("- Avahi Server is not installed. No action is needed.\n")
		report_file.write("\n- Avahi Server is not installed. No action is needed.\n")

def scan_dhcp():
	if check_dhcp():
		print(f"- DHCP Server is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
		report_file.write(f"\n- DHCP Server is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
	else:
		print("- DHCP Server is not installed. No action is needed.\n")
		report_file.write("\n- DHCP Server is not installed. No action is needed.\n")
	
def scan_ldap():
	if check_ldap():
		print(f"- Lightweight Directory Access Protocol is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
		report_file.write(f"\n- Lightweight Directory Access Protocol is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
	else:
		print("- Lightweight Directory Access Protocol is not installed. No action is needed.\n")
		report_file.write("\n- Lightweight Directory Access Protocol is not installed. No action is needed.\n")

def scan_nfs():
	if check_nfs():
		print(f"- Network File System is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
		report_file.write(f"\n- Network File System is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
	else:
		print("- Network File System is not installed. No action is needed.\n")
		report_file.write("\n- Network File System is not installed. No action is needed.\n")

def scan_dns():
	if check_dns():
		print(f"- DNS Server is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
		report_file.write(f"\n- DNS Server is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
	else:
		print("- DNS Server is not installed. No action is needed.\n")
		report_file.write("\n- DNS Server is not installed. No action is needed.\n")

def scan_vsftpd():
	if check_vsftpd():
		print(f"- FTP Server is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
		report_file.write(f"\n- FTP Server is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
	else:
		print("- FTP Server is not installed. No action is needed.\n")
		report_file.write("\n- FTP Server is not installed. No action is needed.\n")

def scan_http():
	if check_http():
		print(f"- HTTP Server is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
		report_file.write(f"\n- HTTP Server is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
	else:
		print("- HTTP Server is not installed. No action is needed.\n")
		report_file.write("\n- HTTP Server is not installed. No action is needed.\n")

def scan_imap_pop3():
	if check_imap_pop3():
		print(f"- IMAP and POP3 is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
		report_file.write(f"\n- IMAP and POP3 is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
	else:
		print("- IMAP and POP3 is not installed. No action is needed.\n")
		report_file.write("\n- IMAP and POP3 is not installed. No action is needed.\n")

def scan_samba():
	if check_samba():
		print(f"- Samba Server is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
		report_file.write(f"\n- Samba Server is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
	else:
		print("- Samba Server is not installed. No action is needed.\n")
		report_file.write("\n- Samba Server is not installed. No action is needed.\n")

def scan_squid():
	if check_squid():
		print(f"- HTTP Proxy Server is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
		report_file.write(f"\n- HTTP Proxy Server is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
	else:
		print("- HTTP Proxy Server is not installed. No action is needed.\n")
		report_file.write("\n- HTTP Proxy Server is not installed. No action is needed.\n")

def scan_snmp():
	if check_snmp():
		print(f"- SNMP Server is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
		report_file.write(f"\n- SNMP Server is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
	else:
		print("- SNMP Server is not installed. No action is needed.\n")
		report_file.write("\n- SNMP Server is not installed. No action is needed.\n")

def scan_nis():
	if check_nis():
		print(f"- NIS Server is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
		report_file.write(f"\n- NIS Server is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
	else:
		print("- NIS Server is not installed. No action is needed.\n")
		report_file.write("\n- NIS Server is not installed. No action is needed.\n")

def scan_dnsmasq():
	if check_dnsmasq():
		print(f"- DNSMASQ is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
		report_file.write(f"\n- DNSMASQ is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
	else:
		print("- DNSMASQ is not installed. No action is needed.\n")
		report_file.write("\n- DNSMASQ is not installed. No action is needed.\n")

def scan_rsync():
	if check_rsync():
		print(f"- Rsync is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
		report_file.write(f"\n- Rsync is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
	else:
		print("- Rsync is not installed. No action is needed.\n")
		report_file.write("\n- Rsync is not installed. No action is needed.\n")

def scan_rsh():
	if check_rsh():
		print(f"- Rsh Client is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
		report_file.write(f"\n- Rsh Client is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
	else:
		print("- Rsh Client is not installed. No action is needed.\n")
		report_file.write("\n- Rsh Client is not installed. No action is needed.\n")

def scan_talk():
	if check_talk():
		print(f"- Talk Client is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
		report_file.write(f"\n- Talk Client is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
	else:
		print("- Talk Client is not installed. No action is needed.\n")
		report_file.write("\n- Talk Client is not installed. No action is needed.\n")

def scan_telnet():
	if check_telnet():
		print(f"- Telnet Client is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
		report_file.write(f"\n- Telnet Client is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
	else:
		print("- Telnet Client is not installed. No action is needed.\n")
		report_file.write("\n- Telnet Client is not installed. No action is needed.\n")

def scan_ldap_utils():
	if check_ldap_utils():
		print(f"- LDAP Client is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
		report_file.write(f"\n- LDAP Client is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
	else:
		print("- LDAP Client is not installed. No action is needed.\n")
		report_file.write("\n- LDAP Client is not installed. No action is needed.\n")

def scan_rpcbind():
	if check_rpcbind():
		print(f"- RPC Client is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
		report_file.write(f"\n- RPC Client is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
	else:
		print("- RPC Client is not installed. No action is needed.\n")
		report_file.write("\n- RPC Client is not installed. No action is needed.\n")

# ======================================= Service Purge Functions =================================

def purge_xserver():
	if check_xserver():
		if ask("X Windows System"):
			print(f"- X Windows System is installed.{Fore.RED} Proceeding to uninstall...{Style.RESET_ALL}\n")
			report_file.write(f"\n- X Windows System is installed.{Fore.RED} Proceeding to uninstall.{Style.RESET_ALL}\n")
			os.system("apt purge xserver-xorg*")
		else:
			print("\n- X Windows was not removed due to user input.\n")
			report_file.write("\n- X Windows was not removed due to user input.\n")
	else:
		print("- X Windows System is not installed. No action needed.\n")
		report_file.write("\n- X Windows System is not installed. No action needed.\n")

def purge_avahi():
	if check_avahi():
		if ask("Avahi Server"):
			print(f"- Avahi Server is installed.{Fore.RED} Proceeding to uninstall...{Style.RESET_ALL}\n")
			report_file.write(f"\n- Avahi Server is installed.{Fore.RED} Proceeding to uninstall...{Style.RESET_ALL}\n")
			os.system("systemctl stop avahi-daemon.service")
			os.system("systemctl stop avahi-daemon.socket")
			os.system("apt purge avahi-daemon")
		else:
			print("\n- Avahi Server was not removed due to user input.\n")
			report_file.write("\n- Avahi Server was not removed due to user input.\n")
	else:
		print("- Avahi Server is not installed. No action needed.\n")
		report_file.write("\n- Avahi Server is not installed. No action needed.\n")

def purge_dhcp():
	if check_dhcp():
		if ask("DHCP Server"):
			print(f"- DHCP Server is installed.{Fore.RED} Proceeding to uninstall...{Style.RESET_ALL}\n")
			report_file.write(f"\n- DHCP Server is installed.{Fore.RED} Proceeding to uninstall...{Style.RESET_ALL}.\n")
			os.system("apt purge isc-dhcp-server")
		else:
			print("\n- DHCP Server was not removed due to user input.\n")
			report_file.write("\n- DHCP Server was not removed due to user input.\n")
	else:
		print("- DHCP Server is not installed. No action needed.\n")
		report_file.write("\n- DHCP is not installed. No action needed.\n")

def purge_ldap():
	if check_ldap():
		if ask("Lightweight Directory Acesss Protocol"):
			print(f"- Lightweight Directory Access Protocol is installed.{Fore.RED} Proceeding to uninstall...{Style.RESET_ALL}\n")
			report_file.write(f"\n- Lightweight Directory Access Protocol is installed.{Fore.RED} Proceeding to uninstall...{Style.RESET_ALL}\n")
			os.system("apt purge slapd")
		else:
			print("\n- Lightweight Directory Access Protocl was not removed due to user input.\n")
			report_file.write("\n- Lightweight Directory Access Protocol was not removed due to user input\n")
	else:
		print("- Lightweight Directory Access Protcol is not installed. No action is needed.\n")
		report_file.write("\n- Lightweight Directory Access Protocol is not installed. No action needed\n")

def purge_nfs():
	if check_nfs():
		if ask("Network File System"):
			print(f"- Network File System is installed.{Fore.RED} Proceeding to uninstall...{Style.RESET_ALL}\n")
			report_file.write(f"\n- Network File System is installed.{Fore.RED} Proceeding to uninstall...{Style.RESET_ALL}\n")
			os.system("apt purge nfs-kernel-server")
		else:
			print("\n- Network File System is installed. Proceeding to uninstall...\n")
			report_file.write("\n- Network File System was not removed due to user input\n")
	else:
		print("- Network File System is not installed. No action needed\n")
		report_file.write("\n- Network File System is not installed. No action needed\n")

def purge_dns():
	if check_dns():
		if ask("DNS Server"):
			print(f"- DNS Server is installed.{Fore.RED} Proceeding to uninstall...{Style.RESET_ALL}\n")
			report_file.write(f"\n- DNS Server is installed.{Fore.RED} Proceeding to uninstall...{Style.RESET_ALL}\n")
			os.system("apt purge bind9")
		else:
			print("\n- DNS Server was not removed due to user input.\n")
			report_file.write("\n- DNS Server was not removed due to user input.\n")
	else:
		print("- DNS Server is not installed. No action is needed.\n")
		report_file.write("\n- DNS Server is not installed. No action is needed.\n")

def purge_vsftpd():
	if check_vsftpd():
		if ask("FTP Server"):
			print(f"- FTP Server is installed.{Fore.RED} Proceeding to uninstall...{Style.RESET_ALL}\n")
			report_file.write(f"\n- FTP Server is installed.{Fore.RED} Proceeding to uninstall...{Style.RESET_ALL}\n")
			os.system("apt purge vsftpd")
		else:
			print("\n- FTP Server was not removed due to user input.\n")
			report_file.write("\n- FTP Server was not removed due to user input.\n")
	else:
		print("- FTP Server is not installed. No action is needed.\n")
		report_file.write("\n- FTP Server is not installed. No action is needed.\n")

def purge_http():
	if check_http():
		if ask("HTTP Server"):
			print(f"- HTTP Server is installed,{Fore.RED} Proceeding to uninstall...{Style.RESET_ALL}\n")
			report_file.write(f"\n- HTTP Server is installed.{Fore.RED} Proceeding to uninstall...{Style.RESET_ALL}\n")
			os.system("apt purge apache2")
		else:
			print("\n- HTTP Server was not removed due to user input.\n")
			report_file.write("\n- HTTP Server was not removed due to user input.\n")
	else:
		print("- HTTP Server is not installed. No action is needed.\n")
		report_file.write("\n- HTTP Server is not installed. No action is needed.\n")

def purge_imap_pop3():
	if check_imap_pop3():
		if ask("IMAP and POP3"):
			print(f"- IMAP and POP3 is installed.{Fore.RED} Proceeding to uninstall...{Style.RESET_ALL}\n")
			report_file.write(f"\n- IMAP and POP3 is installed.{Fore.RED} Proceeding to uninstall...{Style.RESET_ALL}\n")
			os.system("apt purge dovecot-impad dovecot-pop3d")
		else:
			print("\n- IMAP and POP3 was not removed due to user input.\n")
			report_file.write("\n- IMAP and POP3 was not removed due to user input.\n")
	else:
		print("- IMAP and POP3 is not installed. No action needed.\n")
		report_file.write("\n- IMAP and POP3 is not installed. No action needed.\n")

def purge_samba():
	if check_samba():
		if ask("Samba Server"):
			print(f"- Samba Server is installed.{Fore.RED} Proceeding to uninstall...{Style.RESET_ALL}\n")
			report_file.write(f"\n- Samba Server is installed.{Fore.RED} Proceeding to uninstall...{Style.RESET_ALL}\n")
			os.system("apt purge samba")
		else:
			print("\n- Samba Server not removed due to user input.\n")
			report_file.write("\n- Samba was not removed due to user input.\n")
	else:
		print("- X Samba Server is not installed. No action needed.\n")
		report_file.write("\n- Samba Server is not installed. No action needed.\n")

def purge_squid():
	if check_squid():
		if ask("HTTP Proxy Server"):
			print(f"- HTTP Proxy Server is installed.{Fore.RED} Proceeding to uninstall...{Style.RESET_ALL}\n")
			report_file.write(f"\n- HTTP Proxy Server is installed.{Fore.RED} Proceeding to uninstall...{Style.RESET_ALL}\n")
			os.system("apt purge squid")
		else:
			print("\n- HTTP Proxy Server not removed due to user input.\n")
			report_file.write("\n- HTTP Proxy Server was not removed due to user input.\n")
	else:
		print("- HTTP Proxy Server is not installed. No action needed.\n")
		report_file.write("\n- HTTP Proxy Server is not installed. No action needed.\n")

def purge_snmp():
	if check_snmp():
		if ask("SNMP Server"):
			print(f"- SNMP Server is installed.{Fore.RED} Proceeding to uninstall...{Style.RESET_ALL}\n")
			report_file.write(f"\n- SNMP Server is installed.{Fore.RED} Proceeding to uninstall...{Style.RESET_ALL}\n")
			os.system("apt purge snmpd")
		else:
			print("\n- SNMP Server not removed due to user input.\n")
			report_file.write("\n- SNMP Server was not removed due to user input.\n")
	else:
		print("- SNMP Server is not installed. No action needed.\n")
		report_file.write("\n- SNMP Server is not installed. No action needed.\n")

def purge_nis():
	if check_nis():
		if ask("NIS Server"):
			print(f"- NIS Server is installed.{Fore.RED} Proceeding to uninstall...{Style.RESET_ALL}\n")
			report_file.write(f"\n- NIS Server is installed.{Fore.RED} Proceeding to uninstall...{Style.RESET_ALL}\n")
			os.system("apt purge nis")
		else:
			print("\n- NIS Server not removed due to user input.\n")
			report_file.write("\n- NIS Server was not removed due to user input.\n")
	else:
		print("- NIS Server is not installed. No action needed.\n")
		report_file.write("\n- NIS Server is not installed. No action needed.\n")

def purge_dnsmasq():
	if check_dnsmasq():
		if ask("DNSMASQ"):
			print(f"- DNSMASQ is installed.{Fore.RED} Proceeding to uninstall...{Style.RESET_ALL}\n")
			report_file.write(f"\n- DNSMASQ is installed.{Fore.RED} Proceeding to uninstall...{Style.RESET_ALL}\n")
			os.system("apt purge dnsmasq-base")
		else:
			print("\n- DNSMASQ not removed due to user input.\n")
			report_file.write("\n- DNSMASQ was not removed due to user input.\n")
	else:
		print("- DNSMASQ is not installed. No action needed.\n")
		report_file.write("\n- DNSMASQ is not installed. No action needed.\n")

def purge_rsync():
	if check_rsync():
		if ask("Rsync"):
			print(f"- Rsync is installed.{Fore.RED} Proceeding to uninstall...{Style.RESET_ALL}\n")
			report_file.write(f"\n- Rsync is installed{Fore.RED} Proceeding to uninstall...{Style.RESET_ALL}\n")
			os.system("apt purge rsync")
		else:
			print("\n- Rsync not removed due to user input.\n")
			report_file.write("\n- Rsync was not removed due to user input.\n")
	else:
		print("- Rsync is not installed. No action needed.\n")
		report_file.write("\n- Rsync is not installed. No action needed.\n")

# ======================================= Service Clients Check Section ================================

def check_rsh():
	result = os.system("dpkg -l | grep rsh-client > /dev/null 2>&1")
	if result == 0:
		return True
	else:
		return False

def check_talk():
	result = os.system("dpkg -s talk > /dev/null 2>&1")
	if result == 0:
		return True
	else:
		return False

def check_telnet():
	result = os.system("dpkg -l | grep telnet > /dev/null 2>&1")
	if result == 0:
		return True
	else:
		return False

def check_ldap_utils():
	result = os.system("dpkg -l | grep ldap-utils > /dev/null 2>&1")
	if result == 0:
		return True
	else:
		return False

def check_rpcbind():
	result = os.system("dpkg -l | grep rpcbind > /dev/null 2>&1")
	if result == 0:
		return True
	else:
		return False

# ======================================= Service Clients Purge Section ================================

def purge_rsh():
	if check_rsh():
		if ask("Rsh Client"):
			print(f"- Rsh Client is installed.{Fore.RED} Proceeding to uninstall...{Style.RESET_ALL}\n")
			report_file.write(f"\n- Rsh Client is installed.{Fore.RED} Proceeding to uninstall...{Style.RESET_ALL}\n")
			os.system("apt purge rsh-client")
		else:
			print("\n- Rsh Client not removed due to user input.\n")
			report_file.write("\n- Rsh Client was not removed due to user input.\n")
	else:
		print("- Rsh Client is not installed. No action needed.\n")
		report_file.write("\n- Rsh Client is not installed. No action needed.\n")

def purge_talk():
	if check_talk():
		if ask("Talk Client"):
			print(f"- Talk Client is installed.{Fore.RED} Proceeding to uninstall...{Style.RESET_ALL}\n")
			report_file.write(f"\n- Talk Client is installed.{Fore.RED} Proceeding to uninstall...{Style.RESET_ALL}\n")
			os.system("apt purge talk")
		else:
			print("\n- Talk Client not removed due to user input.\n")
			report_file.write("\n- Talk Client was not removed due to user input.\n")
	else:
		print("- Talk Client is not installed. No action needed.\n")
		report_file.write("\n- Talk Client is not installed. No action needed.\n")

def purge_telnet():
	if check_telnet():
		if ask("Telnet Client"):
			print(f"- Telnet Client is installed.{Fore.RED} Proceeding to uninstall...{Style.RESET_ALL}\n")
			report_file.write(f"\n- Telnet Client is installed.{Fore.RED} Proceeding to uninstall...{Style.RESET_ALL}\n")
			os.system("apt purge telnet")
		else:
			print("\n- Telnet Client not removed due to user input.\n")
			report_file.write("\n- Telnet Client was not removed due to user input.\n")
	else:
		print("- Telnet Client is not installed. No action needed.\n")
		report_file.write("\n- Telnet Client is not installed. No action needed.\n")

def purge_ldap_utils():
	if check_ldap_utils():
		if ask("LDAP Client"):
			print(f"- LDAP Client is installed.{Fore.RED} Proceeding to uninstall...{Style.RESET_ALL}\n")
			report_file.write(f"\n- LDAP Client is installed.{Fore.RED} Proceeding to uninstall...{Style.RESET_ALL}\n")
			os.system("apt purge ldap-utils")
		else:
			print("\n- LDAP Client not removed due to user input.\n")
			report_file.write("\n- LDAP Client was not removed due to user input.\n")
	else:
		print("- LDAP Client is not installed. No action needed.\n")
		report_file.write("\n- LDAP Client is not installed. No action needed.\n")

def purge_rpcbind():
	if check_rpcbind():
		if ask("RPC Client"):
			print(f"- RPC Client is installed.{Fore.RED} Proceeding to uninstall...{Style.RESET_ALL}\n")
			report_file.write(f"\n- RPC Client is installed.{Fore.RED} Proceeding to uninstall...{Style.RESET_ALL}\n")
			os.system("apt purge rpcbind")
		else:
			print("\n- RPC Client not removed due to user input.\n")
			report_file.write("\n- RPC Client was not removed due to user input.\n")
	else:
		print("- RPC Client is not installed. No action needed.\n")
		report_file.write("\n- RPC Client is not installed. No action needed.\n")

# ======================================= Running Services Check Section ================================

def check_non_services():
	command = "ss -ltr"
	result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, text=True)

	if result.returncode == 0:
		lines = result.stdout.splitlines()

		print(lines[0])

		for index, line in enumerate(lines[1:], start=1):
			print(f"Index {index}: {line}")
			report_file.write(f"Index {index}: {line}\n")
	else:
		print(f"Error running command: {result.stderr}")
	print("\n")

def report_int():
	print(f"{Fore.RED} = Please Use the Command 'cat report.txt | less' when viewing the report! = {Style.RESET_ALL}\n")

# ==================================== Firewall Configuration Section ==============================



# ============================================ Main Functions ======================================

def scan_actions():
	services_report_head()
	services_output_head()
	time.sleep(1)
	scan_xserver()
	time.sleep(1)
	scan_avahi()
	time.sleep(1)
	scan_dhcp()
	time.sleep(1)
	scan_ldap()
	time.sleep(1)
	scan_nfs()
	time.sleep(1)
	scan_dns()
	time.sleep(1)
	scan_vsftpd()
	time.sleep(1)
	scan_http()
	time.sleep(1)
	scan_imap_pop3()
	time.sleep(1)
	scan_samba()
	time.sleep(1)
	scan_squid()
	time.sleep(1)
	scan_snmp()
	time.sleep(1)
	scan_nis()
	time.sleep(1)
	scan_dnsmasq()
	time.sleep(1)
	scan_rsync()
	time.sleep(1)
	scan_rsh()
	time.sleep(1)
	scan_talk()
	time.sleep(1)
	scan_telnet()
	time.sleep(1)
	scan_ldap_utils()
	time.sleep(1)
	scan_rpcbind()
	time.sleep(1)

def purge_actions():
	services_report_head()
	services_output_head()
	time.sleep(1)
	purge_xserver()
	time.sleep(1)
	purge_avahi()
	time.sleep(1)
	purge_dhcp()
	time.sleep(1)
	purge_ldap()
	time.sleep(1)
	purge_nfs()
	time.sleep(1)
	purge_dns()
	time.sleep(1)
	purge_vsftpd()
	time.sleep(1)
	purge_http()
	time.sleep(1)
	purge_imap_pop3()
	time.sleep(1)
	purge_samba()
	time.sleep(1)
	purge_squid()
	time.sleep(1)
	purge_snmp()
	time.sleep(1)
	purge_nis()
	time.sleep(1)
	purge_dnsmasq()
	time.sleep(1)
	purge_rsync()
	time.sleep(1)
	purge_rsh()
	time.sleep(1)
	purge_talk()
	time.sleep(1)
	purge_telnet()
	time.sleep(1)
	purge_ldap_utils()
	time.sleep(1)
	purge_rpcbind()
	time.sleep(1)

def running_services_action():
	runningservices_output_head()
	time.sleep(1)
	check_non_services()

def services_purge_main():
	purge_actions()
	running_services_action()
	report_int()
	report_file.write("\n")

def services_scan_main():
	scan_actions()
	running_services_action()
	report_int()
	report_file.write("\n")

def option():
	while True:
		choice = ask_choice()
		if choice == "1":
			while True:
				conf_choice = input("\nYou have chosen Special Services. Are you Sure? y/n ")
				if conf_choice.lower() == "y":
					print("\nYou have chosen Special Services Scan. Proceeding with scan...\n")
					services_purge_main()
					return True
				elif conf_choice.lower() == "n":
					print("\nYou have canceled your action.\n")
					return False
				else:
					print("\nPLEASE ENTER A VALID INPUT")
		elif choice == "2":
			while True:
				conf_choice = input("\nYou have chosen Firewall. Are you sure? y/n ")
				if conf_choice.lower() == "y":
					print("\nYou have chosen Firewall Scan. Proceeding with scan.../n")

					#Firewall Main goes here

					return True
				elif conf_choice.lower() == "n":
					print("\n You have canceled your action.\n")
					return False
				else:
					print("\nPLEASE ENTER A VALID INPUT")
		elif choice.lower() == "e":
			print("\nYou have exited the script :( \n")
			return True
		else:
			print(f"{Fore.RED}PLEASE ENTER A VALID INPUT.{Style.RESET_ALL}\n")

def scan_type():
	while True:
		choice = ask_scan_type()
		if choice == "1":
			while True:
				conf_choice = input("\nYou have chosen only the Compliance Scan. Are you Sure? y/n ")
				if conf_choice.lower() == "y":
					print("\nYou have chosen the Compliance Scan. Proceeding with scan...\n")
					services_scan_main()
					return True
				elif conf_choice.lower() == "n":
					print("\nYou have canceled your action.\n")
					return False
				else:
					print("\nPLEASE ENTER A VALID INPUT\n")
		elif choice == "2":
			while True:
				conf_choice = input("\nYou have chosen only the Practical Scan. Are you Sure? y/n ")
				if conf_choice.lower() == "y":
					print("\nYou have chosen the Practical Scan. Proceeding with scan...\n")
					option()
					return True
				elif conf_choice.lower() == "n":
					print("\nYou have canceled your action.\n")
					return False
				else:
					print("\nPLEASE ENTER A VALID INPUT\n")
		elif choice.lower() == "e":
			print("\nYou have exited the script :( \n")
			return True
		else:
			print(f"{Fore.RED}PLEASE ENTER A VALID INPUT.{Style.RESET_ALL}\n")


scan_type()

report_file.close()

# ============================================ End of Script ======================================