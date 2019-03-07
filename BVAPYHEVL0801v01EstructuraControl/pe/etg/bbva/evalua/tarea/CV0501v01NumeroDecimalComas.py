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
    for j in range(sNumeroCadena):
         if sNumeroCadena[j:1]==SIGNO_DECIMAL:
            sParteEntera = sNumeroCadena[j:]
            sParteDecimal = sNumeroCadena[:j+1]
            break

    sNumeroCadena = sParteEntera
    while iLongitudNumero > TOPE_TAMANO_MILES:
        iLongitudNumero = iLongitudNumero - TOPE_TAMANO_MILES
        sNumeroCadena = sNumeroCadena[:iLongitudNumero] + SIGNO_COMA + sNumeroCadena[iLongitudNumero:]

    return sNumeroCadena


def principal():

    print("Base Valor Exponente")
    iValorDecimal = input("Ingrese un valor decimal : ")
    for i in range(-100,-2):
        print('%3d %20s' %(i, ponerComa(5000*i)))
    #print('%3d  %20s' %(i, 3000*i))


principal()

