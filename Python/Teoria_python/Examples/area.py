# Crear una función que calcule el área de la circunferencia pasando como parámetro el radio. 
# Y sabiendo que podemos aproximar el numero pi a 3.1416 
# y es necesario que se defina como variable del cuerpo de la función, ya que esta va a ir aumentando su funcionalidad.

def area_calc(r):
  """
    USO: calcular el area de una circunferencia pasando el radio como parámetro
    VARIABLES:
      pi[float]: numero pi aproximado a 3.1416
      a[int/float]: el cálculo del area (pi*r**2)
    PARAMETROS:
      r[int/float]: radio de la circunferencia
    RETURN: el area de la circunferencia
  """

  pi = 3.1416
  a = pi*r**2
  return a

print(area_calc(3))