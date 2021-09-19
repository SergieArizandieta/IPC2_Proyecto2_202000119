import carga as c
class linea:
  def __init__(self,no,componentes,tiempoE):
    self.no=no
    self.componentes=componentes
    self.tiempoE=tiempoE
    self.Actual=0
    self.Prioridad= False
    self.Timeout= 0
    self.destino = 0
    self.noEnsamble = 0

    self.Ensablar=False # -- No lo he usado

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
      print("destino: ", actual.ensable.destino )
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

  def ElaborarManual(self,producto,valor):
    setPrimeaVezEnsablar = True
    ElboracionProgrsss = True
    ElbaFinalizado = False
    CSegs = 0

    actual = self.primero
    print(actual.ensable.no,"----", valor)
  
    PActual = c.Lproductos.buscar(producto)
    if PActual is not None:
      #PActual.elaboracion.recorrer()

      self.Inicializar(PActual)
      self.AgregarDestino(PActual)

      while ElboracionProgrsss == True :
        CSegs += 1
        print("Segundo",CSegs )

        #Recorrer los que tengan destino-------------------------
        actualNuevo= self.primero
        while actualNuevo != None:
          if actualNuevo.ensable.destino != 0 and int(actualNuevo.ensable.Actual) < actualNuevo.ensable.destino:
            actualNuevo.ensable.Actual += 1  
            print("Line",actualNuevo.ensable.no,"posicion actual",actualNuevo.ensable.Actual)

          elif actualNuevo.ensable.destino != 0 and int(actualNuevo.ensable.Actual) == actualNuevo.ensable.destino:
            if  actualNuevo.ensable.Prioridad:

              if setPrimeaVezEnsablar:
                actualNuevo.ensable.Timeout = actualNuevo.ensable.tiempoE
                setPrimeaVezEnsablar = False

              if actualNuevo.ensable.Timeout > 0:
                actualNuevo.ensable.Timeout -= 1
                print("Line",actualNuevo.ensable.no, "Tiempo restante:",actualNuevo.ensable.Timeout )

              elif actualNuevo.ensable.Timeout == 0:
                print("Line",actualNuevo.ensable.no, "Tiempo Temrinado" )
                actualNuevo.ensable.Prioridad = False
                #PActual.elaboracion.
              #print("Line",actualNuevo.ensable.no, "Ensamblado" )
              
            else:
              print("Line",actualNuevo.ensable.no, "Ensamblado a espera")
          actualNuevo = actualNuevo.siguiente
        #fin recorrer=-----------------------

       
        if CSegs == 4 or ElbaFinalizado== True:
          ElboracionProgrsss = False
          break
        
        
        #ElbaFinalizado = True
    
    #print(c.Lproductos.primero.producto.nombre)
  
  def Inicializar(self,PActual):
    #Iniclizar primer ensamble-------------------------
      actualNuevo= self.primero
      while actualNuevo != None:
        if actualNuevo.ensable.no == int( PActual.elaboracion.InicizarlizarLinea()):
          actualNuevo.ensable.Prioridad =  True
          actualNuevo.ensable.noEnsamble =  int( PActual.elaboracion.InicizarlizarPosicionEn())
          break
      actualNuevo = actualNuevo.siguiente
      #fin inicializar=-----------------------
      
  def AgregarDestino(self,PActual):
     #Aggregando destino-------------------------
      actualNuevo= self.primero
      while actualNuevo != None:
        actualNuevo.ensable.destino =  PActual.elaboracion.buscarDestino(int(actualNuevo.ensable.no))
        #print(actualNuevo.ensable.destino)
        actualNuevo = actualNuevo.siguiente
      #Terminando Destino=-----------------------
"""if __name__ == "__main__":
    e1 = linea(1,1,1)
    e2 = linea(2,2,2)
    e3 = linea(3,3,3)
    lista_e = lista_brazos()
    lista_e.insertar(e1)
    lista_e.insertar(e2)
    lista_e.insertar(e3)
    lista_e.recorrer()"""
        