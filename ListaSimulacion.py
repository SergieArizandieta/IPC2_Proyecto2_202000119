from cargaMaquina import *
import cargaMaquina as c

class productos:
  def __init__(self,nombre,Producto):
    self.nombre=nombre
    self.Producto=Producto

class nodo:
    def __init__(self,producto =None,siguiente=None):
      self.producto=producto
      self.siguiente=siguiente

class Listado_SimulacionP:
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
      #print("nombre: ", actual.producto.nombre,"Producto: ", actual.producto.Producto.recorrer())
      print("nombre simulaciom: ", actual.producto.nombre,"Producto: ", actual.producto.Producto)
      actual = actual.siguiente

  def cantidad(self):
    cantidad = 0
    actual= self.primero
    while actual != None:
      cantidad+=1
      actual = actual.siguiente
    return cantidad

  def Simular(self):
        actual= self.primero
        while actual != None:
            c.LLineas.ElaborarManual(actual.producto.Producto,"MASIVO")
            #print("Producto: ", actual.producto.Producto)
            actual = actual.siguiente



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
      if actual.producto.nombre == nombre:
        #print("nombre: ", actual.producto.nombre)
        #print("Lista: ", actual.producto.Producto)
        #actual.producto.Producto.recorrer()
        return actual.producto

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