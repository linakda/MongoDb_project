import requests
import json
from pprint import pprint
from pymongo import MongoClient
import time


# Business program:

atlas = MongoClient('mongodb+srv://dbLina:isen2020@cluster0.io2qf.mongodb.net/BicycleStation?retryWrites=true&w=majority')

collection = atlas.bicycle

# collection.update()

const query = { "reviews.0": {"$exists": true}};

const projection = { "_id": 0, "name":1};

return collection.find(query, update, options).sort({name:1}).toArray().then(items => { 
    console.log('${item.length} stations found')
    items.forEach(console.log)
    return items
    })
    .catch(err => console.error('Stations not found: $err}'))