#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	28Feb2018
# Objetivo			:	Funciones de cadena
# Fecha Edición		:
# Descripción		:   Funciones de cadena

#==============================================================================

sCadena = "Arquitectura Host"

print("1.upper.- Convertir a mayúsculas")
print(sCadena.upper())

print("2.lower.- Convertir a minusculas")
print(sCadena.lower())

print("3.capitalize.- Devuelve una copia de la cadena con la primera letra en mayúscula")
sCadena = "illari"
print(sCadena.capitalize())

print("4.center.- Devuelve una copia de la cadena centrada y con longitud n")
# n = Indica los espaciones que hay a la izquierda
sCadena = "illari"
print(sCadena.center(40))
