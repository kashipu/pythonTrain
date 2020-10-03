#Entradas
cantidadPersonas = int(input())
opinionPersonas = list(map(int, input().split(' ')))
#Si contiene 0 es facil 
#Si contiene 1 es Dificil
def opinion(x):
    resultado = ""
    if 1 in x:
        resultado = "DIFICIL"
    else:
        resultado = "FACIL"
    return print(resultado)

opinion(opinionPersonas)

