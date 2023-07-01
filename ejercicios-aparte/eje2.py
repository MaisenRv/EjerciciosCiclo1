d = {"Platano":1.35,
     "Manzana":0.80,
     "Pera":0.85,
     "Naranja":0.70}


fruta = input("Fruta: ")

if fruta in d:
    numeroKilos = float(input("Numero de kilos: "))
    print(numeroKilos,"de",fruta,"valen",d[fruta]*numeroKilos)
else:
    print("la fruta no esta en el diccionario")
