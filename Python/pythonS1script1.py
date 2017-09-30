#!/user/bin/env python

import getpass
import sys
import telnetlib

HOST = "10.0.0.2"
user = raw_input("Enter your Telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("enable\n")
tn.write("cisco\n")
tn.write("conf t\n")
tn.write("vlan 20\n")
tn.write("name Python_VLAN_20\n")
tn.write("exit\n")
tn.write("vlan 21\n")
tn.write("exit\n")
tn.write("vlan 22\n")
tn.write("exit\n")
tn.write("end\n")
tn.write("exit\n")

print tn.read_all()