#modifica los datos sin borrar lo que tanga a dentro
f = open("salida.txt","a")

n = int(input("numero de registros: "))

for i in range(n):
    cedula = input("cedula: ")
    nombre = input("nombre: ")
    correo = input("correo: ")

    linea = cedula+ "\t"+ nombre +"\t" + correo + "\n"
    f.write(linea)

f.close()