d = {"C001":"Juan","C002":"crema dental"}

codigo = input("Codigo: ")

if codigo in d:
    print("ese codigo ya existe")
    exit()

producto = input("Producto: ")

#Inserta un nuevo elemento y una nueva llave
d[codigo] = producto

print(d)