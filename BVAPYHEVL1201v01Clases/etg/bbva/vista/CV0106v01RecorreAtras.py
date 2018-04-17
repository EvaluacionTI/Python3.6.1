#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	09Abr2018
# Periódo           :   09Abr/2018
# Objetivo			:   Clase
# Fecha Edición		:
# Descripción		:   Mostrar un texto en forma inversa
#
#==============================================================================
class CEReserva:
    def __init__(self, datos):
        self.datos = datos
        self.indice = len(datos)
    def __iter__(self):
        return self
    def __next__(self):
        if self.indice == 0:
            raise StopIteration
        self.indice = self.indice - 1
        return self.datos[self.indice]

def principal():
    oCEReserva = CEReserva('MongoDb')
    iter(oCEReserva)
    for char in oCEReserva:
        print(char)

principal()