from cargaSimulacion import*
from cargaMaquina import *
import cargaMaquina as c

from Grafica import *
if __name__ == "__main__":
    #try:
        
        
        
        #ventanas()
        
       
        txt = "Archivos de prueba/maquina.xml"
        cargarListas(txt)

      

        #txt = "Archivos de prueba/simulacion.xml"
        #cargarListasSimulacino(txt)

        c.LLineas.ElaborarManual("Guitarra")
        #c.LLineas.ElaborarManual("Piano")
    
        print("\n\nExito\n\n")
        
        #c.LLineas.reiniciar()
       
    #except Exception:
    #    print(Exception)
        
    
    