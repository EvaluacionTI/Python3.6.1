#==============================================================================
# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	EVL (Evaluación de Python 3.6.1.)
# Módulo			        :   Reduce
# Fecha	Creación	    :	15Mar2019
# Objetivo			        :	Reduce la lista
# Descripción		    :   La función Reduce reduce los valores de la lista a un solo valor aplicando una
#                                       funcion reductora.
#                                       A partir de la versión 3 se utiliza con el import functools
# La primera vez se aplica al primer y segundo elemento
# La siguiente, se aplicará al valor devuelto por la función junto al tercer elemento y así,
# sucesivamente, reduciendo la lista hasta que quede un sólo elemento.
#
# La función Reduce también cuenta con un tercer argumento que es el valor inicial o default.
# Por ejemplo si quisiéramos sumarle 10 a la suma de los elementos de la lista items, solo
# tendríamos que agregar el tercer argumento.
#
# Formato                  :    reduce(funcion reductora, lista)
#==============================================================================
import functools

items=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]


def suma_valores(p_eje_x, p_eje_y):
    return p_eje_x + p_eje_y


def multiplica_valores(p_eje_x, p_eje_y):
    return p_eje_x * p_eje_y


def principal():
    print(":-"*80)
    print("1. Reduce la lista por suma de valores ")
    print("Lista de valores : ", items)
    suma_lista = functools.reduce(suma_valores, items)
    print("Acumulado de la lista :", suma_lista)
    print(":-" * 80)

    print("2. Multiplica la lista de valores ")
    print("Lista de valores : ", items)
    multiplica_lista = functools.reduce(multiplica_valores, items)
    print("Acumulado de la lista :", multiplica_lista)
    print(":-" * 80)

    print("3. Suma la lista de valores con lambda")
    print("Lista de valores : ", items)
    suma_lambda_lista = functools.reduce(lambda x, y: x + y, items)
    print("Acumulado de la lista :", suma_lambda_lista)
    print(":-" * 80)

    print("4. Suma la lista de valores con lambda y un tercer elemento a reduce")
    print("Lista de valores : ", items)
    suma_lambda_lista = functools.reduce(lambda x, y: x + y, items, 5)
    print("Acumulado de la lista :", suma_lambda_lista)
    print(":-" * 80)

principal()