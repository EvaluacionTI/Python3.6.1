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

    cmdSQL = "UPDATE DIP.EVLt01_canal SET  cod_canal =:3, txt_abrv=:4, txt_desc=:5 WHERE id_canal =:6"
    oCursor.execute(cmdSQL, ('DA', 'SUNAD', 'ADUANAS', 5))
    print("Numero filas afectadas : ", str(oCursor.rowcount))

except(oFormatDB.DatabaseError):
    oCxn.rollback()
    print("Error : %s" % oFormatDB.DatabaseError)
finally:
    oCxn.commit()

oCxn.close()
