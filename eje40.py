n = int(input("numero de datos: "))
suma = 0
cadena = ""

for i in range(n):
    dato = float(input("Datos " + str(i+ 1) + ": ")) 
    suma += dato
    cadena += str(dato) + ":"

t1 = tuple(cadena[:-1].split(":"))
print("tupla:",t1)
print("promedio:",suma/n)