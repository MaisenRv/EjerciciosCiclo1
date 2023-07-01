d = {}

nombre = input("Nombre: ")
edad = input("Edad: ")
direccion = input("Direccion: ")
telefono = input("Telefono: ")

d["nombre"] = nombre
d["edad"] = edad
d["direccion"] = direccion
d["telefono"] = telefono

print(d)

print(d["nombre"],"tine",d["edad"],"años, vive en",d["direccion"], " y su numero de telefono es",d["telefono"])