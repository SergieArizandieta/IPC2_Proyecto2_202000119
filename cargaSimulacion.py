from os import name
from tkinter import *
from tkinter import filedialog
from xml.dom import minidom
import xml.etree.ElementTree as ET

from ListaSimulacion import*



LsitadoSimulacio = Listado_SimulacionP()
def cargarListasSimulacino(xmlRuta):
    

        name = ""
        ruta = xmlRuta 
        gestion = ET.parse(ruta)
        root = gestion.getroot()
        
        for Simulacion in root:

            for NombreSimulacion in Simulacion.iter('Nombre'):
                name = (NombreSimulacion.text)
                #print(name)
                
            for ListadoP in Simulacion.iter('ListadoProductos'): 
                for Producto in ListadoP.iter('Producto'): 
                    producto = (Producto.text)
                    #print(producto)
                    e1 = productos(name,producto)
                    LsitadoSimulacio.insertar(e1)

        LsitadoSimulacio.Simular()   
        print("\nArchivo Cargado con Exito\n")
        return True
    


def openSimulacion():
    Tk().withdraw()
    archivo = filedialog.askopenfilename(
        title = "Seleccionar un archivo LFP",
        initialdir = "./",
        filetypes = (
            ("archivos xml", "*.xml"),
            ("todos los archivos",  "*.*")
        )
    )
    if archivo is None:
        print('\nNo se seleccionó ningun archivo')
        return None
    else:
        print('\n"Lectura exitosa"')
        return archivo



"""if __name__ == "__main__":
    #txt = "Archivo prueba.xml"
    txt = "Archivos de prueba/simulacion.xml"
    cargarListasSimulacino(txt)
    #cargarListas(openExtra())
    """