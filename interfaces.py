#!/usr/bin/env python

from datetime import datetime
from netmiko import ConnectHandler
from getpass import getpass

host = input("Home_SW: ")
device = {
    'device_type': 'cisco_ios',
    'host': '172.18.5.6',
    'username': 'markdibr',
    'password': getpass(),
}
net_connect = ConnectHandler(**device)
output = net_connect.send_command("sho ip int bri | i Vlan")
print(output)

net_connect = ConnectHandler(**device)
output = net_connect.send_command("sho Vlan")
print(output)