# Burte-force the hash function you've just written!
# Implement a function crack that given a string "s", loops until it finds a different string that collides with it, and returns the
# different string. 

from itertools import product
from string import printable
# how to use the itertools.product()
# 1- it makes the Cartesian product of two sets A and B.
#   it is the set of all ordered pairs (a,b) where a is in A and b in B.
# 2- it is equivalent to nested "for" loopes. 

#example =list(product([1,2,3],repeat=3))
#print(example)
def simple_hash(s):
    r = 7
    for c in s:
        r = (r * 31 + ord(c)) % 2**16
    return r

def crack(s):
    # getting the hash
    hash=simple_hash(s)
    match="empty"
    extractValue=tuple(s)
    possibleValues=list(product(printable, repeat=3))
    for value in possibleValues:
        if value!=extractValue and hash== simple_hash(value):
            match = ''.join(value)
            break
    return match

# some samples
print(crack("01"))
print("----------------")
print(crack("11"))
print("----------------")
print(crack("21"))
print("----------------")
print(crack("31"))
print("----------------")