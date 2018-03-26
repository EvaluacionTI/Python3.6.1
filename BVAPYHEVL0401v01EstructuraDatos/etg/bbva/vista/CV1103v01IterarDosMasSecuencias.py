#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	13Mar2018
# Periódo           :   13Mar/2018
# Objetivo			:	Lista de comprensión anidada
# Fecha Edición		:
# Descripción		:
#==============================================================================

aMatriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
aResultado = ['java', 'spring', 'cobol']

print("1. Dos o mas secuencias")
for p, r in zip (aMatriz, aResultado):
    print("Cual es tu {0}? = {1} ".format(p,r))

print("2. Lista reversado, inicia en 1 y de tres en tres")
for i in reversed(range(1,20,3)):
    print(i)

print("3. Ordenado una lista")
aListaOrdenada = ['manzana', 'naranja', 'manzana', 'pera', 'platano', 'granadilla']
for i in sorted(set(aListaOrdenada)):
    print(i)