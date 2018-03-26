#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	15Mar2018
# Periódo           :   15Mar/2018
# Objetivo			:	Bucle
# Fecha Edición		:
# Descripción		:   For
#==============================================================================

print("1. Forma 1 de for")
for i in "Disciplina PAAS":
    print("%s" %i)

print("2. Forma 2 de for con una lista")
aLista = ["Banco", "Continental", 'Arquitectura Host', 'Arquitectura Distribuido']
for i in aLista:
    print(i)

print("3. Forma 3 con range (n) - lista hasta n-1")
print("Rango de : ", range(5))
for i in range(5):
    print(i)

print("4. Forma 4 con range (n,m) - lista desde n hasta m-1")
print("Rango de : ", range(5,30))
for i in range(5,30):
    print(i)

print("4. Forma 4 con range (n,m,j) - lista desde n hasta m-1 con saltos de j")
print("Rango de : ", range(5,30, 22))
for i in range(5,30, 22):
    print(i)

print("Rango de : ", range(3,9, -4))
for i in range(3,9,-4):
    print(i)

print("Rango de : ", range(9,3,-4))
for i in range(9,3,-4):
    print(i)


print("5. Forma 5 elemento con el índice")
sNombre = "Banco Continental"
print("Posición, Dato")
for pos, c in enumerate(sNombre):
    print(pos, c)
