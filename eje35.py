def invertir(cadena):
    invertido = ""
    for i in cadena:
        invertido = i + invertido
    return invertido

print(invertir("hola que hace"))