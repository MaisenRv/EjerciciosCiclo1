from os import system
system("cls")

#la cadena queda en minuscula
cadena = input("cadena: ").replace(" ","").lower()
salida = ""



for x in cadena:
    salida = x + salida

if salida == cadena:
    print("es palimdrome")
else:
    print("no es palindrome")