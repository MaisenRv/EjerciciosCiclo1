factura = {"F0001":"Manzana","F0002":"Pera","F0003":"Banano"}

while True:
    producto = input()

    if producto == "*":
        break

    maxfac = max(factura.keys())
    n = int(maxfac[1:])+ 1

    nuevoPro = "F" + str(n).zfill(4)


    factura[nuevoPro] = producto

print(factura)