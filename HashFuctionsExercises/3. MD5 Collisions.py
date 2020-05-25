import hashlib
from itertools import product
from string import printable
import time
# The function "weak_md5" is a "weaker" version of MD5, 
# using the first 5 bytes of the MD5 hash. This means its hashing size is n=40 and it can be
# be brute forced rather easily.

# implement a function "find_colissions" that loops over all the possible strings until it finds an arbitrary
# that is, two different strings whose hash is the same- and returns them (as a tuple)


def weak_md5(s):
    return hashlib.md5(s).digest()[:5]


def find_collisions():
    s1=""
    s2=""
    dictionary={}
    possibleValues=list(product(printable[:95],repeat=4))
    #print(len(possibleValues))
    for value in possibleValues:
        valor="".join(value)
        hashed=weak_md5(valor.encode("utf-8"))
        if hashed in dictionary:
            # we have found a collision
            s1=dictionary[hashed]
            s2="".join(value)
            break
        else:   
            #updating the hash dictionary
            dictionary[hashed]=valor
    return(s1,s2)


start_time=time.time()
matchedValues =find_collisions()
print("-------- %s seconds -------" % (time.time()-start_time))
print(matchedValues)
print(weak_md5(matchedValues[0].encode("utf-8")))
print(weak_md5(matchedValues[1].encode("utf-8")))