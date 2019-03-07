#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	03Abr2018
# Periódo           :   03Abr/2018
# Objetivo			:	Definición de clase
# Fecha Edición		:
# Descripción		:   Características:
#                       La palabra reservada utilizada es class
# Generalmente, la definici´on de la clase consiste en una serie de funciones que ser´an los
# m´etodos de la clase.
# Todos los m´etodos tienen self como primer par´ametro. Este es el par´ametro con el que se
# pasa el objeto. El nombre self es convencional, puede ser cualquier otro.
# Existe un m´etodo especial __init__. A este m´etodo se le llama cuando se crea un objeto de
# la clase.
# Los atributos (campos de datos) de la clase se crean como las variables de Python, mediante
# una asignaci´on sin declaraci´on previa.
#==============================================================================
class CENombreClase:
    #declaracion 1
    tasa = 10;
    baseCalculo = 360;

    #declaracion N
    def mostrar(self):
        return "Definir clase"


def principal():
    print("Tasa = ", CENombreClase.tasa)
    print("Base calculo = ", CENombreClase.baseCalculo)
    direccionClase = CENombreClase();
    print("Direccion de clase = ", direccionClase)
    print(CENombreClase.mostrar("ss"))

principal()


