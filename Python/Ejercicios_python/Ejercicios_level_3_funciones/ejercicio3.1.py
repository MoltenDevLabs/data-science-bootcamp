# Escribir una función que aplique un descuento a un precio y otra que aplique el IVA a un precio. Escribir una tercera función que reciba un diccionario con los precios y porcentajes de una cesta de la compra, y una de las funciones anteriores, y utilice la función pasada para aplicar los descuentos o el IVA a los productos de la cesta y devolver el precio final de la cesta.

def descuento(precio, descuento):
  """
  USO: Devuelve el precio con el descuento aplicado
  PARAMETROS:
    precio[float/int]: precio del producto
    descuento[int]: descuento en %
  VARIABLES:
    precio_descuento[float]: precio con el descuento aplicado
  RETURN:
    [float]
  """
  precio_descuento = precio - (precio * descuento)/100
  return precio_descuento

def iva(precio, iva):
  """
  USO: Devuelve el precio con el iva aplicado
  PARAMETROS:
    precio[float/int]: precio del producto
    iva[int]: iva en %
  VARIABLES:
    precio_iva[float]: precio con el iva aplicado
  RETURN:
    [float]
  """
  precio_iva = precio + (precio * iva)/100
  return precio_iva

def carrito(productos, f):
  """
  USO: Devuelve el importe del carrito de la compra en funcion de los descuentos e ivas
  PARAMETROS:
    productos[dict]: diccionario precio-%
    f[func]: funcion que aplica iva o descuento
  VARIABLES:
    total[float]: total del carrito con iva y descuento aplicado
  RETURN:
    total[float]: total del carrito con iva y descuento aplicado
  """
  total = 0
  for i, j in productos.items():
    return


dic1, dic2 = {10:10,50:15,10:30}, {10:4,50:21,10:21}
discount = carrito(dic1,descuento)
impuesto = carrito(dic2,iva)

print(f"Total con descuento: {discount:.2f}€ - Total con impuestos: {impuesto:.2f}")