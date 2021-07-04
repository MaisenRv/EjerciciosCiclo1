
#si ya hay un archivo con informacion por dentro
#borrar el contenido y lo deja en blanco
f = open("salida.txt","w")
#w ---> escritura
#r --->lectura
#a --->edicion

#funcion para escribir
f.write("buenos dias\n")
f.write("como estan")

#muestra el nombre del archivo
#---> f.name

#solo lee dentro de los parametros que yo le doy
#---> f.seek(final,inicio)

#muestra el tamaño del archivo
#---> f.tell()


#cierra el archivo plano
f.close()
