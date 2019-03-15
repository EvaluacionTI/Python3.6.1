#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	02Mar2018
# Periódo           :   02Mar/2018
# Objetivo			:	Lectura de un archivo
# Fecha Edición		:
# Descripción		:   Open with w: Escribir en un fichero. Este borra su
#                       contenido previo si existiera
#==============================================================================

print("Escribir un archivo")
file = open("CV0201v01HostWrite.txt", "w")
print(file)
print(file.buffer)
file.write("LE Libreta Electoral")
file.close()


