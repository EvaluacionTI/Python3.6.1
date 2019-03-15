#==============================================================================
# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	EVL (Evaluación de Python 3.6.1.)
# Módulo			        :
# Fecha	Creación	    :	15Mar2019
# Objetivo			        :	Revisión Job
# Descripción		    :   Convierte una lista a una cadena de texto
# formato                  :  'step'.join(lista)
#                             donde sep representa el o los caracteres que deseamos utilizar como delimitador.
#==============================================================================

lista_paises = ['Argentina', 'Uruguay', 'Chile', 'Paraguay', 'Brasil', 'Bolivia', 'Perú' ]
cadenasinseparador = ''.join(lista_paises)
cadenaseparadorcoma = ','.join(lista_paises)
cadenaseparadorbarra = '|'.join(lista_paises)

print("Lista paises                    : ", lista_paises)
print("Cadena sin separador  : ", cadenasinseparador)
print("Cadena con separador  coma : ", cadenaseparadorcoma)
print("Cadena con separador  barra  : ", cadenaseparadorbarra)



