#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	20Abr2018
# Periódo           :   20Abr/2018
# Objetivo			:	Hilos
# Fecha Edición		:
# Descripción		:   thread

#==============================================================================
from threading import *

class CUHilo(Thread):
    def __init__(self, nombre):
        Thread.__init__(self)
        self.nombre = nombre
    def run(self):
        print("Arquitectura de Servicios : %s", self.nombre)

oCUHilo = CUHilo("Host")
print(oCUHilo)

oCUHilo.start()