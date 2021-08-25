#This script takes one word and inserts random letters into it - Palmfeldt 21-04-05
#Used for testing hashing algorithms
import random, os, string

# Output file
filea = os.getcwd()
filea+="\\uniformitytest.txt"

lowercase = list(string.ascii_lowercase)
uppercase = list(string.ascii_uppercase)
specials = list(set(string.punctuation))

def diffGen(word):
    imputpath = random.randint(0,len(word)-1)
    upperOrLower = random.randint(0,1)
    # Randoms the capitalizations
    word = list(word)
    if upperOrLower == 1:
        word[imputpath]+=(random.choice(lowercase))
    else:
        word[imputpath]+=(random.choice(uppercase))

    word[imputpath]+=(random.choice(specials)) 
    return ''.join(word)


def genAndWrite(filepath, gen, word):
    wordlist = []
    for i in range(gen): #run the script for 4000
        wordlist.append(diffGen(word)) #this is the word
    wordlist = set(wordlist)
    with open(filepath,"w") as myfile: 
        for i in wordlist:
            myfile.write(i+' ')
    return len(wordlist)


#print(genAndWrite(filea, 9000, "Hello World"))
