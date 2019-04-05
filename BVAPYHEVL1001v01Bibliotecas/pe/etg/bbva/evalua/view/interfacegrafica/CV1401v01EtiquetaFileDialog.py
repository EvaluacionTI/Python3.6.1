#==============================================================================
# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	EVL (Evaluación de Python 3.6.1.)
# Módulo			        :   Generacion HTML
# Fecha	Creación	    :	05Abr2019
# Objetivo			        :   Biblioteca Tkinter
#                                  :
# Procedimiento       :   FileDialog
#
# Declaramos una variable llamada oWindowRoot, del tipo Tk().
# Para elegir multipres archivo : files = filedialog.askopenfilenames()
# Para elegir algún filtro : file = filedialog.askopenfilename(filetypes = (("Text files","*.txt"),("all files","*.*")))
# Para solicitar un directorio: dir = filedialog.askdirectory()
#
#==============================================================================
import tkinter as oFormat
from tkinter import filedialog as oFormatFileDialog

# 1. Declarar la ventana padre
oWindowRoot = oFormat.Tk()

oWindowRoot.title(".....[ Módulo de Evaluación ].....")
oWindowRoot.config(bg="pink")       # Color de fondo de la ventana
oWindowRoot.geometry("800x600") # Tamaño de la ventana 800 pixel de ancho y 600 de alto

# 2. Declarar Etiquetas
# 2.1 Título de la Ventana
oLabel = oFormat.Label(oWindowRoot, text="Arquitectura APX / HOST ", font=("Arial Bold", 20), bg="green", fg="blue")
oLabel.grid(column=0, row=0)


# 3. Declarar FileDialog
# 3.1. Etiqueta
oLabelFileDialog = oFormat.Label(oWindowRoot, text="Seleccionar archivo :")
oLabelFileDialog.grid(column=0, row=1)

# 3.2 Declaración
oFileDialog = oFormatFileDialog.askopenfilename()

oLabelPath = oFormat.Label(oWindowRoot, text=oFileDialog)
oLabelPath.grid(column=0, row=2)


oWindowRoot.mainloop()      # Evento que llama al inicio de nuestro programa
