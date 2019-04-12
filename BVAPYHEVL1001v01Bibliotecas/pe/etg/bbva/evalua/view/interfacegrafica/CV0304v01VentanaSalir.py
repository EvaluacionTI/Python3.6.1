#==============================================================================
# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	EVL (Evaluación de Python 3.6.1.)
# Módulo			        :   Generacion HTML
# Fecha	Creación	    :	12Abr2019
# Objetivo			        :   Biblioteca Tkinter
#                                  :
# Procedimiento       :   Ventana con un boton Salir
#
# Al presionar el botón la aplicación termina su ejecución.
# Una ventana es el elemento fundamental de una aplicación GUI.
# Es el primer objeto que se crea y sobre éste se colocan el resto de objetos
# llamados widgets (etiquetas, botones, etc.).
#==============================================================================
# 1.0 Las dos líneas siguientes son necesaias para hacer
# compatible el interfaz Tkinter con los programas basados
# en versiones anteriores a la 8.6.6, con las más recientes.

import tkinter as oFormat        # Carga módulo tk (widgets estándar)
from tkinter import ttk             # Carga ttk (para widgets nuevos 8.5+)


# 2.0 Define la ventana principal de la aplicación

oWindowRoot = oFormat.Tk()

# 3.0 Define las dimensiones de la ventana, que se ubicará en el centro de la pantalla.
# Si se omite esta línea la  ventana se adaptará a los widgets que se coloquen en
# ella.

oWindowRoot.geometry('800x600') # anchura x altura

# 4.0 Asigna un color de fondo a la ventana. Si se omite esta línea el fondo será gris

oWindowRoot.configure(bg = 'beige')

# 5.0 Asigna un título a la ventana

oWindowRoot.title('Evaluación de Python')

# 6.0 Define un botón en la parte inferior de la ventana
# que cuando sea presionado hará que termine el programa.
# El primer parámetro indica el nombre de la ventana 'raiz'
# donde se ubicará el botón

ttk.Button(oWindowRoot, text='Salir', command=quit).pack(side=oFormat.BOTTOM)

# 7.0 Después de definir la ventana principal y un widget botón
# la siguiente línea hará que cuando se ejecute el programa
# construya y muestre la ventana, quedando a la espera de
# que alguna persona interactúe con ella.

# Si la persona presiona sobre el botón Cerrar 'X', o bien,
# sobre el botón 'Salir' el programa llegará a su fin.

oWindowRoot.mainloop()