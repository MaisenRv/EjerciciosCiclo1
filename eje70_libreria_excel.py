import openpyxl

#direccion del archivo
archivo = openpyxl.load_workbook("archivo.xlsx")

#selecciona la hoja del excel
h1 = archivo["Hoja1"]

#seleccion de una celda en especifico
#row es la fila
#column es la columna
dato = h1.cell(row=10, column=3).value

print(dato)