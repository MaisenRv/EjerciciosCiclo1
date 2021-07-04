def cadenaUnvluida(cadena1, cadena2):
    for i in cadena1:
        if cadena2.find(i) == -1:
            return "No se encuetra"
    return "si lo contiene"    

cadena1 = input("candena 1: ")
cadena2 = input("candena 2: ")

print(cadenaUnvluida(cadena1,cadena2))


