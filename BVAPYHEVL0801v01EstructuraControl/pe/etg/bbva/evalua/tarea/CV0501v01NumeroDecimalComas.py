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

# def ponerComa(pNumero):
#     sNumeroCadena = str(pNumero)
#     iLongitudNumero = len(sNumeroCadena)
#     iPosicionPuntoDecimal = 0
#     for j in range(iLongitudNumero):
#         sCaracter = sNumeroCadena[j:1]
#          if sCaracter==SIGNO_DECIMAL:
#              iPosicionPuntoDecimal = j
#             sParteEntera = sNumeroCadena[:j]
#             sParteDecimal = sNumeroCadena[j:]
#             break
#          else:
#             iPosicion = iPosicion + 1
#
#
#         sNumeroCadena = sParteEntera
#         while iLongitudNumero > TOPE_TAMANO_MILES:
#             iLongitudNumero = iLongitudNumero - TOPE_TAMANO_MILES
#             sNumeroCadena = sNumeroCadena[:iLongitudNumero] + SIGNO_COMA + sNumeroCadena[iLongitudNumero:]
#
#     return sNumeroCadena

def principal():

    print("Base Valor Exponente")
    sValorDecimal = input("Ingrese un valor decimal : ")
    print(sValorDecimal)
    iValorDecimal = float(sValorDecimal)+5.1
    print(iValorDecimal)
    for i in range(1, 5):
        print('%3d  %20s' %(i, iValorDecimal**i))

    print("=========================================")
    for i in range(1,5):
 #       print('%3d %20s' %(i, ponerComa(iValorDecimal**i)))

principal()

