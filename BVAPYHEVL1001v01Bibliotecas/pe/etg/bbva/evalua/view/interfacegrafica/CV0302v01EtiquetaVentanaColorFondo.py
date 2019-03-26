#==============================================================================
# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	EVL (Evaluación de Python 3.6.1.)
# Módulo			        :   Generacion HTML
# Fecha	Creación	    :	26Mar2019
# Objetivo			        :   Biblioteca Tkinter
#                                  :
# Procedimiento       :    Color de fondo de la ventana
# Mainloop es el encargado de manejar y manipular todos los eventos que ocurran durante el codigo.
#==============================================================================
import tkinter as oFormat

oWindowRoot = oFormat.Tk()      # Ventana principal
oWindowRoot.title("Arquitectura Host")      # Titulo de la ventana
oWindowRoot.config(bg="blue")       # Color de fondo de la ventana

oWindowRoot.mainloop()      # Evento que llama al inicio de nuestro programa
