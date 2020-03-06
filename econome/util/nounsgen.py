import random

def genNoun():
    o = open("../data/nounlist.txt","rU")
    s = o.read()
    spl = s.split("\n")
    return random.choice(spl)

print genNoun()
