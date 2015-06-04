#!/usr/bin/env python
import sys
import xmlrpclib

SATELLITE_URL = "http://192.168.1.45/rpc/api"
SATELLITE_LOGIN = "admin"
SATELLITE_PASSWORD = "password"

current_system = sys.argv[1]
current_system = current_system.split('.')

client = xmlrpclib.Server(SATELLITE_URL, verbose=0)

key = client.auth.login(SATELLITE_LOGIN, SATELLITE_PASSWORD)
sw_system = client.system.searchByName(key,current_system[0])
system_id = sw_system[0]['id']
puppet_role = client.system.getCustomValues(key,system_id)

print('---')
print('classes:')
print("  - %s" % puppet_role["puppet_role"])
