#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	23Abr2018
# Periódo           :   23Abr/2018
# Objetivo			:	Multiplos de 7
# Fecha Edición		:
# Descripción		:
#==============================================================================
def multiplo7(n):
    if n%7==0:
        return True
    else:
        return False

for i in range(1,1001):
    if multiplo7(i)==1:
        print(i)