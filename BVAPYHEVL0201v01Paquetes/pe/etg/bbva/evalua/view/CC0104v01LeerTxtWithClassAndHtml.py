#==============================================================================
# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	EVL (Evaluación de Python 3.6.1.)
# Módulo			        :   Generacion HTML
# Fecha	Creación	    :	22Mar2019
# Objetivo			        :   Codificación con funciones la generación de código HTML
#                                       Para ejecutar en Windows :
#   > python <path><archivo.py> > archivo.html
#   Ej. python CC0104v01LeerTxtWithClassAndHtml.py > LeerTextoClass.html
#
# Declarar python en las variables de entorno si este no se encuentra habilitado
# La clase buffer crea un atributo text en cada instancia que es el texto HTML que se va formando. El método add() se usa para agregar texto a la instancia, mientras que el método pop() es para regresar y vaciar el atributo de texto, como cuando lo vamos a escribir a un archivo.
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


class buffer:
    """Clase para generar objetos que almacenan codigo HTML
    que despues sera escrito a algun archivo."""

    def __init__(self):
        "Constructor, crea el atributo de texto."
        self.text = ''

    def add(self, texto):
        "Agrega texto arbitrario al buffer."
        self.text = self.text + texto

    def pop(self):
        "Regresa el texto del buffer, y borra el buffer."
        temp = self.text
        self.text = ''
        return temp

    def inicio(self, titulo):
        "Inicia el documento HTML."
        self.add( inicio( titulo ) )

    def encabezado( self, nivel, string):
        "Regresa string con encabezado o título HTML, default es H1."
        self.add( encabezado( nivel, string ) )

    def horizontal( self ):
        "Línea horizontal en el documento HTML."
        self.add(horizontal())

    def destino( self, clave, texto ):
        "Regresa texto como destino."
        self.add( destino( clave, texto) )

    def liga( self, url, texto):
        "Liga o hipervínculo a url con texto."
        self.add( liga( url, texto) )

    def parrafo( self, texto ):
        "Genera un párrafo con texto."
        self.add( parrafo( texto) )

    def saltolinea( self ):
        "Genera un salto de línea."
        self.add( saltolinea() )

    def tabla( self, arreglo ):
        "Inserta arreglo en una tabla HTML."
        self.add( tabla( arreglo ) )

    def final( self ):
        "Fin del documento HTML."
        self.add( final() )


