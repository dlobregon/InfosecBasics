# in an imaginary protocol stack, the header structures are as follows:
# the layer 1 has the following structure:
#   - the first 4 bytes are the ID of the sender
#   - the next 4 bytes are the ID of the receiver.
#   - the next 4 bytes are the size of the content (let's call it n)
#   - the next "n" bytes are the content
#
# the layer 2 has the following header and footer:
#   -The first 4 bytes are the session ID
#   -the last 4 bytes are a checksum of the message
#   -the middlebytes are the content
# 
# the layer 3 has the following structure:
#   - the first 4 bytes are the message ID
#   - the rest of the bytes are the message


# here is a message captured on the wire, that was sent using this protocol stack.



from struct import *
import sys
packet = b'\x08\x00\x00\x00\xf6\x01\x00\x00\x24\x00\x00\x00\x03\x00\x00\x00\x0c\x00\x00\x00I think, therefore I am.\xca\xcd\x00\x00'

#### Don't change the code until this line ####

def show_details():
    print("the current packet has the length of : %s " % sys.getsizeof(packet))
    #print()
    # getting the Sender ID
    nByte=iter_unpack('<I', packet)
    #making a list using the iterator
    lista=list(nByte)
    # to get layer 1 structure we need to extract the first 4 tuples from list
    senderId, receiverId, n = lista[0:3]
    print("the sender id: %s " % senderId[0], "the receiver id is: %s " % receiverId[0],"the length of the content: %s " % n[0])
    # re-writting the values
    n=n[0]
    senderId= senderId[0]
    receiverId=receiverId[0]
    # defining the whole packet format string
    formatString="<IIIII"+str(n-12)+"sI"
    #print(formatString)
    # getting the real values
    senderId, receiverId, n, sessionId, messageId, message,messageChecksum = unpack(formatString,packet)
    print("the message is: %s" % message.decode("ascii"))
    print("the session id is: %s " % sessionId)
    print("the messageId is: %s" % messageId)
    print("the message checksum is: %s" % messageChecksum)
    # the next print is required by the platform 
    # uncomment the next print to test and comment the below prints
    #print(senderId,messageId,message.decode("ascii"),messageChecksum)
show_details()
