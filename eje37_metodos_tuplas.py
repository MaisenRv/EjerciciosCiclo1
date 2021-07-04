#las tuplas no se pueden modificar
# se crean para elementos que novarian en el tiempo 
#tuplas son mas rapidas en ejecucion que las listas 


tupla = ("cali", "bogota", "cucuta")
notas = (12,3,14,54,23,54,3,1,1)

#devuelve la posicion del elemento
print(tupla.index("bogota"))

#cuentas los elementos iguales
print(tupla.count("cali"))

#Lo ordena alfabeticamente
#con numeros los ordena de menor a mayor
#devuelve una lista
print(sorted(tupla))
#los ordena al reves
print(sorted(tupla, reverse=True))

#suma los elementos solo numeros
print(sum(notas))

#me dice si la cadena de caracteres esta dentro de la tupla 
#o dentro de otra cadena de caracteres
print("cali" in tupla)


#cuenta los elementos
#tambien cuenta los careacteres de una cadena
print(len(tupla))


#los elementos de las dos tuplas se unen en una sola
print(tupla + notas)

#sale el numero mayor de las notas 
#con cadena de caracteres toma el valor de la tabla ASCII 
print(max(notas))

#se corvierte en una lista
#al reves ---> tuple(notas)
print(list(notas))


#sin la coma aparece como un int
#con la coma aparece como una tupla
pp = (5,)

#borra la tupla
del notas



