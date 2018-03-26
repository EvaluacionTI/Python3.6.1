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

import time
from datetime import datetime

dFechaHoraInicio = time.strftime("%c")
dFechaHoraInicial = datetime.now()

## representacion de fecha y hora
print("Fecha y hora : " + time.strftime("%c"))
## representacion del tiempo
print("Fecha "  + time.strftime("%x"))
## representacion de la hora
print("Hora " + time.strftime("%X"))
## Muestra fecha y hora actual a partir de la variable
print ("Fecha y hora de inicio : %s"  % dFechaHoraInicio )

print("Fecha - Formato 24 horas : ", time.strftime("%H:%M:%S"))
print("Fecha - Formato 12 horas : ", time.strftime("%I:%M:%S"))
print("Fecha inicio : ", time.strftime("%d/%m/%y"))

aListaPrimo = []
for indice in range(1,1001):
    contador = 1
    aListaDivisores = []

    while(contador<=indice):
        resto = indice % contador
        contador += 1
        if resto==0:
            aListaDivisores.append(indice)
    if len(aListaDivisores)==2:
        aListaPrimo.append(indice)

print(aListaPrimo)
dFechaHoraTermino = time.strftime("%c")
dFechaHoraFinal = datetime.now()
print("Fecha y hora final : %s " % dFechaHoraTermino)
print("Tiempo proceso : ", (dFechaHoraFinal - dFechaHoraInicial))