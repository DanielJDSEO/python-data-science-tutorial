
#I want to recreate the game of Blackjack. I will need to use object-oriented programming to do so.
# Think about the different real-world objects in the game. There is a Deck, Cards that constitute the Deck, Players that use the Deck, and a Dealer.
# I will construct the Cards first, since that will constitute the Deck

#Card attributes are set, and so are deck ones. Now, what behaviors does a Deck have?
# A deck should be able to be dealt from, so a draw function should be possible.
# Now I want to create a shoe object to hold the necessary number of decks for one simulation
# I want to ensure I can simulate several shoes per execution of the code with a summarization of the results at the shoe level.

#I don't believe a Deck class is necessary, as the Shoe class totally encapsulates its functionality

#I created a functional Shoe as a single list with each Card as a Tuple of 2 strings, the Value and the Suit. The number of decks in the Shoe is a parameter
# along with deck penetration, although deck penetration is not functional yet. It will be used to determine how prematurely a Shoe simulation ends.
# To play real-time hands one Shoe can be used and for simulations of multiple shoes a simulator object will be created.

#Now that I have my Shoe set up, I will want to create objects for the Player and the Dealer. I will start with the Dealer.
# He needs to have 2 starting cards, one designated the Up card. He also requires the ability to draw additional cards.

#The Player and Dealer exist. Next, the instance for a single round of Blackjack needs to be created. This will mean the Player places a bet, the Dealer
# and Player draw their starting hands, the Player makes their decision, then (if the game continues) the dealer makes their decisions, and a determination
# for the round is made. This is going to necessitate that the lists and tuples are evaluated to number values.

import itertools
import random

class Card:

    list_of_values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    list_of_suits = ["spades","diamonds","hearts","clubs"]

    values_dict = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}

    #Need to figure out mechanism for determining the value of an Ace.


    def __init__(self,value,suit):
        self.value = value
        self.suit = suit

class Shoe:

    def __init__ (self,number_of_decks = 6,deck_penetration = 1.0):

        self.number_of_decks = number_of_decks
        self.deck_penetration = deck_penetration
        self.new_shoe = []

        for self.decks in range (0,number_of_decks):
            self.new_shoe += (list(itertools.product(Card.list_of_values,Card.list_of_suits)))
        
        random.shuffle(self.new_shoe)

    def draw_card(self):
        Card = self.new_shoe.pop()
        print(Card)
        return(Card)

class Dealer:

    def __init__ (self):

        self.starting_hand = []
        self.upcard = []
        

    def draw_card(self):
        Card = Shoe.new_shoe.pop()
        return(Card)

    def draw_starting_hand(self):
        self.starting_hand.append(self.draw_card()) 
        self.starting_hand.append(self.draw_card())
        self.upcard = self.starting_hand[0]
        return self.upcard


class Player:
    
    def __init__ (self):

        self.starting_hand = []
        

    def draw_card(self):
        Card = Shoe.new_shoe.pop()
        print(Card)
        return(Card)

    def draw_starting_hand(self):
        self.starting_hand.append(self.draw_card()) 
        self.starting_hand.append(self.draw_card())


class Round_of_Blackjack:

    def __init__ (self):
        pass

    def begin_round(self):

        #While loop will go up here

        Player.draw_starting_hand()
        Dealer.draw_starting_hand()


#--This is basically the block of code that checks for Blackjacks of all sorts--
        if Dealer.upcard[0] == 'A':
            if input("Insurance? (Y/N)") == 'Y':
                #IDK how insurance works but here's the mechanism placeholder
                pass
            else:
                print("Insurance closed")
            if Card.values_dict.get(Dealer.starting_hand[1][0]) == 10:
                print(Dealer.starting_hand)
                print("Dealer has Blackjack!")
                if Player.starting_hand[0][0] == 'A' or Player.starting_hand[1][0] == 'A':
                    if Card.values_dict.get(Player.starting_hand[0][0]) == 10 or Card.values_dict.get(Player.starting_hand[1][0]) == 10:
                        print("Player has Blackjack! /n Push!")
                        #Break loop here - this is an End condition
                #Break loop here - this is an End condition
        elif Card.values_dict.get(Dealer.starting_hand[0][0]) == 10 and Dealer.starting_hand[1][0] == 'A':
            print("Dealer has Blackjack!")
            if Player.starting_hand[0][0] == 'A' or Player.starting_hand[1][0] == 'A':
                if Card.values_dict.get(Player.starting_hand[0][0]) == 10 or Card.values_dict.get(Player.starting_hand[1][0]) == 10:
                    print("Player has Blackjack! /n Push!")
                    #Break loop here - this is an End condition
            #Break loop here - this is an End condition
        else:
            if Player.starting_hand[0][0] == 'A' or Player.starting_hand[1][0] == 'A':
                if Card.values_dict.get(Player.starting_hand[0][0]) == 10 or Card.values_dict.get(Player.starting_hand[1][0]) == 10:
                    print("Player has Blackjack!")
#--This is basically the block of code that checks for Blackjacks of all sorts--
    
    



        

        #print(Card.values_dict.get(Player.starting_hand[0][0]))
        #print(Dealer.upcard)
        print(Dealer.starting_hand)
        #print(len(Shoe.new_shoe))




Round_of_Blackjack = Round_of_Blackjack()
Shoe = Shoe()
Dealer = Dealer()
Player = Player()

Round_of_Blackjack.begin_round()
