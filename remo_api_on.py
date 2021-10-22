import json
import requests

apikey = "XXX"

#Get JSON
headers = {
  'accept': 'application/json',
  'Content-Type': 'application/x-www-form-urlencoded',
  'Authorization': 'Bearer ' + apikey ,
}

response = requests.get('https://api.nature.global/1/devices', headers=headers, verify=False)
signal_id = "04c70d4b-65b2-4b82-b24d-49364ae56a02"

#AirCon
response2 = requests.post("https://api.nature.global/1/appliances/04c70d4b-65b2-4b82-b24d-49364ae56a02/aircon_settings",headers=headers)

#TV
response3 = requests.post("https://api.nature.global/1/appliances/5b4116f6-25b1-4c9b-845f-4cce16c44437/tv",data="button=power",headers=headers)

#Light
response4 = requests.post("https://api.nature.global/1/appliances/36f3ff20-dba0-4156-9551-cd310c638a64/light",data="button=on",headers=headers)


rjson = response.json()
print(rjson)




