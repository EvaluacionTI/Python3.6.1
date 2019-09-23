#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	18Abr2018
# Periódo           :   18Abr/2018
# Objetivo			:	Hilos
# Fecha Edición		:
# Descripción		:   thread

#==============================================================================
import _thread

def f(nombre):
    print("Arquitectura de Servicios, %s" %nombre)

f("with Host")
numero = _thread.start_new_thread(f, ('BBVA',))
print(numero)