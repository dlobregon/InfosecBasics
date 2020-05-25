from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

key = RSA.generate(2048)

private_key = key.exportKey('PEM')
public_key = key.publickey().exportKey('PEM')

def encrypt(m, public_key):
    key = RSA.importKey(public_key)
    cipher = PKCS1_OAEP.new(key)
    ciphertext =cipher.encrypt(m)
    return ciphertext

def decrypt(c, private_key):
    key = RSA.importKey(private_key)
    cipher=PKCS1_OAEP.new(key)
    plaintext=cipher.decrypt(c)
    return plaintext
message = b"hola jodido mundo"
print(message)
ciphertext = encrypt(message, public_key)
print(ciphertext)
plaintext = decrypt(ciphertext, private_key)
print(plaintext)


# the following is to run in the old version fo PyCrypto
# and is the version that course codeboard has.
key = RSA.generate(2048)

private_key = key.exportKey('PEM')
public_key = key.publickey().exportKey('PEM')

def encrypt1(m, public_key):
    key = RSA.importKey(public_key)
    #cipher = PKCS1_OAEP.new(key)
    ciphertext =key.encrypt(m, None)
    return ciphertext

def decrypt2(c, private_key):
    key = RSA.importKey(private_key)
    #cipher=PKCS1_OAEP.new(key)
    plaintext=key.decrypt(c)
    return plaintext
