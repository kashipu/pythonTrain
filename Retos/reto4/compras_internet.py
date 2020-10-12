# Datos de entrada 
# https://raw.githubusercontent.com/arleserp/MinTIC2022/master/json/comprassmall.json

# Importando librerias
import json
import math
import requests
from pprint import pprint
from requests.models import Response

# Request 
    #Petición a URL
URL = requests.get("https://raw.githubusercontent.com/arleserp/MinTIC2022/master/json/comprassmall.json")
purchaseData = json.loads(URL.text)
i = 0
# Variables Globales
    #Información Cabeza de la tirilla
infoCabezaFactura = """Centro Comercial Unaleño
Compra más y Gasta Menos
NIT: 899.999.063"""
tirillas = len(purchaseData)


# Funciones
    # Imprime la cedula del cliente
def cedulaCliente(x, i):
    cedula = x[i]["cliente"]
    print("Cliente:", cedula)
    return cedula

    # Imprime el listado de productos
def productosCompra(x, i):
    productos = x[i]["productos"]
    for detalle in productos:
        nombreProducto = detalle["nombre"]
        cantidadProducto = int(detalle["cantidad"])
        precioProducto = int(detalle["precio unitario"])
        cantXPrecio = precioProducto * cantidadProducto
        print(nombreProducto, ("X" + str(cantidadProducto)), ("$" + str(cantXPrecio)))

    # Calculo de total
def calculoPrecioTotal(x, i):
    precios = x[i]["productos"]
    total = 0
    for x in precios:
        total += x["precio unitario"] * int(x["cantidad"])
    ahorroCompra = int(descuento(total))
    precioFinal = total - ahorroCompra
    print("Total:", ("$" + str(precioFinal)))
    print("En esta compra tu descuento fue", ("$" + str(ahorroCompra)))
    print("Gracias por tu compra")
    print("---")
    return ahorroCompra, precioFinal

    # Calculo de descuento
def descuento(x):
    if x > 150000 and x <= 300000:
        d = math.ceil(x * 0.1)
        print(d)
        return d
    elif x > 300000 and x <= 700000:
        d = math.floor(x * 0.15)
        print(d)
        return d
    elif x > 700000:
        d = math.ceil(x * 0.2)
        
        return d
    else:
        return 0

# Recibe X: Datos Json Compras, Y: numero iterador
def generarTirilla(alert, x, y):
    print(alert)
    cedulaCliente(x, y)
    print("Art Cant Precio")
    productosCompra(x, y)
    calculoPrecioTotal(x, y)

while i < tirillas:
    generarTirilla(infoCabezaFactura, purchaseData, i)
    i += 1
