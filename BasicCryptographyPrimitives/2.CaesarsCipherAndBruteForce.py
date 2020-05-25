# implementing a simple Caesar's cipher 
# then brute-force the cipher finding the plaintext and key
# the ciphertext is "kyvtrmrcipnzccrkkrtbwifdkyvefikynvjkrkeffe"


alphabet = "abcdefghijklmnopqrstuvwxyz"

def encrypt(plaintext, k):
    ciphertext = []
    for c in plaintext:
        i = alphabet.index(c)
        j = (i + k) % len(alphabet)
        ciphertext.append(alphabet[j])
    return ''.join(ciphertext)

def decrypt(ciphertext, k):
    return encrypt(ciphertext, -k)
    
def brute_force(ciphertext):
    for i in range(0,len(alphabet)):
        #print(len(alphabet)-i)
        print(decrypt(ciphertext, -i))
    
brute_force("kyvtrmrcipnzccrkkrtbwifdkyvefikynvjkrkeffe")
