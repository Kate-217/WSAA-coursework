from lab04_requests import read_books

import requests
import json

url = "http://andrewbeatty1.pythonanywhere.com/books"
 
json_data = read_books()

#print(json_data)
#print(type(json_data))

sum_price = 0
books_count = 0
for book in json_data:
    sum_price += book['price']
    books_count += 1  
    
print(sum_price)
print(books_count)
print(f"The average price is {sum_price/books_count}")

    

