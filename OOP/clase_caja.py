class Caja:

    def __init__(self,altura,ancho,largo):
        self.altura = altura
        self.ancho = ancho
        self.largo = largo
    
    def volumen(self):
        volumen = self.altura * self.ancho * self.largo
        return str(volumen) + "cm cuadrados"


caja = Caja(2,3,4)

print(caja.volumen())