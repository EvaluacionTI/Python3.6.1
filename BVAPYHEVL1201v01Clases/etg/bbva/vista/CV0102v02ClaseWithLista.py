#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	05Abr2018
# Periódo           :   05Abr/2018
# Objetivo			:	Definición de clase con uso de listas
# Fecha Edición		:
# Descripción		:   Características:
#
#
#==============================================================================
class CEPerro:
    def __init__(self, psNombre):     #Método implicito que permite crear la instancion de
        self.sNombre = psNombre
        self.aTruco = []    # Crea una nueva lista vacia para cada perro
    def agregarTruco(self, aTruco):
        self.aTrucos = aTruco

def principal():
    print("Clase CEPerro = ", CEPerro("Rotwailer"))
    asignacion = CEPerro('Fido')
    asignacion.agregarTruco('Saltar')
    asignacion.agregarTruco('Dar vuelta')
    print(asignacion.aTrucos)

principal()


