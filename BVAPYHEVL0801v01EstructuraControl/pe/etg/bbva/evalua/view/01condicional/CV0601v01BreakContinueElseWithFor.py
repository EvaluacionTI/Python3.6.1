#==============================================================================
# Entidad			        :	Entelgy - Banco Continental
# Proyecto			        :	EVL (Evaluación de Python 3.6.5.)
# Módulo			        :
# Fecha	Creación	    :	21Febrary2019
# Objetivo			        :	Flujo Condicional
#                                      BREAK CONTINUE ELSE
# Fecha Edición		    :
# Descripción		    :   Validar un número primo
#
#==============================================================================
for n in range(2, 17):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'es igual a', x, '*', n/x)
            break
        else:
            # sigue el tarea sin encontrar un factor
            print(n, 'es un numero primo')