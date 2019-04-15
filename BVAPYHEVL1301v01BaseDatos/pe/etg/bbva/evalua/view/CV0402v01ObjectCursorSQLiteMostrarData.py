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

oArchivoDB = "F:\BBVA11SQLite\INVFINDesarrollo.bd"
SELECT_PREDIO = "SELECT * FROM PREt01_empresa "

oCxn = oConexionSQLite.connect(oArchivoDB)
print("Dirección de conexion : ", oCxn)

oCursor = oCxn.cursor()
oCursor.execute(SELECT_PREDIO)

for oRow in oCursor:
    print("ID = ", oRow[0], "Nombre =", oRow[1], "Edad = ", oRow[2], "Dirección = ", oRow[3], "Salario = ", oRow[4])

oCxn.close()