#==============================================================================
# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	EVL - Evaluacion
# Módulo			        :   Módulo de Predios
# Fecha	Creación	    :	26Abr2019
# Objetivo			        :   Conexion a Postgres
#                                  :
# Procedimiento       :   Evaluation conexion a Postgres
#
#
#==============================================================================
import psycopg2

oCxn = None
try:
    oCxn = psycopg2.connect(database="bbvarquitectura", user="postgres", password="aemsa152027")
    print("Conexion realizada : ", oCxn)
except(psycopg2.DatabaseError):
    print("Error %s" % psycopg2.DatabaseError)
finally:
    oCxn.close()