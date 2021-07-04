#numero es donde estan los numeros
f = open("numeros.txt","r")

p = open("pares.txt","w")
i = open("impares.txt","w")

#sapara los numeros pares e impares en dos diferentes archovos 
#planos
for linea in f:
    numero = int(linea[:-1])

    if numero % 2 == 0:
        p.write(str(numero) + "\n")
    else:
        i.write(str(numero) + "\n")



f.close()
p.close()
i.close()