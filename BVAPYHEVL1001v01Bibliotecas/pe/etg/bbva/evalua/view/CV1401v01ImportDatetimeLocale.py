#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	19Abr2018
# Periódo           :   19Abr/2018
# Objetivo			:	Import datetime
# Fecha Edición		:
# Descripción		:   datetime y locale
#==============================================================================
from datetime import date
import locale

hoy = date.today();
print("Fecha de hoy : ", hoy)

#locale.setlocale(locale.LC_ALL, locale.getdefaultlocale())

hoy.strftime("%m-%d-%y. %d %b %Y es %A. hoy es %d de %B.")
print(hoy)

nacimiento = date(1969,8,6)
print("Fecha Nacimiento", nacimiento)
edad = hoy - nacimiento
print("Edad = ", edad)

