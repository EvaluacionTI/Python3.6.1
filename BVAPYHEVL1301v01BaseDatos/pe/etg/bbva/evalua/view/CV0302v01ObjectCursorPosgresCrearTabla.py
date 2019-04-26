#==============================================================================
# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	Evaluation de Python
# Módulo			        :   Base de Datos
# Fecha	Creación	    :	26Abr2019
# Objetivo			        :   Conexion a Postgres
#                                  :
# Procedimiento       :   El objeto cursor se utiliza para obtener, insertar, actualizar o borrar datos de
#                                      nuestra base de datos.
#
#
#==============================================================================
import psycopg2 as oFormatDBPg2

oArchivoDB = "F:\BBVA11SQLite\BBVARQUITECTURA.sqlite3"
TABLE_EMPLEADO = '''
    CREATE TABLE EVLt01_empleado(
        id                 INT PRIMARY KEY,
        txt_nom     TEXT    NOT NULL,
        edad            INT      NOT NULL,
        txt_dir         VARCHAR(50)  NOT NULL,
        salario         REAL)
'''
oCxn = None
try:
    oCxn = oFormatDBPg2.connect(database="bbvarquitectura", user="postgres", password="aemsa152027")
    print("Conexion realizada : ", oCxn)
    oCursor = oCxn.cursor()
    print("Cursos habilitado : ", oCursor)
    oCursor.execute(TABLE_EMPLEADO)
except(oFormatDBPg2.DatabaseError):
    oCxn.rollback()
    print("Error %s" % oFormatDBPg2.DatabaseError)
finally:
    oCxn.commit()
    oCxn.close()

