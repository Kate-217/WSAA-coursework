import requests

# request to NASA photo
url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
response = requests.get(url)
data = response.json()

print("Name:", data["title"])
#print("Explanation:", data["explanation"])
#print("photo:", data["url"])
#print(data)

