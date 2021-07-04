from os import system

system("cls")

i = 1

n = int(input())
suma = 0
while i <= n:

    if i == n:
        print(i, end=" = ")
    else:    
        print(i, end=" + ")
    suma += i
    i += 1

print(suma)