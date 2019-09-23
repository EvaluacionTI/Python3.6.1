#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	21Mar2018
# Periódo           :   21Mar/2018
# Objetivo			:	Manejo de import
# Fecha Edición		:
# Descripción		:   Serie de Fibonaci
#==============================================================================

# Escribe la serie fibonnaci
def fibonaci(piNumero):
    a, b = 0,1
    while(b<piNumero):
        print(b, end='')
        a, b = b, a+b
    print()

# Devuelve la serie de fibonaci
def fibonaci1(piNumero):
    aResultado = []
    a, b = 0, 1
    while( b < piNumero):
        aResultado.append(b)
        a,b = b,a+b
        print(aResultado)
    return aResultado