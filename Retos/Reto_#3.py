# Autor : David Santiago Mancera Robles
# Fecha : 26/06/2021

letras = input().split()
listaNumeros = []
listaOrdenGeneros = []

contadorH = 0
contadorM = 0

for i in range(len(letras)):
   
    if letras[i] == "H" and contadorH == 0:
        listaNumeros.append(str(contadorM))
        contadorM = 0 
        contadorH += 1
        listaOrdenGeneros.append(letras[i])
    
    elif letras[i] == "H" and contadorH > 0:
        contadorH += 1
    
    elif letras[i] == "M" and contadorM == 0:
        listaNumeros.append(str(contadorH))
        contadorH = 0
        contadorM += 1
        listaOrdenGeneros.append(letras[i])
    else:
        contadorM += 1

    if i + 1 == len(letras) and contadorH == 0:
        listaNumeros.append(str(contadorM))
    elif i + 1 == len(letras) and contadorM == 0:
        listaNumeros.append(str(contadorH))

stringNumeros = " ".join(listaNumeros[1:])

print(" ".join(listaOrdenGeneros))
print(stringNumeros)