#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	02Abr2018
# Periódo           :   02Abr/2018
# Objetivo			:	Excepción
# Fecha Edición		:
# Descripción		:   Control de excepciones
#==============================================================================
import sys

def verificarArchivo():
    try:
        f = open('miarchivo.txt')
        s = f.readline()
        i = int(s.strip())

    except OSError as ex:
        print("Error OS : {0}".format(ex))
    except ValueError:
        print("No se puede convertir el dato a numero")
    except:
        print("Error inesperado", sys.exc_info()[0])

def divisionPorCero():
    resultado = 15172027 / 0

def principal():
    verificarArchivo()
    try:
        divisionPorCero()
    except ZeroDivisionError as ex:
        print("Manejando error en tiempo de ejecución : ", ex)

principal()