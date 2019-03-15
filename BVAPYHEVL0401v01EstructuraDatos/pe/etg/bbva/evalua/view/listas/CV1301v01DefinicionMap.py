#==============================================================================
# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	EVL (Evaluación de Python 3.6.1.)
# Módulo			        :   Mapear
# Fecha	Creación	    :	13Mar2019
# Objetivo			        :	Mapear una lista
# Descripción		    :   Aplica una función sobre todos los elementos y como resultado se devuelve
#                                      un iterable de tipo map
# Formato                  :    map(funcion, lista)
#==============================================================================

items = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
acuadrado_sin_map = []
acuadrado_sin_lambda = []
acuadrado_con_lambda = []
alist_items_con_lambda = []


def cuadrado_sin_map():
    for i in items:
        acuadrado_sin_map.append(i**2)
    return acuadrado_sin_map


def cuadrado_con_map_sin_lambda(pvalor):
    return pvalor**2


def cuadrado_con_map_lambda():
    return lambda valor: valor ** 2


def principal():
    print("Lista de datos original :", items)
    print("Sin cuadrado de map :", cuadrado_sin_map())
    print("-"*80)
    acuadrado_sin_lambda = map(cuadrado_con_map_sin_lambda, items)
    print("Cuadrado sin lambda  :", list(acuadrado_sin_lambda))
    print("-"*80)

    acuadrado_con_lambda = map(cuadrado_con_map_lambda(), items)
    alist_items_con_lambda = list(acuadrado_con_lambda)
    print("Iterable map                    :", acuadrado_con_lambda)
    print("Convertir iterable a list :", alist_items_con_lambda)
    print("-" * 80)

principal()