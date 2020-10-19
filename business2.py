import requests
import json
from pprint import pprint
from pymongo import MongoClient
import time
from flask import Flask, jsonify, request 
from flask_cors import CORS


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

app = Flask(__name__) 
atlas = MongoClient('mongodb+srv://dbLina:isen2020@cluster0.io2qf.mongodb.net/BicycleStation?retryWrites=true&w=majority')

db=atlas.get_database('bicycle')

Table=db.SampleTable

@app.route('/find-one/<argument>/<value>/', methods=['GET']) 
def findOne(argument, value): 
    queryObject = {argument: value} 
    query = Table.find_one(queryObject) 
    query.pop('_id') 
    return jsonify(query) 

findOne('nom',station)


