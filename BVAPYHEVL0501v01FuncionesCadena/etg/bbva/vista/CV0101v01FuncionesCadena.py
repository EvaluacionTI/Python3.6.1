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

print("5.Capitalize.- Devuelve una copia de la cadena con la primera letra en mayúscula")
sCadena = "illari"
print(sCadena.capitalize())

print("6.find(sub,[,desde[,hasta].- Devuelve la posición de la primera posición de sub en la cadena;")
print("si se incluye desde, la búsqueda comienza con esa posición y termina en hasta, si se especifica")
sCadena = "Arquitectura Host"
print(sCadena.find("ec"))
print(sCadena.find("t",10))
print(sCadena.find("e",10,20))

print("7.isalnum.- Devuelve cierto si la cadena no es vacía y sólo contiene letras y dígitos")
sCadena = "2018BancoContinental"
print(sCadena.isalnum())

print("8.isalpha.- Devuelve cierto si la cadena no es vacía y sólo contiene letras")
sCadena = "BancoContinental"
print(sCadena.isalpha())

print("9.isdigit.- Devuelve cierto si la cadena no es vacía y sólo contiene dígitos")
sCadena = "2018"
print(sCadena.isdigit())

print("10.islower.- Devuelve cierto si todas las letras de la cadena son minúsculas")
sCadena = "banco"
print(sCadena.islower())

print("11.isspace.- Devuelve cierto si la cadena no es vacía y todos sus caracteres son espacios")
sCadena = "     "
print(sCadena.isspace())

print("12.isupper.- Devuelve cierto si todas las letras de la cadena son mayúsculas y hay al menos una mayúscula")
sCadena = "CONTINENTAL     "
print(sCadena.isupper())

print("13.lstrip.- Devuelve una copia de la cadena con los blancos iniciales omitidos")
sCadena = "    BANCO CONTINENTAL     "
print("+++", sCadena.lstrip())

print("14.rstrip.- Devuelve una copia de la cadena con los blancos finales omitidos")
sCadena = "    BANCO CONTINENTAL     "
print("+++", sCadena.rstrip(), "++++")

print("15.rstrip.- Devuelve una copia de la cadena con los blancos finales omitidos")
sCadena = "    BANCO CONTINENTAL     "
print("+++", sCadena.strip(), "++++")

print("16.replace.- Devuelve una copia de la cadena donde se han sustituido todas las apariciones de la cadena v por n")
sCadena = "    BANCO CONTINENTAL     "
print("+++", sCadena.replace("O", "eia"), "++++")

print("17.split[s].- Devuelve la lista que contiene las palabras de la cadena. Si se incluye la cadena s, se utiliza como separador")
sCadena = "    BANCO CONTINENTAL - Arquitectura host    "
print(sCadena.split())
