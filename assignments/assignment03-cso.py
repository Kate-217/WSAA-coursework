# Assignment 03
# Author Kate Lisovenko

import requests
import json

#url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en/STATISTIC"
url_beginning ="https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/" 
url_end = "/JSON-stat/2.0/en/STATISTIC"


def get_all(dataset):
    url = url_beginning + dataset + url_end     
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f'Error {response.status_code}: {response.text}')
    else:
        print(response.status_code)
    return response.json()

if __name__ == "__main__":
    dataset = "FIQ02"
    get_all(dataset)
    