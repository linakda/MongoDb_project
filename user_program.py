import requests
import json
from pprint import pprint
from pymongo import MongoClient
import time
import urllib2


#User program: give available stations name next to the user lat, lon with last data (bikes and stand)

atlas = MongoClient('mongodb+srv://dbLina:isen2020@cluster0.io2qf.mongodb.net/BicycleStation?retryWrites=true&w=majority')

db = atlas.bicycle

def get_user_lat_lon():
  try:
    return json.load(urllib2.urlopen('http://ipinfo.io/json'))
  except urllib2.HTTPError:
    return False

location = get_user_lat_lon()

print location['city'] + ' (' + location['loc'] + ')'

def get_vlille():
    url = "https://opendata.lillemetropole.fr/api/records/1.0/search/?dataset=vlille-realtime&q=&rows=-1&facet=libelle&facet=nom&facet=commune&facet=etat&facet=type&facet=etatconnexion"
    response = requests.request("GET", url)
    response_json = json.loads(response.text.encode('utf8'))
    return response_json.get("records", [])

vlilles = get_vlille()

vlilles_to_insert = [
    {
        'name': elem.get('fields', {}).get('nom', '').title(),
        'geometry': elem.get('geo'),
        'size': elem.get('fields', {}).get('nbvelosdispo') + elem.get('fields', {}).get('nbplacesdispo'),
        'source': {
            'dataset': 'Lille',
            'id_ext': elem.get('fields', {}).get('libelle')
        },
        'tpe': elem.get('fields', {}).get('type', '') == 'AVEC TPE'
    }
    for elem in vlilles
]



atlas = MongoClient('mongodb+srv://dbLina:isen2020@cluster0.io2qf.mongodb.net/BicycleStation?retryWrites=true&w=majority')

db = atlas.bicycle

for vlille in vlilles_to_insert:
    db.Lille_program.insert_one(vlille)

for elem in vlille:
    try:
        print (elem.get('geo'))

    except AttributeError:
        pass
#if (elem.get('geo')location['loc'])