#Serialización
import json
import requests
from pprint import pprint


# data = {
#     "presidente": {
#         "nombre": "Ivan Duque",
#         "edad": 44
#     }
# }

# with open("./president.json", "w") as write_file:
#     json.dump(data, write_file)

#Serialización a texto
    #string = json.dumps(data)
    #print(string, type(string))



#Argumentos función dump
# indent permite ajustar la identacion de las estructuras anidadas
# string = json.dumps(data, indent=4)
# print(string, type(string))

#Leer Json desde un archivo
# with open("./president.json", "r") as read_file:
#     data = json.load(read_file)

# print(data["presidente"])



#leer Json desde internet
response = requests.get("https://jsonplaceholder.typicode.com/todos")

pendientes = json.loads(response.text)


pprint(pendientes[:5]) #imprime el json cargado


pendiente_por_usuario = {}

for pendiente in pendientes:
    if pendiente["completed"]:
        # print(pendiente)
        if pendiente["userId"] in pendiente_por_usuario:
                pendiente_por_usuario[pendiente["userId"]] += 1
        else:
            pendiente_por_usuario[pendiente["userId"]] = 1






