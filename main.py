from os import readlink
from xml.etree.ElementTree import PI
from carga import *
import carga as c


if __name__ == "__main__":
    #try:
        txt = "Archivos de prueba/maquina.xml"
        cargarListas(txt)
        print("Exito")
        c.LLineas.ElaborarManual("Guitarra")
        c.LLineas.ElaborarManual("Piano")
    #except Exception:
        #print(Exception)
        
    
    