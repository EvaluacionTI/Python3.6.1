#==============================================================================
# Entidad			    :	Entelgy - Banco Continental
# Proyecto			    :	EVL (Evaluación de Python 3.6.5.)
# Módulo			    :
# Fecha	Creación	:	18Ene2019
# Objetivo			    :	Mostrar los valores negativos enteros con formato comas
#
# Fecha Edición		:
# Descripción		:   1. Definir una funcion principal y de asignación de comas
#   2. Definir las variables para la coma y espaciamiento de miles
#   3. Convertir a cadena, para poder tomar cada dígito.
#==============================================================================


def ponerComa(pNumero):
    sNumeroCadena = str(pNumero)
    iLongitudNumero = len(sNumeroCadena)
    TOPE_TAMANO_MILES = 3
    SIGNO_COMA = ','

    #print("Número en cadena    : ", sNumeroCadena)
    #print("Longitud de Número : ", iLongitudNumero)

    while iLongitudNumero > TOPE_TAMANO_MILES:
        iLongitudNumero = iLongitudNumero - TOPE_TAMANO_MILES
        # print("Nueva Longitud de Número : ", iLongitudNumero)
        # print("Nuevo derecha : ", sNumeroCadena[:iLongitudNumero])
        # print("Nuev izquierda : ", sNumeroCadena[iLongitudNumero:])
        sNumeroCadena = sNumeroCadena[:iLongitudNumero] + SIGNO_COMA + sNumeroCadena[iLongitudNumero:]

    return sNumeroCadena


def principal():

    print("Base Valor Exponente")
    for i in range(-100,-2):
        print('%3d %20s' %(i, ponerComa(5000*i)))
    #print('%3d  %20s' %(i, 3000*i))


principal()

