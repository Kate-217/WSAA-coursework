# Author Katerina Lisovenko 
# This program "deals" (prints out) n cards


import requests
#import pandas as pd
from collections import Counter

# Shuffle and get the deck_id

deck_count = 1 #count for decks
count = 5 #count for cards

shuffle_url = f"https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count={deck_count}"
response = requests.get(shuffle_url).json()
deck_id = response['deck_id']
#print(deck_id)

# get the cards
draw_url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count={count}"
cards = requests.get(draw_url).json()["cards"]
#print(cards)

# print the cards
values = []
suits = []
print("Your cards:")
for card in cards:
    print(f"{card['value']} {card['suit']}")
    values.append(card['value'])
    suits.append(card['suit'])
#print(f'Values: {values}')
#print(f'Suits: {suits}')





    

