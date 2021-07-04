import  openpyxl

archivo = openpyxl.load("archivo.xlsx")

H1 = archivo["Hoja1"]

#pone un valor en una celda de excel 
H1.cell(row = 470,column= 1).value = "ejemplo"

#guarda el archivo excel
archivo.save("archivo.xlsx")