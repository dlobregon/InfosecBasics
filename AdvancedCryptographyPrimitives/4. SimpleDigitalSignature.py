
# Implement the function "sign", which receives a number and a private key and returns a signature of it;
# and the function verify, which receives a number with a signature and the public key, and returns whether the signature is valid



n = 33
e = 7
d = 3
public_key = (n, e)
private_key = (n, d)

def sign(m, private_key):
    # computhe sigma
    sigma = m ** private_key[1] % private_key[0]
    return sigma

def verify(m, s, public_key):
    # this function returns true when the signature is valid.
    mprime= s ** public_key[1] % public_key[0]
    return mprime == m

# checking the functions results. 
sigma = sign(4, private_key)
print("the digital signature is: %s " % sigma)
print("the verify result is:  %s " % verify(4,sigma, public_key))
