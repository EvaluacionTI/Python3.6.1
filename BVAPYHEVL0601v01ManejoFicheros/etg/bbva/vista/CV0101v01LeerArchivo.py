#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	02Mar2018
# Periódo           :   02Mar/2018
# Objetivo			:	Lectura de un archivo
# Fecha Edición		:
# Descripción		:   Open : Crea un objeto tipo fichero
#==============================================================================

print("Lectura de un archivo")
file = open("host.txt")
print(file)
print(file.buffer)
for linea in file.readline():
    print("linea ", linea)

file.close()

