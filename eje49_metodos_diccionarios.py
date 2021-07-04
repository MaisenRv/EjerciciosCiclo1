productos = {"c001":"Atun","c002":"Maiz","c003":"Aguacate","c004":"Aceite"}

print(len(productos))


#borra el diccionario (elementos)

#--->print(productos.clear())

#hace una copia del productos
x = productos.copy()


#pasar una lista de tuplas a un diccionaario
l = [(10,"juan"),(20,"luisa"),(30,"raul")]
dict(l)


#buscar si la llave "c002" esta dentro del diccionario 
"c002" in productos

#muestra todas la llaves del diccionario
productos.keys()
#saca las llaves y las pone en una lista
l = list(productos.keys())
"""
for key in productos:
    print(key)
"""
"""
max()
min()
teniendo encuenta la llave
"""
#saca los valores del diccionario
productos.values()

#ordena el dicconario dependiendo la llave
sorted(productos)

#saca el elemento con la llave que se le esta dando 
#saca el elemento del diccionario
z = productos.pop("c004")

#actualiza un elemento
productos["c001"] = "Manzanas"
#crea la llave que no existe y le pone el valor que 
#le doy
productos["c005"] = "Peras"
#ver el elemento con la llave
productos["c002"]

#el "No existe esa llave" es para que si no existe me retorne ese valor
productos.get("c005","No existe esa llave")












