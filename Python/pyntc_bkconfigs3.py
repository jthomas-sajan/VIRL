import json
from pyntc import ntc_device as NTC
iosvl2 = NTC(host='10.0.0.2', username='james', password='cisco', device_type='cisco_ios_ssh')
iosvl2.open()

ios_run = iosvl2.backup_running_config('S1.cfg')

iosvl2.close()

