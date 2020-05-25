# implement the function "weak-HMAC", #
# which receives message and 8-bytes  (64-bit) long key, and returns its HMAC 
# using SHA-1 with the given 8 byte (64 bit) ipad and opad


from hashlib import sha1

ipad = b'123455678'
opad = b'abcdefghi'
#^(
def weak_hmac(m, k, ipad, opad):
    sipad=bytearray(b"")
    sopad=bytearray(b"")
    # first we need to pad the key
    key=k
    #if(len(k)!=len(ipad)):
        #key =str.encode(sha1(k).hexdigest())
        #stringformat="{foo:0"+str(len(ipad))+"d}"
        #print(stringformat)
    #    key=key.rjust(len(ipad),b"0")
    # computing the Sipad
    for i in range(0,len(key)):
        tmp=ipad[i] ^ key[i]
        sipad.append(tmp)
    # computing  the Sopad
    for i in range(0,len(key)):
        tmp = opad[i] ^ key[i]
        sopad.append(tmp)
    # the first concatenation
    #c1 = sipad.append(m)
    c1 = sipad + m
    # computing the inner hash
    h1 = sha1(c1).hexdigest()
    #print(h1)
    # the second concatenation
    c2 = sopad+str.encode(h1)
    # calculating the HMAC
    hmac = sha1(c2)
    return hmac

m=b"holahola9"
key=b"87654321"
print(weak_hmac(m,key,ipad,opad))
print(sha1(ipad).digest_size)