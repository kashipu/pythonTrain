import math

def descuento(x):
    if x > 150000 and x <= 300000:
        d = math.ceil(x * 0.1)
        return d
    elif x > 300000 and x <= 700000:
        d = math.ceil(x * 0.15)
        return d
    elif x > 700000:
        d = math.ceil(x * 0.2)
        return d
    else:
        return 0

print(descuento(300000))