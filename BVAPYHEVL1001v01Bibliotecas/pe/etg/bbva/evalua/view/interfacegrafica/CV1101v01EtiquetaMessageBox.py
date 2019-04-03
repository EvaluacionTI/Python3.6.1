#==============================================================================
# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	EVL (Evaluación de Python 3.6.1.)
# Módulo			        :   Generacion HTML
# Fecha	Creación	    :	03Abr2019
# Objetivo			        :   Biblioteca Tkinter
#                                  :
# Procedimiento       :   MessageBox
#
# Declaramos una variable llamada oWindowRoot, del tipo Tk().
#
# Además de Tk(), podemos declarar más variables
#
# Mainloop es el encargado de manejar y manipular todos los eventos que ocurran durante el codigo.
#==============================================================================
import tkinter as oFormat
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


# 3. Declarar buton
#3.1 Las funciones se debe declarar antes que los botones
def fncSaveApx():
    oFormatMessage.showinfo("Evaluación", "Proceso grabado en APX")

def fncSaveHost():
    oFormatMessage.showerror("Evaluación", "Proceso grabado en APX")

def fncAsk():
    rpta = oFormatMessage.askquestion("Evaluación", "Desea salir del sistema ?")
    print("Respuesta : ", rpta)

#3.2 Definition of the buttons
oButtonAPX  = oFormat.Button(oWindowRoot, text="Mensaje Informativo", width=40, height=10, command=fncSaveApx)
oButtonAPX.grid(column=0, row=1)

oButtonHost  = oFormat.Button(oWindowRoot, text="Mensaje de Error", width=20, height=5, command=fncSaveHost)
oButtonHost.grid(column=0, row=2)

oButtonQuestion = oFormat.Button(oWindowRoot, text="Menssage Type Question ..!", width=10, command=fncAsk)
oButtonQuestion.grid(column=0, row=3)

oWindowRoot.mainloop()      # Evento que llama al inicio de nuestro programa
