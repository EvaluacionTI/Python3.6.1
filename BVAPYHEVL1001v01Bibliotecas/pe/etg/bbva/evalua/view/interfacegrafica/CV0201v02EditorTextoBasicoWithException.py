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

def quit(event):
    "Termina la aplicación"
    raiz.quit()

def save(event):
    "Salva el texto del editor"
    abrir_file = open(nombre_archivo, "w")
    abrir_file.write(editor.get('1.0 '))
    abrir_file.close()
    print("archivo ", nombre_archivo, " salvado")


raiz = oForm.Tk()
editor = oForm.Text(raiz)
editor.pack()
editor.bind('<Control-Q>', quit)
#editor.bind('<Control-S', save)

if len(sys.argv)>1:
    nombre_archivo = sys.argv[1]
    try:
        file_abrir = open(nombre_archivo)
        editor.insert("1.0", file_abrir.read())
    except:
        print("Es archivo nuevo : ", nombre_archivo)
else:
    print("Falta proporcionar nombre de archivo")
    sys.exit()


raiz.mainloop()
