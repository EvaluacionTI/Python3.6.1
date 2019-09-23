#==============================================================================
# Entidad			:
# Proyecto			:	EVL (Evaluación de Python 3.6.1.)
# Módulo			:
# Fecha	Creación	:	20Abr2018
# Periódo           :   20Abr/2018
# Objetivo			:	Import junitest
# Fecha Edición		:
# Descripción		:   Necesita mas esfuerzo que el módulo doctest, pero
#                       permite que se mantenga en un archivo separado un
# conjunto más comprensivo de pruebas
#==============================================================================
import unittest


def promedio(valores):
    return sum(valores) / len(valores)


class CTTestFuncionesEstadisticas(unittest.TestCase):
    def testPromedio(self):
        self.assertEquals(promedio([15,17,20,27]), 30)
        self.assertEquals(round(promedio([15,17,20,27]), 30), 4.3)
        with self.assertRaises(ZeroDivisionError):
            promedio([])
        with self.assertRaises(TypeError):
            promedio(20,30,70)

unittest.main()