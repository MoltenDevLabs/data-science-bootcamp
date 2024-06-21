

cr, c = {}, True

while c:
  k, v = input("Articulo: "), float(input("Valor: "))
  cr[k] = v
  c = input("Quieres continuar (s/n): ").lower() == 's'

c = 0
print("Lista compra: ")
for i, j in cr.items():
  print(f"{i} | {j}")
  c += j

print(f"Coste total: {c} €")