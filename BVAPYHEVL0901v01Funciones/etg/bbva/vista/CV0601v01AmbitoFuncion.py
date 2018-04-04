#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	03Abr2018
# Periódo           :   03Abr/2018
# Objetivo			:	Funciones str
# Fecha Edición		:
# Descripción		:   Ambito de funciones
#==============================================================================
def ambitos():
    def hacerLocal():
        algo = "ambito local"
    def hacerNoLocal():
        nonlocal algo
        algo = "ambito no local"
    def hacerGlobal():
        global algo
        algo = "ambito global"
    algo = "algo de prueba"
    hacerLocal()
    print("1. Luego de la asignación local : ", algo)
    hacerNoLocal()
    print("2. Luego de la asignación no local : ", algo)
    hacerGlobal()
    print("3. Luego de la asignación global : ", algo)

def principal():
    ambitos()
    print("4. Alcance de ambitos : ", algo)

principal()