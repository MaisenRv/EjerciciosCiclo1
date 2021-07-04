
tipoEstudiante = input("Tipo estuddiante (A:Alto, M:Medio, B:Bajo): ")
nota = float (input("Escriba nota: "))

if tipoEstudiante == "A" and nota == 5:
    print ("gana una beca")
elif tipoEstudiante == "A" and nota < 5 and nota >= 3:
    print ("Gana media beca")
elif tipoEstudiante == "M" and nota == 5:
    print("Gana un viaje")
elif tipoEstudiante == "M" and nota < 5 and nota >= 3:
    print("Gana un viaje a melgar")
elif tipoEstudiante == "B" and nota == 5:
    print("Gana un ponque")
elif tipoEstudiante == "B" and nota < 5 and nota >= 3:
    print("Gana premio de consolacion")


input ("Oprima enter para continuar......")