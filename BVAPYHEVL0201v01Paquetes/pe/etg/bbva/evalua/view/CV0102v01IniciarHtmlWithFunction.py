#==============================================================================
# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	EVL (Evaluación de Python 3.6.1.)
# Módulo			        :   Generacion HTML
# Fecha	Creación	    :	22Mar2019
# Objetivo			        :   Codificación con funciones la generación de código HTML
#                                       Para ejecutar en Windows :
#   > python <path><archivo.py> > archivo.html
#   Ej. python CV0102v01IniciarHtmlWithFunction.py > IniciarHtml.html
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


def principal():
    print(inicio( 'Página dinamica'))
    print(encabezado( 'Página generada con Python'))
    print(parrafo( 'Tenemos a continuación una tabla:'))
    print(tabla( [ ['r1c1', 'r1c2'],
               ['r2c1', 'r2c2'] ] ))
    print(final())


principal()
