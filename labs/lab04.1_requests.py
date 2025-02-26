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
    geturl = url + "/" + str(id)
    response = requests.get(geturl)
    return response.json()

if __name__ == "__main__":
    print(read_book(1602))

 