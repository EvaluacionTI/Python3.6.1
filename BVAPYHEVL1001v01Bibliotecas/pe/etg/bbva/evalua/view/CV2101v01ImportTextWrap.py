#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	24Abr2018
# Periódo           :   24Abr/2018
# Objetivo			:	Import textwarp
# Fecha Edición		:
# Descripción		:   Formatea párrafos de texto para que quepan de cierto
#                       ancho de pantalla
#==============================================================================
import textwrap

doc = """El método wrap() es como fill(), excepto que devuelve
... una lista de strings en lugar de una gran string con saltos de
... línea como separadores."""
print(textwrap.fill(doc, width=40))