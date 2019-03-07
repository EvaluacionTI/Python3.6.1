#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	22Mar2018
# Periódo           :   22Mar/2018
# Objetivo			:	Funciones pre definidas
# Fecha Edición		:
# Descripción		:   Funciones pre definidas
#==============================================================================
import math

def funcionesCadena():
    print("1. Valor absoluto : ", abs(-22))
    print("2. Devuelve una cadena con la representación hexadecimal del entero 17 : ", hex(17))
    print("3. Devuelve una cadena con la representación octal del entero 17 : ", oct(17))
    print("4. Devuelve la longitud de la secuencia : ", len("Arquitectura"))
    print("5. Devuelve el máximo de una secuencia : ", max("Arquitectura"))
    print("6. Devuelve el mínimo de una secuencia : ", min("Arquitectura"))
    print("7. Devuelve representaciones legibles ", str("Arquitectura"))
    print("1/7 = ", str(1/7))
    print("8. Genera representaciones leibles por el interpre evalua ", repr("Arquitectura"))
    x = 10 * 3.25;
    y = 200 * 200;
    s = "El valor de x es " + repr(x) + ', y es ' + repr(y) + '...'
    print(s)

def funcionesMatematicas():
    print("1. Valor ascii :", chr(65))
    print("2. Código ascii :", ord('u'))
    print("3. Evalua s interpretandola como expresión Python : ", eval("chr"))
    print("4. Convierte un número entero a flotante : ", float(15))
    print("5. Convierte un número entero o cadena a entero : ", int('15'))
    print("6. Convierte un número entero o cadena a entero largo: ", int('20120105'))
    print("7. La potencia de un número : ", pow(5, 22))
    print("8. Seno de una ángulo : ", math.sin(10))

def principal():
    print("=" *80)
    funcionesCadena()
    print("=" * 80)
    funcionesMatematicas()


principal()