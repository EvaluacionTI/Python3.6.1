#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	07Mar2018
# Objetivo			:	SubSecuencias
# Fecha Edición		:
# Descripción		:   Las cadenas son un tipo especial de subsecuencias.
#                       Todas las secuencias pueden ser troceadas utilizando
# la notación de slices. La secuencia se inicia en la posición 0.
# Cuando hay dos numeros, se devuelve la subsecuencia que comienza en el primero
# y llega hasta el último.
# Los números negativos se consideran posiciones desde el final de la secuencia
# Para saber que se obtiene con
#
#==============================================================================
sCadena = "Holding México"
print("Posición sCadena ", sCadena)
print("Posicion sCadena[3] ", sCadena[3])
print("Posicion sCadena[3:5] ", sCadena[3:5])
print("Posicion sCadena[-3] ", sCadena[-3])
print("Posicion sCadena[-10] ", sCadena[-10])
print("Posicion sCadena[4:-2] ", sCadena[4:-2])
print("Posicion sCadena[10:] ", sCadena[10:])
print("Posicion sCadena[:6] ", sCadena[:6])
