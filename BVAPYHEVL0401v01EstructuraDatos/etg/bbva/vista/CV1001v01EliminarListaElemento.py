#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	07Mar2018
# Periódo           :   07Mar/2018
# Objetivo			:	Eliminar lista o elemento
# Fecha Edición		:
# Descripción		:   a=[1, [2, [3, 4]], 5] en [1,[2,[3,4], [6,7]], 5]
#==============================================================================
aListaFormaA = [1, [2, [3, 4]], 5]
aListaFormaB = [1,[2,[3,4], [6,7]], 5]
print("1. Lista A =", aListaFormaA)
print("1. Lista B =", aListaFormaB)
del aListaFormaA[2]
print("2. Eliminar posición [2] =", aListaFormaA)
del aListaFormaB[1:2]
print("3. Eliminar posición [1:2] =", aListaFormaB)
sVariable = "Eliminar variable completa"
print("4. Variable completa : ", sVariable)
del sVariable
print("5. Variable eliminada : ", sVariable)