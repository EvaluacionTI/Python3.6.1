#==============================================================================
# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	EVL - Evaluación de Python3
# Módulo			        :   Base de Datos
# Fecha	Creación	    :	06May2019
# Objetivo			        :   Insertar
#                                  :
# Procedimiento       :   Insertar información many forma I
#                                      cuando desea insertar varias filas, ejecutando varios comandos insert es
# ineficiente y hace varios viajes a la base de datos
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

    cmdSQL = "DELETE FROM DIP.EVLt01_canal WHERE id_canal =:iden_canal"
    oCursor.execute(cmdSQL, {'iden_canal':6})
    print("Numero filas afectadas : ", str(oCursor.rowcount))

except(oFormatDB.DatabaseError):
    oCxn.rollback()
    print("Error : %s" % oFormatDB.DatabaseError)
finally:
    oCxn.commit()

oCxn.close()
