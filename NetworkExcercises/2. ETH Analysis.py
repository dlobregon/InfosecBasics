from scapy.all import *
from scapy.layers.http import *

### Within the following codeboard we prepared a pcap file for you, - that is, a traffic capture file collected 
# by wireshark. Your task is to process this file, and extract source MAC address of the 3rd captured packet.

#### Don't change the code until this line ####

def show_mac_address():
    packets = rdpcap(recording_path)
    if(packets[2].haslayer("Ethernet")):
        macAddSrc= packets[2].getlayer("Ethernet").src 
        print(macAddSrc)

show_mac_address()


# a function to test the scapy capabilities.
def analyzeEthPack():
    # open the file 
    packets = rdpcap('caputerTest.pcap')
    #print(len(packets))
    # printing the hex values
    #hexdump(packets[0])
    # listing the packet fields
    #ls(packets[0])
    #showing infor with developer approach
    #packets[3].show()
    #print(packets[3].haslayer("Ethernet"))
    # trying to extract the layer 1 source
    if(packets[3].haslayer("Ethernet")):
        macAddSrc= packets[3].getlayer("Ethernet").src 
        print(macAddSrc)


#analyzeEthPack()