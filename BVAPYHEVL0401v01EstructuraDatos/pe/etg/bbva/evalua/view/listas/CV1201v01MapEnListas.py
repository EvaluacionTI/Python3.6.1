#==============================================================================
# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	EVL (Evaluación de Python 3.6.1.)
# Módulo			        :   Mapear
# Fecha	Creación	    :	13Mar2019
# Objetivo			        :	Mapear una lista
# Descripción		    :
#==============================================================================

items=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
acuadrado_sin_map=[]
acuadrado_con_map=[]

def cuadrado_sin_map():
    for i in items:
        acuadrado_sin_map.append(i**2)


def cuadrado_con_map():
    return lambda valor: valor ** 2


def principal():
    print("Lista de datos original :", items)
    cuadrado_sin_map()
    print("Sin cuadrado de map :", acuadrado_sin_map)

    alcuadrado_lambda = map(cuadrado_con_map(), items)
    acuadrado_con_map = list(alcuadrado_lambda)
    print("Con cuadrado de map :", acuadrado_con_map)


principal()