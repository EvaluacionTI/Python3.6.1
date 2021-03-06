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

# Mainloop es el encargado de manejar y manipular todos los eventos que ocurran durante el codigo.
#==============================================================================
import tkinter as oFormat

oWindowRoot = oFormat.Tk()
oWindowRoot.title("Widger Label")
oWindowRoot.config(bg="pink")       # Color de fondo de la ventana
oWindowRoot.geometry("800x600") # Tamaño de la ventana 800 pixel de ancho y 600 de alto

oLabel = oFormat.Label(oWindowRoot, text="Arquitectura HOST / APX ", font=("Arial Bold", 20))
oLabel.grid(column=0, row=0)

oButton = oFormat.Button(oWindowRoot, text="Pulsar Click")
oButton.grid(column=0, row=1)

oWindowRoot.mainloop()      # Evento que llama al inicio de nuestro programa
