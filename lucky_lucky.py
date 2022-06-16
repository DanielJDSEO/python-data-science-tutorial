#I am going to re-create what I've done for Blackjack so far but I'm going to build the Lucky Lucky minigame first. This will be much easier to simulate
# because the game rules are simpler. I will take this opportunity to re-create the class objects using additional things I've learned from watching
# Precipio videos (special methods, the property decorator, getters/setters, subclasses, class vs. instance variables, etc.)

import itertools
import random

class Card:
    list_of_values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    list_of_suits = ["spades","diamonds","hearts","clubs"]

    values_dict = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10,
                    'A':{True: 1, False: 11}}

    def __init__(self,value,suit):
        self.__value = value
        self.__suit = suit


class Shoe:
    
    def __init__ (self,number_of_decks = 6,deck_penetration = 1.0):

        self.__number_of_decks = number_of_decks
        self.__deck_penetration = deck_penetration
        self.__new_shoe = []

        for self.decks in range (0,number_of_decks):
            self.__new_shoe += (list(itertools.product(Card.list_of_values,Card.list_of_suits)))
        
        random.shuffle(self.__new_shoe)

    def draw_card(self):
        Card = self.new_shoe.pop()
        print(Card)
        return(Card)