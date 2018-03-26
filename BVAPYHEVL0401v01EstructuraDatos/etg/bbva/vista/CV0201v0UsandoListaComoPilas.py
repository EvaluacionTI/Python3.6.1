#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	01Mar2018
# Periódo           :   01Mar/2018
# Objetivo			:	Estructura de listas
# Fecha Edición		:
# Descripción		:   Usando listas como pilas. Los métodos de la lista
#                       hacen que resulte muy fácil usar una lista como una
#       pila, donde el último elemento añadido es el primer elemento retirado,
#       es decir "último en entrar, primero en salir".

#==============================================================================

aFrutas = ['orange','apple', 'banana', 'pera', 'kiwi', 'manzana', 'banana']

print("Lista original")
print(aFrutas)

print("Adicionando a la lista original")
aFrutas.append("mango")
aFrutas.append("melocoton")
print(aFrutas)

print("Eliminando de la lista")
print(aFrutas)
aFrutas.pop()   # El último
print(aFrutas)
aFrutas.pop(5)
print(aFrutas)

