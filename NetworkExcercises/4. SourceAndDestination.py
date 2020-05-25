# importing the necessary modules
from scapy.all import *
from scapy.layers.http import *

# in the following hackxercise, use scapy to read the pcap file, which is a recording of some network traffic captured with a sniffer 
# and figure out what is the source ip address of the fourth packet, and the destination IP address in the sixth packet.


# this method is to run on the codeboard test platform.
def show_source_destination_ip_address():
    packets = rdpcap(recording_path)
    fourthPkt= packets[3]
    if fourthPkt.haslayer(IP):
        print(fourthPkt.getlayer(IP).src)
    sixthPkt = packets[5]
    if sixthPkt.haslayer(IP):
        print(sixthPkt.getlayer(IP).dst)
    #pass # print the source and destination ip addresses

#show_source_destination_ip_address()


def showIpAddresses():
    packets = rdpcap('capture2.pcap')
    # this function check the source and destination address of the first package whit that information
    for pkt in packets:
        if pkt.haslayer(IP):
            srcAddress= pkt.getlayer(IP).src
            destAddress= pkt.getlayer(IP).dst  
            print(" the source address is : %s" % srcAddress)
            print(" The destination address is: %s " % destAddress)
            break

showIpAddresses()