# Autor: David Santiago Mancera Robles
# Fecha: 2/06/2021 

gotasRon = int(input())

gotasMar = (gotasRon * 2) + 4
gotasJarabeDulce = (gotasRon + gotasMar)//5

print(gotasRon,gotasMar,gotasJarabeDulce)

if gotasJarabeDulce < 21:
    print("uno")
elif gotasJarabeDulce < 31:
    print("dos")
elif gotasJarabeDulce < 51:    
    print("tres")
elif gotasJarabeDulce > 50:
    print("cuatro")
