#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	19Abr2018
# Periódo           :   19Abr/2018
# Objetivo			:	Import zlib, gzip, bz2, lzma, zipfile, y tarfile
# Fecha Edición		:
# Descripción		:   Import zlib, gzip, bz2, lzma, zipfile, y tarfile
#==============================================================================
import zlib

sCadena='Arquitectura Host'
longitud=len(sCadena)
print(sCadena, " tiene la longitud = ", longitud)

comprimir = zlib.compress(sCadena,2)

sCadena1 = zlib.decompress(comprimir)
print(sCadena1)

sCadena2 = zlib.crc32(sCadena)
#longitud=len(t)
#print(t, " tiene la longitud = ", longitud)