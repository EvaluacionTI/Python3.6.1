#==============================================================================
# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	EVL (Evaluación de Python 3.6.1.)
# Módulo			        :   Generacion HTML
# Fecha	Creación	    :	27Mar2019
# Objetivo			        :   Biblioteca Tkinter
#                                  :
# Procedimiento       :    Buscar predios
#

# Además de Tk(), podemos declarar más variables
#
# Mainloop es el encargado de manejar y manipular todos los eventos que ocurran durante el codigo.
#==============================================================================
import tkinter as oFormat


def ventana_padre(): # 1. Declarar la ventana padre
    oWindowRoot = oFormat.Tk()
    oWindowRoot.title("Módulo de Predios")

    oWindowRoot.config(bg="pink")       # Color de fondo de la ventana
    oWindowRoot.geometry("800x600") # Tamaño de la ventana 800 pixel de ancho y 600 de alto
    return oWindowRoot

# 2. Declarar Etiquetas
#oLabelDireccion = oFormat.Label(oWindowRoot, text="Arquitectura HOST / APX ", font=("Arial Bold", 20), bg="green", fg="blue")
#oLabelDireccion.grid(column=0, row=0)

#oLabelMostrarTexto = oFormat.Label(oWindowRoot, text="", font=("Verdana", 17), bg="yellow", fg="brown")
#oLabelMostrarTexto.grid(column=1, row=1)

# 3. Declarar la entrada de datos
#oTexto = oFormat.Entry(oWindowRoot, width=10)
#oTexto.grid(column=2, row=3)
#oTexto.focus()

#oTextoDisabled = oFormat.Entry(oWindowRoot, width=20, state='disabled')
#oTextoDisabled.grid(column=2, row=4)


# 4. Declarar Botones
#def clicked():
 #   oCapturaEntry = "Ud ha escrito : " + oTexto.get()
 #   oLabelMostrarTexto.configure(text=oCapturaEntry)


#oButton = oFormat.Button(oWindowRoot, text="Pulsar Click", bg="orange", fg="white", command=clicked)
#oButton.grid(column=0, row=5)

def principal():
    oventana = ventana_padre()
    oventana.mainloop()      # Evento que llama al inicio de nuestro programa


principal()


