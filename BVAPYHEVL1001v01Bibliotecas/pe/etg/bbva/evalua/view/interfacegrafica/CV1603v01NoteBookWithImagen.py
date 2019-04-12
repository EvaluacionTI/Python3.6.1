#==============================================================================
# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	EVL (Evaluación de Python 3.6.1.)
# Módulo			        :   Generacion HTML
# Fecha	Creación	    :	08Abr2019
# Objetivo			        :   Biblioteca Tkinter
#                                  :
# Procedimiento       :   Notebook o pestañas
#
#
#==============================================================================
import tkinter as oFormat
from tkinter import ttk as oFormatNoteBook

# 2. Declarar Etiquetas
#oLabel = oFormat.Label(oWindowRoot, text="Arquitectura APX / HOST ", font=("Arial Bold", 20), bg="green", fg="blue")
#oLabel.grid(column=0, row=0)

class CVPestanas(oFormatNoteBook.Frame):
    def __init__(self, powindow_root):
        super().__init__(powindow_root)
        powindow_root.title(".....[ Módulo de Evaluación ].....")

        # Contorno general de la ventana
        powindow_root.configure(width=800, height=600)
        self.place(width=800, height=600)

        self.labelCombo = oFormat.Label(self, text="Generación de Pestañas : ")
        self.labelCombo.place(x=10, y=30)

        # 1. Crear el panel de pestanas
        self.tab_control = oFormatNoteBook.Notebook(self)

        # 2. Crear el contenido de cada una de las pestañas
        self.web_label = oFormat.Label(self.tab_control, text="www.recursospython.com")
        self.forum_label = oFormat.Label(self.tab_control, text="foro.recursospython.com")

        # 3. Añadir al panel
        self.tab_control.add(self.web_label, text="web ")
        self.tab_control.add(self.forum_label, text="Foro ")

        self.tab_control.pack(padx=10, pady=20)
#        self.pack()


def principal():
    oWindowRoot = oFormat.Tk()
    oAppCombo = CVPestanas(oWindowRoot)
    oAppCombo.mainloop()      # Evento que llama al inicio de nuestro programa


principal()
