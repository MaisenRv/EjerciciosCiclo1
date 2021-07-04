epsilon = 2**(-1)
n = 0
valor = 0

while epsilon > 0:
    n -= 1
    valor = epsilon
    epsilon = 2**(n)

print(valor)