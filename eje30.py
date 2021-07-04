from os import system
system("cls")

#la cadena queda en minuscula
cadena = input("cadena: ")
contador = 0

for x in cadena:
    if x == x.upper() and x != " ":
        contador += 1

print(contador) 