from os import system


dataBase = []

while True:
    system("cls")
    print("*******menu********")
    print()
    print("1. Insertar registro")
    print("2. Borror registro")
    print("3. Actualizar registro")
    print("4. Consultar base de datos")
    print("5. Salir")
    print()

    opc = input("seleccione una opcion")

    if opc == "5":
        break
    elif opc == "1":
        system("cls")
        print("modo insertar")
        print()
        cedula = input("cedula: ")
        nombre = input("nombre: ")
        edad = int(input("edad: "))
        correo = input("correo: ")

        dataBase.append([cedula,nombre,edad,correo])
        print("dato insertado")
        input("oprima enter para continiar....")
    
    elif opc == "2":
        system("cls")
        print("modo borrar")
        print()
        cedula = input("cedula: ")

        for i, item in enumerate(dataBase):
            if cedula == item[0]:
                dataBase.pop(i)
                break
        print("dato borrado")
        input("oprima enter para continiar....")
    elif opc == "3":
        system("cls")
        print("modo actualizar")
        print()
        cedula = input("cedula: ")
        
        for i, item in enumerate(dataBase):
            if cedula == item[0]:
                nombre = input("nombre: ["+item[1]+": ").split()
                if nombre == "":
                    nombre = item[1]
                item[1] = nombre

                edad = input("edad: ["+str(item[2])+": ").split()
                if edad == "":
                    edad = item[2]
                item[2] = int(edad)                
                correo = input("edad: ["+item[3]+": ").split()
                if correo == "":
                    correo = item[3]
                item[3] = correo
                print("dato actualizado")
                input("oprima enter para continiar....")
                break
    elif opc == "4":
        system("cls")
        print("modo consulta")
        print()
        print(dataBase)
        input("oprima enter para continiar....")

