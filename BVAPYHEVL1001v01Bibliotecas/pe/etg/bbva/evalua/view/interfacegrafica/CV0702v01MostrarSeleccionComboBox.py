#==============================================================================
# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	EVL (Evaluación de Python 3.6.1.)
# Módulo			        :   Generacion HTML
# Fecha	Creación	    :	28Mar2019
# Objetivo			        :   Biblioteca Tkinter
#                                  :
# Procedimiento       :   Combo Box
#
# Declaramos una variable llamada oWindowRoot, del tipo Tk().
#
# Además de Tk(), podemos declarar más variables
#
# Mainloop es el encargado de manejar y manipular todos los eventos que ocurran durante el codigo.
#==============================================================================
import tkinter as oFormat
from tkinter.ttk import Combobox as oFormatCombo

# 1. Declarar la ventana padre
oWindowRoot = oFormat.Tk()

oWindowRoot.title(".....[ Módulo de Evaluación ].....")
oWindowRoot.config(bg="pink")       # Color de fondo de la ventana
oWindowRoot.geometry("800x600") # Tamaño de la ventana 800 pixel de ancho y 600 de alto

# 2. Declarar Etiquetas
oLabel = oFormat.Label(oWindowRoot, text="Arquitectura APX / HOST ", font=("Arial Bold", 20), bg="green", fg="blue")
oLabel.grid(column=0, row=0)

oLabelCombo = oFormat.Label(oWindowRoot, text="Lista de canal :  ", font=("Verdana", 12))
oLabelCombo.grid(column=0, row=1)

oLabelMostrarValorCombo = oFormat.Label(oWindowRoot, text="Mostrar elemento seleccionado", font=("Verdana", 12), bg="brown", fg="white")
oLabelMostrarValorCombo.grid(column=0, row=2)


def fnc_selected_changed(self):
    print(self)
    elementoSeleccionado = oComboCanal.get()
    indiceElementoSeleccionado = oComboCanal.current()
    print(elementoSeleccionado)
    print(indiceElementoSeleccionado)
    oLabelMostrarValorCombo.configure(text=elementoSeleccionado)

# 3. Declarar el combo
oComboCanal = oFormatCombo(oWindowRoot)
# 3.1 Elementos del combo
oComboCanal['values'] = ('MN', 'MG', 'PH', 'SF', 'XA', 15, 17, 20, 27)
# 3.2 Los valores de la posición inician en 0
#oComboCanal.current(3)  # set the selected item
# 3.3 Mostrar el combo
oComboCanal.grid(column=1, row=1)
oComboCanal.focus()
oComboCanal.bind("<<ComboboxSelected>>", fnc_selected_changed)




oWindowRoot.mainloop()      # Evento que llama al inicio de nuestro programa
