d = {"C001":"Juan","C002":"crema dental"}

i = 0

while True:
    codigo = input(f"Codigo No{i+1}: ")

    if codigo == "*":
        break

    if codigo in d:
        print("ese codigo ya existe")
        exit()
    producto = input("Producto: ")
    #Inserta un nuevo elemento y una nueva llave
    d[codigo] = producto
    i +=1
print(d)