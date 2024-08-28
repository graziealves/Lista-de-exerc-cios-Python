print("\33[1;35;40mQual é o maior número?\33[m \n")

numeros = []
for i in range(5):
  numeros.append(float(input(f"\33[1;35;40mInforme o {i + 1}º número: \33[m \n")))

print("\33[1;35;40mO maior número é: \33[m" , max(numeros))