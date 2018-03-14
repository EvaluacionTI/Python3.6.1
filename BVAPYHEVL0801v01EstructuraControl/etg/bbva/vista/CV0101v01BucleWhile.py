#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	14Mar2018
# Periódo           :   14Mar/2018
# Objetivo			:	Bucle
# Fecha Edición		:
# Descripción		:   While
#==============================================================================
print("1. While simple forma 1")
a = 10
while(a <= 8):
    print("a = ", a)
    a = a + 1

print("2. While forma 2")
a, b = 0, 1
while(b <= 8):
    print("a = ", a, "b = ", b)
    a,b= b, a+b

print("3. While format 3 con range")
a = range(30)
while(a):
    print("a = ", a)
    print("a = ", a[-1])
    del a[-1]
print("a = ", a)

