#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	27Feb2018
# Objetivo			:	Anotaciones
# Fecha Edición		:
# Descripción		:   Las anotaciones se almacenas en el atributo
#                       __annotations__ de la función como un diccionario y no
#                       tienen efecto en ninguna otra parte de la función.
# Las anotaciones de los parámetros se definen luego de dos puntos después del
# nombre del parámetro, seguido de una expresión que evalúa al valor de la
# anotación.
# Las anotaciones de retorno son definidas por el literal ->, seguidas de una
# expresión, entre la lista de parámetros y los dos puntos que marcan el final
# de la declaración def.
#==============================================================================

def anotacion(host: str, distribuido: str = 'Spring') -> str:
    print("Anotaciones : ", anotacion.__annotations__)
    print("Argumentos  : ", host, distribuido)
    print("")
    return host + distribuido

anotacion("Arquitect with ")