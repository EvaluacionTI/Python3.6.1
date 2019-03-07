#==============================================================================
# Entidad			    :	Entelgy - Banco Continental
# Proyecto			    :	EVL (Evaluación de Python 3.6.5.)
# Módulo			    :
# Fecha	Creación	:	15Ene2019
# Objetivo			    :	Adicionar una coma a los importes para mejorar su visualización
#
# Fecha Edición		:
# Descripción		:   1. Crear una función ponerComar que recibe el número
#                                  2. Convertir el numero a cadena, para poder tomar cada dígito.
#                                  3. Recorrer la cadena de derecha a izquierda, de tres en tres dígitos
#                                  4. Se inserta la coma cada vez si todavía quedan más de tres dígitos a la izquierda.
#==============================================================================


def ponerComa(pNumero):
    sNumeroCadena = str(pNumero)
    iLongitudNumero = len(sNumeroCadena)
    TOPE_TAMANO_MILES = 3
    SIGNO_COMA = ','

   # print("Número en cadena    : ", sNumeroCadena)
    #print("Longitud de Número : ", iLongitudNumero)
    while iLongitudNumero > TOPE_TAMANO_MILES:
        iLongitudNumero = iLongitudNumero - TOPE_TAMANO_MILES
       # print("Nueva Longitud de Número : ", iLongitudNumero)
        #print("Nuevo derecha : ", sNumeroCadena[:iLongitudNumero])
        #print("Nuev izquierda : ", sNumeroCadena[iLongitudNumero:])
        sNumeroCadena = sNumeroCadena[:iLongitudNumero] + SIGNO_COMA + sNumeroCadena[iLongitudNumero:]

    return sNumeroCadena


def mostrarDigitoCadena(piNumero):
    print(len(str(piNumero)))
    sNumeroCadena = str(piNumero)
    for i in range(len(sNumeroCadena)):
        print('%3d %3s %3s' %(i, sNumeroCadena[:i], sNumeroCadena[i:]))


print("Mostrar Digitos de la Cadena")
iNumeroEntero = 1705012002
mostrarDigitoCadena(iNumeroEntero)

print("Base Valor Exponente")
for i in range(60):
    print('%3d %20s' %(i, ponerComa(iNumeroEntero**i)))
