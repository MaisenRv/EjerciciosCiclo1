a = (2,8,7,3,5,1,7)
b = (2,5,3,2,5,8,6)
cadena = ""

for i in range(len(a)):
    cadena += str(a [i] + b [i] ) + ":"


c = tuple(cadena[:-1].split(":"))

print(c)