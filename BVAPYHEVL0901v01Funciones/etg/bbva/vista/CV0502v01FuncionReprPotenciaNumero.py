#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	23Mar2018
# Periódo           :   23Mar/2018
# Objetivo			:	Funciones repr
# Fecha Edición		:
# Descripción		:   Funciones repr
#==============================================================================
def potenciaNumero():
    for x in range(1,11):
        tablax2 = repr(x).rjust(4)      # Con justificación a la derecha en 2
        tablax3 = repr(x*x).rjust(9)    # Con justificación a la derecha en 3
        tablax4 = repr(x*x*x).rjust(13)  # Con justificación a la derecha en 4

        print(tablax2, tablax3, end='')
        print(tablax4)

def potenciaWithFormat():
    for x in range(1,11):
        print('{} {} {}'.format(x, x*x, x*x*x))
        print('{0} {1} {2}'.format(x, x*x, x*x*x))
        print('{0:} {1:} {2:}'.format(x, x * x, x * x * x))
        print('{0:2} {1:3} {2:4}'.format(x, x * x, x * x * x))
        print('{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x))

potenciaNumero()
print("=" *80)
potenciaWithFormat()