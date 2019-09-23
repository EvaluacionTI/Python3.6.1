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
import sqlite3 as oBDSql

sPath = 'F:/BaseDatos/SQLite/data/aemsaprueba.sqlite'
oCxn = None
try:
    oCxn = oBDSql.connect(sPath)
    print("Conexion realizada", oCxn)
    oCursor = oCxn.cursor()
    print("Objeto cursor ", oCursor)
    oCursor.execute("SELECT * FROM DESt01_usuario")

    for id, nombre in oCursor.fetchall():
        print (id, nombre)

except(oBDSql.DatabaseError):
    print("Error %s" % oBDSql.DatabaseError)
finally:
    oCxn.close()