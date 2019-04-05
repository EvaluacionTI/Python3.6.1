#==============================================================================
# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	EVL (Evaluación de Python 3.6.1.)
# Módulo			        :   Generacion HTML
# Fecha	Creación	    :	04Abr2019
# Objetivo			        :   Biblioteca Tkinter
#                                  :
# Procedimiento       :   Combo Box
#
# Declaramos una variable llamada oWindowRoot, del tipo Tk().
#
# Además de Tk(), podemos declarar más variables
#
# Mainloop es el encargado de manejar y manipular todos los eventos que ocurran durante el codigo.
#==============================================================================
import tkinter as oFormat
from tkinter import ttk as oFrameMain
from tkinter.ttk import Combobox as oFormatCombo

# 1. Declarar la ventana padre
#oWindowRoot = oFormat.Tk()

#oWindowRoot.title(".....[ Módulo de Evaluación ].....")
#oWindowRoot.config(bg="pink")       # Color de fondo de la ventana
#oWindowRoot.geometry("800x600") # Tamaño de la ventana 800 pixel de ancho y 600 de alto

# 2. Declarar Etiquetas
#oLabel = oFormat.Label(oWindowRoot, text="Arquitectura APX / HOST ", font=("Arial Bold", 20), bg="green", fg="blue")
#oLabel.grid(column=0, row=0)

class CVComboBox(oFrameMain.Frame):
    def __init__(self, oWindowRoot):
        super().__init__(oWindowRoot)
        oWindowRoot.title(".....[ Módulo de Evaluación ].....")

        # Contorno general de la ventana
        oWindowRoot.configure(width=800, height=600)
        self.place(width=800, height=600)

        self.labelCombo = oFrameMain.Label(self, text="Lista desplegable vacia y se puede escribir : ")
        self.labelCombo.place(x=10, y=50)

        self.combo = oFrameMain.Combobox(self)
        self.combo.place(x=250, y=50)


oWindowRoot = oFormat.Tk()
oAppCombo = CVComboBox(oWindowRoot)
oAppCombo.mainloop()      # Evento que llama al inicio de nuestro programa
