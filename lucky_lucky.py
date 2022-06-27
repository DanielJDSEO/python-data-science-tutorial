#I am using the Lucky Lucky class to run the game instance and initializing the Shoe and Player instances within the game instance. This should provide an
# overarching instance to do additional actions: Pull cards from the Shoe instance, move them to the game instance, and then from the game instance
# into the Player instance.

import itertools
import random


class Card:
    
    list_of_values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    list_of_suits = ["spades","diamonds","hearts","clubs"]

    values_dict = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10,
                    'A': 0}

    def __init__ (self,value,suit):
        self.__value = value
        self.__suit = suit


class Shoe(Card):
    
    def __init__ (self,number_of_decks = 6,deck_penetration = 1.0):

        self.__number_of_decks = number_of_decks
        self.__deck_penetration = deck_penetration
        self.__new_shoe = []
        self.__card = []

        for self.decks in range (0,number_of_decks):
            self.__new_shoe += (list(itertools.product(self.list_of_values,self.list_of_suits)))
        random.shuffle(self.__new_shoe)

    def draw_card(self):
        __card = self.__new_shoe.pop()
        print(len(self.__new_shoe))
        print(__card)
        return(__card)

    # def deal_starting_hand(self):
    #     self.draw_card()
    #     self.draw_card()


class Player:
    
    def __init__ (self):
        self.__bet = 0
        self.__starting_hand = []

class Dealer(Player):

    def __init__(self):
        self.__upcard = upcard = []
        self.__starting_hand = starting_hand = []


class lucky_lucky(Shoe,Player):

    def __init__(self):
        self.__s1 = Shoe()
        self.__p1 = Player()
        self.__d1 = Dealer()
        self.__p1holding = []
        self.__d1holding = []
        self.__luckyluckyhand = []
        self.__luckyluckyhand_aces = 0

    def draw_starting_hand(self):
        
        #Cards are drawn from the Shoe instance that is initialized in the lucky_lucky instance. They are then appended to lists initialized in the
        # lucky_lucky instance.
        self.__p1holding.append(self.__s1.draw_card())
        self.__p1holding.append(self.__s1.draw_card())
        self.__d1holding.append(self.__s1.draw_card())
        self.__d1holding.append(self.__s1.draw_card())
        
        #The lists initialized in the lucky_lucky instance are copied to the Player and Dealers' instances' lists that were initialized in the lucky_lucky 
        # instance.
        self.__p1.__starting_hand = self.__p1holding
        self.__d1.__starting_hand = self.__d1holding
        self.__d1.__upcard = self.__d1.__starting_hand[0]

        #The __luckyluckyhand list in the lucky_lucky instance is filled with the Player and Dealer instances' lists using append. In the process,
        # The value of each card is checked to see whether if it's an Ace or not. If so, it adds to the __luckyluckyhand_aces counter.
        if self.__p1.__starting_hand[0][0] == 'A':
            self.__luckyluckyhand.append(self.__p1.__starting_hand[0])
            self.__luckyluckyhand_aces += 1
        else:
            self.__luckyluckyhand.append(self.__p1.__starting_hand[0])

        if self.__p1.__starting_hand[1][0] == 'A':
            self.__luckyluckyhand.append(self.__p1.__starting_hand[1])
            self.__luckyluckyhand_aces += 1
        else:
            self.__luckyluckyhand.append(self.__p1.__starting_hand[1])

        if self.__d1.__upcard[0][0] == 'A':
            self.__luckyluckyhand.append(self.__d1.__upcard)
            self.__luckyluckyhand_aces += 1
        else:
            self.__luckyluckyhand.append(self.__d1.__upcard)

        print(self.__luckyluckyhand)
        print(self.__luckyluckyhand_aces)

#Here's my rough draft concept:
# When drawing the starting hands & upcard, look for Aces. If Aces, add to a counter.
# During win condition evaluation, check to see if the Ace counter is not zero.
# If it isn't, need to generate two hands with 1 and 11 or two hands with 2 and 12, or automatic loss with three Aces.
# Aces will read out of the dict at int 0 to essentially skip them.
# Suit will be evaluated once the more exclusive win conditions are met to save time.


#Now, how to count the Aces as cards are drawn from the Shoe?
# I'm going to count the Aces as they are added to the luckyluckyhand list, since those are the ones we care about.



    def winning_conditions(self):

        if (self.values_dict.get(self.__luckyluckyhand[0][0]) + self.values_dict.get(self.__luckyluckyhand[1][0]) + self.values_dict.get(self.__luckyluckyhand[2][0])) == (19 or 20):
            return print ("Nice!")
        else:
            return print ("Not Nice!")

    def winning_conditions_test(self):
        return print(type(self.values_dict.get(self.__luckyluckyhand[0][0])))



game1 = lucky_lucky()

game1.draw_starting_hand()

# game1.winning_conditions_test()

game1.winning_conditions()