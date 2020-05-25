from scapy.all import *
from scapy.layers.http import *

# in the following  codeboard, use scapy to read the pcap file, which is a recording of some DNS traffic captured with a sniffer, 
# figure out what is the domian that is was being resolved, and what is its IP address. 


# this function runs on the codeboard environment platform
def show_domain_ip_address():
    packets = rdpcap(recording_path)
    for pkt in packets:
        if pkt.haslayer(DNS):
            pkt.show()
            print("--------------")
            print("--------------")

#show_domain_ip_address()

# this function is to explore the excercise in a local environment:
# using an analysis about what the funtion prints:
# the DNS layer has the following structure:
# 1 question record
# 2 DNS resource record.

def showDomainIpAddress():
    packets = rdpcap('caputerTest.pcap')
    for pkt in packets[1:10]:
        if pkt.haslayer(DNS):
            pkt.show()
            print("--------------")
            print("--------------")

showDomainIpAddress()
