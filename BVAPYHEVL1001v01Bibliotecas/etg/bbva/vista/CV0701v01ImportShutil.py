#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	16Abr2018
# Periódo           :   16Abr/2018
# Objetivo			:	Import shutil
# Fecha Edición		:
# Descripción		:   shutil
#                       Para tareas de administracion de archivos y directorios
# el módulo shutil provee de una interfaz de más alto nivel que es más fácil
# de usar
#==============================================================================
import shutil, os
sFileOrigen = "shutilOrigen.txt"
sFileDestino = "shutilDestino.txt"
shutil.copy(sFileOrigen, sFileDestino)

print("Directorio de trabajo : ", os.getcwd())
sDirectorioActual = os.getcwd()
print(sDirectorioActual)

