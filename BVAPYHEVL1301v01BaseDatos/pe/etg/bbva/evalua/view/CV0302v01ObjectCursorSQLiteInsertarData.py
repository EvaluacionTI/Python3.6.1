#==============================================================================
# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	PRE - Actualización de foto de predio del contribuyente
# Módulo			        :   Módulo de Predios
# Fecha	Creación	    :	15Abr2019
# Objetivo			        :   Conexion a SQLite
#                                  :
# Procedimiento       :   El objeto cursor para insertar datos en la tabla
#
#
#==============================================================================
import sqlite3 as oConexionSQLite

oArchivoDB = "F:\BBVA11SQLite\INVFINDesarrollo.bd"
INSERT01_PREDIO = "INSERT INTO PREt01_empresa (id, txt_nom, edad, txt_dir, salario) VALUES (1, 'Esteban', 17, 'Zarate', 100)"
INSERT02_PREDIO = "INSERT INTO PREt01_empresa (id, txt_nom, edad, txt_dir, salario) VALUES (2, 'Illari', 5, 'Cañete', 100)"
INSERT03_PREDIO = "INSERT INTO PREt01_empresa (id, txt_nom, edad, txt_dir, salario) VALUES (3, 'Alexei', 2, '15 Enero', 100)"
INSERT04_PREDIO = "INSERT INTO PREt01_empresa (id, txt_nom, edad, txt_dir, salario) VALUES (4, 'Sayrik', 1, 'Mala', 100)"


oCxn = oConexionSQLite.connect(oArchivoDB)
print("Dirección de conexion : ", oCxn)

oCursor = oCxn.cursor()
oCursor.execute(INSERT01_PREDIO)
oCursor.execute(INSERT02_PREDIO)
oCursor.execute(INSERT03_PREDIO)
oCursor.execute(INSERT04_PREDIO)
oCxn.commit()
oCxn.close()