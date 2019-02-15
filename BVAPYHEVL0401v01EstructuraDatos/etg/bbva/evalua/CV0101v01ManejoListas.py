#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	28Feb2018
# Periódo           :   28Feb al 01Mar/2018
# Objetivo			:	Estructura de listas
# Fecha Edición		:
# Descripción		:   Estructa de listas

#==============================================================================

aFrutas = ['orange','apple', 'banana', 'pera', 'kiwi', 'manzana', 'banana']
aAnimal = ['perro', 'gato', 'león', 'elefante', 'leopardo', 'tigre benagala']

print("1. count.- Cuenta la cantidad de un elemento de la lista")
print(aFrutas.count('banana'))

print("2. index.- Indica la ubicación de algún elemento")
print(aFrutas.index('orange'))
print(aFrutas.index('banana'))

print("3. append.- Agrega un item al final de la lista")
print(aFrutas.append('papaya'))
print(aFrutas)

print("4. extends.- Extiende la lista agrengandole todos los items a la lista dada")
print(aFrutas.extend(aAnimal))
print(aFrutas)

print("5. insert.- Inserta un item en una posición dada. El primer argumento es el índice del item del cual se insertará")
print(aFrutas.insert(5, "mango"))
print(aAnimal.insert(22,"hipopotamo"))
print(aFrutas)
print(aAnimal)

print("6. remove.- Quita el primer item de la lista cuyo valor sea x. Es un error si no existe tal item")
print(aFrutas.remove("orange"))
print(aAnimal.remove("hipopotamo"))
print(aFrutas)
print(aAnimal)

print("7. pop.- Quita el item en la posición dada de la lista y lo devuelve")
print(aFrutas.pop(5))
print(aAnimal.pop())  # El último de la lista
print(aFrutas)
print(aAnimal)

print("8. clear.- Quita todos los elementos de la lista")
print(aFrutas.clear())
print(aAnimal.clear())
print(aFrutas)
print(aAnimal)

print("9. sort.- Ordena los items de la lista in situ")
aOrdenaFruta = aFrutas.sort()
aOrdenaAnimal = aAnimal.sort(key=None, reverse=False)
print(aOrdenaFruta)
print(aOrdenaAnimal)

print("10. reverse.- Ordena los items de la lista in situ")
aOrdenaFruta = aFrutas.reverse()
aOrdenaAnimal = aAnimal.reverse()
print(aOrdenaFruta)
print(aOrdenaAnimal)

print("11. copy.- Devuelve una copia superficial")
copyaFruta = aFrutas.copy()
copyaAnimal = aAnimal[:]
print(aFrutas.copy())
print(aAnimal[:])
print(copyaFruta)
print(copyaAnimal)