import urllib.request
import json
import os
##import pymysql
##import pyodbc
import sqlite3

def googlecode(Foodinput):


    conn = sqlite3.connect('capstone/db.sqlite3')
    cur = conn.cursor()
        # Create the table if it doesn't exist.
    cur.execute( "CREATE TABLE IF NOT EXISTS Googlemodel (Resname TEXT, Address	TEXT,Lat TEXT,Long TEXT)")
    Delete_all_rows = """delete from Googlemodel """
    cur.execute(Delete_all_rows)


    # Create URL string
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json" 
    params = { 
        "query": Foodinput,
        "location": "39.826781,-75.015446",
        "radius": "2000",
        "region": "US",
        "type": "food",
        "key": "AIzaSyD22ufr_NRQ6SRyaPjjZWlc5M5WttvjjsE"
    }    
    query_string = urllib.parse.urlencode( params ) 
    url = url + "?" + query_string
    headers = {"Content-Type": "application/json"}
    print (url)
    print()
    response = urllib.request.urlopen(url)
    data = response.read().decode('UTF-8')

    #Write Json data to file to examine
    file = open("app/API/MapsAPI/data.json","w")
    file.write(data)
    file.close()

    #Open Json Data
    with open("app/API/MapsAPI/data.json") as f:
      data = json.load(f)

    #loop through the data and assign to variables
    for i, item in enumerate(data):
        name=data['results'][i]["name"]
        add=data['results'][i]["formatted_address"]
        lat=data['results'][i]["geometry"]["location"]["lat"]
        long=data['results'][i]["geometry"]["location"]["lng"]

        #insert found variables into database
        cur.execute("INSERT INTO Googlemodel (Resname, Address, Lat, Long) VALUES(?,?,?,?)",(name, add, lat, long))
        conn.commit()





