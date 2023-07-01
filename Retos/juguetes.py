#Autor : David Santiago Mancera Robles
#Fecha : 10/2021

def Productos(A):
    lista_final = []
    
    for juguete in A:
        if not juguete in lista_final:
            lista_final.append(juguete)

    return lista_final


def Faltante (L, M, N):
    faltante = []

    for posicion in L:
        if M[posicion] == N:
            faltante.append(posicion)

    return faltante

def TeFaltan(L1,L2):
    vender = []

    for juguete in L1:
        if not juguete in L2:
            vender.append(juguete)

    return vender



def Intercambiemos(L1,L2):
    numero_juguetes = 0

    comprobar1 = TeFaltan(L1,L2)
    comprobar2 = TeFaltan(L2,L1)

    if len(comprobar1) < len(comprobar2):
        numero_juguetes = len(comprobar1)
    else:
        numero_juguetes = len(comprobar2) 

    return numero_juguetes

def darNombre():
    return __name__
