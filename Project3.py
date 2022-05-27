import random 

def chooseRandomWord(difficulty):
    theword = ""
    words = []
    
    with open('sowpods.txt', 'r') as file:
        words = file.readlines()

        for i in range(len(words)):
           words[i] = words[i].replace('\n','')
        #print(words)

        
    if difficulty=="1":
        while len(theword) != 5 and len(theword) != 6:
            word_index = random.randrange(0, len(words))
            theword = words[word_index]

    if difficulty=="2":
        while len(theword) != 7 and len(theword) != 8:
            word_index = random.randrange(0, len(words))
            theword = words[word_index]

    if difficulty=="3":
        while len(theword) < 9:
            word_index = random.randrange(0, len(words))
            theword = words[word_index]

    return theword

        
# print(chooseRandomWord("1"))