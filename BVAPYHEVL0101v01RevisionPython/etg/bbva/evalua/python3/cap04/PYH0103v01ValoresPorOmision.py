# =============================================================================
# * Proyecto :   Evaluación de Python 3.6.1
# * Módulo   :
# * File     :   PYH0103v01ValoresPorOmision.py
# * Author   :   ALDV
# * Created  :   20 de febrero de 2018, 10:35 AM
# * Objetivo :   Definir una funcción para la serie de fibonaci
# =============================================================================*/
# Definir la función
def pedirConfirmacion(prompt, reintentos=4, recordatorio='Por favor intente nuevamente'):
    while (True):
        ok = input(prompt)
        if ok in ('s', 'S', 'SI', 'si', 'Si'):
            return True
        if ok in ('n', 'no', 'No', 'NO'):
            return False
        reintentos = reintentos - 1
        if (reintentos < 0):
            raise ValueError('Respuesta de usuario inválida')
        print (recordatorio)

# Ejecutar la función
pedirConfirmacion('Realmente quiere salir')
