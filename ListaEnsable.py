class ensamble:
  def __init__(self,posicionE,Linea,posicionC,Anterior):
    self.posicionE=posicionE
    self.posicionC=posicionC
    self.Linea=Linea

    self.Anterior=Anterior
    self.AnteriorPosicionE=0
    self.Verificado=False

   
class nodo:
    def __init__(self,ensamble =None,siguiente=None):
      self.ensamble=ensamble
      self.siguiente=siguiente
class lista_enzamblar:
  def __init__(self):
    self.primero = None

  def insertar(self, ensamble):
    if self.primero is None:
      self.primero = nodo(ensamble=ensamble)
      #print(self.primero.ensamble.Linea, "Aqui")
      return
    actual = self.primero
    while actual.siguiente:
      actual = actual.siguiente
    actual.siguiente = nodo(ensamble=ensamble) 
    #---------------------------------------------------------------------------

    posicionE = actual.siguiente.ensamble.Linea
    elaboracion = actual.siguiente.ensamble.posicionE
    nuevoahora = self.primero
    anterior = None
    while nuevoahora and nuevoahora.ensamble.Linea != posicionE  :
      anterior = nuevoahora
      nuevoahora = nuevoahora.siguiente
      if nuevoahora is None:
        #print("No se encontro la linea:", posicionE)
        break
    if nuevoahora is not None:
      if nuevoahora.ensamble.Linea == posicionE and nuevoahora.ensamble.posicionE != elaboracion and nuevoahora.ensamble.Anterior == False:
        actual.siguiente.ensamble.Anterior = True
        actual.siguiente.ensamble.AnteriorPosicionE = nuevoahora.ensamble.posicionE
        #print("Anteior: ", actual.siguiente.ensamble.Anterior )
    
  def recorrer(self):
    actual= self.primero
    while actual != None:
      #print("Posicion ensamble: ", actual.ensamble.posicionE, "posicion linea: ", actual.ensamble.Linea ,"posicion componente: ", actual.ensamble.posicionC, "Anterioe", actual.ensamble.Anterior)
      #print("Posicion ensamble: ", actual.ensamble.posicionE, "posicion linea: ", actual.ensamble.Linea ,"posicion componente: ", actual.ensamble.posicionC, "ensablado", actual.ensamble.Verificado)
      #print("Posicion ensamble: ", actual.ensamble.posicionE, "posicion linea: ", actual.ensamble.Linea ,"posicion componente: ", actual.ensamble.posicionC, "Anterior", actual.ensamble.Anterior, "PsoicionAnterior",actual.ensamble.AnteriorPosicionE, "ensablado", actual.ensamble.Verificado )
       
      print("L" + str(actual.ensamble.Linea) +  "C" + str(actual.ensamble.posicionC), actual.ensamble.Verificado )

      actual = actual.siguiente

  def ObtenerEnsamblados(self):
      texto=""
      actual= self.primero
      while actual != None:
    
        #print("L" + str(actual.ensamble.Linea) +  "C" + str(actual.ensamble.posicionC), " E:" + str(actual.ensamble.Verificado))
        if actual.ensamble.Verificado == True:
          texto +=  ("L" + str(actual.ensamble.Linea) +  "C" + str(actual.ensamble.posicionC))
        actual = actual.siguiente
      return texto

  def Limpiar(self):
    actual= self.primero
    while actual != None:
      actual.ensamble.Anterior=False
      actual.ensamble.AnteriorPosicionE=0
      actual.ensamble.Verificado=False
      actual = actual.siguiente
  #FUNCIAONLIDADES-------------------------------------------------------------------------------------------------------------------
  def NuevoDestino(self,posicionE):
    actual = self.primero
    anterior = None
    while actual and (actual.ensamble.Linea != posicionE or actual.ensamble.Verificado != False):
      anterior = actual
      actual = actual.siguiente
      if actual is None:
        #print("No se encontro la persona con el no:", posicionE)
        return 0
        
    if actual is not None:
      if actual.ensamble.Linea == posicionE and actual.ensamble.Verificado == False and actual.ensamble.Anterior == False:
        #print("Componente buscado: ", actual.ensamble.posicionC)
        return actual.ensamble.posicionC
  
  def buscarVerificado(self,posicionE):
    actual = self.primero
    anterior = None
    while actual and actual.ensamble.posicionE != posicionE:
      anterior = actual
      actual = actual.siguiente
      if actual is None:
        #print("No se encontro la persona con el no:", posicionE)
        pass
        
    if actual is not None:
      if actual.ensamble.posicionE == posicionE:
        #print("Componente buscado: ", actual.ensamble.posicionC)
        actual.ensamble.Verificado = True
        #self.recorrer()
        #print("Verificado: ", actual.ensamble.Verificado )

  def ActualizarAnteriores(self,posicionE):
    actual = self.primero
    anterior = None
    while actual and actual.ensamble.posicionE != posicionE:
      anterior = actual
      actual = actual.siguiente
      if actual is None:
        #print("No se encontro la persona con el no:", posicionE)
        pass
        
    if actual is not None:
      if actual.ensamble.posicionE == posicionE:
        if actual.ensamble.Verificado == True:

          posicionE = actual.ensamble.Linea
          elaboracion = actual.ensamble.posicionE

          actualNuevo = self.primero
          anterior = None
          while actualNuevo and actualNuevo.ensamble.Anterior != True and actualNuevo.ensamble.AnteriorPosicionE != elaboracion:
            anterior = actualNuevo
            #print("Posicion ensamble: ", actual.ensamble.posicionE, "posicion linea: ", actual.ensamble.Linea ,"posicion componente: ", actual.ensamble.posicionC, "Anterioe", actual.ensamble.Anterior)
            actualNuevo = actualNuevo.siguiente
            if actualNuevo is None:
              #print("No se encontro:", posicionE)
              break
          if actualNuevo is not None:
            if actualNuevo.ensamble.Linea == posicionE and actualNuevo.ensamble.Anterior == True and actualNuevo.ensamble.AnteriorPosicionE == elaboracion and posicionE ==  actualNuevo.ensamble.Linea:
              actualNuevo.ensamble.Anterior = False
              
  def nuevaPrioridad(self):
    try:
      actual = self.primero
      anterior = None
      while actual and (actual.siguiente.ensamble.Verificado != False or actual.ensamble.Verificado != True) :
        anterior = actual
        actual = actual.siguiente
        
        if actual is None:
          return 0
        
          
      if actual is not None:
        if actual.siguiente.ensamble.Verificado == False and actual.ensamble.Verificado == True:
          #print("Nuevo ensamble:", actual.siguiente.ensamble.Linea   )
          return actual.siguiente.ensamble.Linea  
    except Exception:
      return 0
      
  def NuevoCompoennete(self,posicionE):
    actual = self.primero
    anterior = None
    while actual and (actual.ensamble.Linea != posicionE or actual.ensamble.Verificado != False):
      anterior = actual
      actual = actual.siguiente
      if actual is None:
        #print("No se encontro la persona con el no:", posicionE)
        return 0
        
    if actual is not None:
      if actual.ensamble.Linea == posicionE and actual.ensamble.Verificado == False and actual.ensamble.Anterior == False:
        #print("Componente buscado: ", actual.ensamble.posicionC)
        return actual.ensamble.posicionE
        
         
    
#Inicilizar------------------------------------------------------------------------------------------------------------------
  def InicizarlizarLinea(self):
    actual= self.primero
    #print("Posicion ensamble: ", actual.ensamble.posicionE, "posicion linea: ", actual.ensamble.Linea ,"posicion componente: ", actual.ensamble.posicionC, "Anterioe", actual.ensamble.Anterior)
    return actual.ensamble.Linea
  
  def InicizarlizarPosicionEn(self):
    actual= self.primero
    return actual.ensamble.posicionE

  def buscarDestino(self,posicionE):
    actual = self.primero
    anterior = None
    while actual and actual.ensamble.Linea != posicionE:
      anterior = actual
      actual = actual.siguiente
      if actual is None:
        #print("No se encontro la persona con el no:", posicionE)
        return 0
        
    if actual is not None:
      if actual.ensamble.Linea == posicionE and actual.ensamble.Anterior == False :
        #print("Componente buscado: ", actual.ensamble.posicionC)
        return actual.ensamble.posicionC


#SIN USAR-------------------------------------------------------------------------------------------
  def eliminar(self,posicionE):
    actual = self.primero
    anterior = None

    while actual and actual.ensamble.posicionE != posicionE:
      anterior = actual
      actual = actual.siguiente
    
    if anterior is None:
      self.primero = actual.siguiente
    elif actual:
      anterior.siguiente = actual.siguiente
      actual.siguiente = None

  def buscar(self,posicionE):
    actual = self.primero
    anterior = None
    while actual and actual.ensamble.Linea != posicionE:
      anterior = actual
      actual = actual.siguiente
      if actual is None:
        print("No se encontro la persona con el no:", posicionE)
        break
    if actual is not None:
      if actual.ensamble.no == posicionE :
        print("Linea: ", actual.ensamble.Linea)


"""if __name__ == "__main__":
    e1 = ensamble(1,1,1,1)
    e2 = ensamble(2,2,2,2)
    e3 = ensamble(3,3,3,3)
    lista_e = lista_enzamblar()
    lista_e.insertar(e1)
    lista_e.insertar(e2)
    lista_e.insertar(e3)
    lista_e.recorrer()"""
        