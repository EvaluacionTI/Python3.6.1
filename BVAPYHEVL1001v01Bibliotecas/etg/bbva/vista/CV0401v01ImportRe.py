#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	27Mar2018
# Periódo           :   27Mar/2018
# Objetivo			:	Import re
# Fecha Edición		:
# Descripción		:   Define elementos para escribir expresiones regulares

#==============================================================================
import re

id = re.Scanner
idCompile = re.compile("[a-zA-Z][a-zA-Z0-9]*")
print("re.Scanner = ", id)
print("re.compile = ", idCompile)


print(re.findall(r'\bt[a-z]*', 'tres felices tigres comen trigo'))
print(re.sub(r'(\b[a-z]+) \1', r'\1', 'gato en el el sombrero'))