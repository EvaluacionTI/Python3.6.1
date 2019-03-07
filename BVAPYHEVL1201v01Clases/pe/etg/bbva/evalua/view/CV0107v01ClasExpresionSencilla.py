#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	12Abr2018
# Periódo           :   12Abr/2018
# Objetivo			:	Representar expresiones numéricas con sumas y multipli
#                       caciones.
# Fecha Edición		:
# Descripción		:   Características:

#==============================================================================
class CLAst():
    def __init__(self): pass
    def mostrar(self): pass
    def numeroOperaciones(self): pass
    def interpreta(self): pass


class CLNumero(CLAst):
    def __init__(self, valor):
        self.valor = valor
    def mostrar(self):
        return str(self.valor)
    def numeroOperaciones(self):
        return 0
    def interpreta(self):
        return self.valor


class CLOperacion(CLAst):
    def __init__(self, op, izda, dcha):
        self.op = op
        self.izda = izda
        self.dcha = dcha
    def mostrar(self):
        return '(' + self.izda.mostrar() + self.op + self.dcha.mostrar() +')'
    def numeroOperaciones(self):
        return 1 + self.izda.numeroOperaciones() + self.dcha.numeroOperaciones()
    def interpreta(self):
        if self.op=="+":
            return self.izda.interpreta() + self.dcha.interpreta()
        else:
            return self.izda.interpreta() * self.dcha.interpreta()


def principal():
    oCLnumero1 = CLNumero(4)
    oCLnumero2 = CLNumero(5)
    oCLnumero3 = CLNumero(3)
    oCLnumero4 = CLNumero(2)

    oArbol1 = CLOperacion('*', oCLnumero1, oCLnumero2)  #4*5
    oArbol2 = CLOperacion('*', oCLnumero3, oCLnumero4)  #3*2
    oArbolFinal = CLOperacion('+', oArbol1, oArbol2)
    print("Objeto Numero 1 : ", oCLnumero1.valor)
    print("Objeto Numero 2 : ", oCLnumero2.mostrar())
    print("Objeto Numero 3 : ", oCLnumero3.interpreta())
    print("Objeto Numero 4 : ", oCLnumero4.numeroOperaciones())

    print("Arbol final :", oArbolFinal.mostrar())
    print("Arbol contiene en total %d operaciones : ", oArbolFinal.numeroOperaciones())
    print("La expresión se evalua como : ", oArbolFinal.interpreta())

principal()