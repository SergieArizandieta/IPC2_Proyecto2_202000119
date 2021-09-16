from tkinter import *
from tkinter import filedialog
from xml.dom import minidom
import xml.etree.ElementTree as ET


def cargarListas(xmlRuta):
    
    try:
        ruta = xmlRuta 

        gestion = ET.parse(ruta)
        root = gestion.getroot()
        
        for maquina in root:

            for lineas in maquina.iter('CantidadLineasProduccion'):
                print(lineas.text)

           
            for linea in maquina.iter('LineaProduccion'):
                for numero in linea.iter('Numero'):
                        print(numero.text)
                for cantidad in linea.iter('CantidadComponentes'):
                        print(cantidad.text)
                for timepo in linea.iter('TiempoEnsamblaje'):
                        print(timepo.text)

            for producto in maquina.iter('Producto'):
                for nombre in producto.iter('nombre'):
                        print(nombre.text)
                for elaboracion in producto.iter('elaboracion'):
                        print(elaboracion.text)
             

        
        #lista_e.recorrer() 
        print("\nArchivo Cargado con Exito\n")
        return True
    
    except Exception:
        print ("\nError en la ruta ingresada\n")
        return False

def openExtra():
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


if __name__ == "__main__":
    #txt = "Archivo prueba.xml"
    txt = "Archivos de prueba/maquina.xml"
    cargarListas(txt)
    #cargarListas(openExtra())
    