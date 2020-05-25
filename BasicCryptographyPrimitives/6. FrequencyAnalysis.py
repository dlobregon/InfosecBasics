#implement a heuristic plaintext detection using frequency analysis:
#implement a function "is_english":
#1- receives a string
#2- Makes sure it consists of only ASCII charateres (using the provided "is_ascii" function)
#3- counts the most frequent letters in it.
#4- Makes sure they're one of the 6 most frequent letters in English (e,t, a, o,i,n)


from collections import Counter

# random text generated
randomText="""
How promotion excellent curiosity yet attempted happiness. Gay prosperous impression had conviction. For every delay death ask style. Me mean able my by in they. Extremity now strangers contained breakfast him discourse additions. Sincerity collected contented led now perpetual extremely forfeited. 

Full age sex set feel her told. Tastes giving in passed direct me valley as supply. End great stood boy noisy often way taken short. Rent the size our more door. Years no place abode in ﻿no child my. Man pianoforte too solicitude friendship devonshire ten ask. Course sooner its silent but formal she led. Extensive he assurance extremity at breakfast. Dear sure ye sold fine sell on. Projection at up connection literature insensible motionless projecting. 

Kindness to he horrible reserved ye. Effect twenty indeed beyond for not had county. The use him without greatly can private. Increasing it unpleasant no of contrasted no continuing. Nothing colonel my no removed in weather. It dissimilar in up devonshire inhabiting. 

Started several mistake joy say painful removed reached end. State burst think end are its. Arrived off she elderly beloved him affixed noisier yet. An course regard to up he hardly. View four has said does men saw find dear shy. Talent men wicket add garden. 

Depart do be so he enough talent. Sociable formerly six but handsome. Up do view time they shot. He concluded disposing provision by questions as situation. Its estimating are motionless day sentiments end. Calling an imagine at forbade. At name no an what like spot. Pressed my by do affixed he studied. 

Piqued favour stairs it enable exeter as seeing. Remainder met improving but engrossed sincerity age. Better but length gay denied abroad are. Attachment astonished to on appearance imprudence so collecting in excellence. Tiled way blind lived whose new. The for fully had she there leave merit enjoy forth. 

Tolerably earnestly middleton extremely distrusts she boy now not. Add and offered prepare how cordial two promise. Greatly who affixed suppose but enquire compact prepare all put. Added forth chief trees but rooms think may. Wicket do manner others seemed enable rather in. Excellent own discovery unfeeling sweetness questions the gentleman. Chapter shyness matters mr parlors if mention thought. 

Article nor prepare chicken you him now. Shy merits say advice ten before lovers innate add. She cordially behaviour can attempted estimable. Trees delay fancy noise manor do as an small. Felicity now law securing breeding likewise extended and. Roused either who favour why ham. 

Greatest properly off ham exercise all. Unsatiable invitation its possession nor off. All difficulty estimating unreserved increasing the solicitude. Rapturous see performed tolerably departure end bed attention unfeeling. On unpleasing principles alteration of. Be at performed preferred determine collected. Him nay acuteness discourse listening estimable our law. Decisively it occasional advantages delightful in cultivated introduced. Like law mean form are sang loud lady put. 

Agreed joy vanity regret met may ladies oppose who. Mile fail as left as hard eyes. Meet made call in mean four year it to. Prospect so branched wondered sensible of up. For gay consisted resolving pronounce sportsman saw discovery not. Northward or household as conveying we earnestly believing. No in up contrasted discretion inhabiting excellence. Entreaties we collecting unpleasant at everything conviction. 

"""


def is_ascii(s):
    return all(ord(c) < 128 for c in s)

def is_english(s):
    result=False
    simbol_array=[]
    #we need to iterate over the text to find an replace what is not 
    # an ascii symbol
    topCharacters=["e","t","a","o","i","n"]
    if is_ascii(s):
        simbol_array=list(s)              
        # get the the most common values from our simbol array
        letterCounter=Counter(simbol_array)
        mostCommonCharacters=letterCounter.most_common(3)
        #check if the most common characters are in english
        if (mostCommonCharacters[0][0] in topCharacters)or (mostCommonCharacters[1][0] in topCharacters) or (mostCommonCharacters[2][0] in topCharacters):
            result=True
    return result

print(is_english(randomText))
        
