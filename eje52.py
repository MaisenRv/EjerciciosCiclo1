d = {"C001":"Juan","C002":"crema dental"}

n = int(input("cuantos productos quiere incluir"))


for i in range(n):
    codigo = input(f"Codigo No{i+1}: ")

    if codigo in d:
        print("ese codigo ya existe")
        exit()
    producto = input("Producto: ")
    #Inserta un nuevo elemento y una nueva llave
    d[codigo] = producto

print(d)