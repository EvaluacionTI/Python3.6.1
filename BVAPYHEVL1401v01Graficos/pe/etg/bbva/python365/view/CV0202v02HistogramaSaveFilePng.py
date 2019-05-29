#==============================================================================
# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	EVL - Evaluation
# Módulo			        :   Módulo de Graficos
# Fecha	Creación	    :	29/05/2019
# Objetivo			        :   Diagonal de un grafico en el eje x y eje y
# Description            :   Muestra una diagonal en coordenas por defecto (0,0)
#
#==============================================================================
import matplotlib.pyplot as oFormatPlt

ejeX = [5, 22, 30, 9, 29, 6, 28, 8, 7, 6]
oFormatPlt.xlabel("Cantidad Procesos")
oFormatPlt.title("Arquitectura ASTA / ETHER")
oFormatPlt.plot(ejeX)
oFormatPlt.draw()
oFormatPlt.savefig("BBVAEjecucionesAPX", dpi=600)
