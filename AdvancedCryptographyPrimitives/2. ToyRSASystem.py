# implement a Toy RSA system:

# implement the function "encrypt", which receives a number and a public key and returns the encrypted number;
# and the function "decrypt", which receives an encrypted number and the private key, and returns the original number

n = 33
e = 7
d = 3
public_key = (n, e)
private_key = (n, d)

def encrypt(m, public_key):
    c= m ** e % n
    return c

def decrypt(c, private_key):
    m = c ** d % n
    return m

plaintext = 19
ciphertext = encrypt(plaintext,public_key)
print(ciphertext)
plaintextDecrypted = decrypt(ciphertext, private_key)
print(plaintextDecrypted)
