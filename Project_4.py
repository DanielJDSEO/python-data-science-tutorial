from Project3 import chooseRandomWord


def displayHangman(num): 
    print('  +---+') 
    print('  |   |') 
    if num == 1: 
        print('  O   |') 
        print('      |') 
        print('      |') 
    elif num == 2: 
        print('  O   |') 
        print(' /    |') 
        print('      |') 
    elif num == 3: 
        print('  O   |') 
        print(' /|   |') 
        print('      |') 
    elif num == 4: 
        print('  O   |') 
        print(' /|\  |') 
        print('      |') 
    elif num == 5: 
        print('  O   |') 
        print(' /|\  |') 
        print(' /    |') 
    elif num == 6: 
        print('  O   |') 
        print(' /|\  |') 
        print(' / \  |') 
    else: 
        print('      |') 
        print('      |') 
        print('      |') 
    print('      |') 
    print('=========')  
    

#Now that the game is functional, optimize it by:
#Make it pull a word from the sowpods file
#Toggleable difficulty


print("Choose a Difficulty (1 is the easiest, 3 is the hardest")
difficulty = input()

# word = chooseRandomWord(difficulty)

#It's taking the sowpods word BUT not finding all occurences of a single letter guess. Next step is to debug and find why.
 

word="Cheese"
wordupper=word.upper()
answer = list(wordupper)
progress = []
usedletters = []
position = ""
attempts = 0
guess = ""
counter = 0
hitmarker = 0
progress_check = 0
remaining_guesses = 0
number_of_guesses = 6

for char in answer:
        progress.append("_")


while counter < number_of_guesses:

    displayHangman(counter)
    print("\n Pick a letter dumbhead")
    print("=================================================================")
    
    remaining_guesses = number_of_guesses - counter
    
    print(progress)
    print("Guesses Remaining: %s" %remaining_guesses)
    print ("Used Letters: %s" %usedletters )

    guessraw = input()
    guess = guessraw.upper()

    if guessraw.isdigit() == False and len(guessraw) == 1 and guessraw.isalpha() == True:
        pass
    else:
        print("You must enter a single alphabetic character")
        continue


    usedletters.append(guess)

    hitmarker = 0
    progress_check = 0

    for char in answer:
        if char == guess:
            position = answer.index(char,hitmarker)
            hitmarker = 1+position
            progress[position] = guess
        

    if hitmarker == 0:
        counter += 1
    
    
    for char in progress:
        if char != "_":
            progress_check += 1
            if progress_check == len(answer):
                print("The answer is %s . You Win!" %answer)
                counter = number_of_guesses + 1
        if counter == number_of_guesses:
            print ("You suck at this. The answer is %s" %answer)
            break
        