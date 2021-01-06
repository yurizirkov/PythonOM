import requests
import json


print("==================ISS LOCATION==================")
f = "http://api.open-notify.org/iss-now.json"
data = requests.get(f)
tt = json.loads(data.text)
print(tt["timestamp"])
print (tt["iss_position"])
#print(data.text)

print("==================PEOPLE IN SPACE==================")
f = r"http://api.open-notify.org/astros.json"
data2 = requests.get(f)
tt = json.loads(data2.text)
for i in tt["people"]:
    print(i["name"])

print("==================LOCATION==================")
f = r"http://api.open-notify.org/astros.json"
data2 = requests.get(f)
tt = json.loads(data2.text)
for i in tt["people"]:
    print(i["craft"])

    