#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	16Abr2018
# Periódo           :   16Abr/2018
# Objetivo			:	Import glob
# Fecha Edición		:
# Descripción		:   glob
#                       Provee de una función para hacer lista de archivos a
# partir de busqueda de comodines en directorios.
# #==============================================================================
import glob
print(glob.glob("*.py"))

for name in glob.glob('dir/*'):
    print(name)