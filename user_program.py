import requests
import json
from pprint import pprint
from pymongo import MongoClient, GEO2D
import time
import dateutil.parser
import urllib2


atlas = MongoClient('mongodb+srv://dbLina:isen2020@cluster0.io2qf.mongodb.net/BicycleStation?retryWrites=true&w=majority')

db = atlas.bicycle

db.datas.create_index([('station_id', 1),('date', -1)], unique=True)
db.stations1.create_index(['geometry','2dsphere']) #stations1 = collection avec les données de l'API vlille

def get_vlille():
    url = "https://opendata.lillemetropole.fr/api/records/1.0/search/?dataset=vlille-realtime&q=&rows=-1&facet=libelle&facet=nom&facet=commune&facet=etat&facet=type&facet=etatconnexion"
    response = requests.request("GET", url)
    response_json = json.loads(response.text.encode('utf8'))
    return response_json.get("records", [])

def get_user_lat_lon():
  try:
    return json.load(urllib2.urlopen('http://ipinfo.io/json'))
  except urllib2.HTTPError:
    return False
coord = get_user_lat_lon()
print coord['city'] + ' (' + coord['loc'] + ')'


def get_station_id(id_ext):
    tps = db.station1.find_one({ 'source.id_ext':id_ext }, { '_id': 1 })
    return tps['_id']


# cursor = db.station1.find_one({ 'source.id_ext':id_ext }, { '_id': 1 })
# cursor.sort(name)
# return list(cursor)

inp = input(' Enter 0 for manual coordinates input, enter 1 for auto-geolocalisation : ')

def Manual(): 
    print('Enter your latitude : ')
    return 

def Geoloc():
     coord = get_user_lat_lon()
     print coord['city'] + ' (' + coord['loc'] + ')'
     return

switcher ={
     0 : Manual,
     1 : Geoloc,
 }


#Saisie latitude/longitude
print('Entrez votre lat :')
lat = input()
print('Entrez votre lon')
lon = input()

def get_nearest_station(lat,lon):
   nearest= db.station1.find({'geometry': { 
      '$near': { '$geometry': {
        'type': "Point" ,
        'coordinates': [ lat, lon ]},
        '$maxDistance': 1000000,
        '$minDistance': 0 }
        }})
   return(list(nearest))
   
print(get_nearest_station(50.66026,3.087568))












