def palindrome(cadena):
    cadena = cadena.lower().replace(",","").replace(".","").replace(" ", "")
    invertido = ""
    for i in cadena:
        invertido = i + invertido
    
    if cadena == invertido:
        print("es palindrome")
    else:
        print("no es palindrome")

cadena = input("Validar la palabra ingresada si es palindrome o no: ")

palindrome(cadena)

