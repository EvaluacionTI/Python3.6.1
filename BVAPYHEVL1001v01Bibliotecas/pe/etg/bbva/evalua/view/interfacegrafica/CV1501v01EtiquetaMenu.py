#==============================================================================
# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	EVL (Evaluación de Python 3.6.1.)
# Módulo			        :   Generacion HTML
# Fecha	Creación	    :	05Abr2019
# Objetivo			        :   Biblioteca Tkinter
#                                  :
# Procedimiento       :   Menu
#
#
#==============================================================================
import tkinter as oFormat
from tkinter import Menu as oFormatMenu

# 1. Declarar la ventana padre
oWindowRoot = oFormat.Tk()

oWindowRoot.title(".....[ Módulo de Evaluación ].....")
oWindowRoot.config(bg="pink")       # Color de fondo de la ventana
oWindowRoot.geometry("800x600") # Tamaño de la ventana 800 pixel de ancho y 600 de alto

# 2. Declarar Etiquetas
# 2.1 Título de la Ventana
oLabel = oFormat.Label(oWindowRoot, text="Arquitectura APX / HOST ", font=("Arial Bold", 20), bg="green", fg="blue")
oLabel.grid(column=0, row=0)


# 3. Declarar Menu
# 3.1. Etiqueta
oLabelMenu = oFormatMenu(oWindowRoot)
oLabelMenu.add_command(label="Transacciones")
oLabelMenu.add_command(label="Consultas")
oLabelMenu.add_command(label="Informes")
oLabelMenu.add_command(label="Estadísticas")
oLabelMenu.add_command(label="Procesos")
oLabelMenu.add_command(label="Mantenimiento")
oLabelMenu.add_command(label="Salir")

oWindowRoot.config(menu=oLabelMenu)
oWindowRoot.mainloop()      # Evento que llama al inicio de nuestro programa
