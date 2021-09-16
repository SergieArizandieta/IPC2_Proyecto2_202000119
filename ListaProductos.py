class estudiante:
  def __init__(self,nombre,elaboracion):
    self.nombre=nombre
    self.elaboracion=elaboracion
   


class nodo:
    def __init__(self,producto =None,siguiente=None):
      self.producto=producto
      self.siguiente=siguiente

class lista_enlazada:
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
      print("nombre: ", actual.producto.nombre,"Lista: ", actual.producto.elaboracion)
      actual = actual.siguiente

  def eliminar(self,nombre):
    actual = self.primero
    anterior = None

    while actual and actual.producto.nombre != nombre:
      anterior = actual
      actual = actual.siguiente
    
    if anterior is None:
      self.primero = actual.siguiente
    elif actual:
      anterior.siguiente = actual.siguiente
      actual.siguiente = None

  def buscar(self,nombre):
    actual = self.primero
    anterior = None
    while actual and actual.producto.nombre != nombre:
      anterior = actual
      actual = actual.siguiente
      if actual is None:
        print("No se encontro la persona con el no:", nombre)
        break
    if actual is not None:
      if actual.ensable.no == nombre:
        print("nombre: ", actual.ensable.nombre,"nombrembre: ")


if __name__ == "__main__":
    e1 = estudiante(1,1)
    e2 = estudiante(2,2)
    e3 = estudiante(3,3)
    lista_e = lista_enlazada()
    lista_e.insertar(e1)
    lista_e.insertar(e2)
    lista_e.insertar(e3)
    lista_e.recorrer()
        