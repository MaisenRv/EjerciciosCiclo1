#Clcula el area y el volumen de un cilindro.
# Autor: Santiago Mancera
# Fecha: 25/05/2021

from math import pi

h = float (input ("Introdusca la altura del cilindro: "))
r = float (input ("Introdusca el radio del cilindro: "))

#formula para calcular el area del cilindro.
area = 2 * pi * r *(h + r)

#formula para calcular el volumen del cilindro.
volumen = pi * r**2 * h

print ("El area del cilindro es:",round(area,2),"cm^2")
print ("El volumen del cilindro es:",round(volumen,2),"cm^3")
input ("Enter para continuar....")
