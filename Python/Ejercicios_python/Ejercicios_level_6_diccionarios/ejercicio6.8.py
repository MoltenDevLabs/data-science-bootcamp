

d, p = {}, 'perro:dog,gato:cat,hola:hello,el:the,dice:says' #input("Listado de palabras y traducción separado por comas: ")

for k in p.split(','):
  c,v = k.split(':')
  d[c] = v

f, F= 'el perro dice hola al gato', '' #input("Frase a traducir: ")

for x in f.split():
  if x in d:
    F += str(d[x]) + ' '
  else:
    F += x + ' '

print(F[:len(F)])
