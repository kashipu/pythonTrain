import math

#Información Cabeza de la tirilla
infoCabezaFactura = """Centro Comercial Unaleño
Compra más y Gasta Menos
NIT: 899.999.063"""

#Función Imprimir
def printFunction(d, t):
    print("Total: " + "$" + str(t))
    print("En esta compra tu descuento fue "+ "$" + str(d) )

def calculoDescuento(a, b):
    d = int(a * b)
    t = math.ceil(subtotal - d)
    printFunction(d, t)

#Saludo Tirilla
print(infoCabezaFactura)

#Variables Contadores
i = 0
subtotal = int(0)
descuento = 0
cntProdu = int(input())

#Ingreso de información
while i < cntProdu:
    nombre_producto = input()
    precio_producto = int(input())
    #Suma Precios de productos
    subtotal += precio_producto
    # Incremento para cerrar el ciclo
    i = i + 1
    print(nombre_producto, "$" + str(precio_producto))

#Calculo de descuento
d = 0
if subtotal > 0 and subtotal <= 150000:
    d = math.ceil(0)
    t = subtotal 
    printFunction(d, t)
if subtotal > 150000 and subtotal <= 300000:
    calculoDescuento(subtotal, 0.1)
if subtotal > 300000 and subtotal <= 700000:
    calculoDescuento(subtotal, 0.15)
if subtotal > 700000:
    calculoDescuento(subtotal, 0.2)

print("Gracias por tu compra")


