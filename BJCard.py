#This class serves as the first building block, the Card object that will constitute the Deck object. The Deck objects created will go into the Shoe object,
# and the Player and Dealer objects will interact with the Shoe object to draw Card objects. This way unique data-collecting methods can be invoked on any objects.

class Card:
    
    list_of_values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    list_of_suits = ["spades","diamonds","hearts","clubs"]

    values_dict = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10,
                    'A':{True: 1, False: 11}}
