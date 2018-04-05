#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	05Abr2018
# Periódo           :   05Abr/2018
# Objetivo			:	Definición de clase derivada
# Fecha Edición		:
# Descripción		:   Características:
#                       Sufienciente con poner en la declaracion de la clase
# derivada, el nombre de la clase base entre paréntesis
#==============================================================================
class CEVehiculo:
    def __init__(self, piValor):
        self.iValor = piValor
        print("Inicializa la base con un %d" % piValor)
    def formato1(self, piNumero):
        return "Formato 1 recibe un %d " % piNumero

    def formato1(self, piNumero):
       return "Formato 2 recibe un %d " % piNumero


class CEDerivada(CEVehiculo):
    def __init__(self, piValor):
        CEVehiculo.__init__(self, piValor)
        self.iNuevoValorDerivado = piValor
        print("Inicializa la clase derivada con un %d" % piValor)
    def formato3(self, piNumero):
        return "Formato 3 recibe un %d " % piNumero


oCEVehiculo = CEVehiculo(10)
print("Clase Vechiculo : ", CEVehiculo(15))
print("Valor de la instancia : ", oCEVehiculo.iValor)
print("=" *80)
oCEDerivada = CEDerivada(15)
print("Clase derivada : ", oCEDerivada)
print("metodo derivado formato3 : ", oCEDerivada.formato3(17))