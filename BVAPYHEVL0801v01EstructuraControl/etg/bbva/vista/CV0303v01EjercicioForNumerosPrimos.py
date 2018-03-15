#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	15Mar2018
# Periódo           :   15Mar/2018
# Objetivo			:	Bucle - For
# Fecha Edición		:
# Descripción		:   Mostrar por pantalla los números multiplos de 7 entre
#                       1 y 1000. Utilizar range e if si son necesarios.
#==============================================================================

print("3. Ingresar tuplas de numeros")
iNumeroInicial = int(input("Ingrese el primera valor : "))
iNumeroFinal = int(input("Ingrese el primera valor : "))

if iNumeroInicial > iNumeroFinal:
    iNumeroFinal = iNumeroInicial + 1

aListaTupla = []
print("Tupla (", iNumeroInicial, iNumeroFinal, ")")
for indice in range(iNumeroInicial, iNumeroFinal):
    aListaTupla.append(indice)

print("Tupla final : ", aListaTupla)