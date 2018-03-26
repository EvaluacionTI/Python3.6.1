#==============================================================================
# Entidad			:	Entelgy - Banco Continental
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	05Feb2018
# Objetivo			:	Introducción a Python
# Fecha Edición		:
# Descripción		:   Definición de clase
#**********************************************************************************
class PenguiPen:
    def __init__(self):
        print(self)
        self.penguinCount = 0
    def add(self, number=1):
        print(self)
        self.penguinCount = self.penguinCount + number
    def remove(self, number=1):
        print(self)
        self.penguinCount = self.penguinCount - number
        print(self)
    def population(self):
        print(self)
        return self.penguinCount
    def __del__(self):
        pass


penguiPen = PenguiPen()
penguiPen.add(6)
print(penguiPen.population());