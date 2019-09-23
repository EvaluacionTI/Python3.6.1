#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	24Abr2018
# Periódo           :   24Abr/2018
# Objetivo			:	Import locale
# Fecha Edición		:
# Descripción		:   Accede a una base de datos de formatos específicos a
#                       una cultura. El atributo grouping de la función format
# permite una forma directa de formatear números con separadores de grupo.
#==============================================================================
import locale

locale.setlocale(locale.LC_ALL, '')
conv = locale.localeconv()
print("Conversion de locale :", conv)
x=3738393.9
print("variable x = ", x)
locale.format("%d", x, grouping=True)
print("Nuevo formato = ", locale.format("%d", x, grouping=True))
