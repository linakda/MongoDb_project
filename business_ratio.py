# import re
# import json
# from pprint import pprint
# from pymongo import MongoClient
# import requests
# from time import *
# from sched import scheduler

# s = scheduler(time,sleep)


# atlas = MongoClient('mongodb+srv://dbLina:isen2020@cluster0.io2qf.mongodb.net/BicycleStation?retryWrites=true&w=majority')

# db = atlas.bicycle

# def run_auto(start, end, interval, func):
#     chrono = start
#     while chrono > end:
#         s.enterabs(chrono, 0, func, ())
#         chrono += interval
#     s.run()


# def get_velostar():
#     url = "https://data.rennesmetropole.fr/api/records/1.0/search/?dataset=stations_vls&q=&rows=3000&facet=etat&facet=nom&facet=tpe&facet=geo_point_2d&facet=nb_socles"
#     reponse4 = requests.request("GET", url)
#     reponse_json4 = json.loads(reponse4.text.encode('utf8'))
#     return reponse_json4.get("records", [])


# def get_station_id(id_ext):
#     tps = db.station4.find_one({ 'source.id_ext': id_ext }, { '_id': 1 })
#     return tps['_id']

# while True:
#     print('update')
#     velostar = get_velostar()
#     datas = [
#         {
#             "bike_available": elem.get('fields', {}).get('nb_socles'),
#             "date": dateutil.parser.parse(elem.get('fields', {}).get('d_mhs')),
#             "station_id": get_station_id(elem.get('fields', {}).get('objectid'))
#         }
         
#     for elem in velostar
# ]
#     try:
#         db.datas.insert_many(datas, ordered=False)
#         num = elem["bike_available"]
#         denum = elem
#     except:
#         pass

# time.sleep(10)


# def get_ratio():
#     datetime = datetime.datetmie.utcnow()
#     for station in stations[]:


# run_auto(time()+5, time()+(7*24*60*60), 500, get_ratio)