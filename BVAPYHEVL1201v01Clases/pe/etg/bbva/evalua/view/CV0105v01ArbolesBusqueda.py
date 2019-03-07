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

    # Comprobar si un elemento está en el arbol
    def estado(self, buscando):
        if (buscando==self.elto):
            return True
        elif buscando < self.elto:
            if self.izdo==None:
                return False
            else:
                return self.izdo.estado(buscando)
        else:
            if self.dcho == None:
                return False
            else:
                return self.dcho.estado(buscando)

def principal():
    oCEArbol = CEArbol(5)
    print("Instancia de clase - oCEArbol : ", oCEArbol)
    CEArbol(3).inserta(2).inserta(4)
    print("Insertar : ", CEArbol)

principal()