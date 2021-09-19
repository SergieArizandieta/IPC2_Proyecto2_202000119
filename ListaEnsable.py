class ensamble:
  def __init__(self,posicionE,Linea,posicionC,Anterior):
    self.posicionE=posicionE
    self.posicionC=posicionC
    self.Linea=Linea
    self.Anterior=Anterior
    self.Vereficado=False

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

    #print(actual.siguiente.ensamble.Linea, "Aqui")

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
      if nuevoahora.ensamble.Linea == posicionE and nuevoahora.ensamble.posicionE != elaboracion:
        actual.siguiente.ensamble.Anterior = True
        #print("Anteior: ", actual.siguiente.ensamble.Anterior )
    
  def recorrer(self):
    actual= self.primero
    while actual != None:
      print("Posicion ensamble: ", actual.ensamble.posicionE, "posicion linea: ", actual.ensamble.Linea ,"posicion componente: ", actual.ensamble.posicionC, "Anterioe", actual.ensamble.Anterior)
      actual = actual.siguiente


#FUNCIAONLIDADES-------------------------------------------------------------------------------------------------------------------

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
      if actual.ensamble.Linea == posicionE and actual.ensamble.Anterior == False:
        #print("Componente buscado: ", actual.ensamble.posicionC)
        return actual.ensamble.posicionC

  def InicizarlizarLinea(self):
    actual= self.primero
    #print("Posicion ensamble: ", actual.ensamble.posicionE, "posicion linea: ", actual.ensamble.Linea ,"posicion componente: ", actual.ensamble.posicionC, "Anterioe", actual.ensamble.Anterior)
    return actual.ensamble.Linea
  
  def InicizarlizarPosicionEn(self):
    actual= self.primero
    return actual.ensamble.posicionE

  def buscarEnsablado(self,posicionE):
    actual = self.primero
    anterior = None
    while actual and actual.ensamble.Linea != posicionE:
      anterior = actual
      actual = actual.siguiente
      if actual is None:
        #print("No se encontro la persona con el no:", posicionE)
        return 0


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
        