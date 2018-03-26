#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	23Feb2018
# Objetivo			:	Argumento de funciones con valores por omisión
# Fecha Edición		:
# Descripción		:
#==============================================================================
def confirmacion (pMensaje, pReintentos=4, pRecordatorio="Por favor, intentelo nuevamente"):
    while True:
        ok = input(pMensaje)
        if ok in ('s', 'S', 'SI', 'si', 'sI', 'Si'):
            return True
        if ok in ('n', 'N', 'NO', 'no', 'nO', 'No'):
            return False
        pReintentos = pReintentos - 1
        if (pReintentos < 0):
            raise ValueError("Respuesta inválida")
        print(pRecordatorio)


confirmacion("Es Arquitectura Host ? : ")














