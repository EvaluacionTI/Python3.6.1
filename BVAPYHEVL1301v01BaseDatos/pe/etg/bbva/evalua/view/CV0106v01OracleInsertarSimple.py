#==============================================================================
# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	EVL - Evaluación de Python3
# Módulo			        :   Base de Datos
# Fecha	Creación	    :	06May2019
# Objetivo			        :   Insertar
#                                  :
# Procedimiento       :   Insertar información
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
    cmdSQL = "INSERT INTO DIP.EVLt01_canal (id_canal, cod_canal, txt_abrv, txt_desc) VALUES (:2, :3, :4, :5)"
    oCursor.execute(cmdSQL, (5, 'AD', 'ADUANAS', 'SUNAD'))
    print("Mostrar  : ", oCursor)

except(oFormatDB.DatabaseError):
    oCxn.rollback()
    print("Error : %s" % oFormatDB.DatabaseError)
finally:
    oCxn.commit()

oCxn.close()
