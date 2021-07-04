#calcula el numero pi.
n = int(input("terminos: "))
suma = 0
for i in range (1, n+1 ):
    suma += -(-1)**i / (2*i - 1)

print(4 * suma)