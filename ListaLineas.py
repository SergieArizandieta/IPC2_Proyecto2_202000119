from tkinter.constants import NONE
from xml.etree.ElementTree import register_namespace
import cargaMaquina as c
import RegistroLineas as r
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
        print("No se encontro la persona con el no:", no)
        break
    if actual is not None:
      if actual.ensable.no == no:
        print("no: ", actual.ensable.no,"nombre: ")

  def ElaborarManual(self,producto): 
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
      self.recorrer()
      
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
          
          self.recorrerRegistro()
          self.Exportar(producto)
          
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
              
              #self.recorrer()

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

        """if  ElbaFinalizado== True:
          #PActual.elaboracion.recorrer()
          #self.recorrer()
          ElboracionProgrsss = False
          break"""
        
        
        #ElbaFinalizado = True
    
    #print(c.Lproductos.primero.producto.nombre)

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
      actual = actual.siguiente

    c.Lproductos.clean()

  def LineasTotales(self):
    aux =0 

    actual= self.primero
    while actual != None:
      aux +=1
      actual = actual.siguiente
    return aux
      

  def reporte(self):
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
      
      print("Eliminar Repetidos")
    else:
       print("NoEliminar Repetidos")

    self.recorrerRegistro()

    Reporte = ""
    LineasTot = self.LineasTotales()
    #print(LineadTot)

    Reporte = ' <table class="steelBlueCols"><thead><tr>  <th>Segundo</th>'
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

  def Exportar(self,producto):
    Reporte = self.reporte()

    ReporteFinal = htmlInicial + Reporte + htmlFinal
    FileHTML=open("./HTML_Generado/" + producto + ".HTML","w") 
    FileHTML.write(ReporteFinal) 

      
     
   



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
        