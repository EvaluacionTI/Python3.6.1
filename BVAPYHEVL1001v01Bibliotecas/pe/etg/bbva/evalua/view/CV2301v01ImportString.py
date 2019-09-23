#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	24Abr2018
# Periódo           :   24Abr/2018
# Objetivo			:	Import spring
# Fecha Edición		:
# Descripción		:   Incluye una clase versátil Template con una sintaxis
#                       simplificada apta para ser editada por usuarios finales
#
#==============================================================================
from string import Template

t = Template('${village}folk send $$10 to $cause')
resultado = t.substitute(village='Nothingam', cause='the ditch fund')
print(t)
print(resultado)