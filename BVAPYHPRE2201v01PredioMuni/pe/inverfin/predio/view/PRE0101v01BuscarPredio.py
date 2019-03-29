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

oVentanaPrincipal = oFormat.Tk()


def ventana_padre(poVentanaPrincipal): # 1. Declarar la ventana padre
    poVentanaPrincipal.title(".....[ Módulo de Predios ].....")

    poVentanaPrincipal.config(bg="pink")       # Color de fondo de la ventana
    poVentanaPrincipal.geometry("800x600") # Tamaño de la ventana 800 pixel de ancho y 600 de alto
    return poVentanaPrincipal

def declarar_etiquetas(poWindowRoot):  # 2. Declarar Etiquetas
    tituloRegistro = "Búsqueda de Predios por Dirección"

    oLabelTitulo = oFormat.Label(poWindowRoot, text=tituloRegistro, anchor="center", width=80, font=("Arial Bold", 16), bg="green", fg="blue")
    oLabelTitulo.grid(column=0, row=0)

    oLabelDireccion = oFormat.Label(poWindowRoot, text="Dirección de búsqueda : ", anchor="w", font=("Verdana", 12))
    oLabelDireccion.grid(column=0, row=1)

# 3. Declarar la entrada de datos
    oTextoDireccion = oFormat.Entry(poWindowRoot, width=40, font=("Verdana", 12))
    oTextoDireccion.grid(column=0, row=2)
    oTextoDireccion.focus()

    oButton = oFormat.Button(poWindowRoot, text="Procesar", bg="orange", fg="white", command=procesarClicled)
    oButton.grid(column=0, row=3)


# 4. Declarar Botones
def procesarClicled():
   #oCapturaEntry = "Ud ha escrito : " + oTextoDireccion.get()
   print("Ud. esta procesando")
#   oLabelMostrarTexto.configure(text=oCapturaEntry)




def principal():
    oventana = ventana_padre(oVentanaPrincipal)
    declarar_etiquetas(oventana)
    oventana.mainloop()      # Evento que llama al inicio de nuestro programa


principal()


