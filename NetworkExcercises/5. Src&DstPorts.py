# importing the libraries needed
from scapy.all import *
from scapy.layers.http import *

# in the following hackxercise, use scapy to read the pcap file, which is a recording of some network traffic captured
# with a sniffer, and figure out "destination port" of the third packet, and the source port address in the fourth packet.


# function to run in the codeboard environment platform
def show_source_destination_ports():
    packets = rdpcap(recording_path)
    thirdPktDport = packets[2].getlayer(TCP).dport
    fourthPktSport= packets[3].getlayer(TCP).sport
    print("The third package destination port is %s " % thirdPktDport)
    print("The fourth package source port is %s " % fourthPktSport)
    #pass # print destination port of third packet and source port of fourth packet
#show_source_destination_ports()

def getPortInformation():
    packets = rdpcap('capture2.pcap')
    # this function check the source and destination address of the first package with that information
    for pkt in packets:
        if pkt.haslayer(TCP):
            srcPort = pkt.getlayer(TCP).sport 
            dstPort = pkt.getlayer(TCP).dport
            print("The source port is %s " % srcPort)
            print("The destination port is %s " % dstPort)
            break

getPortInformation()