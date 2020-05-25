# implementing a real RSA system
# use pycrypto to sign and verify message usin RSA

from Crypto.PublicKey import RSA

#this library is used in the updated library not on the condeboard environment. 
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256

key = RSA.generate(2048)

private_key = key.exportKey('PEM')
public_key = key.publickey().exportKey('PEM')

# a sample message:
sampleMessage ="Hello world :)"
def sign(m, private_key):
    # importing the private key
    key = RSA.importKey(private_key)
    # creating a hash
    digest = SHA256.new(m.encode("utf8"))
    # if the message is a number
    #digest = SHA256.new(str(m).encode("utf8"))
    sigma = PKCS1_v1_5.new(key).sign(digest)
    return sigma
   
def verify(m, s, public_key):
    key = RSA.importKey(public_key)
    digest= SHA256.new(m.encode("utf8"))
    # if the message is a number
    #digest = SHA256.new(str(m).encode("utf8"))
    sigma= PKCS1_v1_5.new(key).verify(digest,s)
    return sigma

print("the message is %s " % sampleMessage)
sigma = sign(sampleMessage, private_key)
print(sigma)
print("the signature check is %s" % verify(sampleMessage, sigma,public_key))