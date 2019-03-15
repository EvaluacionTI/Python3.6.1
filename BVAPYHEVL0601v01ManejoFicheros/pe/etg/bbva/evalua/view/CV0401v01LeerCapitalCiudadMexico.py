#==============================================================================
# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	EVL (Evaluación de Python 3.6.1.)
# Módulo			        :   Manejo de Ficheros
# Fecha	Creación	    :	11Mar2019
# Objetivo			        :	Apertura de archivo y mostrarlo en lista ordenado
# Descripción		    :   Lectura de las capitales de la Ciudad de Mexico.
#==============================================================================

archivo_texto = 'CV0401v01CapitalCiudadMexico.txt'
list_capitales = []
list_estados = []
list_unicos = []


def abrir_archivo_texto(parchivo):
    oarchivo = open(parchivo)
    print ("1. Open Archivo : ", oarchivo)
    return oarchivo


def leer_datos(poarchivo):
    odatos = poarchivo.read()
    print("2. Lectura y Datos : \n", odatos )
    return odatos


def quitar_coma(pCaracter):
    return pCaracter.split(',')


def nombre_unico_de_listas():
    for nombre in list_capitales + list_estados:
        if nombre not in list_unicos:
            list_unicos.append(nombre)
        else:
            print("Nombre igual : ", nombre)

    print(".-" * 80)
    print("Lista de unicos   : ", list_unicos)
    print("Cantidad unicos : ", list_unicos.__len__())


def principal():
    oarchivo = abrir_archivo_texto(archivo_texto)
    odata = leer_datos(oarchivo)
    print(".-"*80)

    print("3. Convertimos los datos a lista identificando el separador \n")
    print("Quitar el cambio de linea")
    lista_data = odata.split('\n')
    print("Lista de datos : ", lista_data)
    print(".-"*80)

    print("4. Convertimos cada elemento de la lista a una pareja, usamos una función lambda: ")
    # pares_clave_valor = map(lambda e: odata.split(e, ','), lista_data)
    pares_clave_valor = map(quitar_coma, lista_data)
    list_final_map = list(pares_clave_valor)

    print("Map iterable : ", pares_clave_valor)
    print("Lista iterable : ", list_final_map)
    print(".-"*80)

    print("5. Lista de capitales y estado")
    print("Lista final de map : ", list_final_map)
    for capital, estado in list_final_map:
          list_capitales.append(capital)
          list_estados.append(estado)
    print("Lista de capitales : ", list_capitales)
    print("Lista de estados    : ", list_estados)
    print(".-" * 80)
    nombre_unico_de_listas()


principal()
