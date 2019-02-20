#==============================================================================
# Entidad			    :	Entelgy - Banco Continental
# Proyecto			    :	EVL (Evaluación de Python 3.6.5.)
# Módulo			    :
# Fecha	Creación	:	18Ene2019
# Objetivo			    :	Adicionar una coma a los importes para mejorar su visualización
#
# Fecha Edición		:
# Descripción		:   Convertir a cadena, para poder tomar cada dígito.
#                                  Recorrer la cadena de derecha a izquierda, de tres en tres dígitos
#                                  Se inserta la coma cada vez si todavía quedan más de tres dígitos a la izquierda.
#==============================================================================


def ponerComa(pNumero):
    sNumeroCadena = str(pNumero)
    iLongitudNumero = len(sNumeroCadena)
    TOPE_TAMANO_MILES = 3
    SIGNO_COMA = ','

    print("Número en cadena    : ", sNumeroCadena)
    print("Longitud de Número : ", iLongitudNumero)

    while iLongitudNumero > TOPE_TAMANO_MILES:
        iLongitudNumero = iLongitudNumero - TOPE_TAMANO_MILES
        print("Nueva Longitud de Número : ", iLongitudNumero)
        print("Nuevo derecha : ", sNumeroCadena[:iLongitudNumero])
        print("Nuev izquierda : ", sNumeroCadena[iLongitudNumero:])
        sNumeroCadena = sNumeroCadena[:iLongitudNumero] + SIGNO_COMA + sNumeroCadena[iLongitudNumero:]

    return sNumeroCadena


print("Base Valor Exponente")
for i in range(-100,-2):
    print('%3d %20s' %(i, ponerComa(5000*i)))
    #print('%3d  %20s' %(i, 3000*i))