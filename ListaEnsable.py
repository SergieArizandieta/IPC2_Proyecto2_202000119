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
      return
    actual = self.primero
    while actual.siguiente:
      actual = actual.siguiente
    actual.siguiente = nodo(ensamble=ensamble)
    
  def recorrer(self):
    actual= self.primero
    while actual != None:
      print("Posicion ensamble: ", actual.ensamble.posicionE, "posicion linea: ", actual.ensamble.Linea ,"posicion componente: ", actual.ensamble.posicionC)
      actual = actual.siguiente

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
    while actual and actual.ensamble.posicionE != posicionE:
      anterior = actual
      actual = actual.siguiente
      if actual is None:
        print("No se encontro la persona con el no:", posicionE)
        break
    if actual is not None:
      if actual.ensable.no == posicionE:
        print("posicionE: ", actual.ensable.posicionE,"posicionEmbre: ")


"""if __name__ == "__main__":
    e1 = ensamble(1,1,1,1)
    e2 = ensamble(2,2,2,2)
    e3 = ensamble(3,3,3,3)
    lista_e = lista_enzamblar()
    lista_e.insertar(e1)
    lista_e.insertar(e2)
    lista_e.insertar(e3)
    lista_e.recorrer()"""
        