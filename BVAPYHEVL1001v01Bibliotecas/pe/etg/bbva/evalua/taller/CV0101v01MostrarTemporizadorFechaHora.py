#==============================================================================
# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	EVL (Evaluación de Python 3.6.1.)
# Módulo			        :   Generacion HTML
# Fecha	Creación	    :	28Mar2019
# Objetivo			        :   Biblioteca Tkinter
#                                  :
# Procedimiento       :   Mostrar temporizador para la hora y fecha del sistema
#
# 1. Importar las clases tk y time.
# 2. Crear un funcion para obtener el resultado de la hora y fecha
# 3. Crear una clase para el manejo de la aplicación en la ventana
#==============================================================================

import tkinter as tk
import time

def current_iso8601():
    """Get current date and time in ISO8601"""
    # https://en.wikipedia.org/wiki/ISO_8601
    # https://xkcd.com/1179/
    return time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())

class Application(tk.Frame):
    def __init__(self, master=None):
     tk.Frame.__init__(self, master)
     self.pack()
     self.createWidgets()

    def createWidgets(self):
     self.now = tk.StringVar()
     self.time = tk.Label(self, font=('Helvetica', 24))
     self.time.pack(side="top")
     self.time["textvariable"] = self.now

     self.QUIT = tk.Button(self, text="QUIT", fg="red", command=root.destroy)
     self.QUIT.pack(side="bottom")

     # initial time display
     self.onUpdate()

    def onUpdate(self):
     # update displayed time
     self.now.set(current_iso8601())
     # schedule timer to call myself after 1 second
     self.after(1000, self.onUpdate)


root = tk.Tk()
app = Application(master=root)
root.mainloop()