import socket
import subprocess
import ipaddress

subnet = "192.168.1.0/24"
online_ips = []

for ip in ipaddress.IPv4Network(subnet):
    result = subprocess.run(['ping', '-c', '1', str(ip)], stdout=subprocess.DEVNULL)
    if result.returncode == 0:
        online_ips.append(str(ip))

print("Active devices:")
print("\n".join(online_ips))
