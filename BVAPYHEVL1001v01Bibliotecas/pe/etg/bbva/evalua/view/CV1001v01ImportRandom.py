#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	16Abr2018
# Periódo           :   16Abr/2018
# Objetivo			:	Import random
# Fecha Edición		:
# Descripción		:   random
#                       Provee de herramientas para realizar seleccionar al azar
# #==============================================================================
import random

print(random.choice(['manzana', 'pera', 'banana']))
print(random.sample(range(100), 10))
print(random.random())
print(random.randrange(5))