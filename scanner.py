import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    print("IP\t\t\tMAC Address")
    print("-----------------------------------------")
    for element in answered:
        print(element[1].psrc + "\t\t" + element[1].hwsrc)

# Example usage
scan("192.168.1.1/24")
