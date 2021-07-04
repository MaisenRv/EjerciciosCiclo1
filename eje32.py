from os import system

system("cls")

n = int(input("cantidad de valores: "))
suma = 0
salida = ""

for i in range(1, n + 1):
    valor = int(input("valor "+ str(i) + ": "))
    suma += valor
    salida += str(valor).rjust(10, " ")+ "\n"

print(salida, end="")
print("----------".rjust(10," "))
print(str(suma).rjust(10, " "))