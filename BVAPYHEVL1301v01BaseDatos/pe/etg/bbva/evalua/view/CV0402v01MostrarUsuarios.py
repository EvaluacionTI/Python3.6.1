#==============================================================================
# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	PRE - Actualización de foto de predio del contribuyente
# Módulo			        :   Módulo de Predios
# Fecha	Creación	    :	15Abr2019
# Objetivo			        :   Conexion a SQLite
#                                  :
# Procedimiento       :   El objeto cursor se utiliza para obtener, insertar, actualizar o borrar datos de
#                                      nuestra base de datos.
#
#
#==============================================================================
import psycopg2 as oFormatDBPg2


oCxn = None
try:
    oCxn = oFormatDBPg2.connect(database="bbvarquitectura", user="postgres", password="aemsa152027")
    print("Conexion realizada", oCxn)
    oCursor = oCxn.cursor()
    print("Objeto cursor ", oCursor)
    oCursor.execute("SELECT * FROM EVLt01_compra")

    for id_compra, txt_nombre in oCursor.fetchall():
        print (id_compra, txt_nombre)

except(psycopg2.DatabaseError):
    print("Error %s" % psycopg2.DatabaseError)
finally:
    oCxn.close()