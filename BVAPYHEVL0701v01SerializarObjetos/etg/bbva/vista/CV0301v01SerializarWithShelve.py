#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	14Mar2018
# Periódo           :   14Mar/2018
# Objetivo			:	Serializar
# Fecha Edición		:
# Descripción		:
#==============================================================================
import shelve

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
# El archivo no tiene que existir
serializar = shelve.open("SerializarShelve.txt")
print("2. Serializar = ", serializar)
# Guarda datos en la clave
serializar["1"] = oCECliente
serializar["2"] = "Arquitectura Host"
serializar["tres"] = "Arquitectura Distribuido"
serializar["cuatro"] = "Banco Continental"
lista = serializar.keys()
print("3. Lista de claves", lista)

print("4. Elimina de claves", serializar["cuatro"])
del serializar["cuatro"]

print("5. Cerrando shelve")
print(serializar)
serializar.close()