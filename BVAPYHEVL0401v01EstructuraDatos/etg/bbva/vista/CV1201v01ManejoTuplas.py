#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	12Mar2018
# Periódo           :
# Objetivo			:	Estructura de tuplas
# Fecha Edición		:
# Descripción		:   Una tupla consiste de un numero de valores separados
#                       por comas.
# Son secuencias inmutables de objetos, no pueden modificarse ello permite que
# sea más eficiente su tratamiento
# Las salidas de las tuplas siempre se encierran entre parentesis
#==============================================================================

aValores = 12345, 8373, 'perro', 'gato', 'león', 'elefante', 'leopardo', 'tigre benagala'

print("1. Tuplas")
print(aValores)

print("2. Posición de la tupla")
print("Posición 5", aValores[4])

print("3. Anidar tuplas ")
tAnidada = aValores, "celular", "audifono", "cargador"
print("Anidado = ", tAnidada)

print("4. Inmutable ")
# tAnidada[2] = 998877
print(tAnidada)

print("5. Las tuplas vacías se construyen mediante un par de parentesis vacío")
tTuplaVacia = ()
print(tTuplaVacia)

print("6. La tupla de un ítem se construye poniendo una coma a continuación del valor")
tTuplaUnItem = "Cuenta Vista",
print(tTuplaUnItem)

print("7. Empaquetado de tuplas")
tEmpaquetado = 152027, 19671969, "tamps"
print(tEmpaquetado)

print("8. Desempaquetado de tuplas")
x, y, z = tEmpaquetado
print(x,y,z)
