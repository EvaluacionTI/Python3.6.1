#==============================================================================
# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	EVL (Evaluación de Python 3.6.1.)
# Módulo			        :   Manejo de Ficheros
# Fecha	Creación	    :	11Mar2019
# Objetivo			        :	Apertura de archivo y mostrarlo en lista ordenado
# Descripción		    :   Lectura de las capitales de la Ciudad de Mexico.
#==============================================================================

archivo_texto = 'CV0401v01CapitalCiudadMexico.txt'
matriz = []


def abrir_archivo_texto(parchivo):
    oarchivo = open(parchivo, "r")
    print(" Open Archivo : ", oarchivo)
    return oarchivo


# Lectura de datos con readline
def leer_datos(poarchivo):
    for orow_record in poarchivo.readlines():
        lista_fila = convertir_lista(orow_record)
        matriz.append(lista_fila)
        print(" Fila leida  : ", orow_record)
        print(" Fila convertida a map  ' : ", lista_fila)
    print(" Matriz devuelta  ' : ", matriz)

    return matriz


def cerrar_archivo(poarchivo):
    poarchivo.close()


def quitar_coma(pCaracter):
    return pCaracter.split(',')


def convertir_lista(podata):
    lista_data = list(map(quitar_coma, podata))
    return lista_data


def principal():
    print(".-"*80)
    print("1. Abrir archivo de texto y leer los datos \n")
    oarchivo = abrir_archivo_texto(archivo_texto)
    print(".-"*80)

    matriz_pais = leer_datos(oarchivo)
#    for renglon in matriz_pais:
 #       for celda in renglon:
  #          print ('%20s' %celda)


principal()
