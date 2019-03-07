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
class CEPersona:
    def __init__(self):
        self.paas = "Distribuido"

class CEVehiculo:
    # Método implicito que permite crear la instancion de un objeto
    def __init__(self, psNombre, psApellidos):
        self.sNombre = psNombre
        self.sApellido = psApellidos

def principal():
    print("Iniciar la instancia sin argumentos")
    print("Clase CEPersona : ", CEPersona())
    print("Atributo paas de la clase CEPersona : ", CEPersona().paas)
    print("=" *80)
    print("Iniciar la instancia con argumentos")
    print("Clase CEVehiculo : ", CEVehiculo("15", "17"))
    print("Atributo paas de la clase CEVehiculo : ", CEVehiculo("Illari", "Díaz").sNombre, CEVehiculo("Luis", "Díaz").sApellido)
    instanciar = CEVehiculo("Esteban","Díaz")
    print(instanciar)
    print("Atributo de la clase CEVehiculo : ", instanciar.sNombre, instanciar.sApellido)


principal()

