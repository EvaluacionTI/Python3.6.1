#==============================================================================
# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	EVL (Evaluación de Python 3.6.1.)
# Módulo			        :   Generacion HTML
# Fecha	Creación	    :	10Abr2019
# Objetivo			        :   Biblioteca Tkinter
#                                  :
# Procedimiento       :   Notebook o pestañas
#
#                                   Establecer el color de fondo de las pestañas
#==============================================================================
import tkinter
from tkinter import ttk

oWindowRoot = tkinter.Tk()
oWindowRoot.title(".....[ Módulo de Evaluación ].....")
oWindowRoot.config(bg="pink")       # Color de fondo de la ventana
oWindowRoot.geometry("800x600") # Tamaño de la ventana 800 pixel de ancho y 600 de alto

nb = ttk.Notebook(width=200, height=200)
nb.pressed_index = None
f1 = tkinter.Frame(nb, background="red")
f2 = tkinter.Frame(nb, background="green")
f3 = tkinter.Frame(nb, background="blue")
nb.add(f1, text='Red', padding=3)
nb.add(f2, text='Green', padding=3)
nb.add(f3, text='Blue', padding=3)
nb.pack(expand=1, fill='both')

oWindowRoot.mainloop()