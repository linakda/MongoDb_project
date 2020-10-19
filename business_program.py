import requests
import json
from pprint import pprint
from pymongo import MongoClient
import time


# Business program:

atlas = MongoClient('mongodb+srv://dbLina:isen2020@cluster0.io2qf.mongodb.net/BicycleStation?retryWrites=true&w=majority')

db = atlas.bicycle



# Find station with name
 
station = input("Enter the name or first letters of the station you want: ")
print("We are looking for: "+station)


def get_vlille():
    url = "https://opendata.lillemetropole.fr/api/records/1.0/search/?dataset=vlille-realtime&q=&rows=-1&facet=libelle&facet=nom&facet=commune&facet=etat&facet=type&facet=etatconnexion"
    response = requests.request("GET", url)
    response_json = json.loads(response.text.encode('utf8'))
    return response_json.get("records", [])

vlilles = get_vlille()

atlas = MongoClient('mongodb+srv://dbLina:isen2020@cluster0.io2qf.mongodb.net/BicycleStation?retryWrites=true&w=majority')

db = atlas.bicycle


for elem in vlille:
    try:
        if (elem.get('name'))==station:
            print(elem.get('name'))
        elif (elem.get('name'))!=station:
            start = [idx for idx in vlille if idx[0].lower() == station.lower()]
            print("The list of matching first(s) letter(s): "+ str(start))
        else:
            print("We haven't found the station, you can try with the exact name or only the first letter.")

    except AttributeError:
        pass