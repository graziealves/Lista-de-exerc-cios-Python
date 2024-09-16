nota = []

for i in range (4):
    nota.append(float(input(f"\33[1;35;40mInforme a {i+1}ª nota: \33[m")))

media = sum(nota)/4
print(f"\33[1;31;40mA média das notas é {media}\33[m")

for i in range (4):
  if (nota[i] >= media):
    print (f"\33[1;35;40mA nota {nota[i]} é maior ou igual a média\33[m")
