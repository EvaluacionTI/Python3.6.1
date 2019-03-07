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

def primeraExcepcion():
    while True:
        try:
            iNumero = input("Ingrese un número : ")
            break
        except ValueError:
            print("Oops..!, No era válido. Intente nuevamente")

def segundaExcepcion():
    iTope=5
    while (iTope > -2):
        try:
            print("100 / ", iTope, "Resultado = ", 100/iTope)
            iTope = iTope - 1
        except ZeroDivisionError:
            print(iTope)
            break


def principal():
    primeraExcepcion()
    segundaExcepcion()

principal()