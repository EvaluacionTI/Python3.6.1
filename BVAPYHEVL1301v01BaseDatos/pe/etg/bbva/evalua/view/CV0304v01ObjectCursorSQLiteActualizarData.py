#==============================================================================
# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	PRE - Actualización de foto de predio del contribuyente
# Módulo			        :   Módulo de Predios
# Fecha	Creación	    :	15Abr2019
# Objetivo			        :   Conexion a SQLite
#                                  :
# Procedimiento       :   El objeto cursor para actualizar datos en la tabla
#
#
#==============================================================================
import sqlite3 as oConexionSQLite

oArchivoDB = "F:\BBVA11SQLite\BBVARQUITECTURA.sqlite3"
UPDATE_PREDIO = "UPDATE EVLt02_empleado SET salario = 4500 WHERE id=2"

oCxn = oConexionSQLite.connect(oArchivoDB)
print("Dirección de conexion : ", oCxn)

oCursor = oCxn.cursor()
oCursor.execute(UPDATE_PREDIO)
oCxn.commit()
oCxn.close()