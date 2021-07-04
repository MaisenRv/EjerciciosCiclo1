f = open("salida.txt","w")

cedula = input("cedula: ")
nombre = input("nombre: ")
correo = input("correo: ")

linea = cedula+ "\t"+ nombre +"\t" + correo

f.write(linea)

f.close()