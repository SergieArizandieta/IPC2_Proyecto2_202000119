from os import name
from tkinter import *
from tkinter import filedialog
from xml.dom import minidom
import xml.etree.ElementTree as ET

from ListaLineas import *
from ListaProductos import *
from ListaEnsable import*
from RegistroLineas import *

Lproductos = lista_productos()
LLineas = lista_brazos()



def cargarListas(xmlRuta):
    
    try:
        contador = 0
        LineasDeclaradas= 0 
        ruta = xmlRuta 
        gestion = ET.parse(ruta)
        root = gestion.getroot()
        
        for maquina in root:

            for LineasBrazos in maquina.iter('CantidadLineasProduccion'):
                LineasDeclaradas = int(LineasBrazos.text)
                
                
              

            for LineasBrazos in maquina.iter('LineaProduccion'):
                contador += 1
                if contador <= LineasDeclaradas: 
                    for numero in LineasBrazos.iter('Numero'):
                            num = int(numero.text)
                    for cantidad in LineasBrazos.iter('CantidadComponentes'):
                            can = int(cantidad.text)
                    for timepo in LineasBrazos.iter('TiempoEnsamblaje'):
                            time = int(timepo.text)
                    NewLinea = lista_Registro()
                    e1 = linea(num,can,time,NewLinea)
                    LLineas.insertar(e1)
                else:
                    print("Se han ingesado mas lineas de las esperadas")

            for producto in maquina.iter('Producto'):
                for nombre in producto.iter('nombre'):
                        name = nombre.text
                for elaboracion in producto.iter('elaboracion'):
                        elab = elaboracion.text
                        lista = purificacion(elab,LineasDeclaradas)
                        if lista != None:
                            agregar = True
                            #lista.recorrer()
                            pass
                        else:
                            agregar = False
                if agregar:    
                    e1 = productos(name,lista)
                    Lproductos.insertar(e1)
                        
        
        LLineas.recorrer()
        Lproductos.recorrer()
        
        print("\nArchivo Cargado con Exito\n")
        return True
    
    except Exception:
        print ("\nError en la ruta ingresada\n")
        #return False

def purificacion(text,LineasDeclaradas):
    LEnsamble = lista_enzamblar()
    contador = 0
    componenete = 0
    linea = 0
    agregar = True
    #print(text)
    estado =0 
    for txt in text:
        if estado ==0 :
            if ord(txt) == 76: #L
                contador +=1 
                estado = 1
            else:
                if ord(txt) == 32: #
                    pass
                else:
                    agregar = False
                    print("Se ingreso caracteres fuera de paraemetros", txt)
          
        elif estado ==1:
            if isNumero(txt):
                estado = 3
                if LineasDeclaradas>=int(txt):
                    linea = int(txt)
                    
                else:
                    agregar = False
                    print("No existe la linea para enasmblar", txt)
            else:
                if ord(txt) == 32: #
                    pass
                else:
                    agregar = False
                    print("Se ingreso caracteres fuera de paraemetros", txt)
               
        elif estado ==3:
            if ord(txt) == 112: #p
                estado = 4
            else:
                if ord(txt) == 32: #
                    pass
                else:
                    agregar = False
                    print("Se ingreso caracteres fuera de paraemetros", txt)
                
        elif estado ==4:
            if ord(txt) == 67: #C
                estado = 5
            else:
                if ord(txt) == 32: #
                    pass
                else:
                    agregar = False
                    print("Se ingreso caracteres fuera de paraemetros", txt)
               
        elif estado ==5:
            if isNumero(txt):
                estado = 6
                componenete = int(txt)
            else:
                if ord(txt) == 32: #
                    pass
                else:
                    agregar = False
                    print("Se ingreso caracteres fuera de paraemetros", txt)
               
        elif estado ==6:
            if ord(txt) == 112: #p
                estado = 0
                e1 = ensamble(contador,linea,componenete,False)
                LEnsamble.insertar(e1)
            else:
                if ord(txt) == 32: #
                    pass
                else:
                    agregar = False
                    print("Se ingreso caracteres fuera de paraemetros", txt)
                
        else:
            if ord(txt) == 32: #
                pass
            else:
                print("Se ingreso caracteres fuera de paraemetros", txt)
    if agregar:
        return LEnsamble
    else: 
        return None

def isNumero(txt):
    if ((ord(txt) >= 48 and ord(txt) <= 57)):
        return True
    else:
        return False

def openMaquina():
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
       
        print(archivo)
        return archivo

"""
if __name__ == "__main__":
    #txt = "Archivo prueba.xml"
    txt = "Archivos de prueba/maquina.xml"
    cargarListas(txt)
    #cargarListas(openExtra())
    """