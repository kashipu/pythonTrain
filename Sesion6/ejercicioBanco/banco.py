billeteCien =100000
billeteCincuenta =50000
billeteVeinte =20000
billeteDiez =10000
solicitud = int(input("Cuanto Retira "))

#Calculo Cuantos billetes de 100
retiro_cien = solicitud // billeteCien
#Calculo Residuo
residuo = solicitud % billeteCien
#Calculo cuantos billetes de 50
retiro_cincuenta = residuo // billeteCincuenta
#Calculo Residuo
residuo = residuo % billeteCincuenta
#Calculo cuantos billetes de 20
retiro_veinte = residuo // billeteVeinte
#Calculo Residuo
residuo = residuo % billeteVeinte
#Calculo cuantos billetes de 10
retiro_diez = residuo // billeteDiez
#Calculo Residuo
residuo = residuo % billeteDiez


print(retiro_cien,"X",billeteCien)
print(retiro_cincuenta, "X", billeteCincuenta)
print(retiro_veinte, "X", billeteVeinte)
print(retiro_diez, "X", billeteDiez)