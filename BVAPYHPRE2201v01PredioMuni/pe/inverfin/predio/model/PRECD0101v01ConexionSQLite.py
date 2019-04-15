#==============================================================================
# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	PRE - Actualización de foto de predio del contribuyente
# Módulo			        :   Módulo de Predios
# Fecha	Creación	    :	15Abr2019
# Objetivo			        :   Conexion a SQLite
#                                  :
# Procedimiento       :
#
#
#==============================================================================
import sqlite3 as oFormatSQLite
import pe.inverfin.predio.entity.PRECE0101v01ConstanteSQLite as oFormatConstante

class CDDatabaseSQLite:

#    db = 'F:\BBVA11SQLite\INVFINDesarrollo.bd'

    def __init__(self):
        self.connection = oFormatSQLite.connect(oFormatConstante.CEConstanteSQLite.ARCHIVO_DB)
        self.cursor = self.connection.cursor()

    def insert_predio(self):
        try:
            self.cursor.execute(oFormatConstante.CEConstanteSQLite.INSERT_PREDIO)
            self.connection.commit()
        except:
            self.connection.rollback()
    
    def abm_table(self, pSQLQuery):
        try:
            self.cursor.execute(pSQLQuery)
            self.connection.commit()
        except:
            self.connection.rollback()

    def query_by_all(self, pSQLQuery):
        cursor = self.connection.cursor( oFormatSQLite.cursors.DictCursor )
        cursor.execute(pSQLQuery)

        return cursor.fetchall()

    def __del__(self):
        self.connection.close()


if __name__ == "__main__":

    db = CDDatabaseSQLite()