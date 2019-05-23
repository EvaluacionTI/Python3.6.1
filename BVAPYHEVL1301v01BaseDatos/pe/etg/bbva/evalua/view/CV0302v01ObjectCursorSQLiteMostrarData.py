#==============================================================================
# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	PRE - Actualización de foto de predio del contribuyente
# Módulo			        :   Módulo de Predios
# Fecha	Creación	    :	15Abr2019
# Objetivo			        :   Conexion a SQLite
#                                  :
# Procedimiento       :   El objeto cursor para mostrar datos en la tabla
#
#
#==============================================================================
import sqlite3 as oConexionSQLite

oArchivoDB = "F:\BBVA11SQLite\BBVARQUITECTURA.sqlite3"
SELECT_PREDIO = "SELECT * FROM EVLt02_empleado "

oCxn = oConexionSQLite.connect(oArchivoDB)
print("Dirección de conexion : ", oCxn)

oCursor = oCxn.cursor()
oCursor.execute(SELECT_PREDIO)

for oRow in oCursor:
    print("ID = ", oRow[0], "Nombre =", oRow[1], "Edad = ", oRow[2], "Dirección = ", oRow[3], "Salario = ", oRow[4])

oCxn.close()