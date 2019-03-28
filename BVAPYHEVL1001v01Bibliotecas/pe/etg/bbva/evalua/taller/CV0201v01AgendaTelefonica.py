#==============================================================================
# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	EVL (Evaluación de Python 3.6.1.)
# Módulo			        :   Generacion HTML
# Fecha	Creación	    :	28Mar2019
# Objetivo			        :   Biblioteca Tkinter
#                                  :
# Procedimiento       :   Agenda telefónica
#
#==============================================================================
import tkinter as oFormatoVentana
import time

# 1. Declarar el frame de la ventana
oVentana = oFormatoVentana.Tk()
oVentana.title("....[ Módulo de Evaluación ].....")
oVentana.configure(bg="pink")
oVentana.geometry("800x600")

# 2. Declarar las variables a utilizar
oListaContactos = {}
Nombre=oFormatoVentana.StringVar()
Apellido=oFormatoVentana.StringVar()
Celular=oFormatoVentana.StringVar()

# 3. Declarar etiquetas y datos de entry
oLabelNombre = oFormatoVentana.Label(oVentana, text="Nombres : ", width=5, font=("Verdana", 6)).grid(column=0, row=0)
oTextoNombre = oFormatoVentana.Entry(oVentana, text=Nombre, width=30).grid(column=1, row=0)

oLabelApellido = oFormatoVentana.Label(oVentana, text="Apellidos : ", width=10, font=("Verdana", 8)).grid(column=0, row=1)
oTextoApellido = oFormatoVentana.Entry(oVentana, text=Apellido, width=20)
oTextoApellido.grid(column=1, row=1)

oLabelCelular = oFormatoVentana.Label(oVentana, text="Celular : ", width=15, font=("Verdana", 10)).grid(column=0, row=2)
oTextoCelular = oFormatoVentana.Entry(oVentana, text=Celular, width=10)
oTextoCelular.grid(column=1, row=2)


# 4. Declarar los botones
def grabarContacto():
    sNombre = Nombre.get()
    sApellido = Apellido.get()
    sCelular = Celular.get()
    oListaContactos[sNombre + sApellido] = sCelular


oButtonGrabar = oFormatoVentana.Button(oVentana, text="Grabar", font=("Verdana", 12), command=grabarContacto)
oButtonGrabar.grid(column=0, row=3, columnspan=2, sticky='ew')
oButtonImprimir = oFormatoVentana.Button(oVentana, text="Imprimir", font=("Verdana", 12), command=lambda : print(oListaContactos))
oButtonImprimir.grid(column=0, row=4, columnspan=2, sticky='ew')


# 5. Ejecución de la ventana
oFormatoVentana.mainloop()