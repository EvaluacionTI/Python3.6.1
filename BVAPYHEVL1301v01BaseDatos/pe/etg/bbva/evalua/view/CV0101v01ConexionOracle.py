#==============================================================================
# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	EVL - Evaluacion
# Módulo			        :   Base de datos
# Fecha	Creación	    :	26Abr2019
# Objetivo			        :   Conexion a Oracle
#                                  :
# Procedimiento       :   Evaluation conexion a Oracle
#
#
#==============================================================================
import cx_Oracle as oFormatDB

ipaddress = '127.0.0.1'
username = 'sys'
password = 'aemsa152027'
port = '1521'
sid = 'orcl'

oCxn = None
try:
    oCxn = oFormatDB.connect(username + '/' + password + '@' + ipaddress + ':' + port + '/' + sid, mode=oFormatDB.SYSDBA)

    print("Conexion realizada : ", oCxn)
except(oFormatDB.DatabaseError):
    print("Error %s" % oFormatDB.DatabaseError)
finally:
    oCxn.close()