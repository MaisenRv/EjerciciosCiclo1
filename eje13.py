import os
os.system("cls")

while True:
    try:
        #Pide los las horas,minutos y el momento del dia (am o pm)
        #Descarta los errores correspondientes a los metodos de int con el except.
        horas = int(input("Horas: "))
        minutos = int(input("Minutos: "))
        momentoDia  = input("¿am o pm?: ")

        #Valida que los inputs esten acordes a los las horas (1 a 12), minutos (1 a 59)
        #y si se escribio algo deferente de am o pm en el momento del dia
        #si hay algun error vuelve y pregunta al usuario.
        while  horas > 12 or horas < 1 or minutos > 59 or minutos < 0 or momentoDia != "am" and momentoDia != "pm":
            if  horas > 12 or horas < 1:
                print("El valor de las horas debe estar entre 1 y 12")
                horas = int(input("Horas: "))
            if minutos > 59 or minutos < 0:
                print("El numero de los minutos debe estar entre 0 y 59")
                minutos = int(input("Minutos: "))
            if momentoDia != "am" and momentoDia != "pm":
                print("Debe escribir am o pm")
                momentoDia  = input("¿am o pm?: ")        
            
        break
    except :
        print("Los valores puestos no son validos")

if momentoDia == "am":
    doceHoras = 720
    if horas == 12 and minutos == 0:
       minutosFaltantes = 1440
    else:
        minutosFaltantes = doceHoras + ((11 - horas) * 60) + (60 - minutos)
else:
    if horas == 11:
        minutosFaltantes = 60 - minutos
    else:
        minutosFaltantes = ((11 - horas) * 60) + (60 - minutos)
        


print("Faltan",minutosFaltantes,"para las 12")