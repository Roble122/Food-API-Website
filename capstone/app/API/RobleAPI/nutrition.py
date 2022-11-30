import sqlite3
import requests
import sys
import json
non_bmp_map =dict.fromkeys(range (0x10000, sys.maxunicode+1), 0xfffd)


def foodnutritioncode(Macroinput):


    query = Macroinput
    api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
    response = requests.get(api_url, headers={'X-Api-Key': '94NlwilwGgEF0vQlagmVag==spsVNqhqSR9o5iTg'})
    if response.status_code == requests.codes.ok:
        print(response.json())

    else:
        print("Error:", response.status_code, response.text)



    data = json.loads(response.text)


    conn = sqlite3.connect('capstone/db.sqlite3')
    cur = conn.cursor()

    cur.execute(
    """CREATE TABLE IF NOT EXISTS NutritionFix(
    id INTEGER PRIMARY KEY,
    qname varchar(50),
    qcalories varchar(50),
    qserving varchar(50),
    qfattotal varchar(50),
    qfatsat varchar(50),
    qprotein varchar(50),
    qsodium varchar(50),
    qpotassium varchar(25),
    qcholesterol varchar(25),
    qcarb varchar(25),
    qfibe varchar(25),
    qsugar varchar(25)
    );"""
    )
   
    for value in data:
        qname = value['name'].translate(non_bmp_map)
        qcalories =value['calories']
        qserving = value['serving_size_g']
        qfattotal = value['fat_total_g']
        qfatsat = value['fat_saturated_g']
        qprotein = value['protein_g']
        qsodium = value['sodium_mg']
        qpotassium = value['potassium_mg']
        qcholesterol =value['cholesterol_mg']
        qcarb = value['carbohydrates_total_g']
        qfibe = value['fiber_g']
        qsugar = value['sugar_g']
        sql = '''INSERT INTO NutritionFix(qname, qcalories, qserving, qfattotal, qfatsat, qprotein, qsodium, qpotassium, qcholesterol, qcarb, qfibe, qsugar) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
        cur.execute(sql,(qname, qcalories, qserving, qfattotal, qfatsat, qprotein, qsodium, qpotassium, qcholesterol, qcarb, qfibe, qsugar))
    
    conn.commit()
    conn.close()

print("records inserted")

