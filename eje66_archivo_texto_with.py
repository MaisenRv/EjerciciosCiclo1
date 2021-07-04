#mejor forma de utilizar archivos planos 
#no se necesita el f.close()
with open ("numeros.txt","r") as f:
    data = f.read()
    print(data)