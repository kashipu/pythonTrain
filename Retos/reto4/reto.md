# Reto para la semana 4: Componente de lectura de compras desde internet
## Límite de entrega: Tuesday, 13 de October de 2020, 23:59

En esta ocasión el centro comercial tiene en formato JSON archivos con el listado de compras realizadas en internet. Dado este formato, se requiere su ayuda para que se generen las tirillas de compra que se encuentran almacenadas en un sitio determinado de internet.

El formato de tirilla es similar al del último reto.

El cálculo de descuento se mantiene y se debe generar la misma tirilla que se generó en el reto anterior. Dado el valor total de la compra se continúa con la campaña titulada compra más y gasta menos con los siguientes descuentos:

Por compras mayores a 150000 lleva un 10% de descuento.
Por compras mayores a 300000 lleva un 15% de descuento.
Por compras mayores a 700000 lleva un 20% de descuento.


Entrada: Este programa tiene como entrada un enlace que corresponde al archivo json que se quiere procesar. Puede ser cualquier enlace, pero se garantiza que el archivo maneja el mismo formato del archivo de ejemplo.

Salida: Tirillas de compra de acuerdo al procesamiento del archivo de internet especificado.


Nota: Como el centro comercial está siendo muy generoso con los descuentos, el valor a cobrar en caso de tener centavos se debe aproximar a techo usando la función ceil de python (https://www.tutorialspoint.com/python/number_ceil.htm)

Ejemplo: 

Entrada: https://raw.githubusercontent.com/arleserp/MinTIC2022/master/json/comprassmall.json

Salida:

Centro Comercial Unaleño
Compra más y Gasta Menos
NIT: 899.999.063
Cliente: 80849599
Art Cant Precio
Chocolatinas Cohete x3 $900
Mora x1 $1000
Pan de Maiz x5 $1500
Total: $3400
En esta compra tu descuento fue $0
Gracias por tu compra

Centro Comercial Unaleño
Compra más y Gasta Menos
NIT: 899.999.063
Cliente: 1022734737
Art Cant Precio
Televisor x2 $3000000
Teatro en Casa x1 $450000
Total: $2760000
En esta compra tu descuento fue $690000
Gracias por tu compra


