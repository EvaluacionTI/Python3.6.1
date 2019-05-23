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

oArchivoDB = "F:\BBVA11SQLite\BBVARQUITECTURA.sqlite3"
INSERT01_PREDIO = "INSERT INTO EVLt02_empleado (id, txt_nom, edad, txt_dir, salario) VALUES (1, 'Esteban', 17, 'Zarate', 100)"
INSERT02_PREDIO = "INSERT INTO EVLt02_empleado (id, txt_nom, edad, txt_dir, salario) VALUES (2, 'Illari', 5, 'Cañete', 100)"
INSERT03_PREDIO = "INSERT INTO EVLt02_empleado (id, txt_nom, edad, txt_dir, salario) VALUES (3, 'Alexei', 2, '15 Enero', 100)"
INSERT04_PREDIO = "INSERT INTO EVLt02_empleado (id, txt_nom, edad, txt_dir, salario) VALUES (4, 'Sayrik', 1, 'Mala', 100)"
INSERT05_PREDIO = "INSERT INTO EVLt02_empleado (id, txt_nom, edad, txt_dir, salario) VALUES (5, 'Elizabeth Bobadilla', 1, 'Mala Bravo Chico', 10000.00)"

oCxn = oConexionSQLite.connect(oArchivoDB)
print("Dirección de conexion : ", oCxn)

oCursor = oCxn.cursor()
oCursor.execute(INSERT01_PREDIO)
oCursor.execute(INSERT02_PREDIO)
oCursor.execute(INSERT03_PREDIO)
oCursor.execute(INSERT04_PREDIO)
oCursor.execute(INSERT05_PREDIO)
oCxn.commit()
oCxn.close()