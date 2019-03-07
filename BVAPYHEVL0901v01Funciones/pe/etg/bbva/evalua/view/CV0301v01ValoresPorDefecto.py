#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	20Mar2018
# Periódo           :   20Mar/2018
# Objetivo			:	Manejo de funciones
# Fecha Edición		:
# Descripción		:   Funciones por referencia
#==============================================================================
def convierte(pNumero, pBase=10):
    if (pNumero == 0):
        return [0]
    elif(pNumero < 0):
        pNumero = -pNumero
        bFlagNegativo = True
    else:
        bFlagNegativo = False

    aListaR = []
    while (pNumero > 0 ):
        aListaR.append(pNumero % pBase)
        pNumero = pNumero / pBase
    if bFlagNegativo:
        aListaR.append('-')

    aListaR.reverse()

    return aListaR


print(convierte(123))
print(convierte(123,8))