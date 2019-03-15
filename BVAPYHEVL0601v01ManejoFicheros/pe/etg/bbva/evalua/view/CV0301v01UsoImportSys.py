#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	02Mar2018
# Periódo           :   02Mar/2018
# Objetivo			:	Print
# Fecha Edición		:
# Descripción		:   stdout en Python es sys.stdout, stdin es sys.stdin
#==============================================================================
import sys

class CVPrintRedirect:
    def __init__(self):
        print(self)
    def __init__(self, pFileName):
        self.filename = pFileName
    def write(self, pMsg):
        file = open(self.filename, 'a')
        file.write(pMsg)
        file.close()

sys.stdout = CVPrintRedirect('CV0301v01LogSysTmp.log')
print("Log de mensaje 1")
print("Log de mensaje 2")
print("Log de mensaje 3")
print("Log de mensaje 4")
print("Log de mensaje 5")