#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	06Mar2018
# Periódo           :   06Mar/2018
# Objetivo			:	Comparar Listas for e if
# Fecha Edición		:
# Descripción		:   Comparar las listas
#==============================================================================
comparar = []


def forma_compara01():
    comparar = [(x, y) for x in [1,2,3,4,5] for y in [5, 6, 8] if x!= y]

    print("Forma 01 = ", comparar)


def forma_compara02():
    comparar = []
    for x in [1,2,3,4,5]:
        for y in [5,6,8]:
            if x!=y:
                comparar.append((x,y))
    print("Forma 02 = ", comparar)


forma_compara01()
forma_compara02()
