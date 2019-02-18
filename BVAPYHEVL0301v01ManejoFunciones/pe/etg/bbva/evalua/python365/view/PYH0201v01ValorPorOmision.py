#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	23Feb2018
# Objetivo			:	Argumento de funciones con valores por omisión
# Fecha Edición		:
# Descripción		: a) El valor por omision es evaluado una sola vez
#==============================================================================
i = 5
print("1. Valor asignado i = ", i)
def valorPorOmision(arg=i):
    print("2. Valor por Omisión i = ", arg)

print("3. Asignando un nuevo valor")
i=22
print("3.1 Valor i = ", i)

print("4. Llamando a la función para i = ", i)
print("4.1 Resultado sin parámetro = ", valorPorOmision())
print("4.1 Resultado con parámetro = ", valorPorOmision(22))