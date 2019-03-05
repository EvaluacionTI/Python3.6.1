#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	12Mar2018
# Periódo           :
# Objetivo			:	Manejo de conjuntos
# Fecha Edición		:
# Descripción		:   Un conjunto es una colección no ordenada y sin elementos
#                       repetidos.
# Los usos básicos de éstos incluyen verificación de pertenencia y eliminación
# de entradas duplicadas.
# Los conjuntos tambien soportan operaciones matemáticas como la unión,
# intersección, diferencia y diferencia simétrica.
# Las llaves o función set() pueden usarse para crear conjuntos.
#==============================================================================

aValores = {12345, 8373, 'perro', 'gato', 'león', 'elefante', 'leopardo', 'tigre benagala'}

print("1. Conjuntos")
print(aValores)
print("2. Inclusión")
print("leopardo" in aValores)
print("yerba" in aValores)

print("3. Operaciones")
a=set("abracadabra")
b=set('alacazam')
print ("3.1. Letras únicas")
print("Para a = ", a)
print("Para b = ", b)

print("3.2. Letras en a y no en b")
print(a-b)

print("3.3. Letras en a o en b")
print(a|b)

print("3.4. Letras en a y en b")
print(a&b)

print("3.5. Letras en a o en b pero no en ambos")
print(a^b)

print("4. Comprensión de conjuntos")
c = {x for x in a if x not in 'abc'}
print(c)


