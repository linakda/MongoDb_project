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

# TODO: update station
def update_station():
    
    return 0


def delete_station(id):
    stations.delete_one({"_id":id})
#    print("\nThe station of id "+id+" has been deleted.\n")


try:
    business = input("You can choose to: \nSearch for a station with the entry: [S] \nUpdate a station: [U] \nDelete a station and datas: [D] \nAreawise delete stations: [A] \nPrint the percentage of bicycles used per station: [P] \nFor any operation on a station you'll need its id. You can find it with the first entry: [S]")
    business = business.lower()
    while business != 's' and business != 'u' and business != 'd' and business != 'a' and business != 'p':
        business = input("Please try again one of the following entries:")
        business = input("You can choose to: \nSearch for a station with the entry: [S] \nUpdate a station: [U] \nDelete a station and datas: [D] \nAreawise delete stations: [A] \nPrint the percentage of bicycles used per station: [P]")
    
    if business == 's':
        search = get_station()
        while search == 0:
            business = input("No such station was found.")
        print("\n%d station(s) correspond to your search:"%search[0])
        display = list(search[1])
        for finding in display:
            pprint(finding)
            print('\n')
    
    if business =='u':
        search = get_station()
        while search == 0:
            business = input("No such station was found.")
        print("\n%d station(s) correspond to your search:"%search[0])
        display = list(search[1])
        for finding in display:
            pprint(finding)
            print('\n')
        update = update_station()
    
    if business == 'd':
        search = get_station()
        while search == 0:
            business = input("No such station was found.")
        print("\n%d station(s) correspond to your search:"%search[0])
        display = list(search[1])
        for finding in display:
            pprint(finding)
            print('\n')
        pick = int(input("Please enter the number of the station to be deleted (from 0): "))
        pickI=display(pick)
        delete = delete_station(pickI["_id"])
        print("\nThe station "+pickI["name"]+" has been deleted.\n")


    if business == 'a':
        0

    if business == 'p':
        0

# TODO : proper list

