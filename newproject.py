
#Initialize the game
#Present options - rock paper scissors
#Take user input
#Computer makes its decision (random)
#Determine who wins

import random

def rock_paper_scissors ():
    player_choice = ""
    computer_choice = ""
    player_wins = 0
    computer_wins = 0
    ROCK = "ROCK"
    PAPER = "PAPER"
    SCISSORS = "SCISSORS"
    options = [ROCK,PAPER,PAPER]

    while player_wins < 3 and computer_wins < 3:
        player_choice = input("Rock, Paper, or Scissors? \n" ).upper()
        computer_choice = random.choice(options)
    
        if player_choice == ROCK:
            if computer_choice == ROCK:
                print("Tie")
            elif computer_choice == PAPER:
                print("Paper beats Rock. Computer wins!")
                computer_wins += 1
            elif computer_choice == SCISSORS:
                print("Rock beats Scissors. Player wins!")
                player_wins += 1
        elif player_choice == PAPER:
            if computer_choice == ROCK:
                print("Paper beats Rock. Player wins!")
                player_wins += 1
            elif computer_choice == PAPER:
                print("Tie")
            elif computer_choice == SCISSORS:
                print("Scissors beats Paper. Computer wins!")
                computer_wins += 1
        elif player_choice == SCISSORS:
            if computer_choice == ROCK:
                print("Rock beats Scissors. Computer wins!")
                computer_wins += 1
            elif computer_choice == PAPER:
                print("Scissors beats Paper. Player wins!")
                player_wins += 1
            elif computer_choice == SCISSORS:
                print("Tie")
        else:
            print("Learn to type retard kek")


rock_paper_scissors()