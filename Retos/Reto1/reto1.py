# Variables de entrada
nombreProducto = str(input())
costoUnitario = int(input())
precioVentaPublico = int(input())
unidadesDisponibles = int(input())

# Calculos
ganancia = (precioVentaPublico - costoUnitario)*unidadesDisponibles

#Impresión Salida
print("Producto:", nombreProducto)
print("CU:", costoUnitario)
print("PVP:", precioVentaPublico)
print("Unidades Disponibles:", unidadesDisponibles)
print("Ganancia:", ganancia)