# A un niño pequeño le gusta escribir al reves. Sin embargo ha escrito unas cadenas muy largas y se tiene la traducción. El necesita su ayuda para saber si lo que ha escrito al revés es lo mismo que piensa.

# Entrada:
# Dos Strings uno con la cadena al derecho y otro con la posible cadena invertida.

# Salida:

# La palabra SI si la palabra corresponde a su versión invertida.  La palabra NO en caso contrario.

# Ejemplo:

# Input                                                                                    

# Output

# No tengo ningún consejo para darle a aquel que desespera.
# .arepsesed euq leuqa a elrad arap ojesnoc núgnin ognet oN

# Return
# SI


#Variable de entrada
texto = input()
invertido = input()

#Función que recibe el valor 
def validador(a, b):
    if a == b[::-1]:
        print("SI")
    else:
        print("NO")

#Invocando función
validador(texto, invertido)