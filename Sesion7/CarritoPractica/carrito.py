#Importar libreria Math para traer el valor de PI 
# import math / Trae toda la libreria
from math import pi

#Variables
cuadrado_altura1 = float(input("Altura 1: "))
cuadrado_base1 = float(input("Base 1: "))
cuadrado_altura2 = float(input("Altura 2: "))
cuadrado_base2 = float(input("Base 2: "))
radio1 = float(input("Radio 1: "))
radio2 = float(input("Radio 2: "))

# Área del Cuadrado: a^2
def areaCuadrado(base, altura):
    return base * altura

# Área circulo Pi * Radio^2
def areaCirculo(radio):
    return pi * (radio * radio)

#Solucion cuadrados
area_Cuadrado1 = float(areaCuadrado(cuadrado_altura1, cuadrado_base1))
area_Cuadrado2 = float(areaCuadrado(cuadrado_altura2, cuadrado_base2))

#Solucion Circulos
area_circulo1 = float(areaCirculo(radio1))
area_circulo2 = float(areaCirculo(radio2))

#Suma Areas
def sumaAreas(a, b, c, d):
    totalSuma = float(a + b + c + d)
    return totalSuma

print("suma total =",sumaAreas(area_Cuadrado1,area_Cuadrado2,area_circulo1,area_circulo2))