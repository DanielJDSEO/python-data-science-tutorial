
#I want to recreate the game of Blackjack. I will need to use object-oriented programming to do so.
#Think about the different real-world objects in the game. There is a Deck, Cards that constitute the Deck, Players that use the Deck, and a Dealer.
#I will construct the Cards first, since that will constitute the Deck

#Card attributes are set, and so are deck ones. Now, what behaviors does a Deck have?
#A deck should be able to be dealt from, so a draw function should be possible.

import itertools
import random


class Card:

    list_of_values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    list_of_suits = ["spades","diamonds","hearts","clubs"]

    def __init__(self,value,suit):
        self.value = value
        self.suit = suit


class Deck:
    
    new_deck = list(itertools.product(Card.list_of_values,Card.list_of_suits))
    random.shuffle(new_deck)

    def __init__ (self):
        pass

    def draw_card(self):
        Card = self.new_deck.pop()
        print(Card)
        return(Card)

Deck_1 = Deck()

# Deck_1.draw_card()
# Deck_1.draw_card()

cards_burned = 0

for cards in range(0,50): 
    Deck_1.draw_card()
    cards_burned += 1
print(len(Deck_1.new_deck))
print(Deck_1.new_deck)
print(cards_burned)