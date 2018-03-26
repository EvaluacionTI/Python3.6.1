#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	08Mar2018
# Periódo           :   08Mar/2018
# Objetivo			:	Serializar
# Fecha Edición		:
# Descripción		:   Serializar y deserializar un objeto con dump
#                       Existen distintos tipos de serializacion, accesibles
# a través de la librería estandar: marshal, shelve y pickle.
# dump() y load(), que escriben y leen en un archivo determinado
#==============================================================================
import pickle

class CECliente:
    def __init__(self, dni, nombre, apellidoPaterno, apellidoMaterno):
        self.dni = dni
        self.nombre = nombre
        self.apellidoPaterno = apellidoPaterno
        self.apellidoMaterno = apellidoMaterno
    def __str__(self):
        return "DNI = " + self.dni + " " + self.nombre + " " + self.apellidoPaterno + " " + self.apellidoMaterno
    def get_dni(self):
        return self.dni
    def get_nombre(self):
        return self.nombre
    def get_apellidoPaterno(self):
        return self.apellidoPaterno
    def get_apellidoMaterno(self):
        return self.apellidoMaterno

oCECliente = CECliente("0937352", "ILLARI", "DIAZ", "VEGA")
print("1. Objeto = ", oCECliente)
serializar = pickle.dumps(oCECliente)
print("2. Serializar = ", serializar)

print("3. Grabando el archivo serializado : SerializarCliente.txt")
oFile = open("SerializarCliente.txt", "wb")
pickle.dump(oCECliente, oFile)
oFile.close()

print("4. Leyendo un archivo")
oFile = open("SerializarCliente.txt", "rb")
deserializar = pickle.load(oFile)
print("Lectura", deserializar)
oFile.close()
