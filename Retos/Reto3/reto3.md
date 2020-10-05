Límite de entrega: Tuesday, 6 de October de 2020, 23:59
Número máximo de ficheros: 1
Tipo de trabajo: Individual
El Centro Comercial Unaleño está muy cerca de crear carrito de compras. Ahora lo que se requiere de su parte es que se puedan agregar un número indefinido de artículos y calcular la cuenta.

 Se han definido varios comandos para realizar la prueba de la lógica del carrito de compras a bajo nivel. Para esto se definen ahora diferentes comandos que se realizan al momento de realizar una compra y que presentan la siguiente sintaxis: 

comando&sintaxis_comando

 Los comandos definidos ahora son:

 Comando 1:  Añadir ítem al carrito de compras

 La sintaxis del comando 1 es la siguiente:

1&nombre_articulo&cantidad&precio

 Comando 2: Generar tirilla de compras

 La sintaxis del comando 2 es la siguiente:

2&cedula_cliente

Esta función debe retornar la tirilla de compras en texto
El cálculo de descuento se mantiene y se debe generar la misma tirilla que se generó en el reto anterior, pero incluyendo la cédula del cliente y la cantidad de artículos por producto en el formato indicado en el ejemplo.  Dado el valor total de la compra se continúa con la campaña titulada compra más y gasta menos con los siguientes descuentos:
Por compras mayores a 150000 lleva un 10% de descuento.
Por compras mayores a 300000 lleva un 15% de descuento.
Por compras mayores a 700000 lleva un 20% de descuento
Al imprimir la tirilla, la aplicación elimina ese carrito de compras y queda disponible para ejecutar de nuevo comandos.
Comando 3 – Salir de la aplicación

La sintaxis del comando 3 es la siguiente:

3

 Este comando simplemente permite salir de la aplicación

Entrada: Diferentes comandos según el cargue y la impresión de tirillas de venta

Salida: Salidas dependiendo del comando especificado anteriormente

Nota: Como el centro comercial está siendo muy generoso con los descuentos, el valor a cobrar en caso de tener centavos se debe aproximar a techo usando la función ceil de python (https://www.tutorialspoint.com/python/number_ceil.htm)

Ejemplo:

Entrada

Salida

1&Chocolatinas Cohete&3&300
1&Mora&1&1000
1&Pan de Maiz&5&300
2&1022734737
1&Televisor&2&1500000
1&Teatro en Casa&1&450000
2&99999287
3

Centro Comercial Unaleño
Compra más y Gasta Menos
NIT: 899.999.063
Cliente: 1022734737
Art Cant Precio
Chocolatinas Cohete 3 $900
Mora 1 $1000
Pan de Maiz 3 $1500
Total: $3400
En esta compra tu descuento fue $0
Gracias por tu compra
---
Centro Comercial Unaleño
Compra más y Gasta Menos
NIT: 899.999.063
Cliente: 99999287
Art Cant Precio
Televisor 2 $3000000
Teatro en Casa 1 $450000
Total: $2760000
En esta compra tu descuento fue $690000
Gracias por tu compra
---

 

