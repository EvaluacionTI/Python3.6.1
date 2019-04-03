#==============================================================================
# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	EVL (Evaluación de Python 3.6.1.)
# Módulo			        :   Generacion HTML
# Fecha	Creación	    :	03Abr2019
# Objetivo			        :   Biblioteca Tkinter
#                                  :
# Procedimiento       :   SpinBox for Numbers
#
# Declaramos una variable llamada oWindowRoot, del tipo Tk().
#
# Además de Tk(), podemos declarar más variables
#
# Mainloop es el encargado de manejar y manipular todos los eventos que ocurran durante el codigo.
#==============================================================================
import tkinter as oFormat
from tkinter import Spinbox as oFormatNumers

# 1. Declarar la ventana padre
oWindowRoot = oFormat.Tk()

oWindowRoot.title(".....[ Módulo de Evaluación ].....")
oWindowRoot.config(bg="pink")       # Color de fondo de la ventana
oWindowRoot.geometry("800x600") # Tamaño de la ventana 800 pixel de ancho y 600 de alto

# 2. Declarar Etiquetas
# 2.1 Título de la Ventana
oLabel = oFormat.Label(oWindowRoot, text="Arquitectura APX / HOST ", font=("Arial Bold", 20), bg="green", fg="blue")
oLabel.grid(column=0, row=0)


# 3. Declarar SpinBox
oLabelRangeNumber = oFormat.Label(oWindowRoot, text="Rango de Números :")
oLabelRangeNumber.grid(column=0, row=1)
oTextRangeNumber = oFormatNumers(oWindowRoot, from_=0, to=100, width=10)
oTextRangeNumber.grid(column=1, row=1)

oLabelRangeFijo = oFormat.Label(oWindowRoot, text="Rango Fijo de Números :")
oLabelRangeFijo.grid(column=0, row=2)
oRangeFijo = oFormatNumers(oWindowRoot, values=(15,17,20,27), width=5)
oRangeFijo.grid(column=1, row=2)

oLabelValueDefecto = oFormat.Label(oWindowRoot, text="Valor por Defecto :")
oLabelValueDefecto.grid(column=0, row=3)
valorDefecto = oFormat.IntVar()
valorDefecto.set(22)
oLabelValueDefecto = oFormatNumers(oWindowRoot, from_=5, to=87, width=3, textvariable=valorDefecto)
oLabelValueDefecto.grid(column=1, row=3)


oWindowRoot.mainloop()      # Evento que llama al inicio de nuestro programa
