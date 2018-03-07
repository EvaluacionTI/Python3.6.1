# =============================================================================
# * Proyecto :   Evaluación de Python 3.6.1
# * Módulo   :
# * File     :   PYH0201v01DeclararImport.py
# * Author   :   ALDV
# * Created  :  21 de febrero de 2018, 09:57 AM
# * Objetivo : Capturar un excepción
# =============================================================================*/

# Formas de declarar un módulo

# 1. Importa módulo Test. Referirse a X en test con test.x
import test

print("Dirección de test ----> ", test)

# 2. Importa X de IO. Referirse a X en test con "x"
from io import FileIO
print("Dirección io ---->", FileIO.mro())

# 3. Importa todos los objetos de _collections. Referirse a x en _collections con x
from _collections import *

# 4. Importa <moduulo> con un alias
import _thread as hilo
print("thread - hilo ---->", hilo._count())