#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	24Abr2018
# Periódo           :   24Abr/2018
# Objetivo			:	Import pprint
# Fecha Edición		:
# Descripción		:   Ofrece un control más sofisticado de la forma en que se
#                       imprimen tanto los objetos predefinidos como los objetos
# definidos por el usuario, de manera que sean legibles por el interprete.
#==============================================================================
import pprint

t = [[[['negro', 'turquesa'], 'blanco', ['verde', 'rojo']], [['magenta',
'amarillo'], 'azul']]]

pprint.pprint(t, width=30)