import requests
import json

# Lille
def get_vlille():
    url = "https://opendata.lillemetropole.fr/api/records/1.0/search/?dataset=vlille-realtime&q=&rows=3000&facet=libelle&facet=nom&facet=commune&facet=etat&facet=type&facet=etatconnexion"
    reponse = requests.requests("GET",url)
    reponse_json = json.loads(response.text.encode('utf8'))         # json turned into dictionary
    return reponse_json.get("records",[])

# Lyon
def get_vélov():
    url = "https://public.opendatasoft.com/explore/dataset/station-velov-grand-lyon/api/?dataset=station-velov-grand-lyon&q=&rows=3000&facet=name&facet=commune&facet=status&facet=available&facet"
    reponse = requests.requests("GET",url)                      
    reponse_json = json.loads(response.text.encode('utf8'))
    return reponse_json.get("records",[])

# Paris
def get_vlib():
    url = "https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_information.json"
