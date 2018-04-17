#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	22Mar2018
# Periódo           :   22Mar/2018
# Objetivo			:	Import sys
# Fecha Edición		:
# Descripción		:   Import sys : Da acceso a las variables del intérprete
#                       y las funciones que interactúan con él
# import types - Define nombre para los tipos de objetos del intérprete
# import string - Operaciones sobre cadenas
# import re - Expresiones regulares
# import math - funciones matemáticas

#==============================================================================
import sys
import math


print(" stdin = ", sys.stdin)
print(" stdout = ", sys.stdout)
print(" stderr = ", sys.stderr)
print(" path = ", sys.path)

print("dir(), lista de nombres definidos = ", dir())
print("dir(sys) = ", dir(sys))
print("dir(math) = ", dir(math))
for i in sys.argv:
    print(i)

print(" exit = ", sys.exit())