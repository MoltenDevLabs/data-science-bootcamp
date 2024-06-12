def fun_decorador_a(fun_a_recibir):
  def funcion_intermedia():
    print("Codigo antes de ejecutar la funcion")
    fun_a_recibir()
    print("Codigo despues de ejecutar la funcion")

  return funcion_intermedia

@fun_decorador_a
def saludar():
  print("hola")

saludar()