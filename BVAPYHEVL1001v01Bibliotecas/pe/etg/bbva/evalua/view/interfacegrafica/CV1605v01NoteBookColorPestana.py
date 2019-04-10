#==============================================================================
# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	EVL (Evaluación de Python 3.6.1.)
# Módulo			        :   Generacion HTML
# Fecha	Creación	    :	10Abr2019
# Objetivo			        :   Biblioteca Tkinter
#                                  :
# Procedimiento       :   Notebook o pestañas
#
#                                   Establecer el color del encabezado de las pestañas
# color. Para el padding: [5,1], 5 Ancho y 1  Alto
#fdd57e = Color del fondo del titulo de la pestaña para este caso es rojo
#==============================================================================
import tkinter
from tkinter import ttk


oWindowRoot = tkinter.Tk()
oWindowRoot.title(".....[ Módulo de Evaluación ].....")
oWindowRoot.config(bg="pink")       # Color de fondo de la ventana
oWindowRoot.geometry("800x600") # Tamaño de la ventana 800 pixel de ancho y 600 de alto

style = ttk.Style()
settings = {"TNotebook.Tab":
                {"configure": {"padding": [5, 1],
                                        "background": "#fdd57e"
                                        },
                 "map": {"background": [("selected", "#C70039"),
                                                     ("active", "#fc9292")],
                                "foreground": [("selected", "#ffffff"),
                                                     ("active", "#000000")]
                              }
                 }
           }

style.theme_create("mi_estilo", parent="alt", settings=settings)
style.theme_use("mi_estilo")

nb = ttk.Notebook(width=200, height=200)
nb.pressed_index = None
f1 = tkinter.Frame(nb)
f2 = tkinter.Frame(nb)
f3 = tkinter.Frame(nb)
nb.add(f1, text='Pestaña 1')
nb.add(f2, text='Pestaña 2')
nb.add(f3, text='Pestaña 3')
nb.pack(expand=1, fill='both')
oWindowRoot.mainloop()