#==============================================================================
# Entidad			:	Entelgy - Banco Continental
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	22Feb2018
# Objetivo			:	Paquetes en Python
# Fecha Edición		:
# Descripción		:   Declarar clase para su uso en import
#==============================================================================
class CEModulo1:
    def __init__(self):
        self.descripcion = 'iniciar clase CEModulo1'
        print(self)
    def show(self):
        print(self.descripcion)

def CEModulo():
    print("Clase CEModulo1")