#Brute force a message encrypted with AES-CBC, given that it was encrypted with a key that represents a phone number of someone
#from Tel-Aviv, padded with zeroes (in other words, 9 digits, begining with 036, and with trailing "0" to a length of 16 bytes.
# like this 036######0000000





from Crypto.Cipher import AES
from Crypto import Random
from collections import Counter
import itertools
#import sys # ignore
#sys.path.insert(0,'.') # ignore
#from Root.prev_func import aes_decrypt, is_english

#Functions to test the brute_force_aes
# the goal is to crack the key
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
def is_ascii(s):
    return all(ord(c) < 128 for c in s)

def is_english(s):
    result=False
    simbol_array=[]
    #we need to iterate over the text to find an replace what is not 
    # an ascii symbol
    topCharacters=["e","t","a","o","i","n"]
    if is_ascii(s):
        for i in range(0,len(s)):
            # check if the current character is a valid english Character. 
            currentCharacter= s[i]
            if is_ascii(currentCharacter):
                # insert each character valid in the simbol array.
                simbol_array.append(currentCharacter)                
        # get the the most common values from our simbol array
        letterCounter=Counter(simbol_array)
        mostCommonCharacters=letterCounter.most_common(3)
        #check if the most common characters are in english
        if (mostCommonCharacters[0][0] in topCharacters)or (mostCommonCharacters[1][0] in topCharacters) or (mostCommonCharacters[2][0] in topCharacters):
            result=True
    return result

def brute_force_aes(ciphertext):
    plaintext=""
    #defining the start of the key
    startKey="036"
    endKey="0000000"
    cracked=False
    middleKey=""
    # we need to make an array with the all the combinations of numbers to generate a six digits numbers
    digits= [p for p in itertools.product([0,1,2,3,4,5,6,7,8,9], repeat=6)]
    #pass # return plaintext (in 'latin1', from aes_decrypt()), k
    for cc in range(0,len(digits)):
        middleKey=str(digits[cc][0])+str(digits[cc][1])+str(digits[cc][2])+str(digits[cc][3])+str(digits[cc][4])+str(digits[cc][5])
        completeKey=startKey+middleKey+endKey
        completeKey1=completeKey.encode()
        suggestedPlaintext=aes_decrypt(ciphertext,completeKey1)
        cracked=is_english(suggestedPlaintext)
        if cracked:
            plaintext=suggestedPlaintext
            break
    # in this case we enconde the plaintext to "latin-1", just to see the response in our test.
    return plaintext.encode("latin-1"), completeKey.encode() 
#printing the plaint
print(brute_force_aes(cipher))