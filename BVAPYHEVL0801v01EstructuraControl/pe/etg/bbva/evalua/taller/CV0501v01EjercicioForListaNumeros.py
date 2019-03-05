#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	15Mar2018
# Periódo           :   15Mar/2018
# Objetivo			:	Bucle
# Fecha Edición		:
# Descripción		:   For
#==============================================================================

# 1. Utilice un for para crear una lista de número de 1 al 10 y lo muestre en
#    pantalla

aListaNumero = []
print("1. Lista de Numeros")
for indice in range(1,11):
    aListaNumero.append(indice)

print("Lista de números : ", aListaNumero)

# 2. Que a partir de una tupla, obtenga una lista con todos los elementos de la tupla
#    Utilice un tarea

print("2. Ingresar tuplas de numeros")
iNumeroInicial = int(input("Ingrese el primera valor : "))
iNumeroFinal = int(input("Ingrese el primera valor : "))

if iNumeroInicial > iNumeroFinal:
    iNumeroFinal = iNumeroInicial + 1

aListaTupla = []
print("Tupla (", iNumeroInicial, iNumeroFinal, ")")
for indice in range(iNumeroInicial, iNumeroFinal):
    aListaTupla.append(indice)

print("Tupla final : ", aListaTupla)