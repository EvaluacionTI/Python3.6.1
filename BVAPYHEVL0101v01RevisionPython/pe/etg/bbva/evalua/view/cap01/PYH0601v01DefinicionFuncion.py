#==============================================================================
# Entidad			:	Entelgy - Banco Continental
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	05Feb2018
# Objetivo			:	Introducción a Python
# Fecha Edición		:
# Descripción		:   Definición de función
#**********************************************************************************
def mostrar(value=None):
    print("Execution starts when 'next()' is called for the first time.")
    try:
       while True:
           try:
                value = (yield value)
           except Exception as e:
                value = e
    finally:
            print("Don't forget to clean up when 'close()' is called.")


generator = mostrar(1)
print(next(generator))

print(next(generator))

print(generator.send(2))

generator.throw(TypeError, "spam")

generator.close()