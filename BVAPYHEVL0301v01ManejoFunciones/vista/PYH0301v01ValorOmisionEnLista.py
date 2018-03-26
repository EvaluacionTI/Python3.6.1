# =============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	23Feb2018
# Objetivo			:	Manejo de funciones
# Fecha Edición		:
# Descripción		: a) Valor por omisión en una lista
# =============================================================================


def valorOmisionLista(a, Lista=[]):
    Lista.append(a)
    return Lista

print("Agregando a la lista con valores por Omision")
print("Valor 5", valorOmisionLista(5))
print("Valor 22", valorOmisionLista(22))
print("Valor 7", valorOmisionLista(7))


def valorOmisionListaNoCompartido(a, Lista=[]):
    if Lista is None:
        Lista=[]
    Lista.append(a)
    return Lista

print("Agregando a la lista sin compartir el valor por omision")
print("Valor 5", valorOmisionListaNoCompartido(5))
print("Valor 22", valorOmisionListaNoCompartido(22))
print("Valor 7", valorOmisionListaNoCompartido(7))
