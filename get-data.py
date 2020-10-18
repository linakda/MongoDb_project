import requests
import json
from pprint import pprint
from pymongo import MongoClient

def get_vlille():
    url = "https://opendata.lillemetropole.fr/api/records/1.0/search/?dataset=vlille-realtime&q=&rows=3000&facet=libelle&facet=nom&facet=commune&facet=etat&facet=type&facet=etatconnexion"
    response = requests.request("GET", url)
    response_json = json.loads(response.text.encode('utf8'))
    return response_json.get("records", [])


vlilles = get_vlille()

vlilles_to_insert = [
    {
        'name': elem.get('fields', {}).get('nom', '').title(),
        'geometry': elem.get('geometry'),
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
    db.stations1.insert_one(vlille)



def get_velov():
    url = "https://public.opendatasoft.com/api/records/1.0/search/?dataset=station-velov-grand-lyon&q=&facet=last_upd_1&fbclid=IwAR2JkyX5O-R1O3ZP_m6zmg-_cczhu4m2jFREdW2NmqHlhM9JpuWirYDiCoE"
    reponse2 = requests.request("GET",url)
    reponse_json2 = json.loads(reponse2.text.encode('utf8'))
    return reponse_json2.get("records",[])


velov = get_velov()

velov_to_insert = [
    {
        'name': elem.get('fields', {}).get('name', '').title(),
        'geometry': elem.get('fields', {}).get('geo_point_2d'),
        'size': elem.get('fields', {}).get('available') + elem.get('fields', {}).get('availabl_1'),
        'source': {
            'dataset': 'station-velov-grand-lyon',
            'id_ext': elem.get('fields', {}).get('gid')
        },
        'tpe': elem.get('fields', {}).get('banking', '') == 'AVEC TPE'
    }
    for elem in velov
]

atlas = MongoClient('mongodb+srv://dbLina:isen2020@cluster0.io2qf.mongodb.net/BicycleStation?retryWrites=true&w=majority')

db = atlas.bicycle

for velov in velov_to_insert:
    db.stations2.insert_one(velov)


def get_vlib():
    url = "https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_information.json"
    reponse3 = requests.request("GET", url)
    reponse_json3 = json.loads(reponse3.text.encode('utf8'))
    return reponse_json3.get("records", [])


vlib = get_vlib()

vlib_to_insert = [
    {
        'name': elem.get('data', {}).elem.get('stations', {}).get('name', '').title(),
        'geometry': elem.get('data', {}).elem.get('stations', {}).get('lon', '').title() + elem.get('data', {}).elem.get('stations', {}).get('lat', '').title(),
        'size': elem.get('data', {}).elem.get('stations', {}).get('capacity'),
        'source': {
            'dataset': 'Velib_Metropole',
            'id_ext': elem.get('data', {}).elem.get('stations', {}).get('station_id')
        },
        'tpe': elem.get('data', {}).elem.get('stations', {}).get('rental_methods', '') == 'AVEC TPE'
    }
    for elem in vlib
]

atlas = MongoClient('mongodb+srv://dbLina:isen2020@cluster0.io2qf.mongodb.net/BicycleStation?retryWrites=true&w=majority')

db = atlas.bicycle

for vlib in vlib_to_insert:
    db.stations3.insert_one(vlib)


def get_velostar():
    url = "https://data.rennesmetropole.fr/api/records/1.0/search/?dataset=stations_vls&q=&rows=3000&facet=etat&facet=nom&facet=tpe&facet=geo_point_2d&facet=nb_socles"
    reponse4 = requests.request("GET", url)
    reponse_json4 = json.loads(reponse4.text.encode('utf8'))
    return reponse_json4.get("records", [])


velostar = get_velostar()

velostar_to_insert = [
    {
        'name': elem.get('fields', {}).get('nom', '').title(),
        'geometry': elem.get('fields', {}).get('geo_point_2d'),
        'size': elem.get('fields', {}).get('nb_socles'),
        'source': {
            'dataset': 'stations_vls',
            'id_ext': elem.get('fields', {}).get('objectid')
        },
        'tpe': elem.get('fields', {}).get('tpe', '') == 'AVEC TPE'
    }
    for elem in velostar
]

atlas = MongoClient('mongodb+srv://dbLina:isen2020@cluster0.io2qf.mongodb.net/BicycleStation?retryWrites=true&w=majority')

db = atlas.bicycle

for velostar in velostar_to_insert:
    db.stations4.insert_one(velostar)