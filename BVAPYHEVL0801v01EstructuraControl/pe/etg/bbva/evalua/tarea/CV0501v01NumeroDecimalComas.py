#==============================================================================
# Entidad			    :	Entelgy - Banco Continental
# Proyecto			    :	EVL (Evaluación de Python 3.6.5.)
# Módulo			    :
# Fecha	Creación	:	07Mar2019
# Objetivo			    :	Mostrar los valores con decimales positivos o negativos con formato comas
#
# Fecha Edición		:
# Descripción		:   1. Definir una funcion principal y de asignación de comas
#   2. Definir las variables para la coma y espaciamiento de miles
#   3. Convertir a cadena, para poder tomar cada dígito.
#==============================================================================

TOPE_TAMANO_MILES = 3
SIGNO_COMA = ','
SIGNO_DECIMAL = "."

def ponerComa(pNumero):

        sNumeroCadena = str(pNumero)
        iLongitudNumero = len(sNumeroCadena)
        iposicion_punto_decimal = 0


        for j in range(iLongitudNumero):
            print(j, sNumeroCadena[j], sNumeroCadena[j:], sNumeroCadena[:j])
            scaracter = sNumeroCadena[j]
            if scaracter == SIGNO_DECIMAL:
                sparte_entera = sNumeroCadena[:j]
                sparte_decimal = sNumeroCadena[j:]
                iposicion_punto_decimal = j
                break

        if iposicion_punto_decimal != 0:
            sNumeroCadena = sparte_entera
            iLongitudNumero = len(sNumeroCadena)

        while iLongitudNumero > TOPE_TAMANO_MILES:
             iLongitudNumero = iLongitudNumero - TOPE_TAMANO_MILES
             sNumeroCadena = sNumeroCadena[:iLongitudNumero] + SIGNO_COMA + sNumeroCadena[iLongitudNumero:]

        return sNumeroCadena + sparte_decimal


def principal():

    print("Base Valor Exponente")
    svalor_decimal = input("Ingrese un valor decimal : ")
    print(svalor_decimal)
    fvalor_decimal = float(svalor_decimal)+5.1
    print(fvalor_decimal)
    for i in range(1, 5):
        print('%3d  %20s' %(i, fvalor_decimal**i))

    print("=========================================")
    for i in range(1,5):
       print('%3d %20s' %(i, ponerComa(fvalor_decimal**i)))


principal()

