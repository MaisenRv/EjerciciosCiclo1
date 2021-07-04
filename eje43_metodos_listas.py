datos = [14, 2.58, "Juan David",(2,4,6,8),["qwe","ewq"]]

#remueve un elemento de la lista
datos.remove(14)

#elimina el ultimo elemento de la lista
#pop(3) elemina el elemento de la posicion 3
datos.pop()

#inserta elementos 
#primer dato lugar de la lista 
# segundo el elemento 
datos.insert(2,13)

#pone los elementos de la lista al reves 
datos.reverse()

#los ordena de mayor a menor datos.sort(reverse = True)
#altera la lista
datos.sort()

#no altera la lista
sorted(datos)

#limpia toda la lista y la leja sin nada de elementos
datos.clear()

#concatena lista en una sola
#---> datos.extend(otra lista)

#----> list(zip(lista1,lista2))
# crea una lista de tuplas [(a1,b1),(a2,b2)]



print(datos)