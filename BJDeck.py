#This Deck class will generate a Deck object consisting of Card objects. It will be used to fill the Shoe object.

import BJCard
import itertools
import random


class Deck:
    
    def __init__(self):
        
        self.__new_deck = new_deck = []

        for self.values in range(0,13):
            card_value = range
            for self.suits in range (0,4):
                card_suite = range
                self.__new_deck += BJCard.Card(card_value,card_suite)

#Left off trying to instantiate 52 Card objects within the BJDeck module. Card object is not iterable so I'm trying to remedy that in the BJCard module.
        
            
    def __len__(self):
        return self.__new_deck

d1 = Deck()

print (d1.__dict__)
