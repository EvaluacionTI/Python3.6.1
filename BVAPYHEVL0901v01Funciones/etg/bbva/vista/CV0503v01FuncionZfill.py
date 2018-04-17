#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	26Mar2018
# Periódo           :   26Mar/2018
# Objetivo			:	Funciones zfill
# Fecha Edición		:
# Descripción		:   Funciones zfill, rellena una cadena numérica a la
#                       izquierda con números
#==============================================================================
def cerosIzquierda():
    numero2 = '2'
    numero3 = '3.176'
    numero4 = "87.74739"
    print(numero2.zfill(2))
    print(numero3.zfill(7))
    print(numero4.zfill(17))

cerosIzquierda()
print("=" *80)
