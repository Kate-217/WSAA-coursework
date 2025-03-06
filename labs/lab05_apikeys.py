import requests
import urllib.parse
import config

target_url = "https://en.wikipedia.org"
api_key = config.htmltopdf_key
api_url = 'https://api.html2pdf.app/v1/generate'

params = {'url':target_url,'apiKey':api_key}
parsedparams = urllib.parse.urlencode(params)
request_url = api_url +"?" + parsedparams

response = requests.get(request_url)
print(response.status_code)

result = response.content

with open("WSAA-coursework/labs/document.pdf","wb") as handler:
    handler.write(result)
    
    