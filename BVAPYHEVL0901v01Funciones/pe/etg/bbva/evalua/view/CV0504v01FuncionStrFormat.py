#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	27Mar2018
# Periódo           :   27Mar/2018
# Objetivo			:	Funciones str
# Fecha Edición		:
# Descripción		:   Función str.format
#                       Las llaves y los caracteres dentro de las mismas (lla-
# mados campos de formato) son reemplazados con los objetos pasados en el
# método.
# Se puede usar !a (aplica apply(), !s (aplica str()) y !r (aplica repr()) para
# convertir el valor antes que se formatee.
#==============================================================================
import math

def imprimirFormat():
    sMensaje = 'Somos los {} quienes decimos "{}"!'
    sMensaje.format('caballeros', 'No')
    print(sMensaje)
    print("2. Las llaves y los caracteres dentro de las mismas (llamados campos de formato) son reemplazados con los objetos pasados en el método")
    print('{0} y {1}'.format('carne', 'huevos'))
    print('{1} y {0}'.format('carne', 'huevos'))
    print("3. Si se usan argumentos nombrados en el método str.format() sus valores seran referidos usando el nombre del argumento")
    print('Esta {comida} es {adjetivo}.'.format(comida='carne', adjetivo='espantosa'))
    print("4. Se pueden combinar arbitrariamente argumentos posicionales y nombrados")
    print('La historia de {0}, {1} y {otro}.'.format('Microsoft', 'IBM', otro='Compaq'))

def imprimirPrefijo():
    contents = 'anguilas'
    print('Mi aerodeslizador está lleno de {}.'.format(contents))
    print('My hovercraft is full of {!r}.'.format(contents))

def formatoPI():
    print("1.- Un : y especificador de formato opcionales pueden ir luego del nombre del campo. Esto aumenta")
    print("el control sobre cómo el valor es formateado")
    print("2.- El valor de PI es aproximadamente {0:.3f}.".format(math.pi))
    aLista = {'Reina': 71967, 'Esteban': 52002, 'Illari': 82014}
    for nombre, telefono in aLista.items():
        print('{0:10} ==> {1:10d}'.format(nombre,telefono))
    print("\n")
    print("3.- Si tienes una cadena de formateo larga que no queres separar, sería bueno que puedas hacer referencia")
    print("a variables a ser formateadas por el nombre en vez de la posición")
    print('Reina:{0[Reina]:d}; Esteban:{0[Esteban]:d}'.format(aLista))
    print("\n")
    print("4.- También se podría efectuar pasando la tabla con argumentos nombrados con la notación **")
    print('Reina:{Reina:d}; Esteban:{Esteban:d}'.format(**aLista))

imprimirFormat()
print("=" *80)
imprimirPrefijo()
print("=" *80)
formatoPI()