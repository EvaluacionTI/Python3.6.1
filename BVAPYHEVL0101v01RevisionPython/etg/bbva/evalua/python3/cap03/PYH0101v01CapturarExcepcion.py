# =============================================================================
# * Proyecto :  Evaluación de Python 3.6.1
# * Módulo   :
# * File     :  PYH0101v01CapturarExcepcion.py
# * Author   :  ALDV
# * Created  :  20 de febrero de 2018, 10:14 AM
# * Objetivo :  Capturar un excepción
# =============================================================================*/
try:
    fh=open("new.txt", "r")
except IOError as err:
    print(err)