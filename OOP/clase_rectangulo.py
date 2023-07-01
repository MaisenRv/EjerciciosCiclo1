class Rectangulo:

    def __init__(self, base,altura):
        self.base = base
        self.altura = altura
    
    def calcularArea(self):
        return self.base * self.altura

base = int(input("base: "))
altura = int(input("altura: "))

rectangulo = Rectangulo(base,altura)

print(rectangulo.calcularArea())