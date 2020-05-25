# implement a funtion that given a plaintext and a 32-bytes ey "k", returns a ciphertext encrypted with a weak variant of RC4.
from Crypto.Cipher import ARC4
from Crypto.Hash import SHA

def rc4(plaintext, key):
    ciphertext=""
    cipher = ARC4.new(key)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext