from os import system

system("cls")

#miestra la letra que esta en corchetes
x = "jose maria cordoba"
print(x[2])

#mayuscula la primera letra
print(x.capitalize())

#El tecto lo pone en mayuscula
print(x.upper())

#Todo en minuscula
print(x.lower())

#centra el texto entre 25 caracteres " "
print(x.center(25,"-"))

#alinea a la de derecha
print(x.rjust(35, "*"))

#alinea a la izquierda
print(x.ljust(35, "*"))

#muestra las letras que estan entre parentecis las pociciones 5 al 9
print(x[5:10])

#cuenta el numero de caracteres que hay en la cadena
print(x.count("a"))

#busca la letra en la cadena y devuelve la pocicion
print(x.find("m")) #tiene otro parametro x.find("0", 2)

#cuenta el numero de los caracteres
print(len(x))

y = "  alejandra                      raquel             "

#quita los espacios del principio y  del final
print(y.strip())

#derecha 
print(y.rstrip())

#izquierda
print(y.lstrip())

#remplaza letras, el tercer parametro es el munero de letras que se quiera
#remplazar
print(x.replace("m","M",1))
print(x.replace("e","E"))


print(x.rjust(40,"0"))

