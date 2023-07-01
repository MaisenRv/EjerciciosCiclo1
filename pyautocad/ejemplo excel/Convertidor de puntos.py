from tkinter import *
from tkinter import ttk, filedialog, font
from pandas import read_excel 

class Aplicacion():
    def __init__(self): 

        self.root = Tk()
        self.ruta = ''

        # Configuracion de la ventana general
        self.fuente = font.Font(size=10, weight='bold')
        self.root.geometry('700x200')
        self.root.config(background= '#ffffff') ##26241E
        self.root.title('Excel a Json')

        # Creacion y cofiguracion de elementos
        self.frame = ttk.Frame(self.root,padding=(10,10))
        self.label = ttk.Label(self.frame, text='Ruta del archivo en Excel: ')
        self.btn_examinar = ttk.Button(self.frame,text='Examinar',padding=(5,5), command=self.open_file)
        self.btn_covertir = ttk.Button(self.frame, text='Covertir a Json', padding=(5,5), command=self.convert)

        # Organizacion de elementos en la ventana
        self.frame.grid(column=0, row=0, padx=5, pady=5, sticky=(N,S,E,W))
        self.label.grid(column=0, row=0, sticky=(E,W))
        self.btn_examinar.grid(column=1, row=0, sticky=(E,W))
        self.btn_covertir.grid(column=1, row=1, sticky=(E,W), pady=5)

        # Redimensionamiento dinamico
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)

        self.root.mainloop()

    # Metodos
    def open_file(self):
        self.ruta = filedialog.askopenfilename(filetypes=[('Excel files','*.xlsx')])  
        self.label_ruta= ttk.Label(self.frame, text= self.ruta)
        self.label_ruta.grid(column=0, row=1, sticky=(E,W), pady=5)
    
    def convert(self):
        if self.ruta != '':
            try:
                data = read_excel(self.ruta, usecols="A:E")
                print(data)
                data.to_json('puntos.json', orient="records")
            
            except:
                self.label_error = ttk.Label(self.frame,
                                                text='Ocurrio un error',
                                                anchor='center',
                                                foreground='red',
                                                font=self.fuente)
                self.label_error.grid(row=2, sticky=(E,W), pady=5, columnspan=2)
            else:
                self.label_success = ttk.Label(self.frame,
                                                text='Convertido con Exito!',
                                                anchor='center',
                                                foreground='green',
                                                font=self.fuente)
                self.label_success.grid(row=2, sticky=(E,W), pady=5, columnspan=2)
            return

        self.label_warning = ttk.Label(self.frame, 
                                        text='Debe seleccionar un archivo de Excel', 
                                        anchor='center', 
                                        foreground='blue',
                                        font=self.fuente)
        self.label_warning.grid(row=2, sticky=(E,W), pady=5, columnspan=2)
        

def main():
    my_app = Aplicacion()
    return 0

if __name__ == '__main__':
    main()


