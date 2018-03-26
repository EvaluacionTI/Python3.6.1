#==============================================================================
# Entidad			:	Entelgy - Banco Continental
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	16Feb2018
# Objetivo			:	Herencia de una clase
# Fecha Edición		:
# Descripción		:
#==============================================================================
class Basic:
    def __init__(self, pName):
        self.name = pName
    def show(self):
        print('Basic - name : %s' %self.name)

# Entre paréntesis la clase base
class Special(Basic):
    def __init__(self, pName, edible):
        Basic.__init__(self, pName); # Se usa para referir a clase Base
        self.upper = pName.upper()
        self.edible()
    def show(self):
        Basic.show(self)
        print("Special -- upper name: %s" %self.upper)
        if self.edible:
            print("It is edible")
        else:
            print("It is not edible")
    def edible(self):
        return self.edible

obj1 = Basic('Arquitectura Host')
obj1.show()
print("="*80)
obj2 = Special('Naranja', True)
obj2.show()
