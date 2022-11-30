import requests
import json

def nutritioncode(input):
  headers = {
      # Already added when you pass json= but not when you pass data=
      # 'Content-Type': 'application/json',
  }





  json_data = {
      'appId': '1b96f64f',
      'appKey': 'f526efa32f0ab250fffe67daca343ec8',
      'query': input,
      "filters":{
        "item_type":1
    }
  }

  response = requests.post('https://api.nutritionix.com/v1_1/search', headers=headers, json=json_data)
  #print(response.json())

  responseJson = response.json()
  #print(responseJson)
\
