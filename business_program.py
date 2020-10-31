import requests
import re
import json
from pprint import pprint
from pymongo import MongoClient
import time


# Business program, connection to the cluster:
atlas = MongoClient('mongodb+srv://dbLina:isen2020@cluster0.io2qf.mongodb.net/BicycleStation?retryWrites=true&w=majority')

db = atlas.bicycle
stations = db.stations
lille = db.data

# Find station with name using collection.find()
def get_station():
    search = input("Enter the name or first letters of the station you want: ")
    print("We are looking for: "+search)
    nameSearch =re.compile(search, re.IGNORECASE)
    get = {"name":nameSearch}
    length = stations.count_documents(get)

    findings = stations.find(get)
    if length == 0:
        return 0
    else:
        return[length, findings]

# TODO : adapt for first letters only
#for elem in db.list_database_names:
#    try:
#        if elem==station:
#            print(elem)
#        elif elem.lower()==station.lower():
#            print(elem)
#        if (elem.get('name'))==station:
 #           print(elem.get('name'))
  #      elif (elem.get('name'))!=station:
   #         start = [idx for idx in db if idx[0].lower() == station.lower()]
    #        print("The list of matching first(s) letter(s): "+ str(start))
     #   else:
      #      print("We haven't found the station, you can try with the exact name or only the first letter.")

#    except AttributeError:
#        pass


