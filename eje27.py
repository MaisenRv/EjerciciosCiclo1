from os import system
system("cls")

#la cadena queda en minuscula
cadena = input("cadena: ").lower()
contador = 0


#cuenta los caracteres menos las vocales
for x in cadena:
    #si x no esta dentro del conjunto de letras 
    if x not in "aeiou":# <---- in
        contador += 1

print(contador)