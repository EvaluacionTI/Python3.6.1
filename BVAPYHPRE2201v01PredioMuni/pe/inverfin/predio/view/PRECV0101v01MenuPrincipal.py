# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	EVL (Evaluación de Python 3.6.1.)
# Módulo			        :   Generacion HTML
# Fecha	Creación	    :	27Mar2019
# Objetivo			        :   Menu principal de predios
#                                  :
# Procedimiento       :   
#

#==============================================================================
import tkinter as oFormat
from tkinter import ttk as oFormatFrame


class CVMenuPrincipal(oFormatFrame.Frame):
    def __init__(self, poWindow_root):
        super().__init__(poWindow_root)
        poWindow_root.title("Módulo de Predios")
        # Contorno general de la ventana
        poWindow_root.configure(width=800, height=600)
        self.place(width=800, height=600)


def principal():
    oWindow_root = oFormat.Tk()
    oApplication = CVMenuPrincipal(oWindow_root)
    oApplication.mainloop()


principal()