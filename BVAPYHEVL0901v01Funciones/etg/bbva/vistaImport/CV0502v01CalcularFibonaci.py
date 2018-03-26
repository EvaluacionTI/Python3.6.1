#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	21Mar2018
# Periódo           :   21Mar/2018
# Objetivo			:	Manejo de import
# Fecha Edición		:
# Descripción		:   Serie de Fibonaci
#==============================================================================
# 1. Esta forma de declarar no incluye el nombre de las funcones definidas en
#    CV0401v01FibonacImport directamente, solo es el espacio de nombres actual

from  BVAPYHEVL0901v01Funciones.etg.bbva.vista.CV0401v01FibonacImport import fibonaci

# 2. Para acceder se debe proceder

fibonaci(10)
# fibonaci1(10), no está importado la función

