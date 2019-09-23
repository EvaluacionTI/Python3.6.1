#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	20Abr2018
# Periódo           :   20Abr/2018
# Objetivo			:	Import doctest
# Fecha Edición		:
# Descripción		:   Provee una herramienta para revisar un módulo y validar
#                       las pruebas integradas en las cadenas de documentación
# (o docstring) del programa.
# La construcción de las pruebas es sencillo como copiar y pegar una ejecución
# típica junto con sus resultados en los docstrings.
#==============================================================================
import doctest

def promedio(valores):
    """Calcula la media aritmética de una lista de números

    print(promedio([15,17,20,27]))
    """
    return sum(valores)/len(valores)

resultado = promedio([15,17,20,27])
print("Promedio es = ", resultado)

print("La línea de código valida automáticamente las pruebas integradas")
doctest.testmod()
