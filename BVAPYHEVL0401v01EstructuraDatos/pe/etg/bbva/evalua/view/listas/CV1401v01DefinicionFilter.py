#==============================================================================
# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	EVL (Evaluación de Python 3.6.1.)
# Módulo			        :   Filter
# Fecha	Creación	    :	15Mar2019
# Objetivo			        :	Filter
# Descripción		    :   aplica un filtro a una lista de datos y devuelve un iterador con los elementos
#                                      que superan el filtro.
# Formato                  :   filter(funcion filtradora, lista)
#==============================================================================

items=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]


def numero_par(pvalor):
    return pvalor % 2 == 0


def filtrar_sin_lambda():
    lista_resultado = filter(numero_par, items)
    print("1. Filtrar la listar sin uso de lambda")
    print("Lista de items : ", items)
    print("Evaluación Numero pares sin lambda : ", list(lista_resultado))
    print(".-"*80)


def filtrar_con_lambda():
    lista_resultado = filter(lambda numero: numero % 2 == 0,items)
    print("2. Filtrar la listar con uso de lambda")
    print(" Lista de items : ", items)
    print(" Evaluación Numero pares con lambda : ", list(lista_resultado))
    print("-"*80)


def principal():
    filtrar_sin_lambda()
    filtrar_con_lambda()


principal()