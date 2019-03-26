#==============================================================================
# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	EVL (Evaluación de Python 3.6.1.)
# Módulo			        :   Generacion HTML
# Fecha	Creación	    :	26Mar2019
# Objetivo			        :   Biblioteca Tkinter
#                                  :
# Procedimiento       :    Color de fondo de la ventana
#
# Declaramos una variable llamada oWindowRoot, del tipo Tk().
#
# Además de Tk(), podemos declarar más variables
#
# Toplevel: Crea una nueva ventana
# Frame: Coloca los páneles para ordenar los elementos
# Canvas: Para dibujar y graficar funciones etc..
# Button: Para colocar un botón
# Label: Coloca un texto
# Message: Coloca un texto
# Entry: Coloca una entrada de texto de una linea
# Text: Coloca una entrada de texto de varias lineas
# Listbox: Coloca una lista con elementos clickeables
# Menú: Coloca un menú que puede contener cascadas y elementos clickeables
#
# Existe toda una mecánica para agregar elementos a una ventana. Además de todo esto se pueden colocar imágenes y otras
#  cosas. Por el momento estos controles básicos son los que aprenderemos a utilizar:

# Mainloop es el encargado de manejar y manipular todos los eventos que ocurran durante el codigo.
#==============================================================================
import tkinter as oFormat

oWindowRoot = oFormat.Tk()     # Ventana principal
oWindowRoot.title("Arquitectura Host")      # Titulo de la ventana
oWindowRoot.config(bg="darkblue")       # Color de fondo de la ventana
oWindowRoot.geometry("500x500")     # Tamaño de la ventana
oWindowRoot.mainloop()      # Evento que llama al inicio de nuestro programa
