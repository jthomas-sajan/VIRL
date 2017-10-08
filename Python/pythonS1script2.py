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

tn.write("conf t\n")

for n in range (20,41):
    tn.write("vlan " + str(n) + "\n")
    tn.write("name Python_VLAN _" + str(n) + "\n")

tn.write("end\n")
tn.write("exit\n")

print tn.read_all()