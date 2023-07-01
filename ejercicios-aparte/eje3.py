def sockMerchant(ar):
    # Write your code here
    diccionario = {}
    
    for calsetin in ar:
        try:
            diccionario[calsetin] += 1 
        except:
            diccionario[calsetin] = 1
    print(diccionario)

ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

sockMerchant(ar)