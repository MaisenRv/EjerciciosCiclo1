# Autor : David Santiago Mancera Robles
# Fecha : 15/06/2021

llave1 = input().upper()
llave2 = input().upper()
llave3 = input().upper()

contadorLlave1 = 0
contadorLlave2 = 0

cadena = ""

for i in range(len(llave3)):
    if llave3[i] in llave1:
        contadorLlave1 += 1
    if llave3[i] in llave2:
        contadorLlave2 += 1

    if contadorLlave1 == contadorLlave2:
        cadena += "x"
    elif contadorLlave1 > contadorLlave2:
        cadena += "-"
    else:
        cadena += "."

print(cadena)