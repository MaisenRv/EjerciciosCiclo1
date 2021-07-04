cedula = input("Cedula: ")
f = open("salida.txt","r")

encontro = False
data = []
#Borra un registro de el archivo plano
for linea in f:
    lista = linea[:-1].split("\t")
    
    #l = f.readlines()
    #lee todas las linesas y me devuelve una lista

    if lista[0] != cedula:
       data.append(linea)
    else:

        encontro = True

f.close()
if not encontro:
    print("No existe ese registro") 
else:
    f = open("salida.txt","w")

    for linea in data:
        f.write(linea)

    f.close()
