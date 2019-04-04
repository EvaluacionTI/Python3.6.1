#==============================================================================
# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	EVL (Evaluación de Python 3.6.1.)
# Módulo			        :   Generacion HTML
# Fecha	Creación	    :	03Abr2019
# Objetivo			        :   Biblioteca Tkinter
#                                  :
# Procedimiento       :   ScrolledText
#
# Declaramos una variable llamada oWindowRoot, del tipo Tk().
#
# Además de Tk(), podemos declarar más variables
#
# Mainloop es el encargado de manejar y manipular todos los eventos que ocurran durante el codigo.
#==============================================================================
import tkinter as oFormat
from tkinter.scrolledtext import ScrolledText as oFormatTextArea

# 1. Declarar la ventana padre
oWindowRoot = oFormat.Tk()

oWindowRoot.title(".....[ Módulo de Evaluación ].....")
oWindowRoot.config(bg="pink")       # Color de fondo de la ventana
oWindowRoot.geometry("800x600") # Tamaño de la ventana 800 pixel de ancho y 600 de alto

# 2. Declarar Etiquetas
# 2.1 Título de la Ventana
oLabel = oFormat.Label(oWindowRoot, text="Arquitectura APX / HOST ", font=("Arial Bold", 20), bg="green", fg="blue")
oLabel.grid(column=0, row=0)

# 3. Declarar el control ScrolledText
oLabelTextArea = oFormat.Label(oWindowRoot, text="Descripción incidencia :")
oLabelTextArea.grid(column=0,row=1)
oTextArea = oFormatTextArea(oWindowRoot, width=40, height=10)
oTextArea.grid(column=1, row=1)
oTextArea.focus()

oLabelTextAreaIniciarDatos = oFormat.Label(oWindowRoot, text="Iniciar datos : ")
oLabelTextAreaIniciarDatos.grid(column=0, row=2)
#oTextAreaIniciar = oFormatTextArea.insert(oFormat.INSERT, "New core banking Ether", "ds")
oTextAreaIniciar = oFormatTextArea(oWindowRoot, width=20, height=5)
oTextAreaIniciar.grid(column=1, row=2)


oWindowRoot.mainloop()      # Evento que llama al inicio de nuestro programa
