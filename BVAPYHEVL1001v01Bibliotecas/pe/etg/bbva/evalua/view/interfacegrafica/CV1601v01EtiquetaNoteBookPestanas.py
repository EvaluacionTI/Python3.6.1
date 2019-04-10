#==============================================================================
# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	EVL (Evaluación de Python 3.6.1.)
# Módulo			        :   Generacion HTML
# Fecha	Creación	    :	08Abr2019
# Objetivo			        :   Biblioteca Tkinter
#                                  :
# Procedimiento       :   Notebook o pestañas
#
#                                   Definir las pestañas
#==============================================================================
import tkinter as oFormat
from tkinter.ttk import  Notebook as oFormatNoteBook

# 1. Declarar la ventana padre
oWindowRoot = oFormat.Tk()

oWindowRoot.title(".....[ Módulo de Evaluación ].....")
oWindowRoot.config(bg="pink")       # Color de fondo de la ventana
oWindowRoot.geometry("800x600") # Tamaño de la ventana 800 pixel de ancho y 600 de alto

# 2. Declarar Etiquetas
# 2.1 Título de la Ventana
oLabel = oFormat.Label(oWindowRoot, text="Arquitectura APX / HOST ", font=("Arial Bold", 20), bg="green", fg="blue")
oLabel.grid(column=0, row=0)


# 3. Declarar NoteBook o pestañas
labelPestana = oFormat.Label(oWindowRoot, text="Generación de Pestañas : ")
labelPestana.place(x=20, y=40)

# 3.1 Declarar la pestaña
oTab_control = oFormatNoteBook(oWindowRoot)
oTab_control.grid(column=0, row=1)

oLabel_canales  = oFormat.Label(oTab_control, text="Consulta Canales")
oLabel_registro_canales  = oFormat.Label(oTab_control, text="Registro Canales")
oLabel_modificacion_canales  = oFormat.Label(oTab_control, text="Modificacion Canales")

oLabel_terminales  = oFormat.Label(oTab_control, text="Terminales")
oLabel_transacciones = oFormat.Label(oTab_control, text="Transacciones")

oTab_control.add(oLabel_canales, text="Datos de Canales1")
oTab_control.add(oLabel_registro_canales, text="Datos de Canales2")
oTab_control.add(oLabel_modificacion_canales, text="Datos de Canales3")

oTab_control.add(oLabel_terminales, text="Datos de Terminales")
oTab_control.add(oLabel_transacciones, text="Datos de Transacciones")

oWindowRoot.mainloop()      # Evento que llama al inicio de nuestro programa

