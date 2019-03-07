#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	09Abr2018
# Periódo           :   09Abr/2018
# Objetivo			:	Conexion a base de datos
# Fecha Edición		:
# Descripción		:   Características:

#==============================================================================
import psycopg2

oCxn = None
try:
    oCxn = psycopg2.connect(database="aemsaprueba", user="postgres", password="aemsa152027")
    print("Conexion realizada", oCxn)
except(psycopg2.DatabaseError):
    print("Error %s" % psycopg2.DatabaseError)
finally:
    oCxn.close()