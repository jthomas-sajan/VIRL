import json
from pyntc import ntc_device as NTC
iosvl2 = NTC(host='10.0.0.2', username='james', password='cisco', device_type='cisco_ios_ssh')
iosvl2.open()
 
ios_output = iosvl2.facts
print (json.dumps(ios_output, indent=4))
 
#iosvl2.config_list(['hostname s1_python', 'router ospf 1', 'network 0.0.0.0 255.255.255.255 area 0'])

iosvl2.config_list(['hostname S1',
                    'router ospf 1',
                    'no network 0.0.0.0 255.255.255.255 area 0',
                    'network 192.168.122.0 0.0.0.255 area 0',
                    'network 10.1.20.0 0.0.0.255 area 1'])
iosvl2.close()

