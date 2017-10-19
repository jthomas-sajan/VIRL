#!/usr/bin/env python

from netmiko import ConnectHandler

iosv_l2_s1 = {
    'device_type': 'cisco_ios',
    'ip': '10.0.0.2',
    'username': 'james',
    'password': 'cisco',
}

iosv_l2_s2 = {
    'device_type': 'cisco_ios',
    'ip': '10.0.0.3',
    'username': 'james',
    'password': 'cisco',
}


all_devices = [iosv_l2_s1, iosv_l2_s2]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    for n in range (3,21):
       print "Deleting VLAN " + str(n)
       config_commands = ['no vlan ' + str(n)]
       output = net_connect.send_config_set(config_commands)
       print output 

