#==============================================================================
# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	EVL - Evaluación
# Módulo			        :   Módulo de Graficos
# Fecha	Creación	    :	24/05/2019
# Objetivo			        :   El estándar es matplotlib, este tiene dos módulos básicos:
#
#  a) pylot.- ofrece una interfaz fácil para crear gráfico fácilmente, automatizando
#                   la creación de figuras y ejes automáticamente cuando hace un gráfico.
#  b) pylab.- combina la funcionalida de pyplot para hacer gráficos con funcionalidad de numpy
#                    para hacer cálculos con arrays usando un único espacio de nombres muy parecido a
#                    Matlab
#
# En general, se recomienda usar pylab cuando se trabaja interactivamente y pyplot cuando se
#                      usan programas.
#
# Descripción            :  Importar el módulo de gráficos bajo la forma from para pylab
#
#       La ventaja de importar de esta manera es que se importará de manera automática los recursos
# gráficos de matplotlib y el módulo numpy.
#
#==============================================================================

from pylab import *
ejeX = range(17)
plot(ejeX)
show()