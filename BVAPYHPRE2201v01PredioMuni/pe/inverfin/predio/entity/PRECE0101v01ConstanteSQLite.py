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


class CEConstanteSQLite:
    ARCHIVO_DB = "F:\BBVA11SQLite\INVFINDesarrollo.bd"

    TABLE_CONTRIBUYENTE = '''
        CREATE TABLE PREt01_contribuyente(
            id_contribuyente            INT,
            cod_contribuyente         TEXT,
            txt_direccion_contri      TEXT,
            txt_path_hr                      TEXT,
            txt_path_hp                     TEXT,
            fec_sistema                     TEXT
    '''

    TABLE_PREDIO = '''
        CREATE TABLE PREt02_predio(
            id_predio_foto                 INT,
            nro_periodo                      INT,
            id_contribuyente             INT,            
            cod_predio                       TEXT,
            txt_direccion_predio      TEXT,
            txt_nro_lote_otro            TEXT,
             sn_cargado                      BOOLEAN,
            fec_cargado                     TEXT,
            fec_sistema                     TEXT            
    '''

    TABLE_PREDIO_FOTO = '''
        CREATE TABLE PREt03_predio_foto(
            id_predio_foto                 INT,
            nro_periodo                     INT,
            txt_path_foto1                TEXT,
            txt_path_foto2                TEXT,
            txt_path_foto3                TEXT,
            img_path_foto1               BLOB,
            img_path_foto2               BLOB,
            img_path_foto3               BLOB,
            txt_path_new_foto1        TEXT,
            txt_path_new_foto2        TEXT,
            txt_path_new_foto3        TEXT,
            img_path_new_foto1       BLOB,
            img_path_new_foto2       BLOB,
            img_path_new_foto3       BLOB,
            fec_sistema                       TEXT            
            
            CONSTRAINT PKPREt01_id_txt_periodo PRIMARY KEY(id_predio_foto, nro_periodo)
        )
    '''

    SELECT_PREDIO_FOTO_ALL = "SELECT * PREt01_predio_foto "
    SELECT_PREDIO_FOTO_BY_ID = "SELECT * FROM PREt01_predio_foto WHERE id_predio_foto = ? AND nro_predio = ? "

    INSERT_PREDIO_FOTO = "INSERT INTO PREt01_predio_foto (id_predio_foto, nro_periodo, " \
                    "txt_path_foto1, txt_path_foto2, txt_path_foto3, img_path_foto1, img_path_foto2, img_path_foto3, " \
                    "txt_path_new_foto1, txt_path_new_foto2, txt_path_new_foto3, img_path_new_foto1, img_path_new_foto2, img_path_new_foto3," \
                    "sn_cargado, fec_cargado) VALUES (?, ?, ?, ?, ?,?, ?, ?, ?, ?,?, ?, ?, ?, ?,?)"

    UPDATE_PREDIO_FOTO = "UPDATE PREt01_predio_foto" \
                  " SET txt_path_new_foto1 = ?, txt_path_new_foto2 = ?, txt_path_new_foto3 = ?," \
                  "img_path_new_foto1 = ?, img_path_new_foto1 = ?, " \
                  "img_path_new_foto2 = ?, img_path_new_foto2 = ?, " \
                  "img_path_new_foto3 = ?, img_path_new_foto3 = ? WHERE id_predio_foto = ? AND nro_predio = ?"

    DELETE_PREDIO_FOTO = "DELETE FROM PREt01_predio_foto WHERE id_predio_foto=? AND nro_predio = ?"
