ciudades = ("bogota","cali","cartagena", "cucuta","rioacha")

for ele in ciudades:
    print(ele)

print()


for i in range(len(ciudades)):
    print(ciudades[i])

print()

#enumera el elemento y muestra el elemento
for i, ele in enumerate(ciudades):
    # i = indice
    # ele = elemento
    print(i,ele)
