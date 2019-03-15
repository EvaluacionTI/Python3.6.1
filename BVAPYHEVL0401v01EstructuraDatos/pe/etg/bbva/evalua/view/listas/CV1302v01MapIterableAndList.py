#==============================================================================
# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	EVL (Evaluación de Python 3.6.1.)
# Módulo			        :   Mapear
# Fecha	Creación	    :	14Mar2019
# Objetivo			        :	Revision del operador Map
# Descripción		    :   El operador Map, toma una función y un iterable como argumentos, y
#                                      devuelve un nuevo iterable con la función aplicada a cada argumento
#==============================================================================


numeros = [15, 17, 20, 27]
lista_provincia_distrito = ['Lima,San Luis', 'Ancash,Cabana', 'Ancash,Pallasca', 'Ancash,Tauca', 'Lima,San Borja']


def add_numero(pNumero):
    return pNumero + 5


def quitar_coma(pCaracter):
    return pCaracter.split(',')


def map_numeros():
    resultado_map = map(add_numero,  numeros)
    resultado_list = list(map(add_numero, numeros))
    print("Lista numertos      : ", numeros)
    print("Conversión a Map : ", resultado_map)
    print("Resultado en list   : ", list(resultado_map))
    print("Resultado a List     : ", resultado_list)
    print('.-'*80)
    print("Valores de la lista")
    for valor in resultado_list:
        print(valor)
    print('.-'*80)


def map_cadenas():
    resultado_map_cadena = map(quitar_coma, lista_provincia_distrito)
    resultado_list_cadena = list(resultado_map_cadena)
    print("Iterable map cadena  : ", resultado_map_cadena)
    print("Lista de cadenas         : ", resultado_list_cadena)
    print('.-' * 80)
    print("Valores de la lista")
    for valor in resultado_list_cadena:
        print(valor)
    print('.-' * 80)


def principal():
    map_numeros()
    map_cadenas()


principal()

