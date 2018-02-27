#==============================================================================
# Entidad			:	Entelgy - Banco Continental
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	07Feb2018
# Objetivo			:	Funciones con argumentos con palabras clave
# Fecha Edición		:
# Descripción		:
#**********************************************************************************
def testArgList(*args, **kwargs):
    print("testArgList")
    print("*args :", args)
    print("**kwargs : ", kwargs)

def testArgList2(arg0, *args, **kwargs):
    print("testArgList2")
    print('argg0 : ', arg0)
    print("*args : ", args)
    print("**kwargs : ", kwargs)

print("=" *80)
testArgList('Arquitectura Host', 'API', arg1='CTS', arg2='Financiero')
print("=" *80)
testArgList2('Python3.6.1', 'Arquitectura Host', 'API', arg1='CTS', arg2='Financiero')