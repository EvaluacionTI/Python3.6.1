#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	28Mar2018
# Periódo           :   28Mar/2018
# Objetivo			:	Import json
# Fecha Edición		:
# Descripción		:   JSON (Javascript Object Notation) permite convertir
#                       a representación de caracteres, es proceso se llama
# serializing. Reconstruir los datos desde la representación de cadena de
# caracteres es llamado deserializing.
# El formato JSON es utilizado para intercambiar datos.
#==============================================================================
import json

aVector = [1, 'Deuda', 'CTS']
print("Vector = ", json.dumps(aVector))
with open('serializar.json', 'w') as fp:
    json.dump(aVector, fp)

with open('serializar.json', 'r') as fp:
    resultado = json.load(fp)

print(resultado)