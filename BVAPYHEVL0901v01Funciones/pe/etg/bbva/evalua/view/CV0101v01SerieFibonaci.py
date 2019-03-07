#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	19Mar2018
# Periódo           :   19Mar/2018
# Objetivo			:	Manejo de funciones
# Fecha Edición		:
# Descripción		:   Serie de Fibonaci
#==============================================================================

m, n = 2,3
print("1. Asignación y Declaración de m, n", m, n)


def revisarVaraibleGlobal():
    global m
    print("2. Declaracion global ", m)
    m, n = 4, 4
    print("3. Asignacion de m, n ", m, n)


def fibonaci(pNumero):
    a,b = 0,1
    print("1. Fibo: inicializar variable a, b", a, b)
    aResultado = []
    while( b < pNumero):
        aResultado.append(b)
        a,b = b,a+b
        print("2. Fibo: nueva asignación a, b", a, b)
    return aResultado


def principal():
    revisarVaraibleGlobal()
    print("4. Asignación final ", m, n)
    print("Lista fibonaci", fibonaci(100))


principal()


