#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	07Mar2018
# Periódo           :   07Mar/2018
# Objetivo			:	Convertir lista de la forma A en B
# Fecha Edición		:
# Descripción		:   a=[1, [2, [3, 4]], 5] en [1,[2,[3,4], [6,7]], 5]
#==============================================================================
aListaFormaA = [1, [2, [3, 4]], 5]
aListaFormaB = [1,[2,[3,4], [6,7]], 5]
print("1. Convertir la lista =", aListaFormaA)
print("   en forma la lista  =", aListaFormaB)

print("Proceso de Conversion")
aListaConversion = aListaFormaA
print(aListaConversion)
aListaConversion[1] = [2,[3,4], [6,7]]
print("Resultado final = ", aListaConversion)
aListaConversion[1][0] = 2, [3,4]
print("Observar con parentesis = ", aListaConversion)
aListaConversion[1][0] = [2, [3,4]]
print("Observar el cambio", aListaConversion)