#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	26Feb2018
# Objetivo			:	Palabra clave como argumento de
# Fecha Edición		:
# Descripción		:   Las funciones también puedes ser llamadas usando
#                       argumentos de palabras clave (o argumentos nombrados)
#                       de la forma keyword = value.
#==============================================================================
# Acepta un argumento obligatorio y tres agumentos opcionales
def voltaje (tension, estado = "muerto", accion='explotar', tipo='Azul Nórdico'):
    print("1. Este loro no va a ", accion, end= ' ')
    print("2. Si le aplicas ", tension, " voltios.")
    print("3. Gran plumaje tiene el ", tipo)
    print("4. Estado", estado)

print("Llamadas válidas")
print("=" *80)
voltaje(1000)
print("=" *80)
voltaje(tension=1000)
print("=" *80)
voltaje(tension=1000, accion="iniciar")
print("=" *80)
voltaje(accion="iniciar", tension=1000)
print("=" *80)
voltaje("un millon", 'despojado de vida', 'saltar')
print("=" *80)
voltaje('mil', estado = 'viendo crecer las flores desde abajo')

print("Llamadas inválidas")
print("=" *80)
voltaje()                       # falta argumento obligatorio
voltaje(tension=5.0, 'muerto')  # argumento posicional luego de uno nombrado
voltaje(110, tension=220)       # valor duplicado para el mismo argumento
voltaje(actor='Arnaldo Aranas') # nombre de argumento desconocido










