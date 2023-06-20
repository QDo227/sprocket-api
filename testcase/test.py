import requests

#GET /sprockets/all
print("---Call http://localhost:5000/sprockets/all---")
response = requests.get("http://localhost:5000/sprockets/all")
print(response.json())

#GET /factory/{id}
#Test existed factory id
response = requests.get("http://localhost:5000/factory/1")
print("---Call http://localhost:5000/factory/1---")
print(response.json())

#GET /factory/{id}
#Test wrong factory id
response = requests.get("http://localhost:5000/factory/4")
print("---Call http://localhost:5000/factory/4---")
print(response.json())

#GET /sprocket/{id}
#Test existed sprocket id
response = requests.get("http://localhost:5000/sprocket/1")
print("---Call http://localhost:5000/sprocket/1---")
print(response.json())

#GET /sprocket/{id}
#Test wrong sprocket id
response = requests.get("http://localhost:5000/sprocket/4")
print("---Call http://localhost:5000/sprocket/4---")
print(response.json())

#POST /sprocket/new
#Create new sprocket with unique id
print("---Call http://localhost:5000/sprocket/new---")
new_sprockets = {'id': 5, 'outside_diameter': 6, 'pitch': 1, 'pitch_diameter': 5, 'teeth': 5}
response = requests.post("http://localhost:5000/sprocket/new", json=new_sprockets)
print(response.json())

#POST /sprocket/new
#Create new sprocket that doesn't have a unique id
print("---Call http://localhost:5000/sprocket/new---")
new_sprockets = {'id': 1, 'outside_diameter': 6, 'pitch': 1, 'pitch_diameter': 5, 'teeth': 5}
response = requests.post("http://localhost:5000/sprocket/new", json=new_sprockets)
print(response.json())

#PUT /sprocket/update/{id}
print("---Call http://localhost:5000/sprocket/update/1---")
updated_sprockets = {'pitch_diameter': 15, 'teeth': 55}
response = requests.put("http://localhost:5000/sprocket/update/1", json=updated_sprockets)
print(response.json())

