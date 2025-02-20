# Write a program that "deals" (prints out) 5 cards

import requests

# Shuffle and get the deck_id

shuffle_url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
response = requests.get(shuffle_url).json()
deck_id = response['deck_id']

#print(deck_id)

# get the cards
draw_url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5"
cards = requests.get(draw_url).json()["cards"]
print(cards)