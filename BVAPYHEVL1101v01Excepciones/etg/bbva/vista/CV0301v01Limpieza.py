#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	03Abr2018
# Periódo           :   03Abr/2018
# Objetivo			:	Limpieza
# Fecha Edición		:
# Descripción		:
#==============================================================================
import sys

# El problema con este código es que deja abierto por un periodo de tiempo
# indeterminado luego de que esta parte termine de ejecutarse
def limpiezaEstandar():
    try:
        for linea in open('miarchivo.txt'):
            print(linea, end="")
    except OSError as ex:
        print("Error OS : {0}".format(ex))
    except ValueError:
        print("No se puede convertir el dato a numero")
    except:
        print("Error inesperado", sys.exc_info()[0])


# With permite que los objetos como archivos sean usados de una forma que
# asegure que siempre se los libera rápido y en forma correcta
def limpiezaWith():
    try:
        with open("miarchivo.txt") as oFile:
            for linea in oFile:
                print(linea, end="")
    except FileNotFoundError as ex:
        print("Archivo no existe : ", ex)
    finally:
        print("Ejecutando la clausula finally")


def principal():
    limpiezaEstandar()
    limpiezaWith()


principal()