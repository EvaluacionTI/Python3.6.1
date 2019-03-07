#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	16Abr2018
# Periódo           :   16Abr/2018
# Objetivo			:	Import statistics
# Fecha Edición		:
# Descripción		:   Calcula propiedades de estadística básica(la media,
#                       mediana, varianza, etc). de datos numéricos
#==============================================================================
import statistics

datos = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
print("Datos : ", datos)
print("La media = ", statistics.mean(datos))
print("La mediana = ", statistics.median(datos))
print("La varianza = ", statistics.variance(datos))