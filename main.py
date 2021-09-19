from os import readlink
from xml.etree.ElementTree import PI
from cargaSimulacion import*
from cargaMaquina import *
import cargaMaquina as c


if __name__ == "__main__":
    try:
        txt = "Archivos de prueba/maquina.xml"
        cargarListas(txt)

        txt = "Archivos de prueba/simulacion.xml"
        cargarListasSimulacino(txt)
    
        print("\n\nExito\n\n")
        
        c.LLineas.reiniciar()
        c.LLineas.ElaborarManual("Guitarra")
        c.LLineas.ElaborarManual("Piano")
    except Exception:
        print(Exception)
        
    
    