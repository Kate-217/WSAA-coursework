import requests

url = "http://andrewbeatty1.pythonanywhere.com/books"
#response = requests.get(url)
#print(response.json())

# Convert that into a function and call it 
# from inside a if __name__ == “__main__”:

def read_books():
    response = requests.get(url)
    return response.json()


if __name__ == "__main__":
    print(read_books())
    
    