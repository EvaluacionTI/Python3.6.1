#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	15Mar2018
# Periódo           :   15Mar/2018
# Objetivo			:	Bucle - For
# Fecha Edición		:
# Descripción		:   Mostrar por pantalla los números multiplos de 7 entre
#                       1 y 1000. Utilizar range e if si son necesarios.
#                       Después haz lo mismo empleando un range con tres
#                       parametros
#==============================================================================

import time
from datetime import datetime

def multiploSeven():
    dFechaHoraInicio = time.strftime("%c")
    dFechaHoraInicial = datetime.now()
    print("=" *80)
    ## Muestra fecha y hora actual a partir de la variable
    print("Fecha y hora de inicio : %s" % dFechaHoraInicio)

    print("Los saltos del rango son de 1 en 1")
    aListaMultiplo = []
    for indice in range(1, 1001):
        contador = 1
        resto = indice % 7

        if resto == 0:
            aListaMultiplo.append(indice)

    print(aListaMultiplo)
    dFechaHoraTermino = time.strftime("%c")
    dFechaHoraFinal = datetime.now()
    print("Fecha y hora final : %s " % dFechaHoraTermino)
    print("Tiempo proceso : ", (dFechaHoraFinal - dFechaHoraInicial))


def multiploSevenIncrementoOf5():
    dFechaHoraInicio = time.strftime("%c")
    dFechaHoraInicial = datetime.now()

    print("=" * 80)
    ## Muestra fecha y hora actual a partir de la variable
    print("Fecha y hora de inicio : %s" % dFechaHoraInicio)

    print("Los saltos del rango son de 5 en 5")
    aListaMultiplo = []
    for indice in range(1, 1001, 5):
        contador = 1
        resto = indice % 7

        if resto == 0:
            aListaMultiplo.append(indice)

    print(aListaMultiplo)
    dFechaHoraTermino = time.strftime("%c")
    dFechaHoraFinal = datetime.now()
    print("Fecha y hora final : %s " % dFechaHoraTermino)
    print("Tiempo proceso : ", (dFechaHoraFinal - dFechaHoraInicial))


def principal():
    multiploSeven()
    multiploSevenIncrementoOf5()

principal()