class Persona:
    
    def __init__(self,nombre,edad, *varios, **d):
        self.nombre = nombre
        self.edad = edad
        self.valores = varios
        self.diccionario = d


    def desplegar(self):
        print("Nombre:",self.nombre)
        print("Edad:",self.edad)
        print("Valores (tupla):",self.valores)
        print("Diccionario:",self.diccionario)

p1 = Persona("juan", 28, 2,4,5, m="manzana",p="pera", j="jicama")

p1.desplegar()