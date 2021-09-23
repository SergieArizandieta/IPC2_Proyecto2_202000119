class register:
  def __init__(self,segundo,proceso):
    self.segundo=segundo
    self.proceso=proceso

class nodo:
    def __init__(self,producto =None,siguiente=None):
      self.producto=producto
      self.siguiente=siguiente

class lista_Registro:
  def __init__(self):
    self.primero = None

  def insertar(self, producto):
    if self.primero is None:
      self.primero = nodo(producto=producto)
      return
    actual = self.primero
    while actual.siguiente:
      actual = actual.siguiente
    actual.siguiente = nodo(producto=producto)
    
  def recorrer(self):
   
    actual= self.primero
    while actual != None:
      print("segundo: ", actual.producto.segundo,"proceso: ", actual.producto.proceso)
      actual = actual.siguiente

  def clean(self):
    actualRecorreor= self.primero
    while actualRecorreor != None:

        actual = self.primero
        anterior = None

        while actual and actual.producto.segundo !=  actualRecorreor.producto.segundo:
            anterior = actual
            actual = actual.siguiente
        
        if anterior is None:
            self.primero = actual.siguiente
        elif actual:
            anterior.siguiente = actual.siguiente
            actual.siguiente = None

        actualRecorreor = actualRecorreor.siguiente  

"""if __name__ == "__main__":
    e1 = register(1,"incio")
    e2 = register(2,"Nada")
    e3 = register(3,"Sber")
    lista_e = lista_Registro()
    lista_e.insertar(e1)
    lista_e.insertar(e2)
    lista_e.insertar(e3)
    lista_e.recorrer()
    lista_e.clean()
    print("Lipiado")
    lista_e.recorrer()"""
        