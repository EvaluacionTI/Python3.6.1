#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	27Feb2018
# Objetivo			:	Expresiones Lambda
# Fecha Edición		:
# Descripción		:   Las funciones lambda puedes ser usadas en cualquier
#                       lugar donde sea requerido un objeto de tipo función.
#==============================================================================
def incrementador(pValor):
    return lambda iResultado : iResultado + pValor

total = incrementador(100)
print(total(0))
print(total(1))
print(total(2))