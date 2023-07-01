class Aritmetica:

    def __init__(self,op1,op2):
        self.op1 = op1
        self.op2 = op2

    def sumar(self):
        return self.op1 + self.op2

    def restar(self):
        return self.op1 - self.op2
    

aritmetica = Aritmetica(2,4)

print(aritmetica.sumar())