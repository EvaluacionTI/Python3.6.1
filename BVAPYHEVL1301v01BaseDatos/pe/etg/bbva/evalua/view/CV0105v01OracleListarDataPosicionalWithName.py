#==============================================================================
# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	EVL - Evaluación de Python3
# Módulo			        :   Base de Datos
# Fecha	Creación	    :	06May2019
# Objetivo			        :   Lista data
#                                  :
# Procedimiento       :   Listar en forma posicional por nombres
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
    # El codigo e iden indican la posición que se ubican para la ejecución de los valores siguinetes que se ingresan
    oCursor.execute("SELECT * FROM DIP.EVLt01_canal WHERE cod_canal=:codigo AND id_canal=:iden", {'codigo':"XA", 'iden':4})

    oRow_found = oCursor.fetchall()
    print("Mostrar  : ", oRow_found)
except(oFormatDB.DatabaseError):
    oCxn.rollback()
    print("Error : %s" % oFormatDB.DatabaseError)
finally:
    oCxn.commit()

oCxn.close()
