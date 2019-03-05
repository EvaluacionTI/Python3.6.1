#==============================================================================
# Entidad			        :	Entelgy - Banco Continental
# Proyecto			        :	EVL (Evaluación de Python 3.6.5.)
# Módulo			        :
# Fecha	Creación	    :	21Febrary2019
# Objetivo			        :	Flujo Condicional
#
# Fecha Edición		    :
# Descripción		    :   IF / IF ELIF / IF ELIF ELSE
#==============================================================================

iValor = int(input("Ingrese un valor : "))
if (iValor < 0):
    print("Valor negativo %d" %(iValor))
elif (iValor == 0):
    print("Valor cero %d" % (iValor))
elif (iValor > 1):
    print("Valor mayor a cero %d" % (iValor))
else:
    print("Excede el rango de enteros")