import json
from napalm import get_network_driver
driver = get_network_driver('ios')
iosvl2 = driver('10.0.0.2', 'james', 'cisco')
iosvl2.open()
 
print ('Accessing 10.0.0.2')
iosvl2.load_merge_candidate(filename='acl1.cfg')
iosvl2.commit_config()
iosvl2.close()
