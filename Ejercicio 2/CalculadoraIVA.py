import math
from tkinter import *
from tkinter import ttk,messagebox

class calculadora():
    __ventana = None
    __PrecioSinIVA = None
    __IVA = None
    __opcion = None
    __PrecioConIVA = None
    __montoIVA = None
    
    
    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.geometry('300x300')
        self.__ventana.title('Calculadora IVA')
        #self.__ventana.config(padx=5, pady=5)
        
        self.__PrecioSinIVA = StringVar()
        self.__PrecioConIVA = StringVar()
        self.__opcion = StringVar()
        self.__IVA = StringVar()
        self.__montoIVA = StringVar()
        
        #Primer Bloque, titulo
        Bloque1 = ttk.Frame(self.__ventana,padding="0 0 0 30")
        Bloque1.pack(side=TOP,fill=BOTH)
        self.Titulo = ttk.Label(Bloque1, text='Cálculo de IVA',background='lightblue2' ,anchor=CENTER,relief="solid",padding=10).pack(side=TOP,fill=BOTH)
        #Segundo Bloque, Ingresa precio sin IVA
        Bloque2 = ttk.Frame(self.__ventana,padding="0 0 0 30")
        Bloque2.pack(side=TOP)
        self.texto1 = ttk.Label(Bloque2, text='Precio sin IVA', padding='0 0 30 0').pack(side=LEFT)
        self.entrada1 = ttk.Entry(Bloque2,textvariable=self.__PrecioSinIVA,justify=CENTER).pack(side=LEFT)
        #Tercer Bloque, (Botones) Selecciona tipo de IVA
        Bloque3 = ttk.Frame(self.__ventana,padding='0 0 0 20')
        Bloque3.pack(side=TOP)
        self.botonIVA1 = ttk.Radiobutton(Bloque3,text='IVA 21 %', value=0,  variable=self.__opcion, command=self.cambiaValorIVA, padding='0 0 170 0').pack(side=TOP)
        self.botonIVA2 = ttk.Radiobutton(Bloque3,text='IVA 10.5 %', value=1, variable=self.__opcion, command=self.cambiaValorIVA, padding='0 10 160 0').pack(side=TOP)
        #Cuarto Bloque, a)muestra descripciones b)muestra resultados
        Bloque4 = ttk.Frame(self.__ventana)
        Bloque4.pack(side=TOP)
        Bloque4a = ttk.Frame(Bloque4)
        Bloque4a.pack(side=LEFT)
        self.texto2 = ttk.Label(Bloque4a, text='IVA').pack(side=TOP)
        self.texto3 = ttk.Label(Bloque4a, text='Precio con IVA').pack(side=TOP)
        Bloque4b = ttk.Frame(Bloque4,padding='40 0 0 0')
        Bloque4b.pack(side=LEFT)
        self.resultado1 = ttk.Label(Bloque4b, textvariable=self.__montoIVA, width=13,relief='solid',background='white',anchor=CENTER).pack(side=TOP)
        self.resultado2 = ttk.Label(Bloque4b, textvariable=self.__PrecioConIVA,width=13,background='white',relief='solid',anchor=CENTER).pack(side=TOP)
        #Quinto Bloque, botones de accion
        Bloque5 = ttk.Frame(self.__ventana,padding='0 50 0 0')
        Bloque5.pack(side= TOP)
        self.botonCalcula = ttk.Button(Bloque5,text='Calcular',command=self.calcula).pack(side=LEFT)
        self.botonSalir = ttk.Button(Bloque5,text='Salir',command=self.__ventana.destroy).pack(side=LEFT)
        
        
        
        self.__ventana.mainloop()
    
    def calcula(self):
        try:
            precioSIN = float(self.__PrecioSinIVA.get())
            iva = float(self.__IVA.get())
            montoiva = (precioSIN*iva)
            precioCON = ( montoiva + precioSIN)
            self.__PrecioConIVA.set(precioCON)
            self.__montoIVA.set(montoiva)
        except ValueError:
            messagebox.showerror(title='Error de valores',message='Faltan ingresar precio sin IVA, intente nuevamente.')
        
    def cambiaValorIVA(self):
            if self.__opcion.get()=='0':
                self.__IVA.set(0.21)
            else:
                if self.__opcion.get()=='1':
                    self.__IVA.set(0.105)
        
        
        

def testAPP():
    app = calculadora()

if __name__ == '__main__':
    testAPP()

        