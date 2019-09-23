#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	09Abr2018
# Periódo           :   09Abr/2018
# Objetivo			:	Generadores
# Fecha Edición		:
# Descripción		:   Los generadores son una simple y poderosa herramienta
# para crear iteradores. Se escriben como funciones regulares pero
# usan la sentencia yield cuando quieren devolver datos.
#==============================================================================
def reversa(datos):
    for indice in range(len(datos)-1, -1, -1):
        yield datos[indice]

def principal():
    for letra in reversa('Palta '):
        print(letra)

principal()