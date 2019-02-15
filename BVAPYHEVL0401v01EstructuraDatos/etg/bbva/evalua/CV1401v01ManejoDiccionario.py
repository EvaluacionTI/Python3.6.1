#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	13Mar2018
# Periódo           :
# Objetivo			:	Manejo de diccionarios
# Fecha Edición		:
# Descripción		:   Llamado vectores asociativos Estos funcionan como vecto
#                       res normales en los que los índices pueden ser cualquier
# tipo de objeto inmutable (números, cadenas y tuplas cuyos componentes sean
# inmutables).
#==============================================================================

aValores = {12345:'perro', 8373: 'gato', 747: 'león', 637:'elefante', 'leopardo' :'tigre benagala'}

print("1. Diccionarios")
print(aValores)

aValores['mery'] = "Reina"
print(aValores)

print("2. Lista de claves usadas en el diccionario")
print(list(aValores.keys()))

del aValores['leopardo']
print("3. Eliminar clave usada en el diccionario")
print(list(aValores.keys()))

print("4. Constructor de diccionario")
aDiccionario = dict([('sape',4139), ('guido',4127), ('jack',4098)])
print(aDiccionario)

print("5. Comprensiones de diccionarios se pueden usar para crear diccionarios")
aResultado = {x:x**2 for x in (2,4,6)}
print(aResultado)

print("6. Cuando las claves son cadenas simples, a veces resulta mas fácil especificar los pares usando argumentos por palabra clave")
aNuevoCadena = dict(illari=222014, mery=71967, esteban=52002)
print(aNuevoCadena)

print("7. Validar si existe una clave que no esta en el diccionario")
print(aValores.get('meryr',29))
print(aValores.get('747',1))
print(aValores.get('747'))
print(aValores.get(747))
