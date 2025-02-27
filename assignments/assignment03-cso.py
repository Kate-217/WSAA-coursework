# Assignment 03
# Author Kate Lisovenko

import requests
import json

url_beginning ="https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/" 
url_end = "/JSON-stat/2.0/en/STATISTIC"

# save in file
def get_all_in_file(dataset):
    url = url_beginning + dataset + url_end     
    response = requests.get(url)
    data = response.json()
    
    with open("cso.json","wt") as fp:
        json.dump(data, fp, indent=4)
    return data    
              
if __name__ == "__main__":
    dataset = "FIQ02"
    get_all_in_file(dataset)

    