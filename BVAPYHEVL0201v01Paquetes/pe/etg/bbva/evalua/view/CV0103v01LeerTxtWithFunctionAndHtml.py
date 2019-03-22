#==============================================================================
# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	EVL (Evaluación de Python 3.6.1.)
# Módulo			        :   Generacion HTML
# Fecha	Creación	    :	22Mar2019
# Objetivo			        :   Codificación con funciones la generación de código HTML
#                                       Para ejecutar en Windows :
#   > python <path><archivo.py> > archivo.html
#   Ej. python CV0103v01LeerTxtWithFunctionAndHtml.py > LeerTexto.html
#
# Declarar python en las variables de entorno si este no se encuentra habilitado
#==============================================================================

def inicio(cadena=''):
    "Inicia el documento HTML."
    return '''<html>
        <head>
        <title>''' + cadena + '''</title>
        </head>
        <body>\n'''


def encabezado(nivel='1', string=''):
        "Regresa string con encabezado o título HTML, default es H1."
        return '<h' + nivel + '>' + string + '</h' + nivel + '>'


def horizontal():
    "Línea horizontal en el documento HTML."
    return '<hr />'


def destino(clave, texto):
    "Regresa texto como destino."
    return '<a name="' + clave + '>' + texto + '</a>'


def liga(url, texto):
    "Liga o hipervínculo a url con texto."
    return '<a href="' + url + '">' + texto + '</a>'


def parrafo(texto):
    "Genera un párrafo con texto."
    return '<p>' + texto + '</p>\n'


def saltolinea():
    "Genera un salto de línea."
    return '<br>\n'


def tabla(arreglo):
    """Muestra arreglo en una tabla HTML.

    Las celdas pueden ser cualquier tipo, se convierten a cadena siempre."""

    temp = '<table border="1">\n'

    for renglon in arreglo:
        temp = temp + '<tr>'
        for celda in renglon:
            temp = temp + '<td>' + str(celda) + '</td>\n'
        temp = temp + '</tr>\n'
    return temp + '</table>\n'


def final():
    "Fin del documento HTML."
    return '''</body>
    </html>'''

def hacertabla( ren=10, col=10, operador='+'):
    """Construye y regresa un arreglo ren x col.

    Cada celda toma un valor que depende de x,y y el
    valor de operador.  El arreglo es de 10 x 10 si
    no se suministran los valores de ren y col."""

    array = []
    for ren in range(1, ren+1):
        array.append( [] )
        for col in range( 1, col+1):
            dato = calcula(ren, col, operador)
            array[-1].append( dato )
    return array


def calcula( a, b, operador):
    "Regresa una cadena tipo 'a operador b = resultado'."
    if operador == '+':
        return str(a) + ' + ' + str(b) + ' = ' + str( a+b)
    elif operador == '*':
        return str(a) + ' * ' + str(b) + ' = ' + str( a*b)


def leedatos( nombrearchivo ):
    "Abre un archivo, lee y regresa un arreglo."
    f = open( nombrearchivo )
    renglones = f.readlines()
    arreglo = map(lambda x: x.split(','), renglones)
    return arreglo


def principal():
    print(inicio( 'Mi primera página dinamica'))
    print(encabezado( 'Página generada con Python'))
    print(parrafo( 'Algunos ejemplos de las rutinas para generar HTML'))
    print(tabla(leedatos( 'CV0103v01CapitalCiudadMexico.txt' ) ))
    print(encabezado('Tabla de sumas' ))
    print(tabla(hacertabla()))
    print(encabezado('Tabla de multiplicación'))
    print(parrafo('Esta tabla usa la misma función con otro contenido'))
    print(tabla(hacertabla(12, 9, '*'), ))
    print(final())


principal()