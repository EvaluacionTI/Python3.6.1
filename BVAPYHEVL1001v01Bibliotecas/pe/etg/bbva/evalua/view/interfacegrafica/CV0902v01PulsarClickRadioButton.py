#==============================================================================
# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	EVL (Evaluación de Python 3.6.1.)
# Módulo			        :   Generacion HTML
# Fecha	Creación	    :	02Abr2019
# Objetivo			        :   Biblioteca Tkinter
#                                  :
# Procedimiento       :   RadioButton
#
# Declaramos una variable llamada oWindowRoot, del tipo Tk().
#
# Además de Tk(), podemos declarar más variables
#
# Mainloop es el encargado de manejar y manipular todos los eventos que ocurran durante el codigo.
#==============================================================================
import tkinter as oFormat
from tkinter.ttk import Radiobutton as oFormatRadioButton

# 1. Declarar la ventana padre
oWindowRoot = oFormat.Tk()

oWindowRoot.title(".....[ Módulo de Evaluación ].....")
oWindowRoot.config(bg="pink")       # Color de fondo de la ventana
oWindowRoot.geometry("800x600") # Tamaño de la ventana 800 pixel de ancho y 600 de alto

# 2. Declarar Etiquetas
oLabel = oFormat.Label(oWindowRoot, text="Arquitectura APX / HOST ", font=("Arial Bold", 20), bg="green", fg="blue")
oLabel.grid(column=0, row=0)

oLabelTipoCanal = oFormat.Label(oWindowRoot, text="Tipo de canal :  ", font=("Verdana", 12))
oLabelTipoCanal.grid(column=0, row=1)


def clicked():
    print("Se ha pulsado APX")


def clickedHost():
    print("Se ha pulsado HOST")


# 3. Declarar el Radio Button
# 3.1 Declara un estado
oRadioCanalAPX = oFormatRadioButton(oWindowRoot, text="APX", value=1, command=clicked)
oRadioCanalAPX.grid(column=1, row=1)

oRadioCanalHost = oFormatRadioButton(oWindowRoot, text="HOST", value=2, command=clickedHost)
oRadioCanalHost.grid(column=1, row=2)


oWindowRoot.mainloop()      # Evento que llama al inicio de nuestro programa
