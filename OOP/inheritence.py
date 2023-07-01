class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def getInfo(self):
        print(self.nombre)
        print(self.edad)
    

#la clase Estudiente esta heredando los atributos
# nombre y edad de la clase Persona 
class Estudiante(Persona):# -->hereda
    pass
       
            

persona = Persona("jose",20)
persona.getInfo()


estudiante = Estudiante("santiago",24)

estudiante.getInfo()

