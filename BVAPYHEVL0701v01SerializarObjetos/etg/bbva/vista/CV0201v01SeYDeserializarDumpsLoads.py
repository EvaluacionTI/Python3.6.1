#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	08Mar2018
# Periódo           :   08Mar/2018
# Objetivo			:	Serializar
# Fecha Edición		:
# Descripción		:   Serializar y deserializar un objeto con dump
#                       Existen distintos tipos de serializacion, accesibles
# a través de la librería estandar: marshal, shelve y pickle.
#  dumps y loads trabajan directamente con el objeto serializado
#==============================================================================
from pickle import dumps, loads

aLista = [True, 100, "Arquitectura Host"]
print("Lista Original = ", aLista)
serializarPickled = dumps(aLista)
print("Serializar pickle = ", serializarPickled)

deserializarUnpickled = loads(serializarPickled)
print("Deserializar = ", deserializarUnpickled)