import requests
import json
from pymongo import MongoClient
from pprint import pprint

#test connection + création de collection
client = MongoClient("mongo "mongodb+srv://cluster0.pnbit.gcp.mongodb.net/get-data" --username dbLina")
db = client.test_database 

collection = db.test_collection 



# Lille
def get_vlille():
    url = "https://opendata.lillemetropole.fr/api/records/1.0/search/?dataset=vlille-realtime&q=&rows=3000&facet=libelle&facet=nom&facet=commune&facet=etat&facet=type&facet=etatconnexion"
    reponse = requests.request("GET",url)
    reponse_json = json.loads(reponse.text.encode('utf8'))         # json turned into dictionary
    return reponse_json.get("records",[])

# Lyon
def get_velov():
    url = "https://public.opendatasoft.com/api/records/1.0/search/?dataset=station-velov-grand-lyon&q=&facet=last_upd_1&fbclid=IwAR2JkyX5O-R1O3ZP_m6zmg-_cczhu4m2jFREdW2NmqHlhM9JpuWirYDiCoE"
    reponse2 = requests.request("GET",url)
    reponse_json2 = json.loads(reponse2.text.encode('utf8'))
    return reponse_json2.get("records",[])

# Paris
def get_vlib():
    url = "https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_information.json"
    reponse3 = requests.request("GET", url)
    reponse_json3 = json.loads(reponse3.text.encode('utf8'))
    return reponse_json3.get("records", [])

# Rennes
def get_velostar():
    url = "https://data.rennesmetropole.fr/api/records/1.0/search/?dataset=stations_vls&q=&rows=3000&facet=etat&facet=nom&facet=tpe&facet=geo_point_2d&facet=nb_socles&facet=coordinates"
    reponse3 = requests.request("GET", url)
    reponse_json3 = json.loads(reponse3.text.encode('utf8'))
    return reponse_json3.get("records", [])
    
#test
vlilles = pprint(get_vlille())


 #print(get_velov())
 #print(get_vlib())

 new_station={
        'name':vlille['name'],
        'ville':vlille['contractName'],
        'localisation':[vlille['position']['latitude']['longitude']],
        'tpe':vlille['banking']
    }

records.insert_one(new_station)

   
