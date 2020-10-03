from math import sqrt, pow

x = tuple(map(int, input().split(' ')))
y = tuple(map(int, input().split(' ')))
#Opera las potencias
def op(h):
    op_d = h[1] - h[0]
    op_end = pow(op_d, 2)
    return(op_end)
#Gerera el resultado
def sumarOperaciones(x, y, z):
    resultado = sqrt(op(x) + op(y) + op(z))
    return print(resultado)

sumarOperaciones(x, y, z)
