from scapy.all import *
from scapy.layers.http import *
# in the following hackxercise, use "scapy" to read the pcap file, which is a recording of some network traffic captured with a sniffer
# and figure out what is the "username", and then "password"


# some Hints:
# the traffic happens over port 8000, which scapy doesn't doesn't interpret as HTTP by default (because HTTP's default port is 80). To have it
# associate HTTP port run :
#bind_layers(TCP, HTTP, dport=8000)
#bind_layers(TCP, HTTP, sport=8000)

# the following function works to solver the hackxercise using the codeboard platform.
def show_username_password():
    bind_layers(TCP, HTTP, dport=8000)
    bind_layers(TCP, HTTP, sport=8000)
    packets = rdpcap(recording_path)
    #pass # print Username and Password
    def show_username_password():
    packets = rdpcap(recording_path)
    for packet in packets:
        if packet.haslayer(Raw):
            content=packet[Raw]
            print(content)



def getUsernamePassword():
    packets = rdpcap('capture2.pcap')
    # To extract the values of username and password is necessary make a pattern recognizer, in this case a regular expression.
    # because the values are the in the packets raw.
    for pkt in packets[7:8]:
        if pkt.haslayer(Raw):
            content =pkt[Raw]#.decode("ascii")
            #print("".join(chr(x) for x in bytearrcontent))
            print(content)
            #print(content.decode("string_escape"))
            #print(content.decode("base64"))
            print("------ -------")

    
getUsernamePassword()
