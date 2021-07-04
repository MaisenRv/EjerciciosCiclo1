f = open("salida.txt","r")

#va linea por linea leyendo
for linea in f:
    #muestara solo los nombres separados por tabulador
    lista = linea[:-1].split("\t")
    print(lista[1])
f.close()