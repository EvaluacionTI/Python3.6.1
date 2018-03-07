# =============================================================================
# * Proyecto :   Evaluación de Python 3.6.1
# * Módulo   :
# * File     :   PYH0101v01DefinirFuncion.py
# * Author   :   ALDV
# * Created  :   20 de febrero de 2018, 10:10 AM
# * Objetivo :   Definir una funcción para la serie de fibonaci
# =============================================================================*/
def fibonacci(pTope):
    """ Serie de fibonani"""
    inicio, termino = 0, 1
    while( inicio < pTope):
        print(inicio, end='')
        inicio, termino = termino, inicio + termino;
    print()


# Llamar a la función de fibonacci
fibonacci(2000)

