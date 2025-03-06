import requests
import json
import config


url =  'https://api.github.com/repos/Kate-217/aprivateone'
apikey = config.git_key

response = requests.get(url, auth=('token',apikey))
repo_json = response.json()

with open("privat_repo.txt","w") as fp:
    json.dump(repo_json,fp,indent=4)
    

