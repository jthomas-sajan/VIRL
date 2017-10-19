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


with open('iosv_l2_config1') as f:
    lines = f.read().splitlines()
print lines

all_devices = [iosv_l2_s1, iosv_l2_s2]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print output 

