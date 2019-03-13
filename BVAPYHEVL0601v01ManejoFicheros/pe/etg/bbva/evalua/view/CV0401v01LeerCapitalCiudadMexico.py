#==============================================================================
# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	EVL (Evaluación de Python 3.6.1.)
# Módulo			        :   Manejo de Ficheros
# Fecha	Creación	    :	11Mar2019
# Objetivo			        :	Apertura de archivo y mostrarlo en lista ordenado
# Descripción		    :   Lectura de las capitales de la Ciudad de Mexico.
#==============================================================================


oarchivo = open("capitalCiudadMexico.txt")
print ("Open Archivo : ", oarchivo)

odatos = oarchivo.read()
print("Leer Datos : ", odatos)

# Partimos la cadena a una lista cuyos elementos son
# los registros de nuestra 'base de datos'
lista = odatos.split()
print("Convertir a Lista : ", lista)

# Convertimos cada elemento de la lista a una pareja,
# usamos una función lambda:

pares_clave_valor = map(lambda e: odatos.split(e, ','), lista)
#nuevalista = list(pares_clave_valor)
print("Pares clave valor: ", pares_clave_valor)
#print("Pares clave valor: ", nuevalista)

# Podemos crear una lista para cada campo:
# una lista de capitales y otra lista de estados.
# Esta es una forma de obtenerlas:
capitales = []
estados = []

#for capital in pares_clave_valor:
#    print(capital)
#    for it in capital:
#        print(capital)
##    capitales.append(capital)
#    estados.append(estado)

#print("Capitales : ", capitales)
#print("Estadio    :  ", estado)

# Cómo determinar los nombres únicos de ambas listas?
# Usamos la concatenación de listas.

#unicos = []
#for nombre in capitales + estados:
#    if nombre not in unicos:
#        unicos.append()
 #   else:
#        print("Nombre : ", nombre)

# cuantos elementos tenemos
#print("Numero elementos : ", len(unicos))

# Los ordenamos alfabeticamente
#unicos.sort()
#print("Ordenados alfabéticamente : ", unicos)