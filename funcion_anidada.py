def sumaResta(a, b, operacion='suma'):
  def suma(a, b):
    return a + b
  
  def resta(a, b):
    return a - b

  if operacion == 'suma':
    return suma(a, b)
  else:
    return resta(a,b)

print(sumaResta(10,2,'resta'))