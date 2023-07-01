import random
from tkinter import *

ventana = Tk()

ventana.mainloop()

intentos = 0
numero = random.randint(1,10)

print ("como te llamas")
nombre = input()

print ("hola " + nombre + " estoy pensando en un numero del 1 al 10 podrias adivinarlo")
print("solo tienes 6 intentos")

while intentos < 6:
    estimacion = input()
    estimacion = int(estimacion)
    intentos += 1
    if(estimacion == numero):
        print("Lo adivinaste, tu numero de intentos fue " + str(intentos))
        break
    if(intentos == 6):
        print("Lo siento ya no tienes intentos, el numero era " + str(numero))
        break
    if(estimacion > numero):
        print("muy alto")
    if(estimacion < numero):
        print("my bajo")



