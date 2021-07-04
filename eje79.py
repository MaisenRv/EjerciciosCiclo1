#recurcion
def sumar(n):
    if n > 0:
        return n + sumar(n-1)
    else:
        return 0