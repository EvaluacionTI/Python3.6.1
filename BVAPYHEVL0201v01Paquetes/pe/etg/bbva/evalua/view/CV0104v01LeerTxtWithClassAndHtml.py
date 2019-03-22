#==============================================================================
# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	EVL (Evaluación de Python 3.6.1.)
# Módulo			        :   Generacion HTML
# Fecha	Creación	    :	22Mar2019
# Objetivo			        :   Codificación con funciones la generación de código HTML
#                                       Para ejecutar en Windows :
#   > python <path><archivo.py> > archivo.html
#   Ej. python CV0104v01LeerTxtWithClassAndHtml.py > LeerTextoClass.html
#
# Declarar python en las variables de entorno si este no se encuentra habilitado
# La clase buffer crea un atributo text en cada instancia que es el texto HTML que se va formando. El método add() se usa para agregar texto a la instancia, mientras que el método pop() es para regresar y vaciar el atributo de texto, como cuando lo vamos a escribir a un archivo.
#==============================================================================
import BVAPYHEVL0201v01Paquetes .pe.etg.bbva.evalua.view.CC0104v01LeerTxtWithClassAndHtml as html

# Crear dos instancias de la clase buffer:

pagina1 = html.buffer()
pagina2 = html.buffer()

# Llenar cara buffer:

pagina1.inicio( 'Página 1' )
pagina1.encabezado( '2', 'Esta es página 1')
pagina1.liga( 'pag2.html', 'Ir a página 2' )
pagina1.final()

pagina2.inicio( 'Página 2' )
pagina2.encabezado( '2', 'Esta es Página 2')
pagina2.liga( 'pag1.html', 'Ir a página 1' )
pagina2.final()

# Vaciar cada buffer a un archivo:

fp = open('pag1.html', 'w')
fp.write(pagina1.pop())
fp = open('pag2.html', 'w')
fp.write(pagina2.pop())