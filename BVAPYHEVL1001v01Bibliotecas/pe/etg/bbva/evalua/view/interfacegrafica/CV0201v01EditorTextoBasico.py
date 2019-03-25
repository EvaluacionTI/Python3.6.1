#==============================================================================
# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	EVL (Evaluación de Python 3.6.1.)
# Módulo			        :   Generacion HTML
# Fecha	Creación	    :	25Mar2019
# Objetivo			        :   Biblioteca Tkinter
#                                  :   Editor de texto
# Procedimiento       :
# 1. Crear una instancia de uno o más elementos para insertar en esta ventana raíz.
# 2. Los elementos pueden ser widgets Label, Canvas, Frame, y otros.
# 3. Enlazar funciones o métodos de la ventana raíz o alguno de los widgets a uno o más eventos del usuario
# 4. Los eventos son los movimientos y acciones del ratón y teclas presionadas en el teclado.
# 5. Mostrar cada elemento con el método pack() que tiene definido.
# 6. Agregar información a los elementos, como puede ser texto al editor o a una etiqueta
# 7. Llamar el método mainloop() de nuestra ventana raíz, para que se active la atención a los eventos.
# 8. Para terminar la aplicación se llama al método quit() de la ventana raíz.
#==============================================================================
import tkinter as oForm
import sys

raiz = oForm.Tk()
editor = oForm.Text(raiz)
editor.pack()

fileOpen = open(sys.argv[0])
editor.insert('1.0', fileOpen.read())

raiz.mainloop()
