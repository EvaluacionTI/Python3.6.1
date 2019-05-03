#==============================================================================
# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	PRE - Actualización de foto de predio del contribuyente
# Módulo			        :   Módulo de Predios
# Fecha	Creación	    :	03May2019
# Objetivo			        :   Lista data
#                                  :
# Procedimiento       :   Listar en forma posicional las data
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
    # El valor :1 y :2 indican la posición que se ubican para la ejecución de los valores siguinetes que se ingresan
    oCursor.execute("SELECT * FROM DIP.EVLt01_canal WHERE cod_canal=:1 AND id_canal=:2", ("XA", 4))

    oRow_found = oCursor.fetchall()
    print("Mostrar  : ", oRow_found)
except(oFormatDB.DatabaseError):
    oCxn.rollback()
    print("Error : %s" % oFormatDB.DatabaseError)
finally:
    oCxn.commit()

oCxn.close()
