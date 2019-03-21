#==============================================================================
# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	EVL (Evaluación de Python 3.6.1.)
# Módulo			        :   Manejo de Ficheros
# Fecha	Creación	    :	11Mar2019 / 21Mar2019
# Objetivo			        :   Lectura de datos en una matriz
# Descripción		    :   Abrir y leer los datos con salto de linea
#                                      Quitar el salto de linea de la lectura de datos, utilizando strip
# Convertir la cadena en una lista de datos, previo retirar la coma como separador
# Adicionar a una lista de datos
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
        print(" Fila leida  : ", orow_record)
        cadena_sin_salto = quitar_salto_linea(orow_record)
        lista_sin_coma = retirar_coma(cadena_sin_salto)
        print(" Quitar salto  : ", cadena_sin_salto)
        print(" Lista sin coma  ' : ", lista_sin_coma)
        matriz.append(lista_sin_coma)
    print(" Matriz devuelta  ' : ", matriz)

    return matriz


def cerrar_archivo(poarchivo):
    poarchivo.close()


def quitar_salto_linea(cadena_evaluar):
    return cadena_evaluar.strip()


def retirar_coma(cadena_evaluar):
    return cadena_evaluar.split(',')


def principal():
    print(".-"*80)
    print("1. Abrir archivo de texto y leer los datos \n")
    oarchivo = abrir_archivo_texto(archivo_texto)
    print(".-"*80)

    matriz_pais = leer_datos(oarchivo)
    print("Matriz de paises", matriz_pais)
    for renglon in matriz_pais:
        for celda in renglon:
            print ('%20s' %celda)
    cerrar_archivo(oarchivo)


principal()
