#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	26Feb2018
# Objetivo			:	Lista de argumentos arbitrarios
# Fecha Edición		:
# Descripción		:   Argumentos organizados en tuplas (Tuplas y secuencias)
#==============================================================================
def muchos_items(archivo, separador, *args):
    archivo.write(separador.join(*args))

def concatenar(*args, sep="/"):
    return sep.join(args)

concatenar("tierra", "marte", "venus")
concatenar("tierra", "marte", "venus", sep=".")