from tkinter.constants import NONE
from xml.etree.ElementTree import register_namespace
import xml.etree.cElementTree as ET
from os import system

import cargaMaquina as c
import RegistroLineas as r
import cargaSimulacion as s



firsTime = True
CantidadMasico = 0
CantidadAux = 0
rootM = None
ListadoPorductosM =None
class linea:
  def __init__(self,no,componentes,tiempoE,registro):
    self.no=no
    self.componentes=componentes
    self.tiempoE=tiempoE
    self.Actual=0
    self.Prioridad= False
    self.Timeout= 0
    self.destino = 0
    self.noEnsamble = 0


    self.registro = registro    
class nodo:
    def __init__(self,ensable =None,siguiente=None):
      self.ensable=ensable
      self.siguiente=siguiente

class lista_brazos:
  def __init__(self):
    self.primero = None

  def insertar(self, ensable):
    if self.primero is None:
      self.primero = nodo(ensable=ensable)
      return
    actual = self.primero
    while actual.siguiente:
      actual = actual.siguiente
    actual.siguiente = nodo(ensable=ensable)
    
  def recorrer(self):
    actual= self.primero
    while actual != None:
      #print("no: ", actual.ensable.no,"Compoenentes: ", actual.ensable.componentes, "Teimpo Ensable",actual.ensable.tiempoE )
      print("no: ", actual.ensable.no,"destino: ", actual.ensable.destino, " Prioridad",actual.ensable.Prioridad )
      #print("no: ", actual.ensable.no," Registro: ", actual.ensable.registro )
      #print("destino: ", actual.ensable.destino )
      actual = actual.siguiente
    
  def recorrerRegistro(self):
    actual= self.primero
    while actual != None:
      print("no: ", actual.ensable.no," Registro: ", actual.ensable.registro )
      actual.ensable.registro.recorrer()
     
      actual = actual.siguiente

  def eliminar(self,no):
    actual = self.primero
    anterior = None

    while actual and actual.ensable.no != no:
      anterior = actual
      actual = actual.siguiente
    
    if anterior is None:
      self.primero = actual.siguiente
    elif actual:
      anterior.siguiente = actual.siguiente
      actual.siguiente = None

  def buscar(self,no):
    actual = self.primero
    anterior = None
    while actual and actual.ensable.no != no:
      anterior = actual
      actual = actual.siguiente
      if actual is None:
        print("No se encontroel producto:", no)
        break
    if actual is not None:
      if actual.ensable.no == no:
        print("no: ", actual.ensable.no,"nombre: ")

  def ElaborarManual(self,producto,tipo): 
    self.reiniciar()
    
    print("PRODUCTO", producto)
    num = 0
    ElboracionProgrsss = True
    ElbaFinalizado = False
    CSegs = 0

    Ensablar = False
    actualizar = False
    tiempoAUX =0
    actualizarTimepo = False
    ubicacionaUX = None
    EstadoContinuar = False
  
    PActual = c.Lproductos.buscar(producto)
    if PActual is not None:
      #PActual.elaboracion.recorrer()

      self.Inicializar(PActual)
      self.AgregarDestino(PActual)
      #self.recorrer()
      
      while ElboracionProgrsss == True :
        CSegs += 1
        EstadoContinuar = False

        print("Segundo",CSegs )
        #Comprobar si hay alguno con destino----------------------------------------------------------------------------------
        actualUtlimo = self.primero
        while actualUtlimo != None:
            if actualUtlimo.ensable.destino != 0:
              EstadoContinuar = True
            actualUtlimo = actualUtlimo.siguiente

        if EstadoContinuar == False and ElbaFinalizado == False:
          ElbaFinalizado == True
          num = CSegs
          
          self.Exportar(producto,tipo)
         

          self.reiniciar()
          
          print("FINALIZA")
          print("\n\n\n")
        
        if actualizarTimepo:
          tiempoAUX  = CSegs

        #Recorrer los que tengan destino-------------------------
        actualNuevo= self.primero
        if EstadoContinuar:
          while actualNuevo != None:
            
            if actualizar  and  tiempoAUX == CSegs:
              ubicacionaUX.ensable.noEnsamble =  PActual.elaboracion.NuevoCompoennete(int(ubicacionaUX.ensable.no))
              PActual.elaboracion.buscarVerificado(ubicacionaUX.ensable.noEnsamble)
              PActual.elaboracion.ActualizarAnteriores(ubicacionaUX.ensable.noEnsamble)
              tiempoAUX = 0
              actualizar = False
              ubicacionaUX.ensable.destino =  PActual.elaboracion.NuevoDestino(int(ubicacionaUX.ensable.no))

              ubicacionaUX.ensable.Prioridad = False
              self.NuevaPrioridad(PActual)

            if actualNuevo.ensable.destino != 0 and int(actualNuevo.ensable.Actual) < actualNuevo.ensable.destino:
              actualNuevo.ensable.Actual += 1  
              print("Line",actualNuevo.ensable.no,"Mover brazo a",actualNuevo.ensable.Actual)

              Registro = r.register(CSegs, " Mover brazo a Componente " + str(actualNuevo.ensable.Actual))
              actualNuevo.ensable.registro.insertar(Registro) 
              

            elif actualNuevo.ensable.destino != 0 and int(actualNuevo.ensable.Actual) > actualNuevo.ensable.destino:
              actualNuevo.ensable.Actual -= 1  
              print("Line",actualNuevo.ensable.no,"Mover brazo a",actualNuevo.ensable.Actual)

              Registro = r.register(CSegs, " Mover brazo a Componente " + str(actualNuevo.ensable.Actual))
              actualNuevo.ensable.registro.insertar(Registro) 
              

            elif actualNuevo.ensable.destino != 0 and int(actualNuevo.ensable.Actual) == actualNuevo.ensable.destino :
              if  actualNuevo.ensable.Prioridad:

                if Ensablar == False:
                  actualNuevo.ensable.Timeout = actualNuevo.ensable.tiempoE
                  
                  Ensablar = True

                actualNuevo.ensable.Timeout -= 1

                if  actualNuevo.ensable.Timeout == 0:
                  print("Linea",actualNuevo.ensable.no, "EnsamblarF" )
                  Ensablar = False
                  actualizar = True
                  actualizarTimepo = True
                  ubicacionaUX = actualNuevo

                  Registro = r.register(CSegs, " Ensamblar Componente " + str(actualNuevo.ensable.Actual))
                  actualNuevo.ensable.registro.insertar(Registro) 
                else:
                  print("Linea",actualNuevo.ensable.no, "Ensamblar" )
                  Registro = r.register(CSegs, " Ensamblar Componente " + str(actualNuevo.ensable.Actual))
                  actualNuevo.ensable.registro.insertar(Registro) 
              
              else:
                print("Linea",actualNuevo.ensable.no, "No hacer nada")
                

                Registro = r.register(CSegs, " No hacer nada " )
                actualNuevo.ensable.registro.insertar(Registro) 
            else:
                
              print("Linea",actualNuevo.ensable.no, "No hacer nada")
              Registro = r.register(CSegs, " No hacer nada " )
              actualNuevo.ensable.registro.insertar(Registro) 

              #Fin comprobacion------------------------------------------------------------------------------------------------------
            
            actualNuevo = actualNuevo.siguiente
          #fin recorrer=-----------------------

        if CSegs == num: 
          
          ElboracionProgrsss = False
          break

  def AgregarDestino(self,PActual):
     #Nueva prioridad-------------------------
      actualNuevo= self.primero
      while actualNuevo != None:
        actualNuevo.ensable.destino =  PActual.elaboracion.buscarDestino(int(actualNuevo.ensable.no))
        #print(actualNuevo.ensable.destino)
        actualNuevo = actualNuevo.siguiente
      #fin nueva prioridad=-----------------------
  
  def Inicializar(self,PActual):
    #Iniclizar primer ensamble-------------------------
      actualNuevo= self.primero
      while actualNuevo != None:
        if actualNuevo.ensable.no == int( PActual.elaboracion.InicizarlizarLinea()):
          actualNuevo.ensable.Prioridad =  True
          #actualNuevo.ensable.noEnsamble =  int( PActual.elaboracion.InicizarlizarPosicionEn())
          
        actualNuevo = actualNuevo.siguiente
      #fin inicializar=-----------------------
      
  def NuevaPrioridad(self,PActual):
     
    #Aggregando destino-------------------------
      actualNuevo= self.primero
      while actualNuevo != None:
        
        if PActual.elaboracion.nuevaPrioridad() is not None:
          if actualNuevo.ensable.no == int( PActual.elaboracion.nuevaPrioridad()):
            actualNuevo.ensable.Prioridad =  True
            
            #actualNuevo.ensable.noEnsamble =  int( PActual.elaboracion.InicizarlizarPosicionEn())
            #print(actualNuevo.ensable.no)
            
            break
          actualNuevo = actualNuevo.siguiente
    #Terminando Destino=-----------------------

  def reiniciar(self):
    
    actual= self.primero
    while actual != None:
      
      actual.ensable.Actual=0
      actual.ensable.Prioridad= False
      actual.ensable.Timeout= 0
      actual.ensable.destino = 0
      actual.ensable.noEnsamble = 0
      actual.ensable.registro.clean()
      actual = actual.siguiente
      
    c.Lproductos.clean()

  def LineasTotales(self):
    aux =0 

    actual= self.primero
    while actual != None:
      aux +=1
      actual = actual.siguiente
    return aux
      
  def reporte(self,producto):
    delete= True
    actualNew= self.primero
    while actualNew != None:
      if actualNew.ensable.registro.Repetido() != " No hacer nada ":
        delete = False
      actualNew = actualNew.siguiente

    if delete:
      actualNew= self.primero
      while actualNew != None:
        actualNew.ensable.registro.eliminarRepetido() 
        actualNew = actualNew.siguiente

    Reporte = ""
    LineasTot = self.LineasTotales()

    Reporte = '<center><h6 class=\"titulos\" ><b>' +  str(producto) + '</b></h6>'

    Reporte += ' <table class="steelBlueCols"><thead><tr>  <th>Segundo</th>'

    for x in range(0+1,LineasTot+1):
      Reporte += '   <th>Linea ' + str(x) + '</th> '
    Reporte += ' </tr></thead></tbody> '
    Reporte +="\n" 
    SegundosTot = self.primero.ensable.registro.SegundosTotales()
    for x in range(0+1,SegundosTot+1):
      Reporte +="<tr> "
      Reporte += "<td>" + str(x) + "</td>"

      actual= self.primero
      while actual != None:
        Reporte += "<td>" + str(actual.ensable.registro.buscarAccion(x)) + "</td>"
        actual = actual.siguiente
      Reporte +="</tr> "
      Reporte +="\n"
    
    Reporte += "</tbody></table><br>" 
    return Reporte

  def Exportar(self,producto,tipo):
    #print("EXPORTTTTTJDSSSSSSSSSSSSSSSSSSS")
    self.exportarxmls(producto,tipo)
    Reporte = self.reporte(producto)

    ReporteFinal = htmlInicial + Reporte + htmlFinal
    if tipo == "MASIVO":
      FileHTML=open("./HTML_Generado/" + producto + "_Masivo.HTML","w") 
      FileHTML.write(ReporteFinal) 

    elif tipo== "INDIVIDUAL":
      FileHTML=open("./HTML_Generado/" + producto + "_Individual.HTML","w") 
      FileHTML.write(ReporteFinal) 

  def exportarxmls(self,producto,tipo):

        if tipo == "MASIVO":
          global firsTime
          global CantidadMasico
          global CantidadAux
          global ListadoPorductosM
          global rootM

          CantidadAux +=1
          if firsTime:
            CantidadMasico = s.LsitadoSimulacio.cantidad()
            rootM = ET.Element("SalidaSimunlacion")
            ET.SubElement(rootM, "Nombre").text = "MASIVO"
            firsTime = False

            ListadoPorductosM = ET.SubElement(rootM, "ListadoProductos")

          Priducto = ET.SubElement(ListadoPorductosM, "Producto")
            
          SegundosTot = self.primero.ensable.registro.SegundosTotales()

          ET.SubElement(Priducto, "Nombre").text = str(producto)
          ET.SubElement(Priducto, "TimepoTotal").text = str(SegundosTot)
          ElaboracionOptima = ET.SubElement(Priducto, "ElaboracionOptima")

          for x in range(0+1,SegundosTot+1):
            Tiempo = ET.SubElement(ElaboracionOptima, "Tiempo", NoSegundo=str(x))
          
            actual= self.primero
            while actual != None:
            
              ET.SubElement(Tiempo, "LineaEnsamblaje", NoLinea= str(actual.ensable.no)).text = str(actual.ensable.registro.buscarAccion(x))
              actual = actual.siguiente

          if CantidadMasico == CantidadAux:
            
            def Bonito(elemento, identificador='  '):
                validar = [(0, elemento)]  

                while validar:
                    level, elemento = validar.pop(0)
                    children = [(level + 1, child) for child in list(elemento)]
                    if children:
                        elemento.text = '\n' + identificador * (level+1)  
                    if validar:
                        elemento.tail = '\n' + identificador * validar[0][0]  
                    else:
                        elemento.tail = '\n' + identificador * (level-1)  
                    validar[0:0] = children 

            Bonito(rootM)
         
            
            archio = ET.ElementTree(rootM) 
            archio.write("./XML_Generado/"  + "MASIVO" + '.xml', encoding='UTF-8')
            s.LsitadoSimulacio.clean()
            firsTime = True
            CantidadMasico = 0
            CantidadAux = 0
            rootM = None
            ListadoPorductosM =None

        if tipo == "INDIVIDUAL":
          root = ET.Element("SalidaSimunlacion")
          ET.SubElement(root, "Nombre").text = (str(producto)+"_"+ str(tipo))

          ListadoPorductos = ET.SubElement(root, "ListadoProductos")
          Priducto = ET.SubElement(ListadoPorductos, "Producto")
          
          SegundosTot = self.primero.ensable.registro.SegundosTotales()

          ET.SubElement(Priducto, "Nombre").text = str(producto)
          ET.SubElement(Priducto, "TimepoTotal").text = str(SegundosTot)
          ElaboracionOptima = ET.SubElement(Priducto, "ElaboracionOptima")

          for x in range(0+1,SegundosTot+1):
            Tiempo = ET.SubElement(ElaboracionOptima, "Tiempo", NoSegundo=str(x))
          
            actual= self.primero
            while actual != None:
            
              ET.SubElement(Tiempo, "LineaEnsamblaje", NoLinea= str(actual.ensable.no)).text = str(actual.ensable.registro.buscarAccion(x))
              actual = actual.siguiente

          def Bonito(elemento, identificador='  '):
              validar = [(0, elemento)]  

              while validar:
                  level, elemento = validar.pop(0)
                  children = [(level + 1, child) for child in list(elemento)]
                  if children:
                      elemento.text = '\n' + identificador * (level+1)  
                  if validar:
                      elemento.tail = '\n' + identificador * validar[0][0]  
                  else:
                      elemento.tail = '\n' + identificador * (level-1)  
                  validar[0:0] = children 

          Bonito(root)
          
          archio = ET.ElementTree(root) 
          archio.write("./XML_Generado/"  + str(producto)+"_"+ str(tipo) + '.xml', encoding='UTF-8')
        
 
    
  def ReporteGraphivz(self,producto,segundo): 
    self.reiniciar()
    
    print("PRODUCTO Grapica", producto)
    num = 0
    ElboracionProgrsss = True
    ElbaFinalizado = False
    CSegs = 0

    Ensablar = False
    actualizar = False
    tiempoAUX =0
    actualizarTimepo = False
    ubicacionaUX = None
    EstadoContinuar = False
  
    PActual = c.Lproductos.buscar(producto)
    if PActual is not None:
      #PActual.elaboracion.recorrer()

      self.Inicializar(PActual)
      self.AgregarDestino(PActual)
      #self.recorrer()
      
      while ElboracionProgrsss == True :
        CSegs += 1
        EstadoContinuar = False

        print("Segundo",CSegs )
        #Comprobar si hay alguno con destino----------------------------------------------------------------------------------
        actualUtlimo = self.primero
        while actualUtlimo != None:
            if actualUtlimo.ensable.destino != 0:
              EstadoContinuar = True
            actualUtlimo = actualUtlimo.siguiente

        if EstadoContinuar == False and ElbaFinalizado == False:
          ElbaFinalizado == True
          num = CSegs
          
          self.GeneraraGrafo(PActual.elaboracion.ObtenerEnsamblados(),producto)
          self.reiniciar()
          
          print("FINALIZA")
          print("\n\n\n")
        
        if actualizarTimepo:
          tiempoAUX  = CSegs

        #Recorrer los que tengan destino-------------------------
        actualNuevo= self.primero
        if EstadoContinuar:
          while actualNuevo != None:
            
            if actualizar  and  tiempoAUX == CSegs:
              ubicacionaUX.ensable.noEnsamble =  PActual.elaboracion.NuevoCompoennete(int(ubicacionaUX.ensable.no))
              PActual.elaboracion.buscarVerificado(ubicacionaUX.ensable.noEnsamble)
              PActual.elaboracion.ActualizarAnteriores(ubicacionaUX.ensable.noEnsamble)
              tiempoAUX = 0
              actualizar = False
              ubicacionaUX.ensable.destino =  PActual.elaboracion.NuevoDestino(int(ubicacionaUX.ensable.no))

              ubicacionaUX.ensable.Prioridad = False
              self.NuevaPrioridad(PActual)

            if actualNuevo.ensable.destino != 0 and int(actualNuevo.ensable.Actual) < actualNuevo.ensable.destino:
              actualNuevo.ensable.Actual += 1  
              print("Line",actualNuevo.ensable.no,"Mover brazo a",actualNuevo.ensable.Actual)

              Registro = r.register(CSegs, " Mover brazo a Componente " + str(actualNuevo.ensable.Actual))
              actualNuevo.ensable.registro.insertar(Registro) 
              

            elif actualNuevo.ensable.destino != 0 and int(actualNuevo.ensable.Actual) > actualNuevo.ensable.destino:
              actualNuevo.ensable.Actual -= 1  
              print("Line",actualNuevo.ensable.no,"Mover brazo a",actualNuevo.ensable.Actual)

              Registro = r.register(CSegs, " Mover brazo a Componente " + str(actualNuevo.ensable.Actual))
              actualNuevo.ensable.registro.insertar(Registro) 
              

            elif actualNuevo.ensable.destino != 0 and int(actualNuevo.ensable.Actual) == actualNuevo.ensable.destino :
              if  actualNuevo.ensable.Prioridad:

                if Ensablar == False:
                  actualNuevo.ensable.Timeout = actualNuevo.ensable.tiempoE
                  
                  Ensablar = True

                actualNuevo.ensable.Timeout -= 1

                if  actualNuevo.ensable.Timeout == 0:
                  print("Linea",actualNuevo.ensable.no, "EnsamblarF" )
                  Ensablar = False
                  actualizar = True
                  actualizarTimepo = True
                  ubicacionaUX = actualNuevo

                  Registro = r.register(CSegs, " Ensamblar Componente " + str(actualNuevo.ensable.Actual))
                  actualNuevo.ensable.registro.insertar(Registro) 
                else:
                  print("Linea",actualNuevo.ensable.no, "Ensamblar" )
                  Registro = r.register(CSegs, " Ensamblar Componente " + str(actualNuevo.ensable.Actual))
                  actualNuevo.ensable.registro.insertar(Registro) 
              
              else:
                print("Linea",actualNuevo.ensable.no, "No hacer nada")
                

                Registro = r.register(CSegs, " No hacer nada " )
                actualNuevo.ensable.registro.insertar(Registro) 
            else:
                
              print("Linea",actualNuevo.ensable.no, "No hacer nada")
              Registro = r.register(CSegs, " No hacer nada " )
              actualNuevo.ensable.registro.insertar(Registro) 

              #Fin comprobacion------------------------------------------------------------------------------------------------------
            
            actualNuevo = actualNuevo.siguiente
          #fin recorrer=-----------------------

        if CSegs == num or CSegs ==  segundo:
          if  CSegs == segundo and segundo!= num:
            firsTime = False
            self.GeneraraGrafo(PActual.elaboracion.ObtenerEnsamblados(),producto)
            self.reiniciar()
            ElboracionProgrsss = False
          break

  def GeneraraGrafo(self,tetxo,producto):
    #print( tetxo)
    aux =0
    contador = 0
    auxtexto = ""
    graphviz = ""


    graphviz +='''digraph L{
    node[shape=box fillcolor="#4ECBF7" style =filled]
    subgraph cluster_p{
        label= "Reporte de cola de secuencia ''' + producto + ''' "
        bgcolor = "#FF7878"\n'''

    if tetxo != "":
      for txt in tetxo:
        aux +=1
        if aux<= 4:
          auxtexto += txt
        if aux ==4:
        
          contador +=1
          graphviz += ('Columna' + str(contador) + '[label =' + auxtexto  + ',group=' + str(contador+1) + '];\n')
          auxtexto =""
          aux=0
      graphviz += "\n"

      for x in range(1,contador):
        graphviz +=('Columna' + str(x) + "->" +'Columna' + str(x+1) +";\n" )

      graphviz +="{rank=same;"

      for x in range(1,contador+1):
        graphviz +=('Columna' + str(x)  + ";")

      graphviz +="}\n } }"
    else:
      graphviz += '''Columna1[label =No_hay_ensambles,group=2];

        {rank=same;Columna1;}\n } }'''
    
    #print(graphviz)

    print("Reporte de cola de secuencia")
    print("Grafo generado...abriendo\n")
    ruta = "./Diagramas/"

    DotName = "ReporteColaSecuencia" + producto + '.dot'
    ImgName = "ReporteColaSecuencia" + producto+ '.png'
    rutacmdImg = "Diagramas/" + ImgName
    rutacmdImg = '"' + rutacmdImg + '"'
    miArchivo= open(ruta + DotName,'w')
    miArchivo.write(graphviz)
    miArchivo.close()
    
    system('dot -Tpng ' + ruta+  DotName + ' -o ' + ruta+ ImgName)
    system('"' + rutacmdImg + '"\n')
    
htmlInicial = """<!DOCTYPE html>
<html>

<!--Encabezado-->
<head>
<meta charset="UTF-8">
<meta name="name" content="Reporte">
<meta name="description" content="name">
<meta name="keywods" content="python,dos,tres">
<meta name="robots" content="Index, Follow">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" type="text/css" href="css/styles.css"/>
<title>Reporte</title>
</head>
<!----Curerpo--->
<body>
   <center><h6 class=\"titulos\" ><b> Reportes </b></h6>"""

htmlFinal = """<br><footer style="background-color:white;">Creado por: Sergie Daniel Arizandieta Yol - 202000119</footer>
</center></body>
</html>"""


"""if __name__ == "__main__":
    e1 = linea(1,1,1)
    e2 = linea(2,2,2)
    e3 = linea(3,3,3)
    lista_e = lista_brazos()
    lista_e.insertar(e1)
    lista_e.insertar(e2)
    lista_e.insertar(e3)
    lista_e.recorrer()"""
        