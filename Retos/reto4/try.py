import json

json_string = '{ "presidente": { "nombre": "Ivan Duque", "edad": 44 }}'
data = json.loads(json_string)
print(data)
