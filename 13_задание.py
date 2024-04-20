from ipaddress import *
net=ip_network(f'192.168.32.128/255.255.255.192',0)

print(2**(f'{net[-1]:b}'.count('1')-f'{net[0]:b}'.count('1'))//2)