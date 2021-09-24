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

  def SegundosTotales(self):
    aux =0 
    actual= self.primero
    while actual != None:
      anterior = actual
      aux = anterior.producto.segundo
      actual = actual.siguiente
    return aux

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

  def buscarAccion(self,segundo):
    actual = self.primero
    
    while actual and actual.producto.segundo != segundo:
      actual = actual.siguiente
      if actual is None:
        print("No se encontro la persona con el no:", segundo)
        break
    if actual is not None:
      if actual.producto.segundo == segundo:

        return actual.producto.proceso

  def Repetido(self):
    

    actual= self.primero
    while actual != None:
      if actual.siguiente == None:
        if actual.producto.proceso == " No hacer nada ":
          return  actual.producto.proceso
      actual = actual.siguiente

  def eliminarRepetido(self):
   

    actual= self.primero
    while actual != None:
      if actual.siguiente == None:
        if actual.producto.proceso == " No hacer nada ":
          eliminar =  actual.producto.segundo
      actual = actual.siguiente

    actual = self.primero
    anterior = None

    while actual and actual.producto.segundo != eliminar:
        anterior = actual
        actual = actual.siguiente
    
    if anterior is None:
        self.primero = actual.siguiente
    elif actual:
        anterior.siguiente = actual.siguiente
        actual.siguiente = None

        



 


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
        