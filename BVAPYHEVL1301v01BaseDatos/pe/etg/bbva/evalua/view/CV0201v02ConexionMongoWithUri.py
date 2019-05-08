#==============================================================================
# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	EVL - Evaluacion
# Módulo			        :   Base de datos
# Fecha	Creación	    :	07May2019
# Objetivo			        :   Conexion a Mongo
#                                  :
# Procedimiento       :   Evaluation conexion a Postgres
#
#
#==============================================================================
from pymongo import MongoClient

oCxn = None
try:

    oCxn = MongoClient("mongodb://localhost:27017")
    print("Conexion realizada : ", oCxn)
except(MongoClient.DatabaseError):
    print("Error %s" % MongoClient.DatabaseError)
finally:
    oCxn.close()