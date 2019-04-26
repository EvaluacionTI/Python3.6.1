#==============================================================================
# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	EVL - Evaluacion
# Módulo			        :   Base de datos
# Fecha	Creación	    :	26Abr2019
# Objetivo			        :   Conexion a Mongo
#                                  :
# Procedimiento       :   Evaluation conexion a Postgres
#
#
#==============================================================================
import pymongo as oFormatDB

oCxn = None
try:
    oCxn = oFormatDB.MongoClient("localhost", 27015)
    print("Conexion realizada : ", oCxn)
except(oFormatDB.DatabaseError):
    print("Error %s" % oFormatDB.DatabaseError)
finally:
    oCxn.close()