#==============================================================================
# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	EVL (Evaluación de Python 3.6.1.)
# Módulo			        :   Generacion HTML
# Fecha	Creación	    :	04Abr2019
# Objetivo			        :   Biblioteca Tkinter
#                                  :
# Procedimiento       :   ProgressBar
#
# Declaramos una variable llamada oWindowRoot, del tipo Tk().
#
# Además de Tk(), podemos declarar más variables
#
# Mainloop es el encargado de manejar y manipular todos los eventos que ocurran durante el codigo.
#==============================================================================
import tkinter as oFormat
from tkinter.ttk import  Progressbar as oFormatProgress

# 1. Declarar la ventana padre
oWindowRoot = oFormat.Tk()

oWindowRoot.title(".....[ Módulo de Evaluación ].....")
oWindowRoot.config(bg="pink")       # Color de fondo de la ventana
oWindowRoot.geometry("800x600") # Tamaño de la ventana 800 pixel de ancho y 600 de alto

# 2. Declarar Etiquetas
# 2.1 Título de la Ventana
oLabel = oFormat.Label(oWindowRoot, text="Arquitectura APX / HOST ", font=("Arial Bold", 20), bg="green", fg="blue")
oLabel.grid(column=0, row=0)


# 3. Declarar ProgressBar

# 3.4 Asignar color al progress bar
oLabelProgressBarColor = oFormat.Label(oWindowRoot, text="Establecer color al Progress Bar :")
oLabelProgressBarColor.grid(column=0, row=3)

# 3.4.1. Establecer un estilo
oStyle = oFormat.ttk.Style()
oStyle.theme_use('default')
oStyle.configure("black.Horizontal.TProgressbar", background='blue')

# El valor 297 es la longitud de la barra
oProgressBarColor = oFormatProgress(oWindowRoot, length=297, style='black.Horizontal.TProgressbar')
oProgressBarColor['value'] = 69
oProgressBarColor.grid(column=1, row=3)


oWindowRoot.mainloop()      # Evento que llama al inicio de nuestro programa
