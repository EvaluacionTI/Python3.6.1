#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	20Abr2018
# Periódo           :   20Abr/2018
# Objetivo			:
# Fecha Edición		:
# Descripción		:
#==============================================================================

def primero():
    print("'\\/\"")
    print('\'\\/"')
    print("=" *80)

def segundo():
    sCadena = "Arquitectura de Servicios"
    print("Original = ", sCadena)
    print("Estructura definida = sCadena[8:] + sCadena[4:8] + sCadena[:4]")
    print(sCadena[8:] + sCadena[4:8] + sCadena[:4])
    print("=" * 80)

def tercero():
    lista=[1, [2, [3,4]]]
    print("Lista = ", lista)
    lista[1]=lista[1]+[[6,7]]
    print("Lista = ", lista)
    print("=" * 80)

def cuarto():
    listaB=[1,2]
    print("Lista B = ", listaB)
    listaC=[listaB, listaB]
    print("Lista C = ", listaC)
    listaB=[3]
    print("Lista B =", listaB)
    listaC[0].append(7)
    print("Lista C :", listaC)
    print("=" *80)


def quinto():
    lista=[]
    i=1
    print("Con while")
    while (i<=10):
        lista.append(i)
        i+=1
    print("Lista con while = ", lista)
    print("Con for")

    for i in range(10):
        lista.append(i*i)
    print("Lista con for = ", lista)
    lista1=range(1,1001)
    for i in lista1:
        if (i%7)==0:
            print("Lista con range ", i)

    print("=" *80)

def principal():
    primero()
    segundo()
    tercero()
    cuarto()
    quinto()

principal()
