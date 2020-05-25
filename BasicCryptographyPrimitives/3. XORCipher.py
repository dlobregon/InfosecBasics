# write a xor cipher: implement a function "encrypt" that given a plaintext string and a key "k", also a string.
# returns a ciphertext where each character is XORed with its respective character in "k". Assume that the plaintext and key have the same lenght.


def encrypt(plaintext, keystream):
    ciphertext =[]
    if len(plaintext)==len(keystream):
        for i in range (0,len(plaintext)):
            #we are going to make covert the two current characters in order to convert to xored value
            plaintextCurrentChar= plaintext[i]
            keystreamCurrentChar=keystream[i]
            xoredChar= ord(plaintextCurrentChar) ^ ord(keystreamCurrentChar)
            #now we need to convert the 
            ciphertext.append(chr(xoredChar)) 
    return "".join(ciphertext)
encrypt("hola","tres")

# I have found this solution on internet but I just write it to prove my own function 
def encrypt2(a, b):
    print(''.join([hex(ord(a[i%len(a)]) ^ ord(b[i%(len(b))]))[2:] for i in range(max(len(a), len(b)))]))
    return ''.join([hex(ord(a[i%len(a)]) ^ ord(b[i%(len(b))]))[2:] for i in range(max(len(a), len(b)))])

encrypt2("hola","tres")