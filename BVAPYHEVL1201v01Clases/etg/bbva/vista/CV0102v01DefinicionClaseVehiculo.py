#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	04Abr2018
# Periódo           :   04Abr/2018
# Objetivo			:	Definición de clase
# Fecha Edición		:
# Descripción		:   Características:
#                       La palabra reservada utilizada es class
# Generalmente, la definici´on de la clase consiste en una serie de funciones que ser´an los
# m´etodos de la clase.
# Todos los m´etodos tienen self como primer par´ametro. Este es el par´ametro con el que se
# pasa el objeto. El nombre self es convencional, puede ser cualquier otro.
# Existe un m´etodo especial __init__. A este m´etodo se le llama cuando se crea un objeto de
# la clase.
# Los atributos (campos de datos) de la clase se crean como las variables de Python, mediante
# una asignaci´on sin declaraci´on previa.
#==============================================================================
class CEVehiculo:
    def __init__(self):     #Método implicito que permite crear la instancion de
                            # un objeto
        self.pos=0
    def __del__(self):      # Se llama al destruir el objeto
        self.pos = 0
    def mueve(self, k):
        self.pos=self.pos + k
    def posicion(self):
        return self.pos

def principal():
    print("Clase CEVehiculo = ", CEVehiculo())
    asignacion = CEVehiculo().mueve(10)
    print(asignacion)

principal()


