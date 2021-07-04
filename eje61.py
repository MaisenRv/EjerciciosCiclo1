f = open("salida.txt","r")

#va linea por linea leyendo
for linea in f:
    print(linea[:-1])

f.close()