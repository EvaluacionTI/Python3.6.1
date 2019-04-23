#==============================================================================
# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	PRE - Actualización de foto de predio del contribuyente
# Módulo			        :   Módulo de Predios
# Fecha	Creación	    :	15Abr2019
# Objetivo			        :   Conexion a SQLite
#                                  :
# Procedimiento       :   Si la bd no existe en la ruta especificada lo crea
#                                      Crear la base de datos en memoria o en fisico
#
#==============================================================================
import sqlite3 as oConexionSQLite

oArchivoDB = "F:\BBVA11SQLite\INVFINDesarrollo.bd"
oArchivoMM = ":memory:"

oCxn = oConexionSQLite.connect(oArchivoDB)
oCxnMM = oConexionSQLite.connect(oArchivoMM)
print("Dirección de conexion : ", oCxn)
print("Dirección de conexion Memory : ", oCxnMM)
print("Versión de la BD : ", oConexionSQLite.sqlite_version)