#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	20Mar2018
# Periódo           :   20Mar/2018
# Objetivo			:	Manejo de funciones
# Fecha Edición		:
# Descripción		:   Funciones por referencia
#==============================================================================
def cambia(n):
    print("Parametro entrante", n)
    n=3
    print("Asignación", n)

print("1. Definiendo por valor numeros")
a=9
cambia(a)
print("Resultado final = ", a)

print("2. Definiendo por valor cadenas")
a="PAAS"
cambia(a)
print("Resultado final = ", a)