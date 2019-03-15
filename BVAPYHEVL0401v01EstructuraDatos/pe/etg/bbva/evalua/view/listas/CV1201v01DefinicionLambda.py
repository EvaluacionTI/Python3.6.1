#==============================================================================
# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	EVL (Evaluación de Python 3.6.1.)
# Módulo			        :
# Fecha	Creación	    :	14Mar2019
# Objetivo			        :	Lambda
# Descripción		    :   La función lambda es una forma de crear funciones anónimas, es decir,
#                                      funciones sin nombre. Estas funciones son desechables, es decir, solo se
# necesitan donde se han creado.
# Las funciones lambda
# Formato                  :    lambda argument_list : expression
#==============================================================================

# 1. Es este ejemplo recibe como parametro el valor 2002 y este valor se multiplica cuyo resultado
#      se almacena en la variable resultado
resultado = lambda numero: numero * 5
print("Resultado de lambda *5 : ", resultado(2002))

# 2. Con una función lambada comprobar si un numero es impar
resultado_impar = lambda valor: valor % 2 != 0
print("El valor es impar : ", resultado_impar(6))

# 3. Función lambda que devuelve la suma de sus dos argumentos:
print("Función lambda que devuelve la suma de sus dos argumentos:")
funcion_x_y = lambda x, y: x + y
print("Resultado suma de dos valores : ", funcion_x_y(1, 5))

# 4. Revertir la cadena ej. Host y pasara a tsoH
revertir = lambda cadena : cadena[::-1]
print(revertir("Arquitectura"))
print(revertir("Host"))

