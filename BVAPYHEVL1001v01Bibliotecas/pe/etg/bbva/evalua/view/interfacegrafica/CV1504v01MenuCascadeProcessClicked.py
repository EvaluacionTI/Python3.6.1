#==============================================================================
# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	EVL (Evaluación de Python 3.6.1.)
# Módulo			        :   Generacion HTML
# Fecha	Creación	    :	05Abr2019
# Objetivo			        :   Biblioteca Tkinter
#                                  :
# Procedimiento       :   Menu Cascade
#
#
#==============================================================================
import tkinter as oFormat
from tkinter import Menu as oFormatMenu
import tkinter.messagebox as oFormatMessage

# 1. Declarar la ventana padre
oWindowRoot = oFormat.Tk()

oWindowRoot.title(".....[ Módulo de Evaluación ].....")
oWindowRoot.config(bg="pink")       # Color de fondo de la ventana
oWindowRoot.geometry("800x600") # Tamaño de la ventana 800 pixel de ancho y 600 de alto

# 2. Declarar Etiquetas
# 2.1 Título de la Ventana
oLabel = oFormat.Label(oWindowRoot, text="Arquitectura APX / HOST ", font=("Arial Bold", 20), bg="green", fg="blue")
oLabel.grid(column=0, row=0)


def fnc_cargar_informacion():
    oFormatMessage.showinfo("Evaluación", "Se ha iniciado el proceso de Carga")


def fnc_generar_pdf_hr():
    oFormatMessage.showinfo("Evaluación", "Generando PDF HR")


def fnc_generar_pdf_hp():
    oFormatMessage.showinfo("Evaluación", "Generando PDF HP")

# 3. Declarar Menu
# 3.1. Etiqueta del Menu Barra
oLabelMenu = oFormatMenu(oWindowRoot)
oLabelMenu.add_command(label="Transacciones")
oLabelMenu.add_command(label="Consultas")
oLabelMenu.add_command(label="Informes")
oLabelMenu.add_command(label="Estadísticas")

# 3.2 Etiqueta del Menu Cascade
oLabelMenuItemProcesos = oFormatMenu(oLabelMenu, tearoff=0)
oLabelMenuItemProcesos.add_command(label="Cargar Información de Predios", command=fnc_cargar_informacion)
oLabelMenuItemProcesos.add_command(label="Generar archivos PDF de HR", command=fnc_generar_pdf_hr)
oLabelMenuItemProcesos.add_command(label="Generar archivos PDF de HP", command=fnc_generar_pdf_hp)
oLabelMenuItemProcesos.add_command(label="Extraer la última foto del predio")
oLabelMenuItemProcesos.add_separator()
oLabelMenuItemProcesos.add_command(label="Transferir información de predios a Celular")
oLabelMenu.add_cascade(label="Procesos", menu=oLabelMenuItemProcesos)

oLabelMenu.add_command(label="Mantenimiento")
oLabelMenu.add_command(label="Salir")

oWindowRoot.config(menu=oLabelMenu)
oWindowRoot.mainloop()      # Evento que llama al inicio de nuestro programa
