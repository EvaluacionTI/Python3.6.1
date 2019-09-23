#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	22Mar2018
# Periódo           :   22Mar/2018
# Objetivo			:	Import sys
# Fecha Edición		:
# Descripción		:   Import types : Define nombres para los tipos que propor
#                       ciona el intérprete.
# Ejempplo: NoneType para el tipo None
#           Inttype para el tipo entero
#           LongType para el tipo entero largo
#           FloatType para el tipo real

#==============================================================================
from types import *

def delete(list, item):
    print(list, item)
    if type(item) is int:
        print("Verdadero")
        del list[item]
    else:
        print("Falso")
        list.remove(item)


aLista = []
aLista.append("PAAS")
aLista.append("HOST")
aLista.append("DISTRIBUIDO")
aLista.append("JAVA")
aLista.append("SPRING")
print(aLista)

# Fuera del rango de la lista, por ello ello el error en eliminar el item
delete(aLista, 5)
print(aLista)