#==============================================================================
# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	EVL (Evaluación de Python 3.6.1.)
# Módulo			        :   Generacion HTML
# Fecha	Creación	    :	01Abr2019
# Objetivo			        :   Class
#                                  :
# Procedimiento       :
#
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


class CCBuffer:
    """
        Clase para generar objetos que almacenan código HTML que después será escrito a un archivo
    """

    def __init__(self):
        "Constructor, crea el atributo definido"
        self.texto = ''

    def add(self, ptexto):
        self.texto = self.texto + ptexto

    def pop(self):
        "Regresa el texto del buffer y borra el buffer"
        aux_texto = self.texto
        self.texto = ""
        return aux_texto

    def inicio(self, titulo):
        "Inicia el documento HTML."
        self.add(inicio(titulo))

    def encabezado(self, nivel, string):
        "Regresa string con encabezado o título HTML, default es H1."
        self.add(encabezado(nivel, string))

    def horizontal(self):
        "Línea horizontal en el documento HTML."
        self.add(horizontal())

    def destino(self, clave, texto):
        "Regresa texto como destino."
        self.add(destino(clave, texto))

    def liga(self, url, texto):
        "Liga o hipervínculo a url con texto."
        self.add(liga(url, texto))

    def parrafo(self, texto):
        "Genera un párrafo con texto."
        self.add(parrafo(texto))

    def saltolinea(self):
        "Genera un salto de línea."
        self.add(saltolinea())

    def tabla(self, arreglo):
        "Inserta arreglo en una tabla HTML."
        self.add(tabla(arreglo))

    def final(self):
        "Fin del documento HTML."
        self.add(final())






