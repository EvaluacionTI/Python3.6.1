#==============================================================================
# Entidad			:	Entelgy - Banco Continental
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	06Feb2018
# Objetivo			:	Calculo del interes
# Fecha Edición		:
# Descripción		:   Definición de clase
#**********************************************************************************
capital = 1500
baseCalculo=360
tasaInteres=3.6
numeroDias=45
base = (1+tasaInteres * 0.01)
exponente = (numeroDias / baseCalculo)
factor = pow(base, exponente) - 1
interes=factor*capital

print("Capital : ", capital)
print("Base de Cálculo : ", baseCalculo)
print("Tasa de Interés : ", tasaInteres)
print("Número de días : ", numeroDias)
print("Base : ", base)
print("Exponente : ", exponente)
print("Factor : ", factor)
print("Interes Corrido : ", interes)
