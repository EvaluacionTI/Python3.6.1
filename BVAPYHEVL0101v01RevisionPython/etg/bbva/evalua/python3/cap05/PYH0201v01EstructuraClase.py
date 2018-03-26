#==============================================================================
# Entidad			:	Entelgy - Banco Continental
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	07Feb2018
# Objetivo			:	Introducción a Python
# Fecha Edición		:
# Descripción		:  Cada método de una clase contiene como primer parámetro
#                       self que hace que referencie a un objeto
#==============================================================================
class CDMantenimiento:
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

# Evaluando los resultados
oClase = CDMantenimiento()
print("Al iniciar : ", oClase.population());
oClase.add(6)
print("Al sumar 6, pero sin asignar : ", oClase.population());
oClase.penguinCount=30
print("Al asignar 30 : ", oClase.population());
oClase.add(15)
print("Al sumar 15 : ", oClase.population());
oClase.remove(3)
print("Al remover 3 : ", oClase.population());
oClase.penguinCount = oClase.population();
print("Al Finalizar asignando : ", oClase.population());