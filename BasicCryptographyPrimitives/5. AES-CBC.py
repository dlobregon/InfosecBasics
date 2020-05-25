# use pyCrypto to enrypt with AES-CBC.
#1- Implement a function "encrypt", that given a plaintext and a 16-byte (128 bit) key k, picks a random 16-byte (128 bits) IV, and returns a ciphertext encrypted
# with AES-CBC with the IV preprended to the ciphertext (in bytes)

# You may assume that the plaintext length (in bytes) is a multiple of 16
#2- Implement a function "decrypt", that  given a ciphertext (as formatted by the encrypt function) and 16-byte (128 bit) key "k", returns the plaintext as decrypted
# by "AES-CBC" (in "latin1")

from Crypto.Cipher import AES
from Crypto import Random

blockSize=16 #bytes
def aes_encrypt(plaintext, k):
    # in this example we assume that the plaintext is in bytes
    # in this example is not necessary transform the plaintext to a padded version of itself.
    #now we generate randomly our IV block
    iv = Random.new().read(blockSize)
    # we need to configure our AES with our IV and the key
    cipher = AES.new(k, AES.MODE_CBC, iv)
    #make the cipherText
    ciphertext = iv + cipher.encrypt(plaintext)
    return ciphertext

def aes_decrypt(ciphertext, k):
    # this function will return the plaintext in "latin1"
    # the firts step is to extract the IV
    iv= ciphertext[:blockSize]
    #make our custom decryptert using the key
    cipher = AES.new(k, AES.MODE_CBC, iv)
    #now we take the real ciphertext extracting the IV block that begins the input ciphertext
    plaintext = cipher.decrypt(ciphertext[AES.block_size:]).decode("latin1")
    return plaintext #(in 'latin1')
# testing the encryption function 
cipher =aes_encrypt(b'hola uno1 dos2  ', b'0361234560000000')
# testing the decryption function
print(aes_decrypt(cipher,b'0361234560000000'))