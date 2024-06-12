## VARIABLE DE LOCAL A GLOBAL (keyword global)
def saludar(nombre):
  global x
  x = f"Hola {nombre}!"
  return x

# print(x) En este caso la variable x no esta definida

print(saludar('Pol'))
print(x) # Ahora que la funcion ya se ha ejecutado, la variable x existe de manera global


## MANEJO DE VARIABLES LOCALES (keyword nonlocal)
def rando():
  var_local = 0

  def nuevo_valor():
    nonlocal var_local
    var_local = 1
  
  nuevo_valor()
  return f"var local ={var_local}"

print(rando())
print(var_local)


## FUNCION LAMBDA
def saludar():
  return "amigo"

lambda_sin_parametros = lambda : "hola"
lambda_con_parametros = lambda a=0, b=2 : a+b

print(saludar())
print(lambda_sin_parametros())
print(lambda_con_parametros(3,5))


## CLOSURES DE FUNCIONES (Llamar una funcion dentro de una funcion y guardarla en una variable)
def operacion (a,b):

  def sumar(a,b):
    return a+b
  
  return sumar

closure = operacion_1 (3,2)

print(closure(), "es identico", operacion_1(3,2)())