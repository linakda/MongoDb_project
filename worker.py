import requests
import json
from pprint import pprint
from pymongo import MongoClient
import time
import dateutil.parser

atlas = MongoClient('mongodb+srv://dbLina:isen2020@cluster0.io2qf.mongodb.net/BicycleStation?retryWrites=true&w=majority')

db = atlas.bicycle

db.datas.create_index([('station_id', 1),('date', -1)], unique=True)

def get_vlille():
    url = "https://opendata.lillemetropole.fr/api/records/1.0/search/?dataset=vlille-realtime&q=&rows=-1&facet=libelle&facet=nom&facet=commune&facet=etat&facet=type&facet=etatconnexion"
    response = requests.request("GET", url)
    response_json = json.loads(response.text.encode('utf8'))
    return response_json.get("records", [])

def get_station_id(id_ext):
    tps = db.station1.find_one({ 'source.id_ext': id_ext }, { '_id': 1 })
    return tps['_id']

while True:
    print('update')
    vlilles = get_vlille()
    datas = [
        {
            "bike_availbale": elem.get('fields', {}).get('nbvelosdispo'),
            "stand_availbale": elem.get('fields', {}).get('nbplacesdispo'),
            "date": dateutil.parser.parse(elem.get('fields', {}).get('datemiseajour')),
            "station_id": get_station_id(elem.get('fields', {}).get('libelle'))
        }
        for elem in vlilles
 ]

    try:
        db.datas.insert_many(datas, ordered=False)
    except:
        pass

time.sleep(10)

def get_velov():
    url = "https://public.opendatasoft.com/api/records/1.0/search/?dataset=station-velov-grand-lyon&q=&facet=last_upd_1&fbclid=IwAR2JkyX5O-R1O3ZP_m6zmg-_cczhu4m2jFREdW2NmqHlhM9JpuWirYDiCoE"
    reponse2 = requests.request("GET",url)
    reponse_json2 = json.loads(reponse2.text.encode('utf8'))
    return reponse_json2.get("records",[])


def get_station_id(id_ext):
    tps = db.station2.find_one({ 'source.id_ext': id_ext }, { '_id': 1 })
    return tps['_id']

while True:
    print('update')
    velov = get_velov()
    datas = [
        {
            "bike_availbale": elem.get('fields', {}).get('available'),
            "stand_availbale": elem.get('fields', {}).get('availabl_1'),
            "date": dateutil.parser.parse(elem.get('fields', {}).get('last_updat')),
            "station_id": get_station_id(elem.get('fields', {}).get('gid'))
        }
    for elem in velov
 ]
    try:
        db.datas.insert_many(datas, ordered=False)
    except:
        pass

time.sleep(10)

def get_vlib():
    url = "https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_information.json"
    reponse3 = requests.request("GET", url)
    reponse_json3 = json.loads(reponse3.text.encode('utf8'))
    return reponse_json3.get("records", [])

def get_station_id(id_ext):
    tps = db.station3.find_one({ 'source.id_ext': id_ext }, { '_id': 1 })
    return tps['_id']

while True:
    print('update')
    vlib = get_vlib()
    datas = [
        {
            "bike_availbale": elem.get('fields', {}).get('capacity'),
            "date": dateutil.parser.parse(elem.get('lastUpdatedOther')),
            "station_id": get_station_id(elem.get('data', {}).elem.get('stations', {}).get('station_id'))
        }

        for elem in vlib
]
    try:
        db.datas.insert_many(datas, ordered=False)
    except:
        pass

time.sleep(10)

def get_velostar():
    url = "https://data.rennesmetropole.fr/api/records/1.0/search/?dataset=stations_vls&q=&rows=3000&facet=etat&facet=nom&facet=tpe&facet=geo_point_2d&facet=nb_socles"
    reponse4 = requests.request("GET", url)
    reponse_json4 = json.loads(reponse4.text.encode('utf8'))
    return reponse_json4.get("records", [])


def get_station_id(id_ext):
    tps = db.station4.find_one({ 'source.id_ext': id_ext }, { '_id': 1 })
    return tps['_id']

while True:
    print('update')
    velostar = get_velostar()
    datas = [
        {
            "bike_availbale": elem.get('fields', {}).get('nb_socles'),
            "date": dateutil.parser.parse(elem.get('fields', {}).get('d_mhs')),
            "station_id": get_station_id(elem.get('fields', {}).get('objectid'))
        }
         
    for elem in velostar
]
    try:
        db.datas.insert_many(datas, ordered=False)
    except:
        pass

time.sleep(10)