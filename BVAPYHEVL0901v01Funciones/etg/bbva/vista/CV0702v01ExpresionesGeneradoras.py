#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	09Abr2018
# Periódo           :   09Abr/2018
# Objetivo			:	Expresiones Generadores
# Fecha Edición		:
# Descripción		:
#==============================================================================
from math import pi, sin

def sumaCuadrados():
    resultado = sum(i*i for i in range(22))
    print("Suma cuadrados = ", resultado)

def productoEscalar():
    xvec = [10, 20, 30]
    yvec = [7, 5, 3]
    resultado = sum(x*y for x,y in zip(xvec, yvec))
    print("Producto escalar = ", resultado)

def tablaSenos():
    resultado = {x:sin(x*pi/180) for x in range(0, 91)}
    print(resultado)

def principal():
    sumaCuadrados()
    productoEscalar()
    tablaSenos()


principal()