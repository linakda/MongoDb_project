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


def delete_station(id):
    stations.delete_one({"_id":id})
#    print("\nThe station of id "+id+" has been deleted.\n")


def update_station(id, field, value):
    stations.update_one({"_id":id},{"$set":{field: value}})

def area_station():
    stations_display=[]
    with open("area.geojson",'r') as map:       # TODO explain & insert file &uncomment
        map=map.read()
        data=json.loads(map)
 #       define=("geometry":{"$geoWithin": {"$geometry":data["features"][0]["geometry"]}}}
 #       concerned=stations.find(define)
#        for station in concerned:
 #           stations_display.append(station["name"])
        return stations_display

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


    
    if business =='u':
        search = get_station()
        while search == 0:
            business = input("No such station was found.")
        print("\n%d station(s) correspond to your search:"%search[0])
        display = list(search[1])
        for finding in display:
            pprint(finding)
            print('\n')
        pick = int(input("Please enter the number of the station to be updated (from 0): "))
        pickI=display(pick)
        
        change = int(input("You can change the name [0] \nor the size parameter/field [1]:"))
        while change != 0 and change != 1:
            change = int(input("Try again \nYou can change the name [0] \nor the length of the field [1]:"))
        
        if change ==0:
            newName=("Enter the new name: ")
            update = update_station(pickI["_id"],"name","newName")
            print("\nThe station %s is now named %s"% pickI["name"], newName)

        if change ==1:
            newSize=("Enter the new length/size for the station: ")
            update = update_station(pickI["_id"],"size","newSize")
            print("\nThe station %s is now sizing %s"% pickI["name"], newSize)


    if business == 'a':
        status = False
        area_result = area_station(status)
        print("\nDeleted stations:\n"+area_result)


    #TODO
    if business == 'p':
        0

    print("Done")


except Exception as alert:
    print("Failed. There may have been an error.")
    pprint(alert)



