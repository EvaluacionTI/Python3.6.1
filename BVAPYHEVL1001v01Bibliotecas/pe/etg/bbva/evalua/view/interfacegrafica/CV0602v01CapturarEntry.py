#==============================================================================
# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	EVL (Evaluación de Python 3.6.1.)
# Módulo			        :   Generacion HTML
# Fecha	Creación	    :	27Mar2019
# Objetivo			        :   Biblioteca Tkinter
#                                  :
# Procedimiento       :    Entreda de Datos
#
# Declaramos una variable llamada oWindowRoot, del tipo Tk().
#
# Además de Tk(), podemos declarar más variables
#
# Mainloop es el encargado de manejar y manipular todos los eventos que ocurran durante el codigo.
#==============================================================================
import tkinter as oFormat

# 1. Declarar la ventana padre
oWindowRoot = oFormat.Tk()
oWindowRoot.title("Widger Label")
oWindowRoot.config(bg="pink")       # Color de fondo de la ventana
oWindowRoot.geometry("800x600") # Tamaño de la ventana 800 pixel de ancho y 600 de alto

# 2. Declarar Etiquetas
oLabel = oFormat.Label(oWindowRoot, text="Arquitectura HOST / APX ", font=("Arial Bold", 20), bg="green", fg="blue")
oLabel.grid(column=0, row=0)

oLabelMostrarTexto = oFormat.Label(oWindowRoot, text="", font=("Verdana", 17), bg="yellow", fg="brown")
oLabelMostrarTexto.grid(column=1, row=1)

# 3. Declarar la entrada de datos
oTexto = oFormat.Entry(oWindowRoot, width=10)
oTexto.grid(column=2, row=3)

# 4. Declarar Botones
def clicked():
    oCapturaEntry = "Ud ha escrito : " + oTexto.get()
    oLabelMostrarTexto.configure(text=oCapturaEntry)


oButton = oFormat.Button(oWindowRoot, text="Pulsar Click", bg="orange", fg="white", command=clicked)
oButton.grid(column=0, row=5)


oWindowRoot.mainloop()      # Evento que llama al inicio de nuestro programa
