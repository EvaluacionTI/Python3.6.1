#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	06Mar2018
# Periódo           :   06Mar/2018
# Objetivo			:	Otras expresiones de listas
# Fecha Edición		:
# Descripción		:   Otras expresiones de listass
#==============================================================================
from math import pi

vec = [-4, -2, 0, 2, 4]
print("1. Lista inicial", vec)

vec = [x * 2 for x in vec]
print("2. Lista duplicados = ", vec)

filtro = [x for x in vec if x >= 0]
print("3. Lista filtro = ", filtro)

aplicaFuncion = [abs(x) for x in vec]
print("4. Aplica función abs(x) a todos los elementos = ", aplicaFuncion)

fruta = ['  banana', '  mora de logan  ',  'maracuya   ']
print("5. Lista de frutas = ", fruta)
aplicaMetodo = [arma.strip() for arma in fruta]
print("Llama un método strip() a cada elemento = ", aplicaMetodo)

print("6. Lista de tuplas de dos como (numero, cuadrado)")
listaTupla = [(z, z**2) for z in range(30)]
print("La tupla entre paréntesis = ", listaTupla)

print("7. Aplanar una lista usando comprensión de listas con dos for")
lineal = [[1,2,3,4,5], [21,22,23,24,25], [15, 17, 20, 17]]
aplanar = [num for elem in lineal for num in elem]
print("Lineal = ", lineal)
print("Aplanar = ", aplanar)

print("8. Expresiones complejas y funciones anidadas")
# Generar hasta 16 decimales con la expresión
complejo = [str(round(pi, i)) for i in range(1,16)]
print("Complejo = ", complejo)