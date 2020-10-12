valorA = int(input("Valor: "))
valorB = int(input("Valor: "))
valorC = int(input("Valor: "))
valorD = int(input("Valor: "))

if valorB > valorC and valorD > valorA and valorC + valorD > valorA + valorB and valorC > 0 and valorD > 0 and valorA % 2 == 0:
    print("Valores Aceptados")
else:
    print("Valores no Aceptados")
    