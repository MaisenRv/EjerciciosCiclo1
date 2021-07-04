from os import system
system("cls")

#la cadena queda en minuscula
cadena = input("cadena: ")
salida = ""

for x in cadena:
    salida = x + salida

print(salida)