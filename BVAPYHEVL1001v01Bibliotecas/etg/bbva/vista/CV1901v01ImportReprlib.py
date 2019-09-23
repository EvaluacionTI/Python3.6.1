#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	24Abr2018
# Periódo           :   24Abr/2018
# Objetivo			:	Import de formatos de salida
# Fecha Edición		:
# Descripción		:
#==============================================================================
# provee una versión repr ajustada para mostrar contenedores grandes o profun-
# damente anidados
import reprlib

print(reprlib.repr(set('arquitecto host')))