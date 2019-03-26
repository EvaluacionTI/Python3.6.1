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
oLabel = oFormat.Label(oWindowRoot, text="Arquitectura HOST / APX ", font=("Arial Bold", 20), bg="green", fg="blue")


def mostrar_ventana():

    oWindowRoot.title("Widger Label")
    oWindowRoot.config(bg="pink")       # Color de fondo de la ventana
    oWindowRoot.geometry("800x600") # Tamaño de la ventana 800 pixel de ancho y 600 de alto

def motrar_etiquetas():

    oLabel.grid(column=0, row=0)

    oButton = oFormat.Button(oWindowRoot, text="Pulsar Click", bg="orange", fg="white", command=clicked)
    oButton.grid(column=0, row=1)


def clicked():
    oLabel.configure(text="Ha pulsado click .....!!")


def principal():
    mostrar_ventana()
    motrar_etiquetas()
    oWindowRoot.mainloop()      # Evento que llama al inicio de nuestro programa


principal()