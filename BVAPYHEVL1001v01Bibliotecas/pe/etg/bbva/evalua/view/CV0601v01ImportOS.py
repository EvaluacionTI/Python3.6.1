#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	12Abr2018
# Periódo           :   12Abr/2018
# Objetivo			:	Import os
# Fecha Edición		:
# Descripción		:   os
#                       provee de funciones para interactuar con el sistema
# operativo. Asegurar de usar la forma "import os" y no la forma "from os
# import *. Esto evitará que la funcion os.open oculte la función integrada
# open que trabaja bastante diferente
#==============================================================================
import os
print("Directorio de trabajo : ", os.getcwd())
sDirectorioActual = os.getcwd()
sCambioDirectorio = "F://2018//03Tecnologia//16Python3.6.1//04Desarrollo//BVAPYHEVL1001v01Bibliotecas//etg//bbva"
os.chdir(sCambioDirectorio)
print("Cambio directorio: ", sCambioDirectorio)
os.chdir(sDirectorioActual)
print("Directorio de trabajo nuevo: ", os.getcwd())

print("Crear el directorio de trabajo : ")
os.system("mkdir prueba")
print("Crear el directorio de trabajo : ")
os.system("rd prueba")

dir(os)

