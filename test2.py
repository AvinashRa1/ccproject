#!/usr/bin/python
import os
import re
import subprocess
import pkg_resources
import time
from datetime import datetime
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

scan_endpath = os.getcwd() + "/scanReport.txt"
comp_endpath = os.getcwd() + "/compReport.txt"

scan_report_file = open(scan_endpath, "w")
report_file = open(comp_endpath, "w")

#Function Section

def banner():
    print("""\033[94m
        |  ____  _              _______ _     _                |
        | |  _ \| |            |__   __| |   (_)               |
        | | |_) | |_   _  ___     | |  | |__  _ _ __   __ _    |
        | |  _ <| | | | |/ _ \    | |  | '_ \| | '_ \ / _` |   |
        \ | |_) | | |_| |  __/    | |  | | | | | | | | (_| |   /
        | |____/|_|\__,_|\___|    |_|  |_| |_|_|_| |_|\__, |   |
        |                                               __/|   |
        |                                              |___/   |
    \033[91m""")

def y_n_choice():
    while True:
        try:
            user_input = input("Enter 'yes' to continue or 'no' to skip: ")

            if user_input is None:
                print("Error: Result is None.")
                return

            user_input = user_input.lower()
            if user_input not in ['yes', 'y', 'no', 'n', '']:
                raise ValueError("Invalid input, please enter 'yes' or 'no'.")

            return user_input
        except ValueError as ve:
            print("Error:", ve)
        except TypeError as ve:
            print("Error:", ve)
        except AttributeError as ve:
            print("Error:", ve)

# ================================= Special Services Section ====================================

colorama_init()

def ask_choice():
	print(f"\n{Fore.RED}== Please choose one of the following scans that you wish to conduct! =={Style.RESET_ALL}\n")
	print("1 - All Benchmark Scan.\n")
	print("2 - Special Services Scan.\n")
	print("3 - Firewall Configuration Scan.\n")
	print("b - Go Back.\n")
	print("e - Exit Scan.\n")
	choice = input("Please enter the number of the Scan you wish to conduct: ")
	return choice

def ask_scan_type():
	print("\n================================== SCAN TYPE =====================================\n")
	print(f"{Fore.RED}== Please Choose one of the following scans that you wish to conduct! =={Style.RESET_ALL}\n")
	print("1 - All Benchmark Scan.\n")
	print("2 - Scan only if the system is Compliant.\n")
	print("3 - Conduct the Scan and make changes.\n")
	print("e - Exit the Script\n")
	choice = input("Please Enter your choice: ")
	return choice

def services_report_head():
	report_file.write("\n")
	report_file.write("====================================================================================\n")
	report_file.write("                                  Services Compliance                               \n")
	report_file.write("====================================================================================\n")

def scan_services_report_head():
	scan_report_file.write("\n")
	scan_report_file.write("====================================================================================\n")
	scan_report_file.write("                                  Services Scan                                     \n")
	scan_report_file.write("====================================================================================\n")

def services_output_head():
	print(f"{Fore.RED}=============================== Services Compliance =============================={Style.RESET_ALL}\n")

def scan_services_output_head():
	print(f"{Fore.RED}=============================== Services Scan =============================={Style.RESET_ALL}\n")

def runningservices_output_head():
	print(f"\n{Fore.RED}================================ Running Services =============================={Style.RESET_ALL}\n")
	report_file.write(f"\n{Fore.RED}================================ Running Services =============================={Style.RESET_ALL}\n")

def scan_runningservices_output_head():
	print(f"\n{Fore.RED}================================ Running Services =============================={Style.RESET_ALL}\n")
	scan_report_file.write(f"\n{Fore.RED}================================ Running Services =============================={Style.RESET_ALL}\n")

def ask(name):
	while True:
		choice = input(f"The script will remove {Fore.RED} " + str(name) + f"{Style.RESET_ALL} . Do you want to remove it y/n ")
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
		scan_report_file.write(f"\n- X Windows System is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
	else:
		print("- X Windows System is not installed. No action is needed.\n")
		scan_report_file.write("\n- X Windows Systtem is not install. No action is needed.\n")

def scan_avahi():
	if check_avahi():
		print(f"- Avahi Server is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
		scan_report_file.write(f"\n- Avahi Server is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
	else:
		print("- Avahi Server is not installed. No action is needed.\n")
		scan_report_file.write("\n- Avahi Server is not installed. No action is needed.\n")

def scan_dhcp():
	if check_dhcp():
		print(f"- DHCP Server is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
		scan_report_file.write(f"\n- DHCP Server is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
	else:
		print("- DHCP Server is not installed. No action is needed.\n")
		scan_report_file.write("\n- DHCP Server is not installed. No action is needed.\n")
	
def scan_ldap():
	if check_ldap():
		print(f"- Lightweight Directory Access Protocol is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
		scan_report_file.write(f"\n- Lightweight Directory Access Protocol is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
	else:
		print("- Lightweight Directory Access Protocol is not installed. No action is needed.\n")
		scan_report_file.write("\n- Lightweight Directory Access Protocol is not installed. No action is needed.\n")

def scan_nfs():
	if check_nfs():
		print(f"- Network File System is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
		scan_report_file.write(f"\n- Network File System is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
	else:
		print("- Network File System is not installed. No action is needed.\n")
		scan_report_file.write("\n- Network File System is not installed. No action is needed.\n")

def scan_dns():
	if check_dns():
		print(f"- DNS Server is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
		scan_report_file.write(f"\n- DNS Server is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
	else:
		print("- DNS Server is not installed. No action is needed.\n")
		scan_report_file.write("\n- DNS Server is not installed. No action is needed.\n")

def scan_vsftpd():
	if check_vsftpd():
		print(f"- FTP Server is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
		scan_report_file.write(f"\n- FTP Server is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
	else:
		print("- FTP Server is not installed. No action is needed.\n")
		scan_report_file.write("\n- FTP Server is not installed. No action is needed.\n")

def scan_http():
	if check_http():
		print(f"- HTTP Server is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
		scan_report_file.write(f"\n- HTTP Server is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
	else:
		print("- HTTP Server is not installed. No action is needed.\n")
		scan_report_file.write("\n- HTTP Server is not installed. No action is needed.\n")

def scan_imap_pop3():
	if check_imap_pop3():
		print(f"- IMAP and POP3 is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
		scan_report_file.write(f"\n- IMAP and POP3 is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
	else:
		print("- IMAP and POP3 is not installed. No action is needed.\n")
		scan_report_file.write("\n- IMAP and POP3 is not installed. No action is needed.\n")

def scan_samba():
	if check_samba():
		print(f"- Samba Server is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
		scan_report_file.write(f"\n- Samba Server is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
	else:
		print("- Samba Server is not installed. No action is needed.\n")
		scan_report_file.write("\n- Samba Server is not installed. No action is needed.\n")

def scan_squid():
	if check_squid():
		print(f"- HTTP Proxy Server is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
		scan_report_file.write(f"\n- HTTP Proxy Server is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
	else:
		print("- HTTP Proxy Server is not installed. No action is needed.\n")
		scan_report_file.write("\n- HTTP Proxy Server is not installed. No action is needed.\n")

def scan_snmp():
	if check_snmp():
		print(f"- SNMP Server is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
		scan_report_file.write(f"\n- SNMP Server is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
	else:
		print("- SNMP Server is not installed. No action is needed.\n")
		scan_report_file.write("\n- SNMP Server is not installed. No action is needed.\n")

def scan_nis():
	if check_nis():
		print(f"- NIS Server is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
		scan_report_file.write(f"\n- NIS Server is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
	else:
		print("- NIS Server is not installed. No action is needed.\n")
		scan_report_file.write("\n- NIS Server is not installed. No action is needed.\n")

def scan_dnsmasq():
	if check_dnsmasq():
		print(f"- DNSMASQ is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
		scan_report_file.write(f"\n- DNSMASQ is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
	else:
		print("- DNSMASQ is not installed. No action is needed.\n")
		scan_report_file.write("\n- DNSMASQ is not installed. No action is needed.\n")

def scan_rsync():
	if check_rsync():
		print(f"- Rsync is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
		scan_report_file.write(f"\n- Rsync is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
	else:
		print("- Rsync is not installed. No action is needed.\n")
		scan_report_file.write("\n- Rsync is not installed. No action is needed.\n")

def scan_rsh():
	if check_rsh():
		print(f"- Rsh Client is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
		scan_report_file.write(f"\n- Rsh Client is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
	else:
		print("- Rsh Client is not installed. No action is needed.\n")
		scan_report_file.write("\n- Rsh Client is not installed. No action is needed.\n")

def scan_talk():
	if check_talk():
		print(f"- Talk Client is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
		scan_report_file.write(f"\n- Talk Client is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
	else:
		print("- Talk Client is not installed. No action is needed.\n")
		scan_report_file.write("\n- Talk Client is not installed. No action is needed.\n")

def scan_telnet():
	if check_telnet():
		print(f"- Telnet Client is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
		scan_report_file.write(f"\n- Telnet Client is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
	else:
		print("- Telnet Client is not installed. No action is needed.\n")
		scan_report_file.write("\n- Telnet Client is not installed. No action is needed.\n")

def scan_ldap_utils():
	if check_ldap_utils():
		print(f"- LDAP Client is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
		scan_report_file.write(f"\n- LDAP Client is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
	else:
		print("- LDAP Client is not installed. No action is needed.\n")
		scan_report_file.write("\n- LDAP Client is not installed. No action is needed.\n")

def scan_rpcbind():
	if check_rpcbind():
		print(f"- RPC Client is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
		scan_report_file.write(f"\n- RPC Client is installed.{Fore.RED} Please Uninstall it.{Style.RESET_ALL}\n")
	else:
		print("- RPC Client is not installed. No action is needed.\n")
		scan_report_file.write("\n- RPC Client is not installed. No action is needed.\n")

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

def check_non_services_scan():
	command = "ss -ltr"
	result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, text=True)

	if result.returncode == 0:
		lines = result.stdout.splitlines()

		print(lines[0])

		for index, line in enumerate(lines[1:], start=1):
			print(f"Index {index}: {line}")
			scan_report_file.write(f"Index {index}: {line}\n")
	else:
		print(f"Error running command: {result.stderr}")
	print("\n")

# ==================================== Firewall Configuration Section ==============================

def log_setup():
    global current_datetime
    log_file_path = "script_log.txt"
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if not os.path.exists(log_file_path):
        with open(log_file_path, "w") as log_file:
            log_file.write(f"-----------------------------------------------------------------------\n")
            log_file.write(f"                           Host Firewall Compliance                         \n")
            log_file.write(f"-----------------------------------------------------------------------\n")

            log_file.write(f"{current_datetime} - ============ SCRIPT INITIATION ============\n")
    else:
        with open(log_file_path, "a") as log_file:
            log_file.write(f"\n{current_datetime} - ============ PROGRAM EXECUTION ============\n")

def log_changes(changes):
    log_file_path = "script_log.txt"
    with open(log_file_path, "a") as log_file:
        log_file.write(f"\nChanges made: {changes}")

def retrieve_from_main_log(choice):
    try:
        control = ["UFW INSTALLATION", "IP-PERSISTENT", "UFW-ENABLING", "LOOPBACK-INTERFACE", "OUTBOUND-RULES",
                   "PORT-RULES", "DEFAULT-DENY-POLICY"]
        if choice == "date":
            main_log_filepath = "script_log.txt"
            output_filepath = current_datetime + ".txt"
            with open(main_log_filepath, 'r') as main_log_file:
                # gets the whole text file as lines
                lines = main_log_file.readlines()
            for index, line in enumerate(lines):
                if current_datetime in line:
                    with open(output_filepath, 'w') as output_file:
                        output_file.writelines(lines[index:])
                        break
        elif choice == "control":
            main_log_filepath = "script_log.txt"
            # for loop to iterate through the list of controls
            i = 0
            flag = False
            for i in range(len(control)):
                output_filepath = (control[i]) + ".txt"
                with open(main_log_filepath, 'r') as main_log_file:
                    # gets the whole text file as lines
                    lines = main_log_file.readlines()
                for index, line in enumerate(lines):
                    if control[i] in line:
                        with open(output_filepath, 'a') as output_file:
                            output_file.writelines(current_datetime + lines[index])
                            flag = True
            if flag:
                print("Log generated successfully")
            elif not flag:
                print("No configuration found for current_datetime")
        elif choice is None:
            print("Please choose either date or control")
            raise ValueError("Please choose either date or control")

    except ValueError as ve:
        print("Error:", ve)
    except TypeError as ve:
        print("Error:", ve)
    except AttributeError as ve:
        print("Error:", ve)

def Log_options_check():
    try:
        choice = input("""
    what type of log do you want,
    Date-wise
    Control-wise
        """).lower()
        if choice == 'date':
            retrieve_from_main_log("date")
        elif choice == 'control':
            retrieve_from_main_log("control")
        else:
            raise ValueError("Please choose either date or control")
    except ValueError as ve:
        print("Error:", ve)
    except TypeError as ve:
        print("Error:", ve)
    except AttributeError as ve:
        print("Error:", ve)
# def Log_options_check():
#     root = tk.Tk()
#     root.withdraw()
#
#     options = ["Date-wise", "Control-wise"]
#     user_input = simpledialog.askstring("Log Options", "Select log type:".join(options)).lower()
#
#     if user_input in options:
#         retrieve_from_main_log(user_input)
#     else:
#         print("Invalid choice. Please choose either Date-wise or Control-wise.")

# function to generate different reports
def log_options():
    try:
        print("""
    \033[91m|==================== Log Options ====================|\033[0m""")
        print("\nDo you want to generate a log report")
        var = y_n_choice()
        var.lower()
        if var == 'y' or var == 'yes' or var == '':
            Log_options_check()
            print("\nExiting...")
        elif var == 'n' or var == 'no':
            print("\nExiting...")
            time.sleep(1)
        elif var is None:
            print("Error: Result is None.")
            return
    except ValueError as ve:
        print("Error:", ve)
    except TypeError as ve:
        print("Error:", ve)
    except AttributeError as ve:
        print("Error:", ve)


def noufwbanner():
    print("CIS recommends installing ufw; proceed with the installation in the configure section.")
    return


def is_ufw_installed():
    try:
        return bool(os.system("command -v ufw >/dev/null 2>&1") == 0)
    except FileNotFoundError:
        noufwbanner()


def ensure_ufw_installed():
    print("""
    \033[91m|=============== Installing Host Firewall ===============|\033[0m
    
    A firewall utility is required to configure the Linux kernel's netfilter framework via the
    iptables or nftables back-end. The Linux kernel's netfilter framework host-based firewall can
    protect against threats originating from within a corporate network, including malicious
    mobile code and poorly configured software on a host.
    
    Note: Only one firewall utility should be installed and configured. UFW is dependent on
    the iptables package.
    """)

    if not is_ufw_installed():
        var = input(
            "This point onwards, the configurations require the installation of UFW. Do you want to install the Host firewall? (yes/no):").lower()
        var.lower()

        if var == 'y' or var == 'yes' or var == '':
            os.system("apt install ufw")
            line = "UFW INSTALLATION: ok"
            log_changes(line)
            print("\n", line)
        elif var == 'n' or var == 'no':
            line = "UFW INSTALLATION: no"
            log_changes(line)
            print("\n", line)
            exit()
        elif var is None:
            print("Error: Result is None.")
            return
    else:
        line = "UFW INSTALLATION:Pre-set"
        log_changes(line)
        print("\n", line)


def is_iptables_persistent_installed():
    return bool(os.system("dpkg -s iptables-persistent >/dev/null 2>&1") == 0)


def ensure_iptables_persistent_packages_removed():
    print("""
    \033[91m|============== Removing IP-Persistent Tables ==============|\033[0m
    
    Running both `ufw` and the services included in the `iptables-persistent` package may lead
    to conflicts.
    """)
    if is_iptables_persistent_installed():
        var = input("Do you want to remove the iptables-persistent packages? (yes/no):").lower()
        var.lower()

        if var == 'y' or var == 'yes' or var == '':
            os.system("apt purge iptables-persistent")
            line = "IP-PERSISTENT:removed"
            log_changes(line)
            print("\n", line)
        elif var == 'n' or var == 'no':
            line = "IP-PERSISTENT: not removed"
            log_changes(line)
            print("\n", line)
        elif var is None:
            print("Error: Result is None.")
            return
    else:
        line = "IP-PERSISTENT:Pre-set"
        log_changes(line)
        print("\n", line)


def is_ufw_enabled():
    try:
        # Run the command to check UFW status
        result = subprocess.run(['ufw', 'status'], capture_output=True, text=True, check=True)

        # Check if the output contains 'Status: active'
        return 'Status: active' in result.stdout
    except FileNotFoundError:
        noufwbanner()
        return False
    except subprocess.CalledProcessError as e:
        # If an error occurs while running the command
        print(f"Error: {e}")
        return False
    except ValueError as ve:
        print("Error:", ve)
    except TypeError as ve:
        print("Error:", ve)
    except AttributeError as ve:
        print("Error:", ve)


def enable_firewall_sequence():
    print("""
    \033[91m|================== Enabling UFW ==================|\033[0m
    
    When running `ufw enable` or starting `ufw` via its initscript, `ufw` will flush its chains.
    This is required so `ufw` can maintain a consistent state, but it may drop existing
    connections (e.g., SSH). `ufw` does support adding rules before enabling the firewall.
    The rules will still be flushed, but the SSH port will be open after enabling the
    firewall.
    Please note that once `ufw` is 'enabled', it will not flush the chains when
    adding or removing rules (but will when modifying a rule or changing the default policy).
    By default, `ufw` will prompt when enabling the firewall while running under SSH.
    """)
    if not is_ufw_enabled():
        print("\nUFW is not enabled, do you want to enable it, ")
        var = y_n_choice()
        var.lower()
        if var == 'y' or var == 'yes' or var == '':
            print(
                "\nufw will flush its chains.This is good in maintaining a consistent state, but it may drop existing connections (eg ssh)")
            os.system("ufw allow proto tcp from any to any port 22")
            # Run the following command to verify that the ufw daemon is enabled:
            print(" \nverifying that the ufw daemon is enabled:")
            os.system("systemctl is-enabled ufw.service")
            # following command to verify that the ufw daemon is active:
            print(" \nverifying that the ufw daemon is active:")
            os.system("systemctl is-active ufw")
            # Run the following command to verify ufw is active
            print(" \nverifying ufw is active:")
            os.system("ufw status")
            # following command to unmask the ufw daemon
            print("\nunmasking ufw daemon:")
            os.system("systemctl unmask ufw.service")
            # following command to enable and start the ufw daemon:
            print("\nenabling and starting the ufw daemon:")
            os.system("systemctl --now enable ufw.service")
            # following command to enable ufw:
            print("\nEnabling the firewall...")
            os.system("ufw enable")
            line = """
    UFW-ENABLING: ok, below commands were executed:
        ufw allow proto tcp from any to any port 22
        systemctl is-enabled ufw.service
        systemctl is-active ufw
        systemctl unmask ufw.service
        systemctl --now enable ufw.service
        ufw enable """
            log_changes(line)
            print("\n", line)
        elif var == 'n' or var == 'no':
            line = "UFW-ENABLING: no"
            log_changes(line)
            print("\nExiting UFW enabling mode... continuing to next configurations")
        elif var is None:
            print("Error: Result is None.")
            return
    else:
        line = "UFW-ENABLING: Pre-set"
        log_changes(line)
        print("\n", line)


def is_loopback_interface_configured():
    try:
        # Create a list to store unconfigured rules
        unconfigured_rules = []

        # Concatenate rules and statuses into a 2D array
        ufw_rules_and_status = [
            ["ufw allow in on lo", "Anywhere on lo"],
            ["ufw allow out on lo", "ALLOW OUT   Anywhere on lo"],
            ["ufw deny in from 127.0.0.0/8", "DENY        127.0.0.0/8 "],
            ["ufw deny in from ::1", "DENY        ::1"]
        ]

        # Get UFW status
        result = subprocess.run(['ufw', 'status'], capture_output=True, text=True, check=True)

        # Check for unconfigured rules
        for rule, status in ufw_rules_and_status:
            if status not in result.stdout:
                unconfigured_rules.append(rule)

        # Print results
        if not unconfigured_rules:
            print("All loopback rules are configured.")
            return True
        else:
            print("\033[91mThe following Loopback rules are not configured:")
            for unconfigured_rule in unconfigured_rules:
                print("\033[33m", unconfigured_rule, "\033[0m")
            return False
    except FileNotFoundError:
        noufwbanner()
    except ValueError as ve:
        print("Error:", ve)
    except TypeError as ve:
        print("Error:", ve)
    except AttributeError as ve:
        print("Error:", ve)


def ensure_loopback_configured():
    try:
        print("""
    \033[91m|========= Configuring the Loopback Interface =========|\033[0m
    
    Loopback traffic is generated between processes on the machine and is typically critical to
    the operation of the system. The loopback interface is the only place that loopback network
    (127.0.0.0/8 for IPv4 and ::1/128 for IPv6) traffic should be seen. All other interfaces
    should ignore traffic on this network as an anti-spoofing measure.
    """)
        if not is_loopback_interface_configured():
            print("\nAll loopback interfaces are not configured, do you want to configure them, ")
            var = y_n_choice()
            var.lower()
            if var == 'y' or var == 'yes' or var == '':
                line = """
    LOOPBACK-INTERFACE: ok, below commands were executed:
        ufw allow in on lo
        ufw allow out on lo
        ufw deny in from 127.0.0.0/8
        ufw deny in from ::1
                    
                """
                log_changes(line)
                print("\nEnabling configurations on lo interfaces...")
                os.system("ufw allow in on lo")
                os.system("ufw allow out on lo")
                os.system("ufw deny in from 127.0.0.0/8")
                os.system("ufw deny in from ::1")
            elif var == 'n' or var == 'no':
                line = "LOOPBACK-INTERFACE: no"
                log_changes(line)
                print("\n", line)
            elif var is None:
                print("Error: Result is None.")
                return
        else:
            line = "LOOPBACK-INTERFACE: Pre-set"
            log_changes(line)
            print("\n", line)
    except ValueError as ve:
        print("Error:", ve)
    except TypeError as ve:
        print("Error:", ve)
    except AttributeError as ve:
        print("Error:", ve)
    except FileNotFoundError:
        noufwbanner()


# check if ufw outbound connections are Pre-set
def is_ufw_outbound_connections_configured():
    try:
        result = subprocess.run("ufw status", shell=True, capture_output=True, text=True)
        if "Anywhere on all" in result.stdout:
            print("The following outbound rule is configured: ufw allow out on all")
            return True
        else:
            print("\033[91mThe following outbound rule is not configured: ufw allow out on all")
            return False
    except FileNotFoundError:
        noufwbanner()
    except subprocess.CalledProcessError as e:
        print("Error:", e)
        return False
    except Exception as e:
        print("Error:", e)
        return False


def ensure_ufw_outbound_connections():
    print("""
    \033[91m|========= Configuring UFW Outbound Connections =========|\033[0m
    
    If rules are not in place for new outbound connections, all packets will be dropped by the
    default policy, preventing network usage.
    
    Do you want to configure your ufw outbound connections if this set of rules are not in place 
    for new outbound connections all packets will be dropped by the default policy preventing network usage.,""")
    if not is_ufw_outbound_connections_configured():
        var = y_n_choice()
        var.lower()
        if var == 'y' or var == 'yes' or var == '':
            # var = input("\n PLease verify all the rules whether it matches all the site policies")
            print("\n implementing a policy to allow all outbound connections on all interfaces:")
            line = """
    OUTBOUND-RULES: ok, below command was executed:
        ufw allow out on all
            """
            log_changes(line)
            os.system("ufw allow out on all")
            print("\nConfiguration successful ...")

        elif var == 'n' or var == 'no':
            line = "OUTBOUND-RULES: no"
            log_changes(line)
            print(line)
        elif var is None:
            print("Error: Result is None.")
            return
    else:
        line = "OUTBOUND-RULES:Pre-set"
        log_changes(line)
        print("\n", line)


def get_allow_deny():
    while True:
        try:
            allw_dny = input("Enter rule (allow or deny): ").lower()
            if allw_dny not in ['allow', 'deny']:
                raise ValueError("Invalid rule. Please enter either 'allow' or 'deny'.")
            elif allw_dny is None:
                print("Error: Result is None.")
                return
            return allw_dny
        except ValueError as ve:
            print("Error:", ve)
        except TypeError as ve:
            print("Error:", ve)
        except AttributeError as ve:
            print("Error:", ve)


def is_valid_decimal(value):
    return 0 <= int(value) <= 255


def is_valid_network_address(address_parts):
    return all(is_valid_decimal(part) for part in address_parts)


def get_network_address():
    while True:
        try:
            netadd = input("Enter network address (in the format xxx.xxx.xxx.xxx): ")
            address_parts = netadd.split('.')
            # Use a regular expression to check if the input matches the expected format
            if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', netadd) or not is_valid_network_address(
                    address_parts):
                raise ValueError(
                    "Invalid network address format or out-of-range values. Please use xxx.xxx.xxx.xxx format.")
            elif netadd is None:
                print("Error: Result is None.")
                return
            return netadd
        except ValueError as ve:
            print("Error:", ve)
        except TypeError as ve:
            print("Error:", ve)
        except AttributeError as ve:
            print("Error:", ve)


def get_proto():
    while True:
        try:
            proto = input("Enter protocol (tcp or udp): ").lower()
            if proto not in ['tcp', 'udp']:
                raise ValueError("Invalid protocol. Please enter either 'tcp' or 'udp'.")
            elif proto is None:
                print("Error: Result is None.")
                return
            return proto
        except ValueError as ve:
            print("Error:", ve)
        except TypeError as ve:
            print("Error:", ve)
        except AttributeError as ve:
            print("Error:", ve)


def get_mask():
    while True:
        try:
            mask = int(input("Enter the whole number value of the subnet mask (16-32): ").lower())
            if 16 <= mask <= 32:
                return str(mask)
            elif mask is None:
                print("Error: Result is None.")
                return
            else:
                raise ValueError("\nInvalid subnet mask. Please enter a value between 16 and 32.")
        except ValueError as ve:
            print("\nError:", ve)


def get_ports_as_a_list(script_path):
    result = subprocess.run(['bash', script_path], capture_output=True, text=True)
    if result.returncode == 0:
        # If the script ran successfully, print the output
        # getting numbers from string
        temp = re.findall(r'\d+', result.stdout)
        ports_list = list(map(int, temp))
        print("Open ports with no FW rule")
        for i in range(0, len(ports_list)):
            print(i, ':', ports_list[i])
        return ports_list

    else:
        # If there was an error, print the error message
        print("Error:")
        print(result.stderr)


def get_port_number(script_path):
    while True:
        try:
            ports_list = get_ports_as_a_list(script_path)
            p_no = int(input("Enter the index number of the port to be configured:"))

            # Check if the user pressed Cancel

            if 0 <= p_no <= len(ports_list) - 1:
                port_number = ports_list[p_no]
                return str(port_number)
            elif p_no is None:
                print("Error: Result is None.")
                return
            else:
                raise ValueError(f"\nInvalid Index Number. Please enter a value between 0 and {len(ports_list) - 1}")
        except ValueError as ve:
            print("Error:", ve)
        except TypeError as ve:
            print("Error:", ve)
        except AttributeError as ve:
            print("Error:", ve)


# def ensure_rules_on_ports_banner():
#

def ensure_rules_on_ports(script_path):
    print("""
    \033[91m|=== Configuring Firewall Rules for All Open Ports ===|\033[0m
    
    To reduce the attack surface of a system, all services and ports should be blocked unless required.
    Your configuration will follow this format:
        ufw allow from 192.168.1.0/24 to any proto tcp port 443
    
    Do you want to continue configuring firewall rules for a port [Y/n]: """)
    var = y_n_choice()
    if var == 'y' or var == 'yes' or var == '':
        port_number = get_port_number(script_path)
        allow = get_allow_deny()
        netad = get_network_address()
        mask = get_mask()
        proto = get_proto()
        rule = ("ufw " + allow + " from " + netad + "/" + mask + " to any proto " + proto + " port " + str(port_number))
        line = ("PORT-RULES: \n: " + str(rule))
        log_changes(line)
        os.system(rule)
        input("\nHit enter to continue [enter]: ")
        ensure_rules_on_ports(script_path)
    elif var == 'n' or var == 'no':
        line = "PORT-RULES: no"
        log_changes(line)
        print("Skipping firewall rule configuration on ports...")
    elif var is None:
        print("Error: Result is None.")
        return


def is_default_deny_policy():
    # check if to deny policies are Pre-set

    return bool(os.system(
        "ufw status verbose | grep 'Default: deny (incoming), deny (outgoing), deny (routed)' >/dev/null 2>&1") == 0)


def ensure_port_deny_policy():
    try:
        print("""
    \033[91m|=============== Default Port Deny Policy ===============|\033[0m
    
    Any port and protocol not explicitly allowed will be blocked.
    Do you want to configure the default deny policy? [Y/n]: """)
        is_default_deny_policy()
        var = y_n_choice()
        var.lower()
        if var == 'y' or var == 'yes' or var == '':
            print("remediation process...")
            print("\n allowing Git...")
            os.system("ufw allow git")
            print("\nallowing http in...")
            os.system("ufw allow in http")
            print("\nallowing http out...")
            os.system("ufw allow out http")
            print("\nallowing https in...")
            os.system("ufw allow in https")
            print("\nallowing https out...")
            os.system("ufw allow out https")
            print("\nallowing port 53 out...")
            os.system("ufw allow out 53")
            print("\nallowing ufw logging on...")
            os.system("ufw logging on")
            print("\ndenying incoming by default...")
            os.system("ufw default deny incoming")
            print("\ndenying outgoing by default...")
            os.system("ufw default deny outgoing")
            print("\ndenying default routing...")
            os.system("ufw default deny routed")
            line = """
    DEFAULT-DENY-POLICY: ok, below commands were executed,
        ufw allow git
        ufw allow in http
        ufw allow out http
        ufw allow in https
        ufw allow out https
        ufw allow out 53
        ufw logging on
        ufw default deny incoming
        ufw default deny outgoing
        ufw default deny routed
            """
            log_changes(line)
        elif var == 'n' or var == 'no':
            line = "DEFAULT-DENY-POLICY: no"
            log_changes(line)
            print("\nexiting port deny policy...")
        elif var is None:
            print("Error: Result is None.")
            return
    except ValueError as ve:
        print("Error:", ve)
    except TypeError as ve:
        print("Error:", ve)
    except AttributeError as ve:
        print("Error:", ve)


def scan_system_configuration():
    try:
        print("""
    \033[91m|============== Scanning System Configuration ==============|\033[0m""")
        # Check if UFW is installed
        if is_ufw_installed():
            print("UFW is installed.")
        else:
            print("\033[91mUFW is not installed.\033[0m")

        # Check if iptables-persistent packages are removed
        if is_iptables_persistent_installed():
            print("\033[91mIptables-persistent packages are not removed.\033[0m")
        else:
            print("Iptables-persistent packages are removed.")
        # Check if UFW is enabled
        if is_ufw_enabled():
            print("UFW is enabled.")
        else:
            print("\033[91mUFW is not enabled.\033[0m")
        # Check if loopback interface is configured already
        if is_default_deny_policy():
            print("Default deny policy is configured.")
        else:
            print("\033[91mDefault deny policy is not configured.\033[0m")
        # Check if loopback interface is configured already
        is_loopback_interface_configured()
        if is_default_deny_policy():
            print("Default deny policy is configured.")
        is_ufw_outbound_connections_configured()

    except FileNotFoundError:
        noufwbanner()
    except ValueError as ve:
        print("Error:", ve)
    except TypeError as ve:
        print("Error:", ve)
    except AttributeError as ve:
        print("Error:", ve)
    # Add more checks for other configurations as needed
    # check if default deny policy is configured


def all_ufw_hardening_controls():
    ensure_ufw_installed()
    time.sleep(1)
    ensure_iptables_persistent_packages_removed()
    time.sleep(1)
    enable_firewall_sequence()
    time.sleep(1)
    # ensure_rules_on_ports_banner()
    script_path = 'ufwropnprts.sh'
    ensure_rules_on_ports(script_path)
    time.sleep(1)
    ensure_port_deny_policy()
    time.sleep(1)
    ensure_loopback_configured()
    time.sleep(1)
    ensure_ufw_outbound_connections()
    time.sleep(1)
    print("""
    \033[91m|================ Configurations Complete ================|\033[0m""")
    time.sleep(1)


# show all the configurations


# function to ask the user if he wants to do a scan or go straight into configurations and call the relevant function in the script and exit if needed
def scan_or_config():
    print("""
    \033[91m|============= UFW CIS Compliance Control=============|\033[0m""")
    print("\nDo you want to scan your system configurations press no to continue configuring: ")
    var = y_n_choice()
    var.lower()
    if var == 'y' or var == 'yes' or var == '':
        scan_system_configuration()
        print("\nExiting...")
        time.sleep(1)
        # ask the user if he needs to do the configurations
        print("\nDo you want to continue to configurations")
        var = y_n_choice()
        var.lower()
        if var == 'y' or var == 'yes' or var == '':
            all_ufw_hardening_controls()
            print("\n\033[91mPress enter to exit the code [enter] \033[0m")
            input()
            print("\nExiting...")
            time.sleep(1)
        if var == 'n' or var == 'no':
            print("\nExiting...")
            time.sleep(1)
        elif var is None:
            print("Error: Result is None.")
            return
    elif var == 'n' or var == 'no':
        print("\nContinuing to configurations...")
        all_ufw_hardening_controls()
        time.sleep(1)
        return
    elif var is None:
        print("Error: Result is None.")
        return

# ============================================ Main Functions ======================================

def scan_actions():
	scan_services_report_head()
	scan_services_output_head()
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

def scan_running_services_action():
	scan_runningservices_output_head()
	time.sleep(1)
	check_non_services_scan()

def services_purge_main():
	purge_actions()
	running_services_action()
	report_file.write("\n")

def services_scan_main():
	scan_actions()
	scan_running_services_action()
	report_file.write("\n")

# Firewall Main Functions

def firewall_main():
    try:
        log_setup()
        scan_or_config()
        log_options()
    except FileNotFoundError:
        noufwbanner()
    except KeyboardInterrupt:
        print("\n\nExited unexpectedly...")

# End of Firewall Main Functions

def option():
	choice = ask_choice()
	if choice == "1":
		conf_choice = input("You have Chosen an All Benchmark Scan. Are you Sure? y/n ")
		if conf_choice.lower() == "y":
			print("\nYou have chosen an All Benchmark Scan. Proceeding with scan...\n")
			services_purge_main()
			firewall_main()
		elif conf_choice.lower() == "n":
			print("\nYou have canceled your action.\n")
			option()
		else:
			print("\nPLEASE ENTER A VALID INPUT")
			option()
	elif choice == "2":
		conf_choice = input("\nYou have chosen Special Services. Are you Sure? y/n ")
		if conf_choice.lower() == "y":
			print("\nYou have chosen Special Services Scan. Proceeding with scan...\n")
			services_purge_main()
		elif conf_choice.lower() == "n":
			print("\nYou have canceled your action.\n")
			option()
		else:
			print("\nPLEASE ENTER A VALID INPUT")
			option()
	elif choice == "3":
		conf_choice = input("\nYou have chosen Firewall. Are you sure? y/n ")
		if conf_choice.lower() == "y":
			print("\nYou have chosen Firewall Scan. Proceeding with scan.../n")
			firewall_main()
		elif conf_choice.lower() == "n":
			print("\n You have canceled your action.\n")
			option()
		else:
			print("\nPLEASE ENTER A VALID INPUT")
			option()
	elif choice.lower() == "b":
		scan_type()
	elif choice.lower() == "e":
		print("\nYou have exited the script :( \n")
	else:
		print(f"{Fore.RED}PLEASE ENTER A VALID INPUT.{Style.RESET_ALL}\n")

def scan_option():
	choice = ask_choice()
	if choice == "1":
		conf_choice = input("You have Chosen an All Benchmark Scan. Are you Sure? y/n ")
		if conf_choice.lower() == "y":
			print("\nYou have chosen an All Benchmark Scan. Proceeding with scan...\n")
			services_scan_main()
			firewall_main()
		elif conf_choice.lower() == "n":
			print("\nYou have canceled your action.\n")
			scan_option()
		else:
			print("\nPLEASE ENTER A VALID INPUT")
			scan_option()
	elif choice == "2":
		conf_choice = input("\nYou have chosen Special Services. Are you Sure? y/n ")
		if conf_choice.lower() == "y":
			print("\nYou have chosen Special Services Scan. Proceeding with scan...\n")
			services_scan_main()
		elif conf_choice.lower() == "n":
			print("\nYou have canceled your action.\n")
			scan_option()
		else:
			print("\nPLEASE ENTER A VALID INPUT")
			scan_option()
	elif choice == "3":
		conf_choice = input("\nYou have chosen Firewall. Are you sure? y/n ")
		if conf_choice.lower() == "y":
			print("\nYou have chosen Firewall Scan. Proceeding with scan.../n")
			firewall_main()
		elif conf_choice.lower() == "n":
			print("\n You have canceled your action.\n")
			scan_option()
		else:
			print("\nPLEASE ENTER A VALID INPUT")
			scan_option()
	elif choice.lower() == "b":
		scan_type()
	elif choice.lower() == "e":
		print("\nYou have exited the script :( \n")
	else:
		print(f"{Fore.RED}PLEASE ENTER A VALID INPUT.{Style.RESET_ALL}\n")

def scan_type():
	banner()
	choice = ask_scan_type()
	if choice == "1":
		conf_choice = input("\nYou have chosen only the Compliance Scan. Are you Sure? y/n ")
		if conf_choice.lower() == "y":
			print("\nYou have chosen the Compliance Scan. Proceeding with scan...\n")
			scan_option()
		elif conf_choice.lower() == "n":
			print("\nYou have canceled your action.\n")
			scan_type()
		else:
			print("\nPLEASE ENTER A VALID INPUT\n")
			scan_type()
	elif choice == "2":
		conf_choice = input("\nYou have chosen only the Practical Scan. Are you Sure? y/n ")
		if conf_choice.lower() == "y":
			print("\nYou have chosen the Practical Scan. Proceeding with scan...\n")
			option()
		elif conf_choice.lower() == "n":
			print("\nYou have canceled your action.\n")
			scan_type()
		else:
			print("\nPLEASE ENTER A VALID INPUT\n")
			scan_type()
	elif choice.lower() == "e":
		print("\nYou have exited the script :( \n")
	else:
		print(f"{Fore.RED}PLEASE ENTER A VALID INPUT.{Style.RESET_ALL}\n")
		scan_type()


scan_type()

report_file.close()
scan_report_file.close()

# ============================================ End of Script ======================================