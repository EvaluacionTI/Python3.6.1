#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	06Mar2018
# Periódo           :   06Mar/2018
# Objetivo			:	Variables globales
# Fecha Edición		:
# Descripción		:   Usar identificador global para referirse a variables
#                       globales
#==============================================================================
NOMBRE = "ILLARI"


def show_global():
    nombre = NOMBRE
    print("Variable global es %s", nombre)


def set_global():
    global NOMBRE
    nombre = "MERY"
    print("Variable global es %s", nombre)

show_global()
set_global()
show_global()
