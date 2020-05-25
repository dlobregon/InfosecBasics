# implement a hash function "simple_hash" that given a string s, computes its hash as follows with R=7,and for every char in the string, 
# multiplies r by 31, adds the character to r, and keeps everything modulo 2 powers 16

def simple_hash(s):
    r=7
    for i in range(0, len(s)):
        r=r*31
        r=(r+ord(s[i]))% (2**16)
    return r

