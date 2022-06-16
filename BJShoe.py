
import BJCard
import itertools
import random

class Shoe:
    
    def __init__ (self,number_of_decks = 6,deck_penetration = 1.0):

        self.__number_of_decks = number_of_decks
        self.__deck_penetration = deck_penetration
        self.__new_shoe = []

        for self.decks in range (0,number_of_decks):
            self.__new_shoe += (list(itertools.product(BJCard.list_of_values,BJCard.list_of_suits)))
        
        random.shuffle(self.__new_shoe)

    def draw_card(self):
        Card = self.__new_shoe.pop()
        print(Card)
        return(Card)