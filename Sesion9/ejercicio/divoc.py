# i = 0

# while i < 5:
#     i = i + 1
#     print(i)


paisA = int(input("PaísA contaminados: "))
paisB = int(input("PaísB contaminados:"))
dia = 1

while paisA > paisB:
    paisA = (paisA * 1.02)
    paisB = (paisB * 1.03)
    dia = dia + 1
    
print(dia)
