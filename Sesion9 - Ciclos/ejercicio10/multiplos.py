# Entradas de datos
numeroMaximo = int(input("digite n:"))
numeroMultiplo = int(input("digite m:"))
#Inicio Variables
i = 0
multiplo = 0
# Ciclo y operación
print("los múltiplos son:")
while multiplo < numeroMaximo:
    multiplo = numeroMultiplo * i
    if multiplo <= numeroMaximo:
        i = i + 1
        print(multiplo)