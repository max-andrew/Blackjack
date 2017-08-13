#
# cards
# author: John Donaldson
#
from random import randint

def shuffle(deck):
    for k in range(100): # do it 100 times
        card = deck.pop(randint(0,51)) # remove a random card from the deck
        deck.append(card)

def make_deck():
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append((suit,rank))
    return deck

suits = ['spades','hearts','diamonds','clubs']
ranks = ['ace','two','three','four','five','six','seven','eight','nine','ten','jack','queen','king']

# create a deck of cards
deck = make_deck()

# print it
print deck
print

# shuffle it
shuffle(deck)

# print the shuffled deck
print [rank+' of '+suit for (suit,rank) in deck]


        
