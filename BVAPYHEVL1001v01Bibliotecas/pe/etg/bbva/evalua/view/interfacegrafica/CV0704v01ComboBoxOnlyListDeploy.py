#==============================================================================
# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	EVL (Evaluación de Python 3.6.1.)
# Módulo			        :   Generacion HTML
# Fecha	Creación	    :	04Abr2019
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
from tkinter import ttk as oFrameMain


# 2. Declarar Etiquetas
#oLabel = oFormat.Label(oWindowRoot, text="Arquitectura APX / HOST ", font=("Arial Bold", 20), bg="green", fg="blue")
#oLabel.grid(column=0, row=0)

class CVComboBox(oFrameMain.Frame):
    def __init__(self, powindow_root):
        super().__init__(powindow_root)
        powindow_root.title(".....[ Módulo de Evaluación ].....")

        # Contorno general de la ventana
        powindow_root.configure(width=800, height=600)
        self.place(width=800, height=600)

        self.labelCombo = oFrameMain.Label(self, text="Lista desplegable y sólo lectura : ")
        self.labelCombo.place(x=10, y=30)

        self.combo = oFrameMain.Combobox(self, state="readonly")
        self.combo.place(x=200, y=30)
        self.combo['values'] = ["APX", "HOST", "COBOL", "JCL", "JAVA", "SPRING"]

        # Obtener el valor del combo
        value = self.combo.get()
        # Obtener el indice del combo
        index = self.combo.current()
        #Establecer el contenido en la lista
        self.combo.set("PYTHON")
        #Obtener todas las opciones de la lista
        values = self.combo['values']


def principal():
    oWindowRoot = oFormat.Tk()
    oAppCombo = CVComboBox(oWindowRoot)
    oAppCombo.mainloop()      # Evento que llama al inicio de nuestro programa


principal()