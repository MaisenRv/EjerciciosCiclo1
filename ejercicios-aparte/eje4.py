n = [0,0,0,0,1,0]


paso = 0
extra = 0
for i in range(6):    
    try:
        if n[i+extra] == n[i+2]:
            paso += 1
            extra += 2
        else:
            paso +=1
    except:
        paso += 1
        break
print (paso)

        
    