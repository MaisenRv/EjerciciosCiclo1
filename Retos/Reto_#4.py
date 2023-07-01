#Autor: David Santiago Mancera Robles
#Fecha: 30/06/2022

import json

j = input()
numeros = input().split()
diccionario = json.loads(j)

suma = 0
codigos = []

for numero in numeros:
    if numero in diccionario:
        suma += diccionario[numero]
        codigos.append(numero)

print(suma)
print(" ".join(codigos))