#Importando math, Libreria para usar squrt(Raíz de) y pow(Porencia de, ala n)
from math import sqrt, pow
#Variables y entrada
x = tuple(map(int, input().split(' ')))
y = tuple(map(int, input().split(' ')))
t = x + y
#Opera las potencias
def op(h):
    op_d = (pow(h[0] - h[3], 2)) + (pow(h[1] - h[4], 2)) + (pow(h[2] - h[5], 2))
    return(op_d)
#Gerera el resultado
def sumarOperaciones(x):
    resultado = sqrt(op(x))
    return print(resultado)
#Invoco Función
sumarOperaciones(t)


