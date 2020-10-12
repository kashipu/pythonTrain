from fractions import Fraction as frac
x = input()
len_input = len(x)

def numeros(x):
    for sym in x:
        if sym == "/":
            symbol = int(x.index(sym))
            num1 = int(x[0 : symbol])
            num2 = int(x[symbol + 1 : len_input])
            simpli = str(frac(num1, num2))
            return simpli

print(numeros(x))
