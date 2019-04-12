#==============================================================================
# Entidad			        :   Entelgy / Banco Continental
# Proyecto			        :	PRE - Actualización de foto de predio del contribuyente
# Módulo			        :   Módulo de Predios
# Fecha	Creación	    :	27Mar2019
# Objetivo			        :   Búsqueda de predios por dirección
#                                  :
# Procedimiento       :
#
#
#==============================================================================
import tkinter as oFormat
from tkinter import ttk as oFormat8

class CVApplication():

    def __init__(self):
        oWindow_root = oFormat.Tk()
        oWindow_root.title(".....[ Módulo de Predios ].....")
        oWindow_root.config(bg="pink")  # Color de fondo de la ventana
        oWindow_root.geometry("800x600")  # Tamaño de la ventana 800 pixel de ancho y 600 de alto
        oWindow_root.resizable(width=False, height=False) # Impide que los bordes puedan desplazarse

        # 1. Etiquetas de la ventana
        self.tituloRegistro = "Búsqueda de Predios por Dirección"
        self.oLabelTitulo = oFormat.Label(oWindow_root, text=self.tituloRegistro, anchor="center", width=80, font=("Arial Bold", 16), bg="green", fg="blue")
        self.oLabelTitulo.place(x=0, y=0)

        self.oLabelFechaAsignacion = oFormat.Label(oWindow_root, text="Fecha de asignación    : ", anchor="w", font=("Verdana", 12))
        self.oLabelDireccionBusqueda = oFormat.Label(oWindow_root, text="Dirección de búsqueda : ", anchor="w", font=("Verdana", 12))
        self.oLabelFiscalizador = oFormat.Label(oWindow_root, text="Fiscalizador asignado  : ", anchor="w", font=("Verdana", 12))

        self.oLabelFechaAsignacion.place(x=5, y=50)
        self.oLabelDireccionBusqueda.place(x=5, y=80)
        self.oLabelFiscalizador.place(x=5, y=110)

        # 2. Etiquetas de entrada de datos
        self.oTextoFechaAsignacion = oFormat.Entry(oWindow_root, width=10, font=("Verdana", 12))
        self.oTextoDireccionBusqueda = oFormat.Entry(oWindow_root, width=30, font=("Verdana", 12))
        self.oComboFiscalizador = oFormat8.Combobox(oWindow_root, state="readonly", width=20, font=("Verdana", 12))

        self.oTextoFechaAsignacion.place(x=215, y=50)
        self.oTextoDireccionBusqueda.place(x=215, y=80)
        self.oComboFiscalizador.place(x=215, y=110)

        #3. Asignación de datos tempora
        self.oTextoFechaAsignacion.insert("1", "12/04/2019")
        self.oTextoDireccionBusqueda.insert("1", "Av. Javier Prado")
        self.oComboFiscalizador['values'] = ["APX", "HOST", "COBOL", "JCL", "JAVA", "SPRING"]

        # 3. Botones
        self.oBotonProcesar = oFormat8.Button(oWindow_root, text='.....')
        self.oBotonAsignar = oFormat8.Button(oWindow_root, text='Asignar')
        self.oBotonProcesar.place(x=520, y=80)
        self.oBotonAsignar.place(x=520, y=110)

        print(self)
        oWindow_root.mainloop()


def principal():
    oventana = CVApplication()
    return 0


if __name__=='__main__':
    principal()


