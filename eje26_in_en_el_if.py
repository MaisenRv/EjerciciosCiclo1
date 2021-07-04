from os import system
system("cls")

#la cadena queda en minuscula
cadena = input("cadena: ").lower()
contador = 0


#cuenta las bocales
for x in cadena:
    #si x esta dentro del conjunto de letras 
    if x in "aeiou":# <---- in
        contador += 1

print(contador)