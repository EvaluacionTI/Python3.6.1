#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	16Abr2018
# Periódo           :   16Abr/2018
# Objetivo			:	Import urllib
# Fecha Edición		:
# Descripción		:   Modulo para acceder a internet y procesar sus
#                       protocolos. Uno simple es urllib.request
#==============================================================================
import urllib.request

with urllib.request.urlopen('http://view.org/') as response:
   html = response.read()
   print(html)

print("=" *80)
sUrl = 'http://www.claro.com.pe'
with urllib.request.urlopen(sUrl) as response:
    for line in response:
        line = line.decode('UTF-8')
        if 'EST' in line or 'EDT' in line:
            print(line)

