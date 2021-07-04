print("****MENU****\n")
print("1.Suma")
print("2.Resta")
print("3.Multiplicacion")
print("4.Division\n")

opcion = input("Seleccione la operacion a ejecutar: ")

if opcion == "1" or opcion =="2" or opcion =="3" or opcion =="4":
    n1 = float (input("Numero 1: "))
    n2 = float (input("Numero 2: "))

    if opcion == "1":
        print("la suma es ",n1 + n2)
    elif opcion == "2":
        print("la resta es ",n1 - n2)
    elif opcion == "3":
        print("la multiplicacion es ",n1 * n2)
    elif opcion == "4":
        if n2 == 0:
            print("El denominador no puede ser 0")
        else:
            print("la division es ",n1 / n2)
else:
    print("Opcion incorrecta")
    input ("Oprima enter para continuar......")
    exit(0)



input ("Oprima enter para continuar......")
