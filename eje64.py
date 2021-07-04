
cedula = input("Cedula: ")
f = open("salida.txt","r")

encontro = False

for linea in f:
    lista = linea[:-1].split("\t")
    if lista[0] == cedula:
        encontro = True
        print("Nombre: " +lista[1])
        print("Correo: " + lista[2])
        break
if not encontro:
    print("No esta registrada la cedula")

f.close()
