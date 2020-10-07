import math
#Información Cabeza de la tirilla
infoCabezaFactura = """Centro Comercial Unaleño
Compra más y Gasta Menos
NIT: 899.999.063"""
#Funciones
def descuento(x):
    if x > 150000 and x <= 300000:
        d = math.ceil(x * 0.1)
        return d
    elif x > 300000 and x <= 700000:
        d = math.floor(x * 0.15)
        return d
    elif x > 700000:
        d = math.ceil(x * 0.2)
        return d
    else:
        return 0

#Proceso inicial
x = input()
subtotal = 0
listadoProductos = []
producto = x.split("&")
i = producto[0]
    
while i == "1" or i == "2":
        producto = x.split("&")
        i = producto[0]
        if i == "2":
            cedula = producto[1]
            print(infoCabezaFactura)
            print("Cliente:", str(cedula))
            print("Art Cant Precio")
            for x in listadoProductos:
                print(x[0], str("X" + x[1]), x[2])
            des = descuento(subtotal)
            total = math.ceil(subtotal - des)
            print("Total:" + "$" + str(total))
            print("En esta compra tu descuento fue $", des)
            print("Gracias por tu compra")
            print("---")
            listadoProductos = []
            subtotal = 0
            x = input()
        elif i == "3":
            break
        else:
            precioTotal = int(producto[3]) * int(producto[2])
            subtotal += precioTotal
            resumenCompra = producto[1], producto[2], "$" + str(precioTotal)
            listadoProductos.append(resumenCompra)
            x = input()

