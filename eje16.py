def cambio (p, m, h, b):
    total_a_pagar = p * 300 + m *3300 + h * 350
    vueltas = b - total_a_pagar
    return vueltas, total_a_pagar


p = int(input("panes: "))
m = int(input("bolsas de leche: "))
h = int(input("huevos: "))
b = int(input("billete: "))
x, y = cambio(p, m, h, b)

print("total a pagar: $",y)
print(x)
