#==============================================================================
# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	PRE - Actualización de foto de predio del contribuyente
# Módulo			        :   Módulo de Predios
# Fecha	Creación	    :	2May2019
# Objetivo			        :   Lista data
#                                  :
# Procedimiento       :   Lista el primer registro
#
#
#==============================================================================
import cx_Oracle as oFormatDB

ipaddress = '127.0.0.1'
username = 'DIP'
password = 'Aemsa152027'
port = '1521'
sid = 'orcl'

oCxn = None
try:
    oCxn = oFormatDB.connect(username + '/' + password + '@' + ipaddress + ':' + port + '/' + sid, mode=oFormatDB.SYSDBA)
    print("Conexion realizada : ", oCxn)
    print("Version conexion realizada : ", oCxn.version)

    oCursor = oCxn.cursor()
    print("Cursor for execute command SQL : ", oCursor)
    oCursor.execute("SELECT * FROM DIP.EVLt01_canal ORDER BY id_canal")
    # Obtener el primer registro
    oRow_first = oCursor.fetchone()
    print("First record using fetchone : ", oRow_first)
    oCursor.execute("SELECT * FROM DIP.EVLt01_canal ORDER BY id_canal")
    # Obtener el primer registro y una posición de la columna esta inicia en 0
    oRow_first = oCursor.fetchone()[0]
    print("First record and column : ", oRow_first)
except(oFormatDB.DatabaseError):
    oCxn.rollback()
    print("Error : %s" % oFormatDB.DatabaseError)
finally:
    oCxn.commit()

oCxn.close()
