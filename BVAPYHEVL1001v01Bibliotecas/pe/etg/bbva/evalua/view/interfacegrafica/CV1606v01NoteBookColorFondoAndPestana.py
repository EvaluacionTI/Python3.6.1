#==============================================================================
# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	EVL (Evaluación de Python 3.6.1.)
# Módulo			        :   Generacion HTML
# Fecha	Creación	    :	10Abr2019
# Objetivo			        :   Biblioteca Tkinter
#                                  :
# Procedimiento       :   Notebook o pestañas
#
#                                   Establecer el color del encabezado y del fondos de las pestañas con el mismo
# color. El padding [25,10] se establece 25 Ancho y 10  Alto
#yellow = Amarillo
#==============================================================================
import tkinter
from tkinter import ttk

oWindowRoot = tkinter.Tk()
oWindowRoot.title(".....[ Módulo de Evaluación ].....")
oWindowRoot.config(bg="pink")       # Color de fondo de la ventana
oWindowRoot.geometry("800x600") # Tamaño de la ventana 800 pixel de ancho y 600 de alto

style = ttk.Style()

settings = {"TNotebook.Tab": {"configure": {"padding": [25, 10],
                                                                            "background": "yellow"
                                                                           }
                                                    }
                  }
style.theme_create("mi_estilo", parent="alt", settings=settings)
style.theme_use("mi_estilo")


def on_tab(event):
    global tab_styles
    global style
    nb = event.widget
    tab = nb.tab(nb.select(), "text")
    st = tab_styles[tab]
    style.map('TNotebook.Tab', **st)


tab_styles = {}
nb = ttk.Notebook(width=200, height=200)
nb.pressed_index = None

f1 = tkinter.Frame(nb, background="red")
f2 = tkinter.Frame(nb, background="green")
f3 = tkinter.Frame(nb, background="blue")

nb.add(f1, text="Rojo")
tab_styles["Rojo"] = {"background": [("selected", "red")],
                      "foreground": [("selected", "#ffffff")]
                     }
nb.add(f2, text="Verde")
tab_styles["Verde"] = {"background": [("selected", "green")],
                      "foreground": [("selected", "#ffffff")]
                     }

nb.add(f3, text="Azul")
tab_styles["Azul"] = {"background": [("selected", "blue")],
                      "foreground": [("selected", "#ffffff")]
                     }

nb.pack(expand=1, fill='both')
nb.bind("<<NotebookTabChanged>>", on_tab)


oWindowRoot.mainloop()