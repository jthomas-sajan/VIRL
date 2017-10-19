import json
from napalm import get_network_driver
driver = get_network_driver('ios')
iosvl2 = driver('10.0.0.2', 'james', 'cisco')
iosvl2.open()
 
ios_output = iosvl2.get_mac_address_table()
print (json.dumps(ios_output, indent=4))

ios_output = iosvl2.get_arp_table()
print (json.dumps(ios_output, indent=4))

ios_output = iosvl2.ping('10.0.0.1')
print (json.dumps(ios_output, indent=4))
