#==============================================================================
# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	EVL (Evaluación de Python 3.6.1.)
# Módulo			        :
# Fecha	Creación	    :	14Mar2019
# Objetivo			        :	Revisión Split
# Descripción		    :   Convierte una cadena de texto en una lista
#==============================================================================
cadena_pais_separador_blanco = 'Argentina Uruguay Chile Paraguay Brasil Bolivia'
cadena_pais_separador_coma = 'Argentina, Uruguay, Chile, Paraguay, Brasil, Bolivia'
cadena_pais_separador_barra = 'Argentina| Uruguay| Chile| Paraguay| Brasil| Bolivia'

lista_pais_de_separador_blanco = cadena_pais_separador_blanco.split()
lista_pais_de_separador_coma = cadena_pais_separador_coma.split(',')
lista_pais_de_separador_barra = cadena_pais_separador_barra.split('|')

print("Lista paises de separador blanco : ", lista_pais_de_separador_blanco)
print("Lista paises de separador coma   : ", lista_pais_de_separador_coma)
print("Lista paises de separador barra    : ", lista_pais_de_separador_barra)
