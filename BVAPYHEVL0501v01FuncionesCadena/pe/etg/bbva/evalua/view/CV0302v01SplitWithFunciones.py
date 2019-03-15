#==============================================================================
# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	EVL (Evaluación de Python 3.6.1.)
# Módulo			        :
# Fecha	Creación	    :	14Mar2019
# Objetivo			        :	Revisión Split
# Descripción		    :   Convierte una cadena de texto en una lista
#==============================================================================
pais_blanco = 'Argentina Uruguay Chile Paraguay Brasil Bolivia'
pais_coma = 'Argentina, Uruguay, Chile, Paraguay, Brasil, Bolivia'


def separar_blanco(pscadena):
    return pscadena.split()


def separar_coma(pscadena):
    return pscadena.split(',')


def principal():
    lista_blanco_pais = separar_blanco(pais_blanco)
    lista_coma_pais = separar_blanco(pais_coma)

    print("Cadena : ", pais_blanco)
    print("Lista     : ", lista_blanco_pais)

    print("Cadena : ", pais_coma)
    print("Lista     : ", lista_coma_pais)


principal()