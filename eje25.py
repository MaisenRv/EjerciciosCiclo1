from os import system
system("cls")

#la cadena queda en minuscula
cadena = input("cadena: ").lower()
contador = 0


#cuenta las bocales
for x in cadena:
    if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
        contador += 1

print(contador)