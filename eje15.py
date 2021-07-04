def area_rectangulo (a,l):
    return a * l

l = float(input("largo: "))
a = float(input("ancho: "))

area = area_rectangulo(a,l)

print("area ", end = " ")
print(area)