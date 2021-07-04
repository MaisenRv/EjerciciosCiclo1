from os import system
system("cls")

#la cadena queda en minuscula
cadena = input("cadena: ")
contador = 0

for x in cadena:
    #ord(x) ---> convierte a numero (tabla ASCII)
    if 65 <= ord(x) <= 90 :
        contador += 1

print(contador) 