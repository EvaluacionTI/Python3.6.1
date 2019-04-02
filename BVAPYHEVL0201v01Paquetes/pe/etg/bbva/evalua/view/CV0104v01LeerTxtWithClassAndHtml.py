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
import BVAPYHEVL0201v01Paquetes.pe.etg.bbva.evalua.controller.CC0201v01ClassBufferHtml as oHtml

# 1. Crear dos instancias de la clase buffer:

pagina1 = oHtml.CCBuffer()
pagina1.add("Muestra datos")
print("Objeto : ", pagina1)
pagina1.add("Arquitectyra ")
print("Objeto : ", pagina1.texto)

pagina2 = oHtml.CCBuffer()

# Llenar cara buffer:

pagina1.inicio( 'Página 1' )
pagina1.encabezado( '2', 'Esta es página 1')
pagina1.liga( 'pag2.html', 'Ir a página 2' )
pagina1.final()

#pagina2.inicio( 'Página 2' )
#pagina2.encabezado( '2', 'Esta es Página 2')
#pagina2.liga( 'pag1.html', 'Ir a página 1' )
#pagina2.final()

# Vaciar cada buffer a un archivo:

fp = open('CV0104v01GenerarPaginaHtml.html', 'w')
fp.write(pagina1.pop())
#fp = open('pag2.html', 'w')
#fp.write(pagina2.pop())