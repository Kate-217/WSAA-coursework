# Author Katerina Lisovenko 
# This program "deals" (prints out) n cards and calculates duplicates and triples in its values.


import requests
#import pandas as pd
from collections import Counter

# Shuffle and get the deck_id

deck_count = 1 #count for decks
shuffle_url = f"https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count={deck_count}"
response = requests.get(shuffle_url).json()
deck_id = response['deck_id']

#print(deck_id)
# get the cards

count=5 #count for cards
draw_url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count={count}"
cards = requests.get(draw_url).json()["cards"]
# print(cards)
#print(type(cards))

values = []
suits = []
print("Your cards:")
for card in cards:
    print(f"{card['value']} {card['suit']}")
    values.append(card['value'])
    suits.append(card['suit'])
#print(f'Values: {values}')
#print(f'Suits: {suits}')

# searched with chatGPT:
counts = Counter(values) 

pairs = len([count for count in counts.values() if count == 2])
triples = len([count for count in counts.values() if count == 3])

if pairs == 1:
    print('You have a pair')
if triples == 1:
    print('You have a triple')



    

