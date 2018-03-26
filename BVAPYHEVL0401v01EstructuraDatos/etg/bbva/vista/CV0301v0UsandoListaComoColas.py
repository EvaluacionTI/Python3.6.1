#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	01Mar2018
# Periódo           :   01Mar/2018
# Objetivo			:	Estructura de listas
# Fecha Edición		:
# Descripción		:   Usando listas como colas, donde el primer elemento
#                       añadido es el primer elemento retirado, es decir
#       "primero en entrar y primero en salir"
#       Para implementar una cola se utiliza collections.deque
#==============================================================================
from collections import deque

oColaFrutas = deque(['orange','apple', 'banana', 'pera', 'kiwi', 'manzana', 'banana'])

print("Cola original")
print(oColaFrutas)

print("Adicionando a la cola original")
oColaFrutas.append("mango")
oColaFrutas.append("melocoton")
print(oColaFrutas)

print("primero en entrar y primero en salir")
print(oColaFrutas.popleft())
print(oColaFrutas.popleft())
print(oColaFrutas.popleft())
print(oColaFrutas)

