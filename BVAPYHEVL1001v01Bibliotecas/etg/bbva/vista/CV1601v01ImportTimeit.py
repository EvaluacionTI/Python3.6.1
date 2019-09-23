#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	20Abr2018
# Periódo           :   20Abr/2018
# Objetivo			:	Import timeit
# Fecha Edición		:
# Descripción		:   Muestra rápidamente una modesta ventaja de rendimiento
#==============================================================================
from timeit import Timer

oResultado = Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
print(oResultado)

oResultado = Timer('a,b = b,a', 'a=1; b=2').timeit()
print(oResultado)