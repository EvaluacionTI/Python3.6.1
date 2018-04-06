#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	05Abr2018
# Periódo           :   05Abr/2018
# Objetivo			:	Definición de clase Arboles de Búsqueda
# Fecha Edición		:
# Descripción		:   Características:
#                       Sufienciente con poner en la declaracion de la clase
# derivada, el nombre de la clase base entre paréntesis
#
#==============================================================================
class CEArbol:
    def __init__(self, elto):
        self.elto = elto
        self.izdo = None
        self.dcho = None

    def inserta(self, pNuevo):
        if pNuevo == self.elto:
            return self
        elif pNuevo < self.elto:
            if self.izdo == None:
                self.izdo = CEArbol(pNuevo)
            else:
                self.izdo = self.izdo.inserta(pNuevo)
        else:
            if (self.dcho==None):
                self.dcho = CEArbol(pNuevo)
            else:
                self.dcho=self.dcho.inserta(pNuevo)
        return self


def principal():
    oCEArbol = CEArbol(5)
    print("Instancia de clase - oCEArbol : ", oCEArbol)

principal()