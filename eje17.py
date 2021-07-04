def intereses (credito):
    mes1 =  (credito + credito *0.03)
    mes2 = mes1 + mes1 * 0.03
    return mes2

print(intereses(500000))