# =============================================================================
# * Proyecto :   Evaluación de Python 3.6.1
# * Módulo   :
# * File     :   PYH0102v01ListaFibonacci.py
# * Author   :   ALDV
# * Created  :   20 de febrero de 2018, 10:27 AM
# * Objetivo :   Devolver una lista de valores de la serie fibonacci
# =============================================================================*/
def serieFibonacci(pTope):
    """ Devuelve una lista conteniendo la serie Fibonacci hasta una valor n """
    result = []
    inicio, termino = 0, 1
    while (inicio < pTope):
        result.append(inicio)
        inicio, termino = termino, inicio + termino
    return result

valorFibonacci = serieFibonacci(220)
print("Lista fibonacci ", valorFibonacci)