#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	18Abr2018
# Periódo           :   18Abr/2018
# Objetivo			:	Conexion a base de datos
# Fecha Edición		:
# Descripción		:   Características:

#==============================================================================
import sqlite3 as oDbSql

oCxn = None
try:
    oCxn = oDbSql.connect('F:/BaseDatos/SQLite/data/aemsaprueba.sqlite')
    print("Conexion realizada", oCxn)
except(oDbSql.DatabaseError):
    print("Error %s" % oDbSql.DatabaseError)
finally:
    oCxn.close()