#==============================================================================
# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	PRE - Actualización de foto de predio del contribuyente
# Módulo			        :   Módulo de Predios
# Fecha	Creación	    :	16Abr2019
# Objetivo			        :   Conexion a SQLite
#                                  :
# Procedimiento       :   Crear tablas
#
#
#==============================================================================
import sqlite3 as oFormatSQLite
from  BVAPYHEVL1301v01BaseDatos.pe.etg.bbva.evalua.entity.CE0101v01ConstanteSQLite import CEConstanteSQLite as  oDBSQLite;


# 1. Declarar la conexión
oCxn = None
try:
    oCxn = oFormatSQLite.connect(oDBSQLite().ARCHIVO_DB)
    print("Dirección de conexion : ", oCxn)

    # 2. Declarar cursos para el manejo e invocación a SQL
    oCursor = oCxn.cursor()
    print("Cursor : ", oCursor)
    # 3. Eliminar tablas
    oCursor.execute(oDBSQLite().DROP_PREDIO_FOTO)
    oCursor.execute(oDBSQLite().DROP_PREDIO)
    oCursor.execute(oDBSQLite().DROP_CONTRIBUYENTE)
    oCursor.execute(oDBSQLite().TABLE_CONTRIBUYENTE)
    oCursor.execute(oDBSQLite().TABLE_PREDIO)
    oCursor.execute(oDBSQLite().TABLE_PREDIO_FOTO)

except(oCxn.DatabaseError):
    print("Error %s" % oCxn.DatabaseError)
    print("Error %s" % oCxn.DataError)
    print("Error %s" % oCxn.Error)
    print("Error %s" % oCxn.InternalError)
    oCxn.rollback()
finally:
    print("OK %s" % oCxn.total_changes)
    print("NOT Error %s" % oCxn.DatabaseError)
    oCxn.commit()
    oCxn.close()


