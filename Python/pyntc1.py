import json
from pyntc import ntc_device as NTC
iosvl2 = NTC(host='10.0.0.2', username='james', password='cisco', device_type='cisco_ios_ssh')
iosvl2.open()
 
ios_output = iosvl2.facts
print (json.dumps(ios_output, indent=4))
 
iosvl2.close()

