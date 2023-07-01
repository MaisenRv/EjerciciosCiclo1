class Persona:
    
    def __init__(self,nombre , edad):
        self.nombre = nombre
        self.edad = edad
"""
#modificar valores 
Persona.nombre = "juan"
Persona.edad = 28


# acceder a los valores
print(Persona.nombre)
print(Persona.edad)
"""

#creacion de un objeto

persona = Persona("juan1",27)

print(persona.nombre)


print(id(persona))

