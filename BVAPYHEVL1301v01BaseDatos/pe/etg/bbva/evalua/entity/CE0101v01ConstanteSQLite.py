#==============================================================================
# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	PRE - Actualización de foto de predio del contribuyente
# Módulo			        :   Módulo de Predios
# Fecha	Creación	    :	16Abr2019
# Objetivo			        :   Conexion a SQLite
#                                  :
# Procedimiento       :
#
#
#==============================================================================


class CEConstanteSQLite:
    def __init__(self):
        self.ARCHIVO_DB = "F:\BBVA11SQLite\BBVARQUITECTURA.sqlite3"

        self.DROP_CONTRIBUYENTE = "DROP TABLE IF EXISTS PREt01_contribuyente"
        self.DROP_PREDIO = "DROP TABLE IF EXISTS PREt02_predio"
        self.DROP_PREDIO_FOTO = "DROP TABLE IF EXISTS PREt03_predio_foto"

        self.TABLE_CONTRIBUYENTE = '''
                CREATE TABLE PREt01_contribuyente(
                    id_contri                          INT,
                    cod_contri                       TEXT,
                    txt_nro_doc                     TEXT,
                    txt_ape_nom_contri       TEXT,
                    txt_direc_contri              TEXT,
                    txt_path_hr                      TEXT,
                    txt_path_hp                     TEXT,
                    fec_sis                              TEXT,
                    
                    CONSTRAINT PKPREt01_id_contribuyente PRIMARY KEY(id_contribuyente)
                );'''

        self.TABLE_PREDIO = '''
                CREATE TABLE PREt02_predio(
                    id_predio                           INT,
                    nro_periodo                      INT,
                    id_contri                           INT,            
                    cod_predio                       TEXT,
                    txt_direc_predio              TEXT,
                    txt_nro_lote_otro            TEXT,
                     sn_cargado                      INT,
                    fec_cargado                     TEXT,
                    fec_sis                              TEXT,
                    
                    CONSTRAINT PKPREt02_predio PRIMARY KEY(id_predio, nro_periodo),
                    CONSTRAINT FKPREt02_id_contribuyente FOREIGN KEY (id_contribuyente) REFERENCES PREt01_contribuyente (id_contribuyente) 
                );'''

        self.TABLE_PREDIO_FOTO = '''
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
                    
                    CONSTRAINT PKPREt03_predio_foto PRIMARY KEY(id_predio_foto, nro_periodo),
                    CONSTRAINT FKPREt03_predio           FOREIGN KEY (id_predio_foto,  nro_periodo) REFERENCES PREt02_predio (id_predio, nro_periodo)
                );'''


        self.DROP_VIEW_CONTRIBUYENTE = "PREVIEWContribuyente"
        self.DROP_VIEW_PREDIO = "PREVIEWContribuyentePredio"
        self.DROP_VIEW_PREDIO_FOTO = "PREVIEWContribuyenteFoto"

        self.VIEW_CONTRIBUYENTE = '''
                CREATE VIEW PREVIWContribuyente
                AS
                SELECT  tco.id_contribuyente AS IdContribuyente, tco.cod_contri AS CodigoContribuyente, tco.txt_nro_doc AS DocumentoIdentidad, txt_ape_nom_contri AS Contribuyente, txt_direc_contri AS DomicilioContribuyente 
                    FROM PREt01_contribuyente tco, 
                                PREt02_predio tpr 
                    WHERE tco.id_contribuyente = tpr.id_contribuyente
        '''

        self.SELECT_PREDIO_FOTO_ALL = "SELECT * PREt01_predio_foto "
        self.SELECT_PREDIO_FOTO_BY_ID = "SELECT * FROM PREt01_predio_foto WHERE id_predio_foto = ? AND nro_predio = ? "

        self.INSERT_PREDIO_FOTO = "INSERT INTO PREt01_predio_foto (id_predio_foto, nro_periodo, " \
                    "txt_path_foto1, txt_path_foto2, txt_path_foto3, img_path_foto1, img_path_foto2, img_path_foto3, " \
                    "txt_path_new_foto1, txt_path_new_foto2, txt_path_new_foto3, img_path_new_foto1, img_path_new_foto2, img_path_new_foto3," \
                    "sn_cargado, fec_cargado) VALUES (?, ?, ?, ?, ?,?, ?, ?, ?, ?,?, ?, ?, ?, ?,?)"

        self.UPDATE_PREDIO_FOTO = "UPDATE PREt01_predio_foto" \
                  " SET txt_path_new_foto1 = ?, txt_path_new_foto2 = ?, txt_path_new_foto3 = ?," \
                  "img_path_new_foto1 = ?, img_path_new_foto1 = ?, " \
                  "img_path_new_foto2 = ?, img_path_new_foto2 = ?, " \
                  "img_path_new_foto3 = ?, img_path_new_foto3 = ? WHERE id_predio_foto = ? AND nro_predio = ?"

        self.DELETE_PREDIO_FOTO = "DELETE FROM PREt01_predio_foto WHERE id_predio_foto=? AND nro_predio = ?"
