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

tab_styles = {}
tab_styles['Canales'] = {"background": [("selected", "green")],
                                                         "foreground": [("selected", "#ffffff")]
                                       }
tab_styles["Terminales"] = {"background": [("selected", "blue")],
                                 "foreground": [("selected", "#ffffff")]
                                 }
tab_styles["Transacciones"] = {"background": [("selected", "orange")],
                                    "foreground": [("selected", "#ffffff")]
                                    }

settings = {"TNotebook.Tab": {"configure": {"padding": [25, 10],
                                                                                "background": "yellow"
                                                                              }
                                                        }
                      }


def fnc_select_nb_tab(event):
    global tab_styles
    global oStyle
    tab_control = event.widget
    tab = tab_control.tab(tab_control.select(), "text")
    st = tab_styles[tab]
    oStyle.map('TNotebook.Tab', **st)


# 2. Declarar Etiquetas
class CVPestanas(oFormatNoteBook.Frame):

    def __init__(self, powindow_root):
        super().__init__(powindow_root)
        powindow_root.title(".....[ Módulo de Evaluación ].....")

        # Contorno general de la ventana
        powindow_root.configure(width=800, height=600)
        self.place(width=800, height=600)

        # 1. Crear el panel de pestanas
        self.tab_control = oFormatNoteBook.Notebook(self, width=200, height=300)

        self.frame_green = oFormat.Frame(self.tab_control, background="green")
        self.frame_blue = oFormat.Frame(self.tab_control, background="blue")
        self.frame_orange = oFormat.Frame(self.tab_control, background="orange")

        # 2. Crear el contenido de cada una de las pestañas
        self.web_label = oFormat.Label(self.tab_control, text="www.recursospython.com")
        self.forum_label = oFormat.Label(self.tab_control, text="foro.recursospython.com")
        self.trans_label = oFormat.Label(self.tab_control, text="foro.recursospython.com")

        # 3. Añadir al panel los nombres de las pestañas
        self.tab_control.add(self.frame_green, text="Canales")
        self.tab_control.add(self.frame_blue, text="Terminales")
        self.tab_control.add(self.frame_orange, text="Transacciones")

        self.tab_control.pack(padx=10, pady=20)
        self.pack(expand=1, fill="both")
        self.tab_control.bind("<<NotebookTabChanged>>", fnc_select_nb_tab)


def principal():
    oWindowRoot = oFormat.Tk()
    oStyle = oFormatNoteBook.Style()
    oStyle.theme_create("estiloConImagen", parent="alt", settings=settings)
    oStyle.theme_use("estiloConImagen")
    oAppCombo = CVPestanas(oWindowRoot)
    oAppCombo.mainloop()      # Evento que llama al inicio de nuestro programa


principal()
