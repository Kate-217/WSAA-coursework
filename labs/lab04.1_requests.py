import requests

url = "http://andrewbeatty1.pythonanywhere.com/books"
#response = requests.get(url)
#print(response.json())

# 3. Convert that into a function and call it 
# from inside a if __name__ == “__main__”:

def read_books():
    response = requests.get(url)
    return response.json()


#if __name__ == "__main__":
    #print(read_books())

# 4. Write the function for find by id and test it.

def read_book(id):
    get_url = url + "/" + str(id)
    response = requests.get(get_url)
    return response.json()

if __name__ == "__main__":
    print(read_book(1602))
    
# 5.Write the code to create and test it.

def create_book(book):
    response = requests.post(url, json=book)
    return response.json()

#if __name__ == "__main__":
#    new_book = {"author":"new", "price":99, "title":"new_title"}
#    print(create_book(new_book)) 
    
# update function:

def update_book(id,book):
    puturl = url + "/" + str(id)
    response = requests.put(puturl, json=book)
    return response.json()


if __name__ == "__main__":
    update = {"author":"A.Dumas","price":88, "title":"The Vicomte de Bragelonne"}
    print(update_book(1609,update)) 