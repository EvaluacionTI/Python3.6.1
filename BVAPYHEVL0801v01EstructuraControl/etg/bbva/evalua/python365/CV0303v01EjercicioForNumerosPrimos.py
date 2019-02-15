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

aListaPrimo = []
for indice in range(1,1001):
    print("Dividendo = ", indice)
    contador = 1
    aListaDivisores = []

    while(contador<=indice):
        print("Divisor = ", contador)
        cociente = indice / contador
        resto = indice % contador
        print("Cociente =", cociente)
        print("Resto = ", resto)
        contador += 1
        if resto==0:
            aListaDivisores.append(indice)
    print(aListaDivisores)
    if len(aListaDivisores)==2:
        aListaPrimo.append(indice)
    print("=" *40)

print(aListaPrimo)
