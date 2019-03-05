#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	07Mar2018
# Periódo           :   07Mar/2018
# Objetivo			:	Sub secuencias con listas
# Fecha Edición		:
# Descripción		:
#==============================================================================
print("1. Posiciones de las listas")
aListaNumeros = [15, 17, 20, 27, 5, 22, 30]
print("Posición general = ", aListaNumeros)
print("Posición [2:4]   = ", aListaNumeros[2:4])

print("2. Asignando números a listas o subsecuencia de listas")
aListaNumeros[2:4] = [2002, 2014, 2017]
print("Numeros asignados ", aListaNumeros);

print("3.Operaciones en las listas +, * y len()");
print("Sumar = ", aListaNumeros + aListaNumeros)
print("Multiplicar = ", aListaNumeros * 4)
print("Longitud = ", len(aListaNumeros))

print("4. Elementos de las listas puedens ser listas")
print("Lista inicial : ", aListaNumeros)
aNuevaLista = [aListaNumeros, aListaNumeros + [5]]
print("Nueva lista : ", aNuevaLista)
aNuevaLista[1][2] = [2, 1, 2018]
print("Nueva lista : ", aNuevaLista)
aNuevaLista[1][0] = [[], [3,2], 30, 7, 2017]
print("Nueva lista : ", aNuevaLista)

print("5. Asignar un objeto compuesto a una variable")
print("Objeto compuesto : ", aListaNumeros)
aNuevaAsignacion = aListaNumeros
print("Nueva asignación : ", aNuevaAsignacion)
aNuevaAsignacion[2] = 1
print("Nueva Reasignación, reemplaza el valor de la posición : ", aNuevaAsignacion)

print("6. Asignar un objeto mayores")
print("Objeto compuesto : ", aListaNumeros)
aObjetoMayor = [aListaNumeros, aListaNumeros]
print("Objeto mayor : ", aObjetoMayor)

print("7. Asignar un objeto mayores 2")
aListaNumeros = [1,2]
aObjetoMayor = [aListaNumeros, aListaNumeros]
print("Objeto aListaNumeros: ", aListaNumeros)
print("Objeto mayor asignado: ", aObjetoMayor)

print("8. Asignar un objeto mayores 3")
aListaNumeros = [3]
#aObjetoMayor = [aListaNumeros, aListaNumeros]
print("Objeto aListaNumeros asignado con [3]: ", aListaNumeros)
print("Objeto mayor queda con el valor asignado : ", aObjetoMayor)