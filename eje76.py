import openpyxl

#crea una archivo nuevo de excel
archivo  = openpyxl.Workbook()
H1 = archivo.active

#se guarda para que aparesca 
archivo.save("nuevo.xlsx")
#----------------------------#

#borra una fila
H1.delete_rows(13,10)#fila,columna