#==============================================================================
# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	PRE - Actualización de foto de predio del contribuyente
# Módulo			        :   Módulo de Predios
# Fecha	Creación	    :	15Abr2019
# Objetivo			        :   Conexion a SQLite
#                                  :
# Procedimiento       :   El objeto cursor se utiliza para obtener, insertar, actualizar o borrar datos de
#                                      nuestra base de datos.
#
#
#==============================================================================
import sqlite3 as oConexionSQLite

oArchivoDB = "F:\BBVA11SQLite\BBVARQUITECTURA.sqlite3"
DROP_TABLE_EMPLEADO = "DROP TABLE IF EXISTS EVLt02_empleado"
TABLE_EMPLEADO = '''
    CREATE TABLE EVLt02_empleado(
        id                 INT PRIMARY KEY,
        txt_nom     TEXT    NOT NULL,
        edad            INT      NOT NULL,
        txt_dir         VARCHAR(50)  NOT NULL,
        salario         REAL)
'''

oCxn = oConexionSQLite.connect(oArchivoDB)
oCursor = oCxn.cursor()

print("Dirección de conexion : ", oCxn)
oCursor.execute(DROP_TABLE_EMPLEADO)
oCursor.execute(TABLE_EMPLEADO)
oCxn.commit()
oCxn.close()
