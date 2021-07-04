# Autor: Santiago Mancera
# Fecha: 26/05/2021

from math import pi

print("****MENU****\n")
print("1.Cuadrado")
print("2.Triangulo")
print("3.Circulo\n")

opcion = input("De que figura quiere hallar el area: ")

if  opcion is  "1" or opcion is "2" or opcion is "3":
    if opcion == "3":
        radio = float (input("Radio del circulo: "))
        print("El area del circulo es:",pi * radio**2)
    else:
        altura = float (input("Altura: "))
        base = float (input("Base: "))

        if opcion == "1":
            print("El area del cuadrado es:",base * altura)
        else:
            print("El area del triangulo es:",(base * altura) / 2)
else:
    print("No es un valor valido")
    input("precione enter para continuar.....")
    exit(0)

input("precione enter para continuar.....")