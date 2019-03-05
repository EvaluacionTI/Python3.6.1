#==============================================================================
# Entidad			:	Entelgy - Banco Continental
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	06Feb2018
# Objetivo			:	Calculo del interes
# Fecha Edición		:
# Descripción		:   Definición de función
#**********************************************************************************


def calculoInteres(pCapital, pTasaInteres, pNumeroDias):
    baseCalculo = 360
    base = (1 + pTasaInteres * 0.01)
    exponente = (pNumeroDias / baseCalculo)
    factor = pow(base, exponente) - 1
    interesCorrido = factor * pCapital
    return interesCorrido

def imprimirInteres(pCapital, pBaseCalculo, pTasaInteres, pNumeroDias, pInteresCorrido):
    print("Capital : ", pCapital)
    print("Base de Cálculo : ", pBaseCalculo)
    print("Tasa de Interés : ", pTasaInteres)
    print("Número de días : ", pNumeroDias)
    print("Interes Corrido : ", pInteresCorrido)

capital = 1500
baseCalculo = 360
tasaInteres = 3.6
numeroDias = 45
interesCalculado = calculoInteres(capital, tasaInteres, numeroDias)
imprimirInteres(capital, baseCalculo, tasaInteres, numeroDias, interesCalculado)