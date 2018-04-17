#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	26Mar2018
# Periódo           :   26Mar/2018
# Objetivo			:	Import String
# Fecha Edición		:
# Descripción		:   Define diversas variables y funciones útiles para
#                       manipular cadenas.

#==============================================================================
import string
sCadena = "     arquitectura Host     "
print("1. Convierte a mayúsculas : ", sCadena.upper())
print("2. Convierte a minúsculas : ", sCadena.lower())
print("3. Letra capital la primera letra : ", sCadena.capitalize())
print("4. Devuelve la lista split : ", sCadena.split())
print("4.1. Devuelve la lista split : ", sCadena.split('r'))
print("4.2. Devuelve la lista split : ", sCadena.split('r'),5)
print("5. Elimina los espacios en blanco : |", sCadena.strip(), "|")