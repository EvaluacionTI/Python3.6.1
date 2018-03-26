#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	26Feb2018
# Objetivo			:	Palabra clave como argumento de
# Fecha Edición		:
# Descripción		:   Cuando un parámetro formal de la forma **nombre está
#                       presente al final
#==============================================================================

def ventaDeQueso(tipo, *argumentos, **palabrasclave):
    print("1. Tiene tipo", tipo)
    print("2. Lo siento nos quedamos sin tipo", tipo)
    for arg in argumentos:
        print (arg)

    print("="*80)
    claves = sorted(palabrasclave.keys())
    for c in claves:
        print(c, " : ", palabrasclave[c])

ventaDeQueso('Serrano', "Es muy suave y saladito", "Hay sin sal", Cliente="Esteban", Vendedor="Alex", Puesto="El Ancashino")