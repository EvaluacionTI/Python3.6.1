#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	06Mar2018
# Periódo           :   06Mar/2018
# Objetivo			:	Comprensión de Listas
# Fecha Edición		:
# Descripción		:   Manejo de listas
#==============================================================================
cuadrados = []


def forma_cuadrado01():
    for x in range(10):
        cuadrados.append(x**2)

    print("Forma 01 - with for x in range(10) = ", cuadrados)


def forma_cuadrado02():
    cuadrados = list(map(lambda x: x**2, range(10)))
    print("Forma 02 - with list(map(lambda x: x**2, range(10))) = ", cuadrados)


def forma_cuadrado03():
    cuadrados = [x**2 for x in range(10)]
    print("Forma 03 - with x**2 for x in range(10) = ", cuadrados)

forma_cuadrado01()
forma_cuadrado02()
forma_cuadrado03()