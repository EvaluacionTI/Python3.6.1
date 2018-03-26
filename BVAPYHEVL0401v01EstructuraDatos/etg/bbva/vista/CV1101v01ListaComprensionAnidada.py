#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	08Mar2018
# Periódo           :   08Mar/2018
# Objetivo			:	Lista de comprensión anidada
# Fecha Edición		:
# Descripción		:
#==============================================================================

aMatriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
print("1. Matriz ", aMatriz)

print("2. Transformando filas y columnas")
aResultado = [[fila[i] for fila in aMatriz] for i in range(4)]
print("Resultado = ", aResultado)

print("3. Matriz transpuesta")
transpuesta = []

for i in range(4):
    transpuesta.append([fila[i] for fila in aMatriz])

print("Resultado transpuesta : ", transpuesta)

print("4. Matriz transpuesta")
transpuesta = []
for i in range(4):
    fila_transpuesta = []
    for fila in aMatriz:
        fila_transpuesta.append(fila[i])
    transpuesta.append(fila_transpuesta)
print("Resultado forma 2 : ", transpuesta)

print("5. Funciones predefinidas")
print(list(zip(aMatriz)))