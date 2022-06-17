#I am going to re-create what I've done for Blackjack so far but I'm going to build the Lucky Lucky minigame first. This will be much easier to simulate
# because the game rules are simpler. I will take this opportunity to re-create the class objects using additional things I've learned from watching
# Precipio videos (special methods, the property decorator, getters/setters, subclasses, class vs. instance variables, etc.)

#Now that I've made the instance variables 'private', I'm having trouble drawing a card from the Shoe instance.
# I want to re-write the code so that Card objects are created and placed into the Shoe object, and then the Dealer and Player draw 
# the Card objects from the Shoe object. Then, I want evaluations performed on the Card objects that the Dealer and Player are holding. I will create separate
# files for the Card and Shoe classes.

import itertools
import random



class lucky_lucky:

    def __init__(self):
        self.__s1 = Shoe()
        self.__p1 = Player()

    def draw_starting_hand(self):
        self.__s1.deal_starting_hand()




class Card:
    
    list_of_values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    list_of_suits = ["spades","diamonds","hearts","clubs"]

    values_dict = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10,
                    'A':{True: 1, False: 11}}

    def __init__ (self,value,suit):
        self.__value = value
        self.__suit = suit


class Shoe:
    
    def __init__ (self,number_of_decks = 6,deck_penetration = 1.0):

        self.__number_of_decks = number_of_decks
        self.__deck_penetration = deck_penetration
        self.__new_shoe = []
        self.__card = []

        for self.decks in range (0,number_of_decks):
            self.__new_shoe += (list(itertools.product(Card.list_of_values,Card.list_of_suits)))
        random.shuffle(self.__new_shoe)

    def draw_card(self):
        __card = self.__new_shoe.pop()
        print(len(self.__new_shoe))
        print(__card)
        return(__card)

    def deal_starting_hand(self):
        self.draw_card()
        self.draw_card()


class Player:
    
    def __init__ (self):
        self.__bet = 0
        self.__starting_hand = []
        self.__current_hand = self.__starting_hand

    def hit(self):
        self.__current_hand.append(self.draw_card())
        print(self.__current_hand)

    # def draw_card(self):
    #     Card = BJShoe.__new_shoe.pop()
    #     print(Card)
    #     return(Card)

    def draw_starting_hand(self):
        self.__starting_hand.append(self.draw_card()) 
        self.__starting_hand.append(self.draw_card())


game1 = lucky_lucky()

game1.draw_starting_hand()