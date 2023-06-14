import math
from tkinter import *
from tkinter import ttk,messagebox

class calculador():
    __ventana = None
    __vestimentacantidad = None
    __vestimentabase = None
    __vestimentaactual = None
    __alimentoscantidad = None
    __alimentosbase = None
    __alimentosactual = None
    __educacionactual = None
    __educacionbase = None
    __educaciocantidad = None
    
    __total=None

    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.geometry('500x300')
        self.__ventana.title('Calculadora IPC')
        
        self.__vestimentacantidad = StringVar()
        self.__vestimentabase = StringVar()
        self.__vestimentaactual = StringVar()
        self.__alimentoscantidad = StringVar()
        self.__alimentosbase = StringVar()
        self.__alimentosactual = StringVar()
        self.__educacionactual = StringVar()
        self.__educacionbase = StringVar()
        self.__educaciocantidad = StringVar()
        self.__total=StringVar()
        

        ttk.Button(self.__ventana, text='Salir', command=self.__ventana.destroy).place(x=340,y=200)
        ttk.Button(self.__ventana,text='Calcular IPC',command=self.calcular).place(x=145,y=200)
        ttk.Label(self.__ventana, text='Item').place(x=20, y=30)
        ttk.Label(self.__ventana, text='Cantidad').place(x=140, y=30)
        ttk.Label(self.__ventana, text='Precio Año base').place(x=240, y=30)
        ttk.Label(self.__ventana, text='Precio Año actual').place(x=360, y=30)
        ttk.Label(self.__ventana, text='Vestimenta').place(x=20, y=70)
        ttk.Label(self.__ventana, text='Alimentos').place(x=20, y=110)
        ttk.Label(self.__ventana, text='Educacion').place(x=20, y=150)
    
        ttk.Entry(textvariable=self.__vestimentacantidad).place(x=130,y=70,width=80)
        ttk.Entry(textvariable=self.__vestimentabase).place(x=250,y=70,width=80)
        ttk.Entry(textvariable=self.__vestimentaactual).place(x=380,y=70,width=80)
        ttk.Entry(textvariable=self.__alimentoscantidad).place(x=130,y=110,width=80)
        ttk.Entry(textvariable=self.__alimentosbase).place(x=250,y=110,width=80)
        ttk.Entry(textvariable=self.__alimentosactual).place(x=380,y=110,width=80)
        ttk.Entry(textvariable=self.__educaciocantidad).place(x=130,y=150,width=80)
        ttk.Entry(textvariable=self.__educacionbase).place(x=250,y=150,width=80)
        ttk.Entry(textvariable=self.__educacionactual).place(x=380,y=150,width=80)
        
        ttk.Label(self.__ventana,text='IPC % XX.XX').place(x=55,y=230)
        ttk.Label(self.__ventana,textvariable=self.__total).place(x=135,y=230)

        self.__ventana.mainloop()
    def calcular(self):
        try:
            vestimentacan = float(self.__vestimentacantidad.get())
            vestimentaba = float(self.__vestimentabase.get())
            vestimentaac = float(self.__vestimentaactual.get())
            alimentoscan = float(self.__alimentoscantidad.get())
            alimentosba = float(self.__alimentosbase.get())
            alimentosac = float(self.__alimentosactual.get())
            educacionact = float(self.__educacionactual.get())
            educacionba = float(self.__educacionbase.get())
            educaciocan = float(self.__educaciocantidad.get())
            
            
            costoBase = ((vestimentaba*vestimentacan) + (alimentosba*alimentoscan) + (educacionba*educaciocan))
            costoActual = ((vestimentaac*vestimentacan) + (alimentosac*alimentoscan) + (educacionact*educaciocan))
            
            
            totalipb=(costoActual/costoBase)
            parteDec, parteEnt = math.modf(totalipb)
            self.__total.set('{0:.2f}%'.format(parteDec * 100))

        except ValueError:
            messagebox.showerror(title='Error de tipo',message='Faltan datos para operacion, intente nuevamente.')

def testAPP():
    miapp = calculador()

if __name__ == '__main__':
    testAPP()