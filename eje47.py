paises = ["Dinamarca","Colombia","Australia","Venezuela","Argentina","Chile"]


for i, x in enumerate(paises):
    paises[i] = x[1] + x

paises.sort()

for i, x in enumerate(paises):
    paises[i] = x[1:]

print(paises)

paises = [x[1]+x for x in paises]

paises.sort()

paises = [x[1:] for x in paises]

print(paises)