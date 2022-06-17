#Going back to simply using the Shoe object as the smallest discrete object rather than constituent Card and Deck objects.

class Card:

    list_of_values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    list_of_suits = ["spades","diamonds","hearts","clubs"]

    values_dict = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10,
                    'A':{True: 1, False: 11}}

    def __init__ (self,value,suit):
        self.__value = value
        self.__suit = suit