#==============================================================================
# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	EVL (Evaluación de Python 3.6.1.)
# Módulo			        :
# Fecha	Creación	    :	13Mar2019
# Objetivo			        :	Manejo de Lambda
# Descripción		    :   Una función lambda es una pequeña función anónima
#                                      Una función lambda puede tomar cualquier número de argumentos,
# pero solo puede tener una expresión
# El poder de lambda se muestra mejor cuando se usan como una función anónima dentro de otra
# función
#
#           Format          : lambda arguments : expresion
#==============================================================================


def estructura_lambda(argumento):
    return lambda expresion : expresion + argumento


def principal():
    print ("1. Estructura básica")
    iresultado = lambda expresion: expresion + 5
    print("Resultado 1 : ", iresultado(1))

    iresultado = lambda eje_x, eje_y: eje_x * eje_y
    print("Resultado 2 : ", iresultado(5, 1))

    iresultado = lambda eje_x, eje_y, eje_z: eje_x  + eje_y + eje_z
    print("Resultado 3 : ", iresultado(5, 1, 2002))

    print("2. Estructura definida en funciones")
    iresultado_lambda = estructura_lambda(1)
    print("Resultado de lambda : ", iresultado_lambda(5))


principal()