
frutas = {1:"Lulo",2:"Manzana",3:"Pera",4:"Banano"}


while True:
    producto = input("Producto: ")

    if producto == "*":
        break

    #coje las llave [1,2,3,4]
    lista = list(frutas.keys())
    #coje el el numero maximo 
    #y le suma 1
    n = max(lista) + 1
    frutas[n] = producto


print(frutas)